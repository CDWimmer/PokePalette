import numpy as np
from typing import Union
from pokes_list import all_pokes
try:
    # optional dependency
    from matplotlib.colors import ListedColormap
except ModuleNotFoundError as e:
    ListedColormap = e


def rgb_to_hex(colours) -> list:
    """
    Turn a tuple/list/array of rgb values into a list of hex colour values.
    """
    # inspired by https://stackoverflow.com/a/43004474/9311137
    as_ints = np.array(colours * 255, dtype=int)  # convert to int
    return ['#%02x%02x%02x' % (r, g, b) for r, g, b in as_ints]  # wtf


def hex_to_rgb(hex_colour: str, floating_point=False) -> tuple:
    """
    Turn a single hex colour value (#112233) into a tuple of R, G, B as ints (0-255) or, if floating_points is set to
     True, floats (0-1).
    """
    # Adapted from https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
    value = hex_colour.lstrip('#')
    lv = len(value)
    if floating_point:
        return tuple(int(value[i:i + lv // 3], 16) / 255 for i in range(0, lv, lv // 3))
    else:
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def verify_pokemon_name(pokemon: Union[str, int]) -> Union[str, None]:
    """
    Verifies that a pokemon name or ID is known to this package and will return the name if it is.
    Otherwise returns None.
    """
    if isinstance(pokemon, int):
        if pokemon < 1:
            raise RuntimeError(f"Pokemon ID cannot be less than 1.")
        if pokemon > len(all_pokes):
            raise RuntimeError(f"Pokemon with ID {pokemon} does not exist in this package!")
        else:
            return all_pokes[pokemon - 1]
    elif isinstance(pokemon, str):
        if pokemon.lower() in all_pokes:
            return pokemon


def get_colours_array(pokemon: Union[str, int]) -> np.ndarray:
    """Return the numpy array of the colour palette for a given pokemon name/id"""
    if p_name := verify_pokemon_name(pokemon):
        return np.loadtxt(f"palettes/{p_name}.csv", dtype=float)


def get_palette(pokemon: Union[str, int], style: str = "hex") -> Union[list, np.ndarray]:
    """
    Get a colour palette as either a list of hex value strings ([#112233, #...], or as a numpy array of rgb
    values: [[r, g, b], [r, g, b], ...]
    """
    if style.lower() == "hex":
        return rgb_to_hex(get_colours_array(pokemon))
    elif style.lower() == "rgb":
        return get_colours_array(pokemon)
    else:
        raise NotImplementedError("The supported colour formats are hex and RGB.")


def get_colourmap(pokemon: Union[str, int]) -> ListedColormap:
    """
    Turns a stored colour palette into a matplotlib ListedColormap.
    Will throw an error if matplotlib isn't available.
    """
    if isinstance(ListedColormap, ModuleNotFoundError):
        raise ListedColormap  # throw error if matplotlib not present
    colours = get_colours_array(pokemon)
    return ListedColormap(colours)


get_colormap = get_colourmap

if __name__ == '__main__':
    pass
