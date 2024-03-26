import ast
import datetime
from collections import OrderedDict

def combine_dicts(file_path):
    merged_dict = OrderedDict()
    out={}
    order_of_countries = []

    with open(file_path, 'r') as file:
        dat=""
        for line in file:
            data = ast.literal_eval(line)
            may_data=data
            for country, files in data.items():
                if country not in merged_dict:
                    my_file=""
                    merged_dict[country] = OrderedDict.fromkeys(files)
                    order_of_countries.append(country)
                else:
                    my_file=""
                    existing_files = merged_dict[country].keys()
                    new_files = [file for file in files if file not in existing_files]
                    merged_data=''
                    merged_dict[country].update(OrderedDict.fromkeys(new_files))

    return merged_dict, order_of_countries

file_path = 'file_mapping.txt'
path=""
result, order_of_countries = combine_dicts(file_path)
for country, files in result.items():
    file_name=files
    # print(f"{country}: {list(files.keys())}")
    for f in files:
   	    print(f)
