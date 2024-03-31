"""Entry point of this addon. This is the first file to be read by Blender.

The registration of classes occurs in cascade in this addon. In the local modules,
the ``bpy.utils.register_class()`` is called to register local classes.

Important:
    If you use Visual Studio Code, install the **Blender Development** or
    **Blender Development [Experimental Fork]**. It will automatically create
    the link in the appropriate folder connecting the addon to Blender.

    If you do not use VSCODE, you can try to create a link to the addon folder
    (``<project_root>\Gemini``) at
    ``C:\\Users\\<USERNAME>\\AppData\\Roaming\\Blender Foundation\\Blender\\4.0\\scripts\\addons``
    with the same name of this addon (Gemini).

    In my tests, it did not work though. Using the extension is the preferred way
    to go.

Warning:
    It is a good idea to install ``fake-bpy-module-latest`` to avoid import
    warnings in the editor.

References:
    `Fake Blender Python API module collection: fake-bpy-module`_

.. _Fake Blender Python API module collection\: fake-bpy-module:
   https://github.com/nutti/fake-bpy-module
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
    """Starts the chain of registration.
    """
    from . addon.register import register_addon
    register_addon()


def unregister():
    """Starts the chain of unregistration.
    """
    from . addon.register import unregister_addon
    unregister_addon()
