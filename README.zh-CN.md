# Deep-Live-Cam 中文文档

[![原项目](https://img.shields.io/badge/原项目-hacksider--Deep-Live-Cam-blue?style=flat-square&logo=github)](https://github.com/hacksider/Deep-Live-Cam)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

> 本文档是 [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)(v2.1.6)README 的中文翻译。**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

## ⚠️ 免责声明(节选翻译)

本软件是为 AI 生成媒体行业打造的生产力工具,可用于动画角色创作、内容制作、服装设计等场景。开发者深知其潜在滥用风险,因此内置了内容检查机制,会阻止处理不当媒体(裸露、血腥、战争等敏感内容)。使用真实人物面部需征得本人同意,并在公开发布时明确标注为 Deepfake。终端用户的一切行为由用户自行负责,请合法、合规、有道德地使用本软件。

## 🚀 三步开启实时换脸

1. 选择一张源人脸照片
2. 选择要使用的摄像头
3. 点击 Live 开播

## ✨ 特性与用途(全部实时)

- **嘴部遮罩(Mouth Mask)**:保留原始嘴部,说话动作精准自然
- **人脸映射(Face Mapping)**:对多个目标人物同时使用不同人脸
- **你的电影你做主**:实时把电影里任何角色换成你想要的脸
- **直播表演(Live Show)**:用于直播节目与演出
- **表情包创作**:用 Many Faces 功能做出最火表情包
- **Omegle 惊喜**:在视频聊天里"变身"逗对方

## 🛠️ 手动安装(需要一定技术基础)

官方提供免安装的快速版本(见原项目 Pre-built 章节),手动安装流程如下:

**1. 平台准备**:Python 3.11–3.14(推荐 3.14)、pip、git、[ffmpeg](https://www.youtube.com/watch?v=OlNWCpFdVMA)(Windows 可用 `iex (irm ffmpeg.tc.ht)` 安装)、[Visual Studio 2022 运行库](https://visualstudio.microsoft.com/visual-cpp-build-tools/)(Windows)。

**2. 克隆仓库**

```bash
git clone --depth 1 https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam
```

**3. 下载模型**(放入 `models` 文件夹)

- [gfpgan-1024.onnx](https://huggingface.co/hacksider/deep-live-cam/resolve/main/gfpgan-1024.onnx)
- [inswapper_128_fp16.onnx](https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx)

也可以在 HuggingFace [一次性下载全部模型](https://huggingface.co/hacksider/deep-live-cam/tree/main)。

**4. 安装依赖**(强烈建议使用 venv 虚拟环境)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

macOS(Apple Silicon)需先 `brew install python@3.14` 和 `brew install python-tk@3.14`(GUI 必需),再用 `python3.14 -m venv venv` 建环境。若安装 gfpgan/basicsr 报错,可从 GitHub 源码重装这两个包(命令见原 README)。

**5. 运行**:无 GPU 直接 `python run.py`(CPU 模式,首次运行会下载约 300MB 模型)。

## ⚡ GPU 加速

**CUDA(NVIDIA 显卡)**:安装 [CUDA Toolkit 12.8.0](https://developer.nvidia.com/cuda-12-8-0-download-archive) 与 [cuDNN v8.9.7](https://developer.nvidia.com/rdp/cudnn-archive)(确保 bin 目录在 PATH 中),然后:

```bash
pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip uninstall onnxruntime onnxruntime-gpu
pip install onnxruntime-gpu==1.26.0
python run.py --execution-provider cuda
```

**CoreML(Apple Silicon)**:requirements.txt 自带的 onnxruntime 已含 CoreML 支持;若装过 `onnxruntime-silicon` 先卸载,再 `python3.14 run.py --execution-provider coreml`。

**DirectML(Windows / AMD 等显卡)**:

```bash
pip uninstall onnxruntime onnxruntime-directml
pip install onnxruntime-directml==1.21.0
python run.py --execution-provider directml
```

**OpenVINO(Intel)**:安装 `onnxruntime-openvino` 与 `openvino`(两个包版本需一一对应,如 onnxruntime-openvino 1.24.1 配 OpenVINO 2025.4.1),运行时加 `--execution-provider openvino`。

## 📖 使用方法

**图像/视频模式**:运行 `python run.py` → 选源人脸图和目标图片/视频 → 点 Start,结果保存在以目标视频命名的目录中。

**摄像头模式**:运行 `python run.py` → 选源人脸图 → 点 Live → 等预览出现(10-30 秒)→ 用 OBS 等工具采集推流;想换脸就重新选源图。

## ⌨️ 命令行参数(代表性条目,官方已不再维护)

```text
-s, --source             选择源人脸图片
-t, --target             选择目标图片或视频
-o, --output             选择输出文件或目录
--frame-processor        帧处理器(face_swapper、face_enhancer 等)
--keep-fps / --keep-audio / --keep-frames   保留原帧率/音频/临时帧
--many-faces             处理画面中的每一张脸
--map-faces              源脸与目标脸一一映射
--mouth-mask             遮罩嘴部区域
--video-encoder          输出编码器(libx264/libx265/libvpx-vp9)
--video-quality          输出画质(0-51)
--execution-provider     执行后端(cpu、cuda、coreml、directml、openvino)
--max-memory             最大内存(GB);--execution-threads 执行线程数
```

使用 `-s/--source` 参数启动即进入纯命令行模式。

## 📰 媒体报道(节选)

- **Ars Technica**:“Deep-Live-Cam 爆火,让任何人都能成为数字分身”
- **Yahoo!**:“这个爆火的 AI 直播软件真的很吓人”
- **PetaPixel**:“Deepfake 工具让你用一张照片在视频通话里变成任何人”

## 🙏 致谢

感谢 ffmpeg、[insightface](https://github.com/deepinsight/insightface)(模型仅限非商业研究用途)、主要贡献者 [Henry](https://github.com/henryruhs) 以及众多社区开发者;代码原作者为 [s0md3v](https://github.com/s0md3v/roop)(roop)。

---

> **代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

本项目为 [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) 的中文翻译版本,所有代码版权归原项目作者所有,遵循其原始许可证。**如果觉得有用,请给原项目点个 Star!** ⭐
