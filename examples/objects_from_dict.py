'''
Usage example for dict_wrangler.

Get custom objects from a Python dictionary
'''
import txt_wrangler as tw
import dict_wrangler as dw
import os
import json

# Defines path to the main file to analyse as well as the modules path
os.chdir(__file__.rpartition(os.sep)[0])
main_file = r"main.txt"
tw.modules_folders = r'.\txt_wrangler\modules'
dw.modules_folders = r'.\dict_wrangler\modules'

print tw.modules_folders
print dw.modules_folders

# Reads the file using text_wrangler
contents_dictionary = tw.read_file(main_file)
print contents_dictionary
print json.dumps(contents_dictionary, indent=4)

# Get objects from dictionary using dict_wrangler
objects_from_dict = dw.read_dict(contents_dictionary)
print objects_from_dict
