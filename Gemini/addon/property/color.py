import bpy
from bpy.props import FloatVectorProperty


class GEM_Color(bpy.types.PropertyGroup):
    """Class responsible for drawing, in the add-on preferences, the colors
    of the font and background. It allows to use the color picker.

    This class is considered a property group.
    """

    font_color: FloatVectorProperty(
        name='Font Color',
        description='Color of the modal font',
        size=4,
        min=0, max=1,
        subtype='COLOR',
        default=(1, 1, 1, 1)
    )

    bg_color: FloatVectorProperty(
        name='BG Color',
        description='Color of the background',
        size=4,
        min=0,
        max=1,
        subtype='COLOR',
        default=(0, 0, 0, 0.75)
    )


def draw_color(prefs, layout):
    """When called, refers back to the ``GEM_Color`` class and its pointer
    properties.

    This function uses the ``GEM_Color`` class inside it.

    Args:
        prefs (bpy.types.AddonPreferences): The preferences of the ``GEM_Color``
            class.
        layout (bpy.types.UILayout): User interface layout.

    References:
        `class bpy.types.UILayout`_

    .. _class bpy.types.UILayout:
       https://docs.blender.org/api/current/bpy.types.UILayout.html#bpy.types.UILayout
    """

    layout.label(text='Colors', icon='RESTRICT_COLOR_ON')

    # Tools
    box = layout.box()

    row = box.row()
    row.prop(prefs.color, 'font_color', text='Font Color')
    row = box.row()
    row.prop(prefs.color, 'bg_color', text='Background Color')
