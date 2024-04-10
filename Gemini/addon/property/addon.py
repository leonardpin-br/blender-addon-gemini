import bpy
from .. utility.addon import addon_name, get_prefs
from bpy.props import PointerProperty

from . color import GEM_Color, draw_color
from . settings import GEM_Settings, draw_settings


class GEM_Props(bpy.types.AddonPreferences):
    """Class responsible for creating the preferences of this add-on in the
    Blender interface.
    """

    bl_idname = addon_name

    # Property Groups (Pointer Property)
    color: PointerProperty(type=GEM_Color)
    settings: PointerProperty(type=GEM_Settings)

    def draw(self, context):
        """This method is responsible for drawing the preferences in the Blender
        interface
        (``(Menu) Edit > Preferences > Add-ons > Community > 3D View: Gemini``)

        Warning:
            This method has to be called ``draw``.

        Args:
            context (bpy.types.Context): This parameter gives the option,
                for example, to get a reference to the selected object. This
                parameter is madatory even when it is not used like in this
                method.
        """

        prefs = get_prefs()
        layout = self.layout

        # General Settings
        box = layout.box()
        draw_color(prefs, box)

        # Drawing settings
        box = layout.box()
        draw_settings(prefs, box)
