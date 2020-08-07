import bpy


class ExamplePanel(bpy.types.Panel):
    bl_idname = "EXAMPLE_PT_panel"
    bl_label = "Example Panel"
    bl_category = "Example Panel Category"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        props = scene.example_props

        # Split properties vertically.
        layout.use_property_split = True

        layout.label(text="Example label")

        layout.prop(props, "example_float")
        layout.prop(props, "example_vector")

        layout.operator("example.operator", text="Do The Thing!")

        box = layout.box()
        box.use_property_split = False

        box.prop(props, "example_bool")
        box.prop(props, "example_float")
        box.prop(props, "example_vector")
