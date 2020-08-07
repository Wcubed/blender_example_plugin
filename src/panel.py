import bpy


class ExamplePanel(bpy.types.Panel):
    bl_idname = "EXAMPLE_PT_panel"
    bl_label = "Example Panel"
    bl_category = "Example Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Example label")
