

import os

path = os.getcwd()

new_path = os.path.join(path,'users.txt')

with open(new_path,'r') as file:
    data = file.read()

print(data)
