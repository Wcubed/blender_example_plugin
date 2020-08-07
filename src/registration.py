if "bpy" in locals():
    # Allow for reloading the script.
    import importlib

    print("Reloading example plugin.")

    importlib.reload(panel)
    importlib.reload(properties)
else:
    from . import panel
    from . import properties

import bpy

classes = [
    panel.ExamplePanel,
    properties.ExampleSceneProperties
]


def register_all():
    for cls in classes:
        bpy.utils.register_class(cls)

    add_properties()


def unregister_all():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    remove_properties()


def add_properties():
    bpy.types.Scene.example_props = bpy.props.PointerProperty(name="Example Scene Properties",
                                                              type=properties.ExampleSceneProperties)
    pass


def remove_properties():
    del bpy.types.Scene.example_props
