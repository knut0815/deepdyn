import os

# Working directory path.(Project root folder)

path = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(path, 'data')
output_path = os.path.join(path, 'out')
conf_path = os.path.join(path,'conf')

