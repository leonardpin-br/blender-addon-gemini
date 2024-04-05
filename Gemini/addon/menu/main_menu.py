"""Creates the main menu for the add-on.
"""

import bpy


class GEM_MT_Main_Menu(bpy.types.Menu):
    """Class responsable for creating the main menu.

    """

    bl_idname = "GEM_MT_Main_Menu"
    """str: The identifier."""

    bl_label = "Gemini Main Menu"
    """str: Name that will appear in the Blender interface."""

    def draw(self, context):
        """Creates what will appear in the interface after pressing the hotkeys.

        Args:
            context (bpy.context): This parameter gives the option,
                for example, to get a reference to the selected object. This
                parameter is madatory even when it is not used like in this
                method.
        """

        layout = self.layout

        layout.operator_context = 'INVOKE_DEFAULT'
        layout.label(text='Gemini Tools')

        layout.operator("gem.add_lights", text="Add Lights", icon="LIGHT")
        layout.operator("gem.solidify", text="Solidify", icon="MOD_SOLIDIFY")
        layout.operator("gem.ray_caster", text="Ray Caster",
                        icon="TRACKING_BACKWARDS_SINGLE")
