# App factory

APP 原型与交互演示集合。

## 水印相机

[打开在线演示](https://ceryuan-3714.github.io/App-factory/) · [查看源文件](watermark-camera/)

包含 22 个 Figma 页面及弹层场景，可演示拍摄、照片编辑、水印模板、字段编辑、画中画、裁剪和图片验证。

- 根目录 `index.html` 是内嵌全部资源的独立演示，亦为 GitHub Pages 首页。
- `watermark-camera/` 保存可维护源代码、场景清单和验证记录。
- 相机、定位、照片保存及验证服务均为模拟；缺少设计稿的入口使用 Toast 提示。
- 已保存内容仅存储于访问者当前浏览器，未接入业务服务。
- 页面按窗口宽高适配，长列表内部滚动。

更新演示后，在 `watermark-camera/` 运行 `python3 build.py`，将生成的 `水印相机-交互演示.html` 复制为根目录 `index.html`，再提交即可更新 Pages。
