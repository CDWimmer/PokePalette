import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import pokepalette


def _plot_example(colormap):
    """
    Helper function to plot data with associated colormap.
    Adapted from matplotlib documentation pages.
    https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html
    """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)
    fig, ax = plt.subplots(figsize=(4, 3),
                            constrained_layout=True, squeeze=False)
    psm = ax.flat[0].pcolormesh(data, cmap=colormap, rasterized=True, vmin=-4, vmax=4)
    fig.colorbar(psm, ax=ax)
    plt.show()


def view(pokemon):
    colours = pokepalette.get_colours_array(pokemon)
    newcmp = ListedColormap(colours)
    print(pokepalette.rgb_to_hex(colours))
    _plot_example(newcmp)


if __name__ == '__main__':
    view("torchic")
