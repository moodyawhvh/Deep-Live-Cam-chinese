> 🌐 本文档由 [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) 翻译,英文原版见原项目。

# 协作规范与代码库质量标准

为了保证协作顺畅并维持代码库的高质量,请遵守以下规范:

## 分支策略

*   **`premain`**:
    *   所有改动一律先推送到 `premain` 分支。
    *   以此保护 `main` 分支免受意外破坏。
    *   所有测试都会在 `premain` 分支上进行。
    *   只有经过数小时乃至数天的严格测试之后,改动才会合并进 `main`。
*   **`experimental`**:
    *   较大的改动或可能造成破坏的改动,请使用 `experimental` 分支。
    *   在考虑合并进 `main` 之前,先在这里进行充分的讨论和审查。

## 提交 Pull Request 前的检查清单

创建 Pull Request(PR)之前,请确保已完成以下测试:

### 功能性

*   **实时换脸(Realtime Faceswap)**:
    *   分别在面部增强器 **开启** 与 **关闭** 两种状态下进行测试。
*   **人脸映射(Map Faces)**:
    *   两种选项(**开启** 与 **关闭**)都要测试。
*   **摄像头列表(Camera Listing)**:
    *   确认所有摄像头都能被准确列出。

### 稳定性

*   **实时帧率(Realtime FPS)**:
    *   确认实时帧率(FPS)没有任何下降。
*   **启动时间(Boot Time)**:
    *   改动不应拖慢应用本身或实时换脸功能的启动速度。
*   **GPU 过载(GPU Overloading)**:
    *   至少持续测试 15 分钟,确保不会出现可能导致崩溃的 GPU 过载。
*   **应用性能(App Performance)**:
    *   应用应保持响应流畅,不得出现任何卡顿。
