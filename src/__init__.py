bl_info = {
    "name": "Blender example add-on",
    "author": "Wybe Westra",
    "version": (0, 0, 1),
    "blender": (2, 83, 4),
    "warning": "This is a beta version!",
    "category": "Generic",
}


def register():
    print("Hello World")


def unregister():
    print("Goodbye World")
