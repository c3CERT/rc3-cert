import json

OUT_DIR = "cube"


START_CUBE = '0.json'
cubes = dict()
todo_list = list()
paths = dict()

todo_list.append(START_CUBE)
paths[START_CUBE] = ['START']

def __get_cube(file_url):
    with open(file_url, 'r') as cube:
        data = cube.read()
        jsondata = json.loads(data)
    return data, jsondata


def __is_exit_cube(data, jsondata):
    if data.count('../audio/cube_introduction.mp3') > 0:
        return False
    if data.count('klinik_1.json') == 0:
        return False
    return True


def __parse_cube(url, cube, path):
    data, jsondata = __get_cube(url)
    exits = dict()
    if not __is_exit_cube(data, jsondata):
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
            final_cube, data, jsondata = __parse_cube(cube_url, next_cube, paths[next_cube])
            if final_cube:
                print("Found final cube: %s" % next_cube)
                print("Path length: %s" % (len(paths[next_cube]), ))
                print("Path: %s" % (paths[next_cube], ))
                return len(paths[next_cube])


if __name__ == '__main__':
    determine_path_to_exit()
