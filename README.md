# CompuCell3D's script for generating nanoHub tools repository

This script was made to make the generation of GitHub repositories to deploy CompuCell3D tools an easier task.

##Requirements:
* Python 3
* Be able to run 'python' from the command line. You can 1) edit your PATH system variable, 2) provide the full path command, or 3) create an alias.
* GitHub account
* NanoHub account

## How to use:

1. Dowload / Clone this repository to your machine.
1. Create a GitHub repository where you're going to have your nanoHub tool ("tool repo"). Have it cloned to your computer.
1. On a command line from the cc3d-nanoHub-settuper directory on your machine call the script ```tool_maker.py```. If successfull it'll copy all the necessary files for the nanoHub tool. You will provide three arguments to the script:
```
python tool_maker.py <short tool name> <full-path-to-new-tool-directory> <full-path-to-your-cc3d-project>
```
The ```<short tool name>``` needs to be between 3 and 15 alphanumeric characters without spaces. The ```<full-path-to-your-cc3d-project>``` is where the ```.cc3d``` of your CompuCell3D simulation is. ```<full-path-to-new-tool-directory>``` is the tool repo.

If you're using Windows some files might have lost run permissions. You need to check two files in your tool repo:
1. ```invoke``` file in the ```middleware``` subdirectory,
1. And the ```.sh``` file in the ```bin``` subdirectory.
