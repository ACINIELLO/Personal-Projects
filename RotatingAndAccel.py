#rotating objects at diff speeds:


#code from:https://blender.stackexchange.com/questions/43086/how-to-rotate-an-object-in-blender-2-74-using-python-script  
import bpy
from math import radians
import mathutilsName = 'RotationTest_1'

scj = bpy.context.scene

OBJECT = bpy.context.object
objData = OBJECT.data
objData.name = Name  
obj= bpy.ops #selects multiple objects
obj2 = bpy.context   
obj2.scene.frame_set(0) #specify frame

OBJECT.rotation_euler[0] 

obj.anim.keyframe_insert(type='LocRotScale',confirm_success=True) #adding keyframe for animation
    
obj2.scene.frame_set(30) #specify frame
#rotating selected object: 
OBJECT.rotation_euler[0] = radians(360)
obj.anim.keyframe_insert(type='LocRotScale',confirm_success=True) #adding keyframe for animation#applying textures: from==> https://blender.stackexchange.com/questions/157531/blender-2-8-python-add-texture-image