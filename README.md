# PokePalette

[![license](https://img.shields.io/github/license/CDWimmer/PokePalette?style=flat-square)](/LICENCE)
[![pyversion](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)]()
[![stars](https://img.shields.io/github/stars/CDWimmer/PokePalette?style=flat-square)]()
[![size](https://img.shields.io/github/languages/code-size/CDWimmer/PokePalette?style=flat-square)]()
[![coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-ko--fi.com%2Fch4rl1e-orange?link=https://ko-fi.com/ch4rl1e&style=social)](https://ko-fi.com/ch4rl1e)

649 Pokémon, broken down into CSVs of their RGB colour palettes. 

Complete with a Python library to convert names or Pokédex IDs into either #hex colours, or MatPlotLib compatible ListedColormaps.

---

The individual CSV files of the palettes as RGB values can be found in the [palettes](/palettes) directory.

## Requirements:
- numpy
- matplotlib (optional)

## Usage:

### Hex values
```python
>>> import pokepalette
>>> my_palette = pokepalette.get_palette(f"torchic")
>>> print(my_palette)
['#fe8a30', '#000000', '#f5dd69', '#e5591f', '#ab8a00', '#edbc30', '#ab400f', '#feab51', '#8a511f', '#7a4917', '#fefefe']
```



### `matplotlib` ListedColormaps Generator
Naturally this requires matplotlib be installed. 
```python
>>> import pokepalette
>>> newcmp = pokepalette.get_colormap(f"torchic")
```


`newcmp` can then be inserted anywhere that takes a qualitative colourmap. A demo viewer for this is included in `pokepalette_viewer`:

```python
>>> import pokepalette_viewer
>>> pokepalette_viewer.view("torchic")
```
![torchic colour palette](https://i.imgur.com/JEfZjBs.png)

### Colour Picker
There is also included a rudimentary "colour picker" GUI tool that displays all colours as clickable buttons, which copies the clicked hex code to your clipboard.
Text entry box accepts both names and IDs. 
```python
>>> import pokepalette_viewer
>>> pokepalette_viewer.picker(pokemon=255, on_top=True)  # torchic = 255
```
![torchic_colour_picker](https://i.imgur.com/WF2ztLz.png)

---
###### And yes, it's using the proper spelling of "colour" internally.
[![Twitter Follow](https://img.shields.io/twitter/follow/CharlesDWimmer?label=Follow%20me&logoColor=orange&style=social)](https://twitter.com/CharlesDWimmer)
