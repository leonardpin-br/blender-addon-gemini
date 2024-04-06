"""Adds the Solidify modifier to the selected object.

"""

import bpy
import traceback
from .. utility.mouse import mouse_warp
from .. utility.draw import draw_quad, draw_text, get_blf_text_dims
from .. utility.addon import get_prefs


class GEM_OP_Solidify(bpy.types.Operator):
    """This class creates a modal.

    This is different from a standard operator. A modal is interactive, that is,
    the user can move the mouse cursor and it affects the result in the
    viewport.

    """

    bl_idname = "gem.solidify"
    """str: ``gem`` works as a category or a namespace."""

    bl_label = "Solidify"
    """str: Name that can be searched for in the Blender interface, and shows up
    as a button, if the ``text=`` parameter (of ``self.layout.operator()``) is
    not given in the ``main_menu.py`` module.
    """

    bl_description = "Solidify Modal"
    """str: Appears when the user hover over a button. Acts as a tooltip."""

    bl_options = {"REGISTER", "UNDO", "BLOCKING"}
    """str: Allows to press CTRL+Z and undo what has just been done."""

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

        # Props
        self.created_modifier = False
        self.original_thickness = 0
        self.modifier = None
        self.obj = context.active_object
        self.divisor = 1000

        # Initialize
        self.setup(context)
        self.draw_handle = bpy.types.SpaceView3D.draw_handler_add(
            self.safe_draw_shader_2d, (context,), 'WINDOW', 'POST_PIXEL')

        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

    def setup(self, context):
        """Checks if there is a solidify modifier already there. If there is
        not, creates one.

        Args:
            context (bpy.types.Context): This parameter gives the option,
                for example, to get a reference to the selected object. This
                parameter is madatory even when it is not used like in this
                method.
        """

        for mod in self.obj.modifiers:
            if mod.type == 'SOLIDIFY':
                self.modifier = mod
                break

        if self.modifier == None:
            self.created_modifier = True
            self.modifier = self.obj.modifiers.new('Solidify', 'SOLIDIFY')

        self.original_thickness = self.modifier.thickness

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
            'PASS_THROUGH', 'FINISHED', 'CANCELLED' and 'RUNNING_MODAL'.

        References:
            `invoke(context, event)`_

            `What do operator methods do? (poll, invoke, execute, draw & modal)`_

        .. _invoke(context, event):
           https://docs.blender.org/api/current/bpy.types.Operator.html#bpy.types.Operator.invoke
        .. _What do operator methods do? (poll, invoke, execute, draw & modal):
           https://blender.stackexchange.com/questions/19416/what-do-operator-methods-do-poll-invoke-execute-draw-modal

        """

        # Utils
        mouse_warp(context, event)

        # Free navigation
        if event.type == "MIDDLEMOUSE":
            return {'PASS_THROUGH'}

        # Confirm
        elif event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            self.remove_shaders(context)
            return {'FINISHED'}

        # Cancel
        elif event.type == 'RIGHTMOUSE' and event.value == 'PRESS':
            self.modifier.thickness = self.original_thickness
            if self.created_modifier == True:
                self.obj.modifiers.remove(self.modifier)
            self.remove_shaders(context)
            return {'CANCELLED'}

        # Adjust
        elif event.type == 'MOUSEMOVE':
            delta = event.mouse_x - event.mouse_prev_x
            delta = delta / self.divisor
            self.modifier.thickness += delta

        return {"RUNNING_MODAL"}

    def remove_shaders(self, context):
        '''Remove shader handle.'''

        if self.draw_handle != None:
            self.draw_handle = bpy.types.SpaceView3D.draw_handler_remove(
                self.draw_handle, "WINDOW")
            context.area.tag_redraw()

    def safe_draw_shader_2d(self, context):

        try:
            self.draw_shaders_2d(context)
        except Exception:
            print("2D Shader Failed in Solidify")
            traceback.print_exc()
            self.remove_shaders(context)

    def draw_shaders_2d(self, context):

        prefs = get_prefs()

        # Props
        text = "Thickness: {:.2f}".format(self.modifier.thickness)
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
