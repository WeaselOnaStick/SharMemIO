import bpy
from . import SharMemIOClasses

bl_info = {'name': "SHAR Memory IO",
           'author': 'Weasel On A Stick',
           'version': (1, 0, 0),
           'blender': (2, 82, 7),
           'location': 'View3D > Sidebar > SharMemIO',
           'description': 'Read/write in-game player/car position for SHAR (REQUIRES PYMEM)',
           #'tracker_url': 'https://github.com/WeaselOnaStick/map-data-editor/issues',
           #'wiki_url': 'https://github.com/WeaselOnaStick/map-data-editor/wiki',
           'category': 'User Interface'}


classes = SharMemIOClasses.to_register


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    
    bpy.types.Scene.SMIO = bpy.props.PointerProperty(
        type=(SharMemIOClasses.SMIOPropGroup),
        name="SHAR Memory IO",
    )


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    del bpy.types.Scene.SMIO


if __name__ == '__main__':
    register()
