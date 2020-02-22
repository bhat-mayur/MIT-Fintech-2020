# Imports
import pandas as pd
import os

def get_directory_paths(dir_path):
    # Specify Directories in this project
    directories={
        "data": dir_path + "/data/"
    }
    return directories

# A function to pull in CSV data
def parse_csv_json_data (in_file, output_type='pandas', index_col=False, nrows=0):
    if ".csv" in in_file.lower():
        # Read in csv file as dataframe
        if nrows>0:
            dataframe=pd.read_csv(in_file, nrows=nrows)
        else:
            dataframe=pd.read_csv(in_file)
    elif ".json" in in_file.lower():
        # Read in json file as dataframe
        dataframe=pd.read_json(in_file)
    else:
        print ('file format not recognized')
    # Determine Output Format
    if output_type=='pandas':
        data_out=dataframe
    elif output_type=='dict':
        data_out=dataframe.to_dict()
    elif output_type=='numpy':
        data_out=dataframe.values()
    else:
        print ('output format not recognized')
    # Return Output
    return data_out

# Define a function to pull and then write any file data
def write_data(out_pd_data, out_file, output_file_type='csv'):
    if output_file_type=='csv':
        out_pd_data.to_csv(out_file, index=False)
    elif output_file_type=='tab':
        out_pd_data.to_csv(out_file, sep='\t', index=False)
    elif output_file_type=='json':
        out_pd_data.to_json(out_file)
