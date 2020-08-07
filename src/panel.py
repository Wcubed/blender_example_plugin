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

        layout.label(text="Example label")

        layout.prop(props, "example_float")
