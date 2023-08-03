"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
import poke_api
import image_lib
import ctypes
import sys


# Get the script and images directory
script_name = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_name)
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.isdir(images_dir):
    os.makedirs(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Information")
root.geometry('600x600')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)

# TODO: Set the icon
app_id = 'comp593.pokeImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

# TODO: Create frames
frm = ttk.Frame(root)
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
frm.rowconfigure(0, weight=0)
frm.grid(row=0, column=0, padx=5, pady=5, sticky=(NSEW, EW))

image_path = ''   #Path could be anything

#create list of pull down pokemon names
pokemon_list = poke_api.get_pokemon_names()
pokemon_list.sort()
cbox_poke_sel = ttk.Combobox(frm, values=pokemon_list, state='readonly')
cbox_poke_sel.set("Select a Pokemon")
cbox_poke_sel.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)



def display_pokemon_info():
    selected_pokemon = cbox_poke_sel.get()
    if selected_pokemon:
        poke_info = poke_api.get_pokemon_info(selected_pokemon)
    if poke_info:
        info_height_label.config(text=f"Height: {poke_info.get('height', '')}")
        info_weight_label.config(text=f"Weight: {poke_info.get('weight', '')}")
            
        types = [t['type']['name'] for t in poke_info.get('types', [])]
        info_type_label.config(text=f"Type: {' '.join(types)}")
        stats = poke_info.get('stats', [])

        for stat in stats:    #Running the progressbars
            if stat['stat']['name'] == 'hp':
                stats_hp_bar.config(value = stat['base_stat'])
            elif stat['stat']['name'] == 'attack':
                stats_attack_bar.config(value = stat['base_stat'])
            elif stat['stat']['name'] == 'defense':
                stats_defense_bar.config(value = stat['base_stat'])
            elif stat['stat']['name'] == 'special-attack':
                stats_special_attack_bar.config(value = stat['base_stat'])
            elif stat['stat']['name'] == 'special-defense':
                stats_special_defense_bar.config(value = stat['base_stat'])
            elif stat['stat']['name'] == 'speed':
                stats_speed_bar.config(value = stat['base_stat'])

btn_get_info = ttk.Button(frm, text='Get Info', command=display_pokemon_info)
btn_get_info.grid(row=0, column=1, padx=5, pady=5, sticky=NSEW)


# Create a button to set the desktop background
def handle_set_desktop():
    """Event handler called when the user clicks the 'Set as Desktop Image' button.
    Sets the desktop background image to the current Pokemon display image.
    """
    image_lib.set_desktop_background_image(image_path)

btn_set_desktop = ttk.Button(frm, text='Set as Desktop Image', command=handle_set_desktop)
btn_set_desktop.state(['!disabled'])
btn_set_desktop.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=NSEW)

# TODO: Populate frames with widgets and define event handler functions
info_frame = ttk.Frame(frm, padding=10, relief='sunken')
info_frame.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)

info_height_label = ttk.Label(info_frame, text="Height:")
info_height_label.grid(row=0, column=0, sticky=W)

info_weight_label = ttk.Label(info_frame, text="Weight:")
info_weight_label.grid(row=1, column=0, sticky=W)

info_type_label = ttk.Label(info_frame, text="Type:")
info_type_label.grid(row=2, column=0, sticky=W)

stats_frame = ttk.Frame(frm, padding=10, relief='sunken')
stats_frame.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

stats_hp_label = ttk.Label(stats_frame, text="HP", width=0)
stats_hp_label.grid(row=0, column=0, sticky=EW)

stats_attack_label = ttk.Label(stats_frame, text="Attack", width=0)
stats_attack_label.grid(row=1, column=0, sticky=EW)

stats_defense_label = ttk.Label(stats_frame, text="Defense", width=0)
stats_defense_label.grid(row=2, column=0, sticky=EW)

stats_special_attack_label = ttk.Label(stats_frame, text="Special Attack", width=0)
stats_special_attack_label.grid(row=3, column=0, sticky=EW)

stats_special_defense_label = ttk.Label(stats_frame, text="Special Defense", width=0)
stats_special_defense_label.grid(row=4, column=0, sticky=EW)

stats_speed_label = ttk.Label(stats_frame, text="Speed", width=0)
stats_speed_label.grid(row=5, column=0, sticky=EW)

#Adjusting the bars 
bar_length = 100    
stats_hp_bar = ttk.Progressbar(stats_frame, length=bar_length, mode='determinate')
stats_hp_bar.grid(row=0, column=1, sticky=W)

stats_attack_bar = ttk.Progressbar(stats_frame, length=bar_length, mode='determinate')
stats_attack_bar.grid(row=1, column=1, sticky=W)

stats_defense_bar = ttk.Progressbar(stats_frame, length=bar_length, mode='determinate')
stats_defense_bar.grid(row=2, column=1, sticky=W)

stats_special_attack_bar = ttk.Progressbar(stats_frame, length=bar_length, mode='determinate')
stats_special_attack_bar.grid(row=3, column=1, sticky=W)

stats_special_defense_bar = ttk.Progressbar(stats_frame, length=bar_length, mode='determinate')
stats_special_defense_bar.grid(row=4, column=1, sticky=W)

stats_speed_bar = ttk.Progressbar(stats_frame, length=bar_length, mode='determinate')
stats_speed_bar.grid(row=5, column=1, sticky=W)

root.mainloop()