import bpy


# See: https://docs.blender.org/api/current/bpy.types.Operator.html
class ExampleOperator(bpy.types.Operator):
    # The bl_idname of an operator should follow this pattern <module>.<operator>.
    # For example: "script.reload"
    bl_idname = "example.operator"
    bl_label = "Example operator"
    bl_description = "An example of an operator"
    bl_options = {'REGISTER'}

    def execute(self, context):

        self.report({'INFO'}, "Did the thing!")

        return {'FINISHED'}
