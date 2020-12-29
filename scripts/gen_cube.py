#!/usr/bin/env python3
#
# Brace yourself, the cube is coming!

from shutil import copyfile, rmtree
from random import choice, shuffle
import json
import uuid
import os
import string

ROOMS = 1024
MIN_PATH_LENGTH = 10
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


def generate_exit(uuids):
    # generate an exit
    exit_cube = OUT_DIR + str(choice(uuids)) + '.json'
    copyfile('cube_assets/outcube.json', exit_cube)
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
    iterator = 13
    uuid_list = []
    static_prefix = []
    static_suffix = []
    for n in range(0, 20):
        static_prefix.append(get_random_string(60))
        static_suffix.append(get_random_string(15))

    for n in range(0, ROOMS):
        uuids = choice(static_prefix) + '-' + str(uuid.uuid4()) + '-' + str(uuid.uuid4()) + '-' + choice(static_suffix) + str(iterator * n)
        uuid_list.append(uuids)
    return uuid_list


def generate_exits(room_json, uuid_list):
    exits = ['exit1', 'exit2', 'exit3', 'exit4']
    shuffle(exits)
    room = room_json
    for layer_i in range(0, len(room['layers'])):
        if room['layers'][layer_i]['name'].startswith('exit'):
            room['layers'][layer_i]['properties'][0]['value'] = str(choice(uuid_list)) + '.json'
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


def get_cube(file_url):
    with open(file_url, 'r') as cube:
        data = cube.read()
        jsondata = json.loads(data)
    return data, jsondata



def is_exit_cube(data, jsondata):
    if data.count('../audio/cube_introduction.mp3') > 0:
        return False
    if data.count('basement.json') == 0:
        return False
    return True



def parse_cube(url, cube, path):
    data, jsondata = get_cube(url)
    exits = dict()
    if not is_exit_cube(data, jsondata):
        for layer in jsondata["layers"]:
            if isinstance(layer, dict) and "properties" in layer:
                for prop in layer["properties"]:
                    if prop["name"] == "exitUrl":
                        direction = None
                        if layer["data"][13] == 10:
                            direction = "up"
                        elif layer["data"][37] == 10:
                            direction = "left"
                        elif layer["data"][43] == 10:
                            direction = "right"
                        elif layer["data"][67] == 10:
                            direction = "down"
                        if not direction:
                            raise("Failed to determine exit direction. Please fix.")
                        exits[direction] = prop["value"]
                        if prop["value"] not in todo_list and \
                                prop["value"] not in cubes and \
                                prop["value"] != cube:
                            todo_list.append(prop["value"])
                            next_path = path[:]
                            next_path.append(direction)
                            paths[prop["value"]] = next_path
        cubes[cube] = exits
        return False, data, jsondata
    else:
        for layer in jsondata["layers"]:
            if isinstance(layer, dict) and "properties" in layer:
                for prop in layer["properties"]:
                    if prop["name"] == "exitUrl":
                        exits[layer["name"]] = prop["value"]
                        if prop["value"] not in todo_list and \
                                prop["value"] not in cubes:
                            todo_list.append(prop["value"])
        cubes[cube] = exits
        return True, data, jsondata


def determine_path_to_exit():
    while True:
        if not todo_list:
            print("Todo list empty, no exit found")
            return 0
        else:
            next_cube = todo_list.pop(0)
            cube_url = "%s/%s" % (OUT_DIR, next_cube, )
            final_cube, data, jsondata = parse_cube(cube_url, next_cube, paths[next_cube])
            if final_cube:
                print("Found final cube: %s" % next_cube)
                print("Path length: %s" % (len(paths[next_cube]), ))
                print("Path: %s" % (paths[next_cube], ))
                return len(paths[next_cube])


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
        generate_cubes(id_list)
        generate_entry(id_list)
        generate_exit(id_list)
        print("Checking path length to exit:")
        path_length = determine_path_to_exit()
