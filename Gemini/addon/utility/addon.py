import bpy

addon_name = __name__.partition('.')[0]


def get_prefs():
    """Returns back the class that is calling this function.

    Returns:
        bpy.types.AddonPreferences: The preferences of the class calling this
        function.
    """

    return bpy.context.preferences.addons[addon_name].preferences
