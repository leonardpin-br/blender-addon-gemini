
import math

import bpy
from bpy.props import IntProperty, FloatProperty


class GEM_OP_Add_Lights(bpy.types.Operator):
    """Adds lights to the scene."""

    bl_idname = "gem.add_lights"
    bl_label = "Add Lights"
    bl_options = {'REGISTER', 'UNDO'}

    radius: FloatProperty(name="Radius", default=5, min=1, max=100)
    count: IntProperty(name="Light Count", default=5, min=3, max=50)
    energy: IntProperty(name="Light Energy", default=500, min=50, max=1700)
    z: FloatProperty(name="Light Height", default=6, min=2, max=12)

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        # print("draw...")
        layout = self.layout

        layout.prop(self, 'radius')
        layout.prop(self, 'count')
        layout.prop(self, 'energy')
        layout.prop(self, 'z')

    def execute(self, context):
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
