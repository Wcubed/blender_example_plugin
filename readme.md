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

### Install add-on into blender

One way to install the add-on in blender, while automatically keeping
it up-to-date while writing code is to add a simlink to the `src` folder
into the blender addons directory.

In my case that would be: `/home/<username>/.config/blender/2.83/scripts/addons`.

The plugin will then appear in the blender addons selector after refreshing the
list, and can then be enabled.

Don't forget to run blender from a terminal, so that you can see
 the output of `print` calls.
 
 To reload all add-ons call "reload scripts" either from the spacebar menu or by binding a key to `script.reload`.