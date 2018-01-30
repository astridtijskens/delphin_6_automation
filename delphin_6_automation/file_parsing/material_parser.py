# Imports:
import os
import codecs
import re
import datetime



# Functions:
def isfloat(num):
    try:
        float(num)
    except ValueError:
        return False
    else:
        return True


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def material_file_to_dict(file_path):

    material_dict = {}
    data = codecs.open(file_path, "r", "utf-8")

    sub_key = ""
    n = 0

    for line in data:

        if line.split(" ")[0] == "D6MARLZ!":
            material_dict["INFO-MAGIC_HEADER"] = line.strip("\n")
            material_dict["INFO-LAST_MODIFIED"] = datetime.datetime.now()
            material_dict["INFO-MATERIAL_NAME"] = os.path.split(file_path)[-1].split("_")[0]
            material_dict["INFO-UNIQUE_ID"] = int(os.path.split(file_path)[-1].split("_")[1].split(".")[0])
            material_dict["INFO-FILE"] = file_path

        elif line[0] == "[":
            main_key = re.sub('[\[\]\n]', '', line)
            name = ""

        elif line[0] == " " and line[3] != " " and "=" in line:
            # dictionary keys
            sub_key = line.split("=")[0].strip()
            key = main_key + "-" + sub_key

            # dictionary data 01
            data = line.split("=")[1].strip()

            if len(data.split(" ")) == 2 and isfloat(data.split(" ")[0]):
                data = num(data.split()[0])
                material_dict[key] = data

            elif line.split("=")[0].strip() == "FUNCTION":
                sub_key_func = line.split("=")[1].strip()
            else:
                material_dict[key] = data

        elif sub_key == "FUNCTION" and len(line) > 5:
            if line[5] == " ":
                n += 1

                data = line.split(" ")
                data = [x for x in data if x]
                data.remove("\n")
                data = [num(i) for i in data]

                key = main_key + "-FUNCTION-" + sub_key_func

                if n  % 2 != 0: #ulige linjer (1)
                    key = key + "-X"
                    material_dict[key] = data

                else: #lige linjer (2)
                    key = key + "-Y"
                    material_dict[key] = data

            elif line[2] == "[":
                sub_key_func = "MODEL"

            elif line[2] == " " and sub_key_func == "MODEL":
                key = main_key + sub_key_func + line.split("=")[0].strip()
                data  = line.split("=")[1].strip()
                #print(data)

                if isfloat(data):
                    data = data.split(" ")
                    data = [num(i) for i in data]

                material_dict[key] = data
        else:
            name = ""

    return material_dict


def dict_to_m6(material: dict, path: str) -> bool:
    """
    Takes an material dict and converts it into a .m6 file.

    :param material: material dict
    :param path: Path to where .m6 should be placed.
    :return: True
    """

    # TODO - Create function
    return True