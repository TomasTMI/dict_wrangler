'''
Usage example for dict_wrangler.

Get custom objects from a Python dictionary
'''
import dict_wrangler as dw
import os

# Defines path to the main file to analyse as well as the modules path
os.chdir(__file__.rpartition(os.sep)[0])
main_dict = {'name': 'David', 'last': 'Martinez', 'data': {'country': 'Spain'}}
dw.modules_folder = r'.\modules'

# Reads the file using text_wrangler
objects_from_dict = dw.read_dict(main_dict)
print objects_from_dict
