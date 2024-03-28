import bpy


class GEM_MT_Main_Menu(bpy.types.Menu):
    bl_idname = "GEM_MT_Main_Menu"
    bl_label = "Gemini Main Menu"

    def draw(self, context):
        layout = self.layout

        layout.operator_context = 'INVOKE_DEFAULT'
        layout.label(text='Gemini Tools')

        layout.operator("gem.add_lights", text="Add Lights", icon="LIGHT")
        layout.operator("gem.solidify", text="Solidify", icon="MOD_SOLIDIFY")
        layout.operator("gem.ray_caster", text="Ray Caster",
                        icon="TRACKING_BACKWARDS_SINGLE")
