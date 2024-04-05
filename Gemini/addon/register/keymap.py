"""Sets the hotkey to be used to invoke this add-on."""

import bpy

keys = []
"""list: When Blender loads up, it will load the keys inside this list.
"""


def register_keymap():
    """Adds the keys to the ``keys`` list.
    """

    wm = bpy.context.window_manager
    addon_keyconfig = wm.keyconfigs.addon
    kc = addon_keyconfig

    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    kmi = km.keymap_items.new(
        "wm.call_menu", "F", "PRESS", ctrl=True, shift=True)
    kmi.properties.name = "GEM_MT_Main_Menu"
    keys.append((km, kmi))


def unregister_keymap():
    """If, at some point, the add-on is uninstalled, the keys are removed by
    this function.

    """

    for km, kmi in keys:
        km.keymap_items.remove(kmi)

    keys.clear()
