import bpy
from bpy.props import *


class ExampleSceneProperties(bpy.types.PropertyGroup):

    # This property is animatable, as the default `options` value is {'ANIMATABLE'}.
    # If you don't want this, add `options=set()` so that no options are passed.
    example_float: FloatProperty(name="Float Property",
                                 description="An example of a float property.",
                                 default=1.5,
                                 min=0.1,
                                 max=10)
