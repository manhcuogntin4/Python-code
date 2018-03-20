import os
import cv2
import xml.etree.ElementTree as ET
import glob

DATA_DIR = './' # to be customized

def check(obj_name):
    return  obj_name == 'nom' or obj_name == 'prenom' \
        or obj_name == 'datenaissance' or obj_name == 'mrz2' \
        or obj_name == 'lieu' or obj_name == 'mrz1' \
        or obj_name == 'mrz' or obj_name=="nomepouse" or obj_name=="person"


def parse_rec(filename):
    """ Parse a PASCAL VOC xml file """
    tree = ET.parse(filename)
    print tree
    objects = []
    for obj in tree.findall('object'):
        print obj.find('name').text
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(bbox.find('xmin').text) - 1,
                              int(bbox.find('ymin').text) - 1,
                              int(bbox.find('xmax').text) - 1,
                              int(bbox.find('ymax').text) - 1]
        objects.append(obj_struct)

    return objects


def readFolder(strFolderName):
    file_list = []
    st=strFolderName+"*.xml"
    for filename in glob.glob(st): #assuming gif
        file_list.append(filename)
    return file_list

def check_annot(person_ymin, person_ymax, value):
    if value >person_ymin and value<person_ymax or value==0:
        return True
    return False

if __name__ == '__main__':
    xlm_list=readFolder(DATA_DIR)
    print xlm_list
    file_error =open("error.txt", "a")
    prenom_error=open("prenom.txt", "a")
    for file in xlm_list:
        print file
        objects=parse_rec(file)
        check=False
        person_ymin, person_ymax=0,0
        prenom_ymin, prenom_ymax=0,0
        nom_ymin, nom_ymax=0,0
        nomepouse_ymin, nomepouse_ymax=0,0
        for obj in objects:
            if obj['name']=='person':
                person_ymin=obj['bbox'][1]
                person_ymax=obj['bbox'][3]
            if obj['name']=='nom':
                nom_ymin=obj['bbox'][1]
                nom_ymax=obj['bbox'][3]
            if obj['name']=='prenom':
                prenom_ymin=obj['bbox'][1]
                prenom_ymax=obj['bbox'][3]
            if obj['name']=='nomepouse':
                nomepouse_ymin=obj['bbox'][1]
                nomepouse_ymax=obj['bbox'][3]
        h_nom=nom_ymax - nom_ymin
        h_prenom=prenom_ymax - prenom_ymin
        if h_prenom>1.6*h_nom:
            prenom_error.write(file)
            prenom_error.write('\n')
        ls_cord=[nom_ymax, prenom_ymin, prenom_ymax, nomepouse_ymin, nomepouse_ymax]
        for cord in ls_cord:
            if check_annot(person_ymin, person_ymax, cord)==False:
                file_error.write(file)
                file_error.write("\n")