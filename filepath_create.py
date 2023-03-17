import os


def filepath_generator(dir_path):
    filepath_list = []
    for filename in os.listdir(dir_path):
        filepath = dir_path + filename
        filepath_list.append(filepath)
    return filepath_list
