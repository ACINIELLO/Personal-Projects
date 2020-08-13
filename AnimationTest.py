import bpy
import mathutils 
import math
from math import radians
import numpy as np 
#method 1:

obj= bpy.ops

angles = np.linspace(0,360,8) 
FrameCount=0
for i in range(0,len(angles)):

            
    obj.transform.rotate(value=angles(i),orient_axis = 'X')

    obj.anim.keyframe_insert(type='LocRotScale',confirm_success=True)
    
    FrameCount = FrameCount +5     
    obj.anim.change_frame(frame=FrameCount)



obj.anim.keyframe_delete_v3d()

#method 2:
'''
#selecting object:

obj = bpy.context.object


#Rotating selection:
obj.keyframe_insert(data_path="euler_rotation",frame=1)

obj.euler_rotation.x = math.radians(45)

obj.keyframe_insert(data_path="euler_rotation",frame=10)

obj.euler_rotation.x = math.radians(90)
'''
