bl_info = {
    "name": "Blender example add-on",
    "author": "Wybe Westra",
    "version": (0, 0, 1),
    "blender": (2, 83, 4),
    "warning": "This is a beta version!",
    "category": "Generic",
}

if "bpy" in locals():
    # Allow for reloading the script.
    import importlib

    importlib.reload(registration)
else:
    from . import registration

import bpy


def register():
    registration.register_all()


def unregister():
    registration.unregister_all()


if __name__ == '__main__':
    register()