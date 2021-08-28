# SlopeCraftR

[English](README.md "README.md") | **中文**  <!-- lang  -->

> 生成在 Minecraft 中可用的 3D 地图像素画

SlopeCraftR（以下简称 SCR）是一个由 [ToKiNoBug](https://github.com/ToKiNoBug "@ToKiNoBug") 的 [SlopeCraft](https://github.com/ToKiNoBug/SlopeCraft "ToKiNoBug/SlopeCraft") **重写**而成，以 *尽可能高的色彩还原度* 将图片转化为 Minecraft 地图像素画，并导出为 *可在游戏内实装的原理图* 的工具

## 特点

### 功能

- 以**地图**（`minecraft:map`）中的展示效果，而非像素画本身的观赏效果为目标
- 提供可深度自定义的方块列表以及若干预设
- 提供多种色彩空间进行颜色转换
- 支持的导出格式
  - [地图文件](https://minecraft.fandom.com/zh/wiki/%E5%9C%B0%E5%9B%BE%E7%89%A9%E5%93%81%E6%A0%BC%E5%BC%8F "地图物品格式 - Minecraft Wiki")
  - [结构方块文件](https://minecraft.fandom.com/zh/wiki/%E7%BB%93%E6%9E%84%E6%96%B9%E5%9D%97%E6%96%87%E4%BB%B6%E6%A0%BC%E5%BC%8F "结构方块文件格式 - Minecraft Wiki")
  - [投影原理图](https://github.com/maruohon/litematica "maruohon/litematica")

### 开发

- 用 Python 重写以提高开发效率
- 采用 `tkinter` 图形库以跨平台适配原生 UI
- 在性能瓶颈处使用 C++ 编写以提高执行效率

## 原理

参考[此处](https://minecraft.fandom.com/zh/wiki/%E5%9C%B0%E5%9B%BE%E7%89%A9%E5%93%81%E6%A0%BC%E5%BC%8F "地图物品格式 - Minecraft Wiki") ~~（绝对不是 lazy）~~

## 警告

SlopeCraftR 仍在开发中，并且由于开发者 [Van-Nya](https://github.com/Van-Nya "@Van-Nya") 的开发能力和空闲时间等因素影响，上述功能的实现均可能无限延迟 ~~（饼先摆在这，人先咕咕咕）~~
