# SlopeCraftR

**English** | [中文](README_cn.md "README_cn.md")  <!-- lang  -->

> Get your map pixel art (all kinds of!) in Minecraft

SlopeCraftR (abbreviated as SCR) is a tool **rewritten** from [SlopeCraft](https://github.com/ToKiNoBug/SlopeCraft "ToKiNoBug/SlopeCraft") of [ToKiNoBug](https://github.com/ToKiNoBug "@ToKiNoBug"), which can convert pictures to Minecraft map pixel art with *as high as possible color reproduction*, and export as *schematic which can build in game* or *map data file(s)*

## Features

### Functions

- Aim at display effect of **map** (`minecraft:filled_map`) instead of viewing effect of pixel art
- Provide block lists which can deeply customize and some presets
- Provide various algorithm to convert images to map pixel arts
- Supported export format
  - [Map file](https://minecraft.fandom.com/wiki/Map_item_format "Map item format - Minecraft Wiki")
  - [Structure block file](https://minecraft.fandom.com/wiki/Structure_Block_file_format "Structure Block file format - Minecraft Wiki")
  - [Litematica mod schematic](https://github.com/maruohon/litematica "maruohon/litematica")
  - [worldEdit mod schematic](https://github.com/EngineHub/WorldEdit "EngineHub/WorldEdit") (in consideration)

### Development

- Rewrite by Python to improve development efficiency
- Use `tkinter` graphics library to adapt to native UI cross-platform
- Use C++ on performance bottleneck to improve execution efficiency

## Principle

See [here](https://minecraft.fandom.com/wiki/Map_item_format "Map item format - Minecraft Wiki") ~~(absolutely not lazy)~~

## Warning

SLopeCraftR is still on development, and the implement of all functions above will delay indefinitely because of the poor developing skill and free time of developer [Van-Nya](https://github.com/Van-Nya "@Van-Nya") ~~(leave a todo list and keep lazy)~~
