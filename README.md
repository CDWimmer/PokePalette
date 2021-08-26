# PokePalette

![license](https://img.shields.io/github/license/CDWimmer/PokePalette?style=flat-square)
![stars](https://img.shields.io/github/stars/CDWimmer/PokePalette?style=flat-square)
![size](https://img.shields.io/github/languages/code-size/CDWimmer/PokePalette?style=flat-square)

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
>>> newcmp = pokepalette.get_colormap("torchic")
```


`newcmp` can then be inserted anywhere that takes a qualitative colourmap. A demo viewer for this is included in `pokepalette_viewer`:

```python
>>> import pokepalette_viewer
>>> pokepalette_viewer.view("torchic")
```
![torchic colour palette](https://i.imgur.com/JEfZjBs.png)

---
###### And yes, it's using the proper spelling of "colour" internally.
![Twitter Follow](https://img.shields.io/twitter/follow/CharlesDWimmer?label=Follow%20me&logoColor=orange&style=social)