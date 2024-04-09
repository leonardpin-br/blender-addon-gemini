PADDING = 80
"""int: Distance (inside Blender' screen) from the edge. When the mouse cursor
is below that distance, it will warp, that is, appear at the other side of the
screen.

"""


def mouse_warp(context, event):
    """Warp the mouse in the screen region.

    This function is preferable to the Blender's warp because this one allows
    navigation during the use of the operator.

    Args:
        context (bpy.types.Context): This parameter gives the option,
            for example, to get a reference to the selected object.
        event (bpy.types.Event): Window Manager Event.

    """

    mouse_pos = (event.mouse_region_x, event.mouse_region_y)
    x_pos = mouse_pos[0]
    y_pos = mouse_pos[1]

    # X Warp
    if mouse_pos[0] + PADDING > context.area.width:
        x_pos = PADDING + 5
    elif mouse_pos[0] - PADDING < 0:
        x_pos = context.area.width - (PADDING + 5)

    # Y Warp
    if mouse_pos[1] + PADDING > context.area.height:
        y_pos = PADDING + 5
    elif mouse_pos[1] - PADDING < 0:
        y_pos = context.area.height - (PADDING + 5)

    if x_pos != mouse_pos[0] or y_pos != mouse_pos[1]:
        x_pos += context.area.x
        y_pos += context.area.y
        context.window.cursor_warp(x_pos, y_pos)
