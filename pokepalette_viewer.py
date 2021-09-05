"""
Helper functions to view the matplotlib colourmap of, or pick from, the palette of a pokemon.
"""

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import pokepalette
from tkinter import *
from functools import partial
from typing import Union
import pokes_list


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
    """
    Display the listedcolourmap of a pokemon.
    """
    colours = pokepalette.get_colours_array(pokemon)
    newcmp = ListedColormap(colours)
    print(pokepalette.rgb_to_hex(colours))
    _plot_example(newcmp)


def invert_rgb(rgb_array, floating_point=False) -> list:
    """
    Inverts a numpy array of RGB values. Supports both ints (0-255) and floating point (0-1) formats.
    """
    if floating_point:
        return 1 - rgb_array
    else:
        return 255 - rgb_array


def picker(pokemon: Union[str, int] = 1, on_top: bool = True):
    """
    Create a GUI colour palette picker window, optionally set the initial `pokemon` by name or id.
    Clicking the buttons will put that colour on the clipboard.
    setting `on_top` to True will make the window try to appear on top of all other windows.
    """
    root = Tk()

    root.title("Palette Picker")
    root.resizable(0, 0)
    root.attributes("-toolwindow", 1)
    if on_top:
        root.wm_attributes("-topmost", 1)
    text = StringVar()
    text.set("Click a button to copy it to clipboard")
    label = Label(root, textvariable=text, width=40)
    label.pack()

    colour_buttons = []  # list to store buttons of colours
    poke_name_entry_text = StringVar(root, value=pokemon)
    poke_name_entry = Entry(root, textvariable=poke_name_entry_text)
    poke_name_entry.pack()

    def set_pokemon_name():
        new_name = poke_name_entry_text.get()
        if new_name.isnumeric():
            poke_id = int(new_name)
            if 0 < poke_id <= len(pokes_list.all_pokes):
                new_name = pokes_list.all_pokes[poke_id - 1]
            else:
                text.set(f"Invalid or unknown ID '{poke_id}'!")
                return
        elif new_name.lower() not in pokes_list.all_pokes:
            text.set("Unknown pokemon name!")
            return

        text.set(f"Loaded {new_name.capitalize()}.")
        poke_name_entry_text.set(new_name.lower())
        for btn in colour_buttons:
            btn.pack_forget()
            btn.destroy()
        make_buttons()

    load_poke_button = Button(root, text="Load pokemon", command=set_pokemon_name)
    load_poke_button.pack()

    def clipboard_me(colour):
        # root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(colour)
        root.update()
        text.set(f"Copied {colour} to clipboard. ")

    def make_buttons():
        rgb_array = pokepalette.get_palette(poke_name_entry_text.get(), style='rgb')
        inverted_rgb_array = invert_rgb(rgb_array, floating_point=True)
        inverted_hex_array = pokepalette.rgb_to_hex(inverted_rgb_array)  # invert for the button labels
        hex_array = pokepalette.get_palette(poke_name_entry_text.get(), style='hex')
        colour_pairs = zip(hex_array, inverted_hex_array)
        for colour in colour_pairs:
            # take the zip list of hex strings and make buttons for each of them
            new_btn = Button(root, text=colour[0], command=partial(clipboard_me, colour[0]), bg=colour[0],
                             fg=colour[1], width=20, height=1, font="sans 11 bold")
            new_btn.pack()
            colour_buttons.append(new_btn)

    make_buttons()
    root.mainloop()


if __name__ == '__main__':
    view("torchic")
    picker("torchic")
