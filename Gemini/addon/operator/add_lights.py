"""Creates a ring of lights in the scene.

"""

import math

import bpy
from bpy.props import IntProperty, FloatProperty


class GEM_OP_Add_Lights(bpy.types.Operator):
    """Adds lights to the scene.

    This is a standard operator, not a modal one.

    """

    bl_idname = "gem.add_lights"
    """str: ``gem`` works as a category"""

    bl_label = "Add Lights"
    """str: Name that can be searched for in the Blender interface, and shows up
    as a button.
    """

    bl_options = {'REGISTER', 'UNDO'}
    """set: Allows to press CTRL+Z and undo what this operator has done."""

    radius: FloatProperty(name="Radius", default=5, min=1, max=100)
    count: IntProperty(name="Light Count", default=5, min=3, max=50)
    energy: IntProperty(name="Light Energy", default=500, min=50, max=1700)
    z: FloatProperty(name="Light Height", default=6, min=2, max=12)

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        """Creates the panel that will appear in the interface during the use
        of the operator.

        Args:
            context (bpy.context): This parameter gives the option,
                for example, to get a reference to the selected object. This
                parameter is madatory even when it is not used like in this
                method.
        """
        # print("draw...")
        layout = self.layout

        layout.prop(self, 'radius')
        layout.prop(self, 'count')
        layout.prop(self, 'energy')
        layout.prop(self, 'z')

    def execute(self, context):
        """Executes, automatically (without being called in this code) the
        creation of lights.

        Args:
            context (bpy.context): This parameter gives the option,
                for example, to get a reference to the selected object. This
                parameter is madatory even when it is not used like in this
                method.

        Returns:
            set: Contains only one string equals to 'FINISHED'.
        """
        objs = []

        for i in range(self.count):
            light = bpy.data.lights.new('Point', 'POINT')
            obj = bpy.data.objects.new("LightObj", light)
            objs.append(obj)
            context.collection.objects.link(obj)

            angle = i * math.pi * 2 / self.count

            loc = (
                math.cos(angle) * self.radius,
                math.sin(angle) * self.radius,
                self.z
            )

            # Set obj props
            obj.location = loc
            obj.data.energy = self.energy

        empty = bpy.data.objects.new('LightEmpty', None)
        empty.location = (0, 0, 0)
        context.collection.objects.link(empty)
        for obj in objs:
            obj.parent = empty

        # print("execute...")

        return {'FINISHED'}
