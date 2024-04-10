import bpy
from bpy.props import IntProperty


class GEM_Settings(bpy.types.PropertyGroup):
    """The settings for this add-on.

    This class is considered a property group.
    """

    font_size: IntProperty(
        name='Font Size',
        description='Font Size',
        min=10,
        max=32,
        default=12
    )


def draw_settings(prefs, layout):
    """Similar to the ``Gemini.addon.property.color.draw_color()``, when called,
    refers back to the ``GEM_Settings`` class and its pointer property.

    This function uses the ``GEM_Settings`` class inside it.

    Args:
        prefs (bpy.types.AddonPreferences): The preferences of the
            ``GEM_Settings`` class.
        layout (bpy.types.UILayout): User interface layout.

    References:
        `class bpy.types.UILayout`_

        `class bpy.types.AddonPreferences`_

    .. _class bpy.types.UILayout:
       https://docs.blender.org/api/current/bpy.types.UILayout.html#bpy.types.UILayout
    .. _class bpy.types.AddonPreferences:
       https://docs.blender.org/api/current/bpy.types.AddonPreferences.html#bpy.types.AddonPreferences
    """

    layout.label(text='General Settings', icon='TOOL_SETTINGS')

    # Tools
    box = layout.box()

    row = box.row()
    row.label(text='Font Size')
    row.prop(prefs.settings, 'font_size', text='Font Size')
