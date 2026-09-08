#!/usr/bin/env python3

import os
import sys

# 将项目根目录加入 PATH,确保捆绑的 ffmpeg/ffprobe 能被找到
project_root = os.path.dirname(os.path.abspath(__file__))
os.environ["PATH"] = project_root + os.pathsep + os.environ.get("PATH", "")

# 在 Windows 上注册 NVIDIA CUDA DLL 目录,让 onnxruntime-gpu 能找到
# cuDNN/cublas。Python 3.8+ 对扩展模块的原生依赖会忽略 PATH,必须使用
# os.add_dll_directory()。同时保留 PATH 设置,供子进程/ffmpeg 使用。
if sys.platform == "win32":
    _site_packages = os.path.join(sys.prefix, "Lib", "site-packages")
    _venv_site_packages = os.path.join(project_root, "venv", "Lib", "site-packages")
    for _sp in (_site_packages, _venv_site_packages):
        _candidate_dirs = []
        _torch_lib = os.path.join(_sp, "torch", "lib")
        if os.path.isdir(_torch_lib):
            _candidate_dirs.append(_torch_lib)
        _nvidia_dir = os.path.join(_sp, "nvidia")
        if os.path.isdir(_nvidia_dir):
            for _pkg in os.listdir(_nvidia_dir):
                _bin_dir = os.path.join(_nvidia_dir, _pkg, "bin")
                if os.path.isdir(_bin_dir):
                    _candidate_dirs.append(_bin_dir)
        for _d in _candidate_dirs:
            os.environ["PATH"] = _d + os.pathsep + os.environ["PATH"]
            try:
                os.add_dll_directory(_d)
            except (OSError, AttributeError):
                pass

    # 在 Windows 上注册 OpenVINO DLL 目录,让 onnxruntime 的
    # OpenVINOExecutionProvider 能找到 openvino.dll。这一步必须在
    # 创建任何 ONNX InferenceSession 之前完成。失败不影响启动:
    # 只是未安装 OpenVINO,onnxruntime 会回退到 CPU 执行。
    try:
        from onnxruntime.tools.add_openvino_win_libs import (  # type: ignore[import-untyped]  # noqa: E501
            add_openvino_libs_to_path,
        )
        add_openvino_libs_to_path()
    except ImportError:
        # 当前 onnxruntime 构建不包含 OpenVINO 工具模块 —— 直接跳过。
        pass
    except FileNotFoundError:
        # site-packages 中不存在 OpenVINO 目录 —— 直接跳过。
        pass
    except SystemExit as exc:
        # 当 OpenVINO 库无法定位时(例如 OPENVINO_LIB_PATHS 未设置),
        # add_openvino_libs_to_path() 会调用 sys.exit()。这里打印其
        # 附带的消息使失败可见,但不中断启动流程。
        print(
            f"[startup] OpenVINO DLL registration skipped: {exc}",
            flush=True,
        )

# 在 Linux 上预加载 venv 内随 pip 轮子(nvidia-cudnn-cu12 等)分发的
# NVIDIA 共享库(cuDNN、cuBLAS、nvrtc...)。Python 启动后无法再设置
# LD_LIBRARY_PATH,因此改用 ctypes.CDLL 配合 RTLD_GLOBAL 加载,使
# onnxruntime dlopen 其 CUDA provider 时能解析到这些符号。
if sys.platform.startswith("linux"):
    import ctypes
    import glob
    _py_lib = f"python{sys.version_info.major}.{sys.version_info.minor}"
    _site_packages_candidates = [
        os.path.join(project_root, "venv", "lib", _py_lib, "site-packages"),
        os.path.join(sys.prefix, "lib", _py_lib, "site-packages"),
    ]
    for _sp in _site_packages_candidates:
        _nvidia_dir = os.path.join(_sp, "nvidia")
        if not os.path.isdir(_nvidia_dir):
            continue
        for _pkg in os.listdir(_nvidia_dir):
            _lib_dir = os.path.join(_nvidia_dir, _pkg, "lib")
            if not os.path.isdir(_lib_dir):
                continue
            # 同时把该目录暴露给子进程,已存在的条目不重复添加。
            _ldp = os.environ.get("LD_LIBRARY_PATH", "")
            if _lib_dir not in _ldp.split(os.pathsep):
                os.environ["LD_LIBRARY_PATH"] = (
                    _lib_dir + (os.pathsep + _ldp if _ldp else "")
                )
            for _so in sorted(glob.glob(os.path.join(_lib_dir, "lib*.so*"))):
                try:
                    ctypes.CDLL(_so, mode=ctypes.RTLD_GLOBAL)
                except OSError:
                    pass
        break

from modules import platform_info
platform_info.print_banner()

from modules import core

if __name__ == '__main__':
    core.run()
