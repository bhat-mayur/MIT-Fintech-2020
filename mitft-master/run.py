# File Imports
import os
from Settings import filename, output_filename
from Code.Main_Code import main_algorithm
from Code.General_Utils import *

# Find the current directory path
dir_path = os.path.dirname(os.path.realpath(__file__))

# Assign Directories
directories=get_directory_paths(dir_path)

# Pull Data In
in_file=directories['data']+filename

# Write out data
out_file=directories['data']+output_filename

# Execute
execute=main_algorithm(in_file, out_file)
