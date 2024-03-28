import bpy
import mathutils
from bpy_extras import view3d_utils
from mathutils import Vector


def mouse_raycast_to_plane(mouse_pos, context, point, normal):
    """Get 3D point on plane from mouse.

    Args:
        mouse_pos (tuple): _description_
        context (bpy.context): _description_
        point (Vector): The planes origin.
        normal (Vector): The planes direction.

    Returns:
        Vector 3D
    """

    #  Get the context arguments
    region = context.region
    rv3d = context.region_data
    intersection = Vector((0, 0, 0))
    try:
        # Camera Origin
        origin = view3d_utils.region_2d_to_origin_3d(region, rv3d, mouse_pos)
        # Mouse origin
        mouse = view3d_utils.region_2d_to_vector_3d(region, rv3d, mouse_pos)
        # Camera Origin + Mouse
        ray_origin = origin + mouse
        # From the mouse to the viewport
        loc = view3d_utils.region_2d_to_location_3d(
            region, rv3d, mouse_pos, ray_origin - origin)
        # Ray to plane
        intersection = mathutils.geometry.intersect_line_plane(
            ray_origin, loc, point, normal)

    except:
        intersection = Vector((0, 0, 0))

    if intersection == None:
        intersection = Vector((0, 0, 0))

    return intersection


def mouse_raycast_to_scene(context, event) -> tuple:
    """Cast a ray from the mouse into the scene returning the ray hit data.

    Args:
        context (bpy.types.Context): _description_
        event (bpy.types.Event): _description_

    Returns:
        tuple: (result, location, normal, index, object, matrix)

    Raises:
        TypeError: If `context.view_layer` is given as the first argument
            to `context.scene.ray_cast()`.

    References:
        `Scene Ray Cast`_

    .. _Scene Ray Cast:
       https://developer.blender.org/docs/release_notes/2.91/python_api/#scene-ray-cast
    """

    mouse_pos = (event.mouse_region_x, event.mouse_region_y)

    origin = view3d_utils.region_2d_to_origin_3d(
        bpy.context.region, bpy.context.region_data, mouse_pos)
    direction = view3d_utils.region_2d_to_vector_3d(
        bpy.context.region, bpy.context.region_data, mouse_pos)

    # hit, location, normal, index, object, matrix = context.scene.ray_cast(context.view_layer, origin, direction)  # TypeError
    hit, location, normal, index, object, matrix = context.scene.ray_cast(
        context.view_layer.depsgraph, origin, direction)
    return hit, location, normal, index, object, matrix
