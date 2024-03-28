import bpy
from .. utility.addon import addon_name, get_prefs
from bpy.props import PointerProperty

from . color import GEM_Color, draw_color
from . settings import GEM_Settings, draw_settings


class GEM_Props(bpy.types.AddonPreferences):
    bl_idname = addon_name

    # Property Groups
    color: PointerProperty(type=GEM_Color)
    settings: PointerProperty(type=GEM_Settings)

    def draw(self, context):

        prefs = get_prefs()
        layout = self.layout

        # General Settings
        box = layout.box()
        draw_color(prefs, box)

        # Drawing settings
        box = layout.box()
        draw_settings(prefs, box)
