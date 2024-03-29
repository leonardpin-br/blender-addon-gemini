"""Entry point of this addon.

Note:
    A link to the folder (``<project_root>\Gemini``)
    should be created at ``C:\\Users\\<USERNAME>\\AppData\\Roaming\\Blender Foundation\\Blender\\4.0\\scripts\\addons``
    with the same name (Gemini).

    The link will not work though. After using the extension (Blender Development)
    another link will be created and the first one can be deleted.

Warning:
    It is a good idea to install ``fake-bpy-module-latest`` to avoid import
    warnings in the editor.

References:
    `Fake Blender Python API module collection: fake-bpy-module`_

.. _Fake Blender Python API module collection\: fake-bpy-module:
   https://chadrick-kwag.net/sphinx-apidoc-ignoring-some-modules-packages/
"""

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
