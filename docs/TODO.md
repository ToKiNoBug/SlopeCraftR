# TODO

- 预处理
  - [ ] 图片编辑
  - [x] 透明像素

- 色彩转换
  - [x] RGB
  - [x] HSV
  - [x] LAB
  - [x] XYZ

- 构建 3D 结构
  - [x] 无损压缩
  - [ ] 有损压缩
  - [ ] AI搭路

- 导出成品
  - [x] 地图文件
  - [ ] 结构方块文件
  - [x] 投影原理图
  - [ ] WE 原理图

## 流程图

```mermaid
flowchart LR
  Start([开始])
  Stop([结束])

  subgraph Import [导入与编辑图片]
  direction TB
    input_pic[/选择图片/]
    edit(编辑图片)
    mix[选择半透明\n像素混合方式]
  end

  subgraph Setting [设置颜色与方块]
  direction TB
    version[游戏版本]
    colors[基色列表]
    blocks[方块列表]
  end

  subgraph Convert [色彩转换]
  direction TB
    algo[选择色彩转换算法]
    shrink(色彩抖动)
    convert[转换色彩]
  end

  subgraph Export [导出地图与原理图]
  direction TB
    file[纯文件]
    3d[3D原理图]
    output_map[/导出地图/]
    output_3d[/导出3D原理图/]
    zip(无损压缩)
    zip_(有损压缩)
    structure[结构文件]
    litematica[投影原理图]
  end


Start
--> Import
--> Setting
--> Convert
--> Export
--> Stop

input_pic --> mix
input_pic -.可选.-> edit -.-> mix

version --> colors --> blocks

algo --> convert
algo -.可选.-> shrink -.-> convert

file --> output_map
3d --> output_map
3d --> output_3d
3d -.可选.-> zip & zip_ -.-> output_3d
output_3d --> structure & litematica
```
