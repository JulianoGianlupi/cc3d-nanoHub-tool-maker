# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:20:26 2019

@author: jferrari
"""
import os
import shutil
import sys
source = r'C:\CompuCell3D\Demos\PluginDemos\AdhesionFlexPython' #where the user's simulation files are
dest = r'C:\Users\jferrari\Documents\cc3d-nanohub-settuper-test' #where the git repo is


shortName = 'asdasdasd' #for the -t in the invoke


if not os.path.isdir(source):
    raise Exception('Path of source not found:', source)
else:
    if 'Simulation' not in os.listdir(source):
        raise Exception('Simulation folder not found in:',source)
    else:
        found_cc3d = False
        for name in os.listdir(source):
            if name.endswith('.cc3d'):
                found_cc3d = True
                cc3d_file_name = name.replace('.cc3d','')
        if not found_cc3d:
            raise Exception('.cc3d file not found in:',source)
        

if not os.path.isdir(dest):
    raise Exception('Path of destination not found:', dest)



print("\n\n STEP 1: copying your simulation files\n")
tool_cc3d_files = os.path.join(dest,'main')
print(source, '-->', tool_cc3d_files)
try:
    shutil.copytree(source,tool_cc3d_files)
except: 
    print("unable to copy")


print("\n\n STEP 2: copying critical tool files\n")
for name in os.listdir('.'):
    try:
        if name[0] !='.':
            if os.path.isdir(name):
                source_dir = name
                dest_dir = os.path.join(dest,name)
                print(source_dir, '-->', dest_dir)
                shutil.copytree(source_dir,dest_dir)
            elif not (name == sys.argv[0] or name == "README.md" or name == "tool_maker.py"):
                source_file = name
                dest_file = os.path.join(dest,name)
                print(source_file, '-->', dest_file)
                shutil.copy(source_file,dest_file)
    except:
        print("unable to copy")



print("\n\n STEP 3: renaming files and content\n")

os.chdir(dest)


with open('middleware/invoke', 'r') as f:
    new_text = f.read().replace("-t toolname", "-t " + shortName)

with open('middleware/invoke', 'w') as f:
    f.write(new_text)

old_sh = os.path.join('bin','nh-cc3d-toolname.sh')
new_sh = os.path.join('bin','nh-cc3d-'+shortName+'.sh')

try:
    shutil.move(old_sh,new_sh)
    print('renamed',old_sh,new_sh)
except:
    print("couldn't rename, carying on")

with open(new_sh, 'r') as f:
    new_text = f.read().replace("toolName",cc3d_file_name)

with open(new_sh,'w') as f:
    f.write(new_text)

















