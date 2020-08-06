Example plugin for Blender v2.83.4

### The right python version
When creating a new project, simply create a new virtual environment
using the current blender install as a base.

For example, when this project was created, the venv was pointed to:
`/media/Data/WybeData/Tools/Blender/blender-2.83.4-linux64/2.83/python/bin/python3.7m`

### Autocomplete module
To get autocomplete in pycharm (or other ide's),
download the 2.83 autocomplete module from:\
https://github.com/Korchy/blender_autocomplete

To connect it to a pycharm project (instructions from [here](https://b3d.interplanety.org/en/using-external-ide-pycharm-for-writing-blender-scripts/))
- "File -> Settings"
- "Project: <name of project> -> Project structure"
- "Add content root"
- Add the 2.83 directory.
  When this project was generated it was: `/media/Data/WybeData/Tools/Blender/blender_autocomplete_modules/2.83`