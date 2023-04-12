from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(path):
    res = []
    for _,__,img_Files in walk(path):
        for img in img_Files:
            full_path = path + '/' + img
            res.append(pygame.image.load(full_path).convert_alpha())
    return res
