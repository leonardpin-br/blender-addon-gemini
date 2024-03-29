import bpy
import blf
import gpu
# from bgl import *
from gpu_extras.batch import batch_for_shader


def draw_quad(vertices=[], color=(1, 1, 1, 1)):
    """Vertices = Top Left, Bottom Left, Top Right, Bottom Right

    Args:
        vertices (list, optional): _description_. Defaults to [].
        color (tuple, optional): _description_. Defaults to (1, 1, 1, 1).

    Raises:
        ValueError: If `2D_UNIFORM_COLOR` is used as argument for
            `gpu.shader.from_builtin()`
        TypeError: If `glEnable(GL_BLEND)` and `glDisable(GL_BLEND)` are called.

    References:
        `OpenGL Wrapper (bgl)`_

    .. _OpenGL Wrapper (bgl):
       https://docs.blender.org/api/current/bgl.html#module-bgl
    """

    indices = [(0, 1, 2), (1, 2, 3)]
    # shader = gpu.shader.from_builtin('2D_UNIFORM_COLOR')    # ValueError: expected a string in ... , got '2D_UNIFORM_COLOR'
    shader = gpu.shader.from_builtin('UNIFORM_COLOR')
    batch = batch_for_shader(
        shader, 'TRIS', {"pos": vertices}, indices=indices)
    shader.bind()
    shader.uniform_float("color", color)
    # glEnable(GL_BLEND)    # TypeError: 'NoneType' object is not callable
    batch.draw(shader)
    # glDisable(GL_BLEND)   # TypeError: 'NoneType' object is not callable

    del shader
    del batch


def draw_text(text, x, y, size=12, color=(1, 1, 1, 1)):
    """Draws the text inside the box.

    Args:
        text (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_
        size (int, optional): _description_. Defaults to 12.
        color (tuple, optional): _description_. Defaults to (1, 1, 1, 1).

    Raises:
        TypeError: If `blf.size()` is called with 3 arguments.

    References:
        `Font Drawing (blf)`_

    .. _Font Drawing (blf):
       https://docs.blender.org/api/current/blf.html#module-blf
    """

    dpi = bpy.context.preferences.system.dpi
    font = 0
    # blf.size(font, size, int(dpi))    # TypeError: blf.size() takes exactly 2 arguments (3 given)
    blf.size(font, size)
    blf.color(font, *color)
    blf.position(font, x, y, 0)
    blf.draw(font, text)


def get_blf_text_dims(text, size):
    '''Return the total width of the string

    Raises:
        TypeError: If `blf.size()` is called with 3 arguments.

    References:
        `Font Drawing (blf)`_

    .. _Font Drawing (blf):
       https://docs.blender.org/api/current/blf.html#module-blf'''

    dpi = bpy.context.preferences.system.dpi
    # blf.size(0, size, dpi)    # TypeError: blf.size() takes exactly 2 arguments (3 given)
    blf.size(0, size)
    return blf.dimensions(0, str(text))
