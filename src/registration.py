if "bpy" in locals():
    # Allow for reloading the script.
    import importlib

    print("Reloading example plugin.")

    importlib.reload(panel)
else:
    from . import panel

import bpy

classes = [
    panel.ExamplePanel
]

def register_all():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister_all():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)