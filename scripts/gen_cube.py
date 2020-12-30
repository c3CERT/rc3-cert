#!/usr/bin/env python3
#
# Brace yourself, the cube is coming!

from shutil import copyfile, rmtree
from random import choice, shuffle, randint
import json
import uuid
import os
import string
import solve_cube

ROOMS = 128
MIN_PATH_LENGTH = 40
PATH_LENGTH = 50
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


START_CUBE = '0.json'
cubes = dict()
todo_list = list()
paths = dict()

todo_list.append(START_CUBE)
paths[START_CUBE] = ['START']


def generate_cubes(random_uuids, path_uuid_list):
    with open("cube_assets/quadrat_inventory.json") as inv_File:
        inventory = json.load(inv_File)
        inv_layers = []
        for layer in inventory['layers']:
            if layer['name'].startswith('inv'):
                inv_layers.append(layer)

    for x in range(0, ROOMS):
        template = choice(TEMPLATES)
        if x < PATH_LENGTH:
            output = OUT_DIR + path_uuid_list.pop(0) + ".json"
            copyfile(template, output)
        else:
            output = OUT_DIR + str(random_uuids[x-PATH_LENGTH]) + ".json"
            copyfile(template, output)
        # tile post processing
        with open(output, 'r') as file:
            if x < PATH_LENGTH:
                if x == 49:
                    # dirty hack
                    path_uuid_list.append("Dirty hack due to call by reference")
                room = generate_exits(json.load(file), random_uuids, path=True, path_exit_uuid=path_uuid_list[0])
            else:
                room = generate_exits(json.load(file), random_uuids)
            # add decoration
            inv = choice(inv_layers)
            room['layers'][1] = inv

        with open(output, 'w') as file:
            json.dump(room, file)


def generate_exit(path_uuid):
    # generate an exit
    exit_cube = OUT_DIR + path_uuid + '.json'
    copyfile('cube_assets/outcube.json', exit_cube)
    print("Exitroom: ", exit_cube)


def generate_entry(random_uuids, path_uuid):
    # generate an entry
    entry = OUT_DIR + '0.json'
    with open('cube_assets/incube.json', 'r') as file:
        room = generate_exits(json.load(file), random_uuids, path=True, path_exit_uuid=path_uuid)
    with open(entry, 'w') as file:
        json.dump(room, file)
    print("Entryroom: ", entry)


def generate_uuids():
    iterator = 17
    uuid_list = []
    static_prefix = []
    static_suffix = []
    for n in range(0, 1):
        static_prefix.append(get_random_string(6))
        static_suffix.append(get_random_string(4))

    for n in range(0, ROOMS):
        uuids = choice(static_prefix) + '-' + str(uuid.uuid4()) + '-' + choice(static_suffix) + str(iterator * n)
        uuid_list.append(uuids)
    return uuid_list


def generate_exits(room_json, uuid_list, path=False, path_exit_uuid=""):
    exits = ['exit1', 'exit2', 'exit3', 'exit4']
    shuffle(exits)
    room = room_json
    id_list = []
    if path:
        id_list.append(path_exit_uuid)
        for x in range(0, 3):
            id_list.append(choice(uuid_list))
    else:
        for x in range(0, 4):
            id_list.append(choice(uuid_list))
    shuffle(id_list)
    for layer_i in range(0, len(room['layers'])):
        if room['layers'][layer_i]['name'].startswith('exit'):
            room['layers'][layer_i]['properties'][0]['value'] = str(id_list.pop()) + '.json'
            room['layers'][layer_i]['name'] = exits.pop(0)
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
    path_length = 0
    while path_length < MIN_PATH_LENGTH:
        cleanup()
        cubes = dict()
        todo_list = list()
        paths = dict()

        todo_list.append(START_CUBE)
        paths[START_CUBE] = ['START']
        id_list = generate_uuids()
        shuffle(id_list)
        random_uuids = id_list[PATH_LENGTH:]
        path_uuids = id_list[:PATH_LENGTH]
        for i in range(0, 5):
            random_uuids.append(choice(path_uuids[0:10]))
        exit_uuid = path_uuids[-1]
        generate_entry(random_uuids=random_uuids, path_uuid=path_uuids[0])
        generate_cubes(random_uuids=random_uuids, path_uuid_list=path_uuids)
        generate_exit(path_uuid=exit_uuid)
        print("Checking path length to exit:")
        path_length = solve_cube.determine_path_to_exit()
