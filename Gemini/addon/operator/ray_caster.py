import bpy
import traceback
import mathutils
from mathutils import Vector
from .. utility.draw import draw_quad, draw_text, get_blf_text_dims
from .. utility.addon import get_prefs
from .. utility.ray import mouse_raycast_to_plane, mouse_raycast_to_scene


class GEM_OP_Ray(bpy.types.Operator):
    """This class creates a modal.

    This is different from a standard operator. A modal is interactive, that is,
    the user can move the mouse cursor and it affects the result in the
    viewport.

    """

    bl_idname = "gem.ray_caster"
    bl_label = "Raycaster"
    bl_description = "Raycaster Modal"
    bl_options = {"REGISTER", "UNDO", "BLOCKING"}

    @classmethod
    def poll(cls, context):
        """This is going to be run before any instance of this class is made.

        It makes sure the operator returns True or False and can run.

        It is advisable to keep the method lite and not do any heavy
        operations inside it.

        Warning:
            This method has to be called ``poll``.

        Args:
            context (bpy.context): This parameter gives the option,
                for example, to get a reference to the selected object.

        Returns:
            bool: True if there is a mesh object selected, False otherwise.

        References:
            `classmethod poll(context)`_

            `What do operator methods do? (poll, invoke, execute, draw & modal)`_

        .. _classmethod poll(context):
           https://docs.blender.org/api/current/bpy.types.Operator.html#bpy.types.Operator.poll
        .. _What do operator methods do? (poll, invoke, execute, draw & modal):
           https://blender.stackexchange.com/questions/19416/what-do-operator-methods-do-poll-invoke-execute-draw-modal

        """

        if context.active_object != None:
            if context.active_object.type == 'MESH':
                return True
            return False

    def invoke(self, context, event):
        """First method to run when an instance of this class is made.

        Warning:
            This method has to be called ``invoke``.

        Args:
            context (bpy.types.Context): This parameter gives the option,
                for example, to get a reference to the selected object.
            event (bpy.types.Event): Window Manager Event.

        Returns:
            set: Set containing only one string equals to "RUNNING_MODAL".

        References:
            `invoke(context, event)`_

            `What do operator methods do? (poll, invoke, execute, draw & modal)`_

        .. _invoke(context, event):
           https://docs.blender.org/api/current/bpy.types.Operator.html#bpy.types.Operator.invoke
        .. _What do operator methods do? (poll, invoke, execute, draw & modal):
           https://blender.stackexchange.com/questions/19416/what-do-operator-methods-do-poll-invoke-execute-draw-modal

        """

        self.obj = context.active_object
        self.scene_cast = True
        self.intersection = Vector((0, 0, 0))
        self.draw_handle = bpy.types.SpaceView3D.draw_handler_add(
            self.safe_draw_shader_2d, (context,), 'WINDOW', 'POST_PIXEL')

        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        """Runs after the ``invoke()`` method when an instance of this class is
        made. It will run until it is finished.

        Warning:
            This method has to be called ``modal``.

        Args:
            context (bpy.types.Context): This parameter gives the option,
                for example, to get a reference to the selected object.
            event (bpy.types.Event): Window Manager Event.

        Returns:
            set: Only one of the following possible strings:
            'PASS_THROUGH', 'CANCELLED' and 'RUNNING_MODAL'.

        References:
            `What do operator methods do? (poll, invoke, execute, draw & modal)`_

        .. _What do operator methods do? (poll, invoke, execute, draw & modal):
           https://blender.stackexchange.com/questions/19416/what-do-operator-methods-do-poll-invoke-execute-draw-modal

        """

        # Free navigation
        if event.type == "MIDDLEMOUSE":
            return {'PASS_THROUGH'}

        # Exit
        elif event.type in {'LEFTMOUSE', 'RIGHTMOUSE'} and event.value == 'PRESS':
            self.remove_shaders(context)
            return {'CANCELLED'}

        # Change ray cast method
        elif event.type == 'R' and event.value == 'PRESS':
            self.scene_cast = not self.scene_cast

        # Adjust
        elif event.type == 'MOUSEMOVE':

            # Scene raycast
            if self.scene_cast == True:
                hit, location, normal, index, object, matrix = mouse_raycast_to_scene(
                    context, event)
                if hit:
                    self.intersection = location

            # Line plane raycast
            else:
                mouse = (event.mouse_region_x, event.mouse_region_y)
                point = Vector((0, 0, 0))
                normal = Vector((0, 0, 1))
                self.intersection = mouse_raycast_to_plane(
                    mouse, context, point, normal)
                self.obj.location = self.intersection

        context.area.tag_redraw()
        return {"RUNNING_MODAL"}

    def remove_shaders(self, context):
        """Remove shader handle.

        Args:
            context (bpy.types.Context): This parameter gives the option,
                for example, to get a reference to the selected object.
        """

        if self.draw_handle != None:
            self.draw_handle = bpy.types.SpaceView3D.draw_handler_remove(
                self.draw_handle, "WINDOW")
            context.area.tag_redraw()

    def safe_draw_shader_2d(self, context):
        """Avoids having the text stuck in the viewport in case of an error in
        the ``draw_shaders_2d()`` method.

        Args:
            context (bpy.types.Context): This parameter gives the option,
                for example, to get a reference to the selected object.
        """

        try:
            self.draw_shaders_2d(context)
        except Exception:
            print("2D Shader Failed in Solidify")
            traceback.print_exc()
            self.remove_shaders(context)

    def draw_shaders_2d(self, context):
        """Draws the shaders in 2D in the Blender interface.

        When drawing text in the Bleder screen, it is necessary to draw the
        rectangle in the background first and then the text inside it.

        In order to render the background, it is necessary to know the
        dimensions of the text. Some padding is going to be added to the width
        and height of the text.

        So, first we get the dimensions of the text, then we draw the background
        and then the text inside that background.

        Args:
            context (bpy.types.Context): This parameter gives the option,
                for example, to get a reference to the selected object.
        """

        prefs = get_prefs()

        # Props
        text = "X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(
            self.intersection.x, self.intersection.y, self.intersection.z)
        font_size = prefs.settings.font_size
        dims = get_blf_text_dims(text, font_size)
        area_width = context.area.width
        padding = 8

        over_all_width = dims[0] + padding * 2
        over_all_height = dims[1] + padding * 2

        left_offset = abs((area_width - over_all_width) * 0.5)
        bottom_offset = 20

        top_left = (left_offset, bottom_offset + over_all_height)
        bot_left = (left_offset, bottom_offset)
        top_right = (left_offset + over_all_width,
                     bottom_offset + over_all_height)
        bot_right = (left_offset + over_all_width, bottom_offset)

        # Draw Quad
        verts = [top_left, bot_left, top_right, bot_right]
        draw_quad(vertices=verts, color=prefs.color.bg_color)

        # Draw Text
        x = left_offset + padding
        y = bottom_offset + padding
        draw_text(text=text, x=x, y=y, size=font_size,
                  color=prefs.color.font_color)

        # Draw ray type
        text = "SCENE" if self.scene_cast else "PLANE"
        draw_text(text=text, x=x, y=y + over_all_height + padding,
                  size=font_size, color=prefs.color.font_color)
