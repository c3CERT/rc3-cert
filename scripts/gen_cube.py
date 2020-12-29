#!/usr/bin/env python3
#
#Brace yourself, the cube is coming!

from shutil import copyfile, rmtree
from random import randint, choice
import json
import uuid
import os
import string

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


def generate_cubes(uuids):
    with open("cube_assets/quadrat_inventory.json") as inv_File:
        inventory = json.load(inv_File)
        inv_layers = []
        for layer in inventory['layers']:
            if layer['name'].startswith('inv'):
                inv_layers.append(layer)

    for x in range(0, ROOMS):
        template = choice(TEMPLATES)
        output = OUT_DIR + str(uuids[x]) + ".json"
        copyfile(template, output)

        # tile post processing

        with open(output, 'r') as file:
            room = generate_exits(json.load(file), uuids)
            # add decoration
            inv = choice(inv_layers)
            room['layers'][1] = inv

        with open(output, 'w') as file:
            json.dump(room, file)


def generate_exit(uuid_list):
    # generate an exit
    exit_cube = OUT_DIR + str(choice(uuids)) + '.json'

    with open('cube_assets/outcube.json', 'r') as file:
        room = generate_exits(json.load(file), uuid_list)
    with open(exit_cube, 'w') as file:
        json.dump(room, file)
    print("Exitroom: ", exit_cube)


def generate_entry(uuid_list):
    # generate an entry
    entry = OUT_DIR + '0.json'

    with open('cube_assets/incube.json', 'r') as file:
        room = generate_exits(json.load(file), uuid_list)
    with open(entry, 'w') as file:
        json.dump(room, file)
    print("Entryroom: ", entry)


def generate_uuids():
    uuid_list = []
    static_prefix = []
    static_suffix = []
    for n in range(0, 20):
        static_prefix.append(get_random_string(60))
        static_suffix.append(get_random_string(60))

    for n in range(0, ROOMS):
        id = choice(static_prefix) + '-' + str(uuid.uuid4()) + '-' + str(uuid.uuid4()) + '-' + choice(static_suffix)
        uuid_list.append(id)
    return uuid_list


def generate_exits(room_json, uuid_list):
    room = room_json
    for layer_i in range(0, len(room['layers'])):
        if room['layers'][layer_i]['name'].startswith('exit'):
            room['layers'][layer_i]['properties'][0]['value'] = str(choice(uuid_list)) + '.json'
    return room


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str


def cleanup():
    rmtree(OUT_DIR)
    os.mkdir(OUT_DIR)
    return


if __name__ == '__main__':
    cleanup()
    uuids = generate_uuids()
    generate_cubes(uuids)
    generate_entry(uuids)
    generate_exit(uuids)
