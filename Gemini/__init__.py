# A link to this folder ("E:\HDD_4TB\cloud\Videoaulas\Udemy - Blender Python Addon Development with ST3\blender-addon-gemini\Gemini")
# should be created at "C:\Users\<USERNAME>\AppData\Roaming\Blender Foundation\Blender\4.0\scripts\addons"
# with the same name (Gemini).
# The link will not work though. After using the extension (Blender Development)
# another link will be created and the first one can be deleted.
# Fake Blender Python API module collection: fake-bpy-module
# https://github.com/nutti/fake-bpy-module


bl_info = {
    "name": "Gemini",
    "description": "Gemini Tools",
    "author": "ST3",
    "version": (1, 0),
    "blender": (4, 0, 2),
    "location": "View3D",
    "category": "3D View"
}


def register():
    from . addon.register import register_addon
    register_addon()


def unregister():
    from . addon.register import unregister_addon
    unregister_addon()
