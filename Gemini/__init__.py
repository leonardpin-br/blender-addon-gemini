"""Entry point of this add-on. This is the first file to be read by Blender.

The registration of classes occurs in cascade in this add-on. In the local modules,
the ``bpy.utils.register_class()`` is called to register local classes.

Important:
    If you use Visual Studio Code, install the **Blender Development** or
    **Blender Development [Experimental Fork]**. It will automatically create
    the link in the appropriate folder connecting the add-on to Blender.

    If you do not use VSCODE, you can try to create a link to the add-on folder
    (``<project_root>\Gemini``) at
    ``C:\\Users\\<USERNAME>\\AppData\\Roaming\\Blender Foundation\\Blender\\4.0\\scripts\\addons``
    with the same name of this add-on (Gemini)::

        mklink /D "C:\\Users\\<USERNAME>\\AppData\\Roaming\\Blender Foundation\\Blender\\4.0\\scripts\\addons\\Gemini" "full\\path\\to\\blender-addon-gemini\\Gemini"

    In my tests, it did not work though. Using the extension is the preferred way
    to go.

Warning:
    It is a good idea to install ``fake-bpy-module-latest`` to avoid import
    warnings in the editor.

References:
    `Fake Blender Python API module collection: fake-bpy-module`_

    `"Installing" bpy for Plugin Development in VSCode`_

.. _Fake Blender Python API module collection\: fake-bpy-module:
   https://github.com/nutti/fake-bpy-module
.. _"Installing" bpy for Plugin Development in VSCode:
   https://blender.stackexchange.com/a/284197
"""

bl_info = {
    "category": "3D View",
    "description": "Gemini Tools",
    "location": "View3D",
    "author": "ST3",
    "version": (1, 0),
    "name": "Gemini",
    "blender": (4, 0, 2)
}
"""dict: Holds the information tha will be displayed in the Blender interface.
It can be found at
``(Menu) Edit > Preferences > Add-ons > Community > 3D View: Gemini``
"""


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
