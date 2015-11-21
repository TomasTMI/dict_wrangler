'''
Usage example for dict_wrangler.

Get custom objects from a Python dictionary
'''
import dict_wrangler as dw
import os

# Defines path to the modules to be used
os.chdir(__file__.rpartition(os.sep)[0])
dw.modules_folders = r'.\modules'

data = {'type': 'file', 'value': [{'type': 'block', 'value': [{'type': 'name', 'value': '1FirstBlock'}, {'type': 'legs', 'value': 3}, {'type': 'comment', 'value': 'Comment in block'}, {'type': 'author', 'value': 'David Martinez'}]}, {'type': 'file', 'value': [{'type': 'block', 'value': [{'type': 'name', 'value': '2FirstBlock'}, {'type': 'legs', 'value': 8}, {'type': 'author', 'value': 'Mr. Brown'}]}, {'type': 'comment', 'value': 'Comment between blocks (in file)'}, {'type': 'block', 'value': [{'type': 'name', 'value': '2SecondBlock'}, {'type': 'legs', 'value': 13}, {'type': 'author', 'value': 'Mr. Lewis'}]}, {'type': 'file', 'value': [{'type': 'block', 'value': [{'type': 'name', 'value': '3FirstBlock'}, {'type': 'legs', 'value': 8}, {'type': 'author', 'value': 'Shakespeare'}]}, {'type': 'block', 'value': [{'type': 'name', 'value': '3SecondBlock'}, {'type': 'legs', 'value': 13}, {'type': 'author', 'value': 'Mr .Rilett'}]}, {'type': 'block', 'value': [{'type': 'name', 'value': '3ThirdBlock'}, {'type': 'legs', 'value': 22}, {'type': 'comment', 'value': 'Comment in block (in file)'}, {'type': 'author', 'value': 'Holden'}]}], 'file': '.\\data\\3rd.txt'}, {'type': 'block', 'value': [{'type': 'name', 'value': '2ThirdBlock'}, {'type': 'legs', 'value': 22}, {'type': 'author', 'value': 'Martin'}]}], 'file': '.\\data\\2nd.txt'}, {'type': 'block', 'value': [{'type': 'name', 'value': '1SecondBlock'}, {'type': 'legs', 'value': 23}, {'type': 'author', 'value': 'John Smith'}]}, {'type': 'comment', 'value': 'Comment between blocks'}, {'type': 'block', 'value': [{'type': 'name', 'value': '1ThirdBlock'}, {'type': 'legs', 'value': 2}, {'type': 'author', 'value': 'Tony Stark'}]}], 'file': '.\\data\\main.txt'}


# Get objects from dictionary using dict_wrangler
objects_from_dict = dw.read_dict(data)

for object in objects_from_dict:
    if object.parent.__repr__() == 'ROOT':
        print "( ROOT ) ... ",
    if object.parent.__repr__() == 'block':
        print "( Block ) ... ", object.__repr__(),
    elif object.parent.__repr__() == 'file':
        print "(", object.parent.name, ") ... ",
    if object.__repr__() == 'file':
        print object.name
    elif object.__repr__() == 'block':
        print "Block"
    else:
        print object.value
