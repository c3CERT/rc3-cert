#!/usr/bin/env python3
#
#Brace yourself, the cube is coming!

from shutil import copyfile
from random import randint, choice
import json
ROOMS = 256
OUT_DIR = "cube/"
TEMPLATES = ["cube_assets/quadrat_t1.json",
             "cube_assets/quadrat_t2.json",
             "cube_assets/quadrat_t3.json",
             "cube_assets/quadrat_t4.json",
             "cube_assets/quadrat_t5.json",
             "cube_assets/quadrat_t6.json",
             "cube_assets/quadrat_t7.json",
             "cube_assets/quadrat_t8.json",
             "cube_assets/quadrat_t9.json",
             "cube_assets/quadrat_darkness.json"
             ]

with open("cube_assets/quadrat_inventory.json") as inv_File:
    inventory = json.load(inv_File)
    inv_layers = []
    for layer in inventory['layers']:
        if layer['name'].startswith('inv'):
            inv_layers.append(layer)

for x in range(0,ROOMS):
    template = choice(TEMPLATES)
    output = OUT_DIR + str(x) + ".json"
    copyfile(template, output)

    #tile post processing


    with open(output, 'r') as file:
        room = json.load(file)
        for layer_i in range(0, len(room['layers'])):
            if room['layers'][layer_i]['name'].startswith('exit'):
                room['layers'][layer_i]['properties'][0]['value'] = str(randint(0,ROOMS-1)) + '.json'
        # add decoration
        inv = choice(inv_layers)
        room['layers'][1]=inv

    with open(output, 'w') as file:
        json.dump(room, file)

## generate an exit
exit = str(randint(0,200))+'.json'
copyfile('cube_assets/outcube.json', OUT_DIR + exit)
print("Exitroom: ", exit)

# generate an entry
entry = '0.json'
copyfile('cube_assets/incube.json', OUT_DIR + entry)
print("Entryroom: ", entry)

# generate the exits for the incube
with open (OUT_DIR+entry, 'r') as incube:
    room_incube = json.load(incube)
    for layer_incube in range(0, len(room_incube['layers'])):
        if room_incube['layers'][layer_incube]['name'].startswith('exit'):
            room_incube['layers'][layer_incube]['properties'][0]['value'] = str(randint(0, ROOMS-1)) + '.json'