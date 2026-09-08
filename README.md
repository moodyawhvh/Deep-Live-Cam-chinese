<div align="center">

# Deep-Live-Cam 中文翻译版

**[中文版] Deep-Live-Cam — 实时 AI 换脸与一键视频 Deepfake,仅需一张照片**

[![原项目](https://img.shields.io/badge/原项目-hacksider--Deep-Live-Cam-blue?style=flat-square&logo=github)](https://github.com/hacksider/Deep-Live-Cam)
[![中文文档](https://img.shields.io/badge/中文文档-README.zh--CN.md-orange?style=flat-square)](README.zh-CN.md)
[![GitHub Stars](https://img.shields.io/github/stars/hacksider/Deep-Live-Cam?style=flat-square&label=原项目Stars)](https://github.com/hacksider/Deep-Live-Cam/stargazers)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

---

> 这是 [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) 的中文翻译版本。
> 完整源代码请访问原项目:https://github.com/hacksider/Deep-Live-Cam

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

## 📖 项目简介

Deep-Live-Cam 是一款开源的实时 AI 换脸工具:只需一张源人脸照片,就能在摄像头直播画面中实时换脸,也可以对目标图片或视频一键完成 Deepfake(深度伪造)合成。项目内置内容安全检查,面向 AI 生成媒体行业的创作者,曾在 GitHub 上爆火,并被 Ars Technica、Yahoo 等多家媒体报道。

## ✨ 主要特性

- **实时换脸**:一张照片即可驱动摄像头画面实时换脸,延迟低、效果自然
- **一键视频 Deepfake**:选好源人脸和目标图片/视频,点一下 Start 就出结果
- **嘴部遮罩(Mouth Mask)**:保留你原本的嘴部动作,说话口型更真实
- **人脸映射(Face Mapping)**:多个目标人物同时映射不同的脸
- **全平台 GPU 加速**:支持 NVIDIA CUDA、Apple Silicon CoreML、Windows DirectML、Intel OpenVINO
- **三种步骤上手**:选脸 → 选摄像头 → 点 Live,三步开播
- **内置内容安全检查**:自动拦截不当媒体内容,倡导合法合规使用
- **支持命令行模式**:丰富的 CLI 参数,方便自动化与批量处理

## 📁 文件说明

| 文件 | 说明 |
|:-----|:-----|
| README.md | 本文件(中文简介) |
| README.zh-CN.md | 详细中文文档(完整汉化) |

## 🚀 快速开始

**1. 准备环境**:Python 3.11–3.14(推荐 3.14)、pip、git、ffmpeg,Windows 还需 Visual Studio 2022 运行库。

**2. 克隆仓库**

```bash
git clone --depth 1 https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam
```

**3. 下载模型**:下载 `gfpgan-1024.onnx` 和 `inswapper_128_fp16.onnx`,放入 `models` 文件夹([模型下载地址](https://huggingface.co/hacksider/deep-live-cam/tree/main))。

**4. 安装依赖**(推荐使用 venv)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**5. 运行**

```bash
python run.py
```

首次启动会自动下载约 300MB 的模型;没有 GPU 也能用 CPU 运行,只是速度较慢。

**6. 使用方式**:图像/视频模式——选择源人脸和目标图片/视频后点 Start;摄像头模式——选好源人脸后点 Live,等 10-30 秒出预览,再用 OBS 等采集工具推流。NVIDIA 显卡可安装 CUDA 12.8 + cuDNN 后用 `python run.py --execution-provider cuda` 加速,详见[中文文档](README.zh-CN.md)。

完整源代码与最新版本请访问原项目:https://github.com/hacksider/Deep-Live-Cam

## 📞 联系方式

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

本项目为 [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) 的中文翻译版本,所有代码版权归原项目作者所有,遵循其原始许可证。

**如果觉得有用,请给原项目点个 Star!** ⭐
