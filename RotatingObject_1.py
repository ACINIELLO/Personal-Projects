#code from: Blender 3D - Physically Realistic Animation textbook
'''
from visual import *
import math

# -------------------------- method 1:


#this program makes an object and rotates it
#pmb, 10/24/02


# make axes
xaxis = cylinder ( pos=(0,0,0), axis=(5,0,0), radius=0.05, color=color.red )
yaxis = cylinder ( pos=(0,0,0), axis=(0,5,0), radius=0.05, color=color.green )
zaxis = cylinder ( pos=(0,0,0), axis=(0,0,5), radius=0.05, color=color.blue )
# label axes
xlabel = label ( pos= (5,0,0),text='X',height=10, border=5 )
ylabel = label ( pos= (0,5,0),text='Y',height=10, border=5 )
zlabel = label ( pos= (0,0,5),text='Z',height=10, border=5 )
#
# make a box
whiteBox = box(pos=(0,0,0), length= 5.0, height=1.0, width=0.1, color=color.white)
#
# setup for rotation
dt = 0.05
angPos = 0.0
angVel = 0.0
angAcc = 2 * 3.14159 /100.0
angAxis = ( 0,1,0 )
#
# draw paths??
drawPaths = 0
if drawPaths:
path1 = curve( pos=[], radius= 0.02, color= color.yellow )
r1 = 2.0
path2 = curve( pos=[], radius= 0.02, color= color.yellow )
r2 = 1.5
#
# main loop
while 1:
rate(20)
# find angular velocity
angVel = angVel + angAcc * dt
angPos = angPos + angVel * dt
# the vpython "rotate" takes CHANGES to omega as argument, not omega
whiteBox.rotate( angle= angVel * dt, axis = angAxis )
# draw paths if wanted
if ( drawPaths ):
x1 = r1 * cos ( angPos )
y1 = 0.0
z1 = -r1 * sin ( angPos )
path1.append ( pos= ( x1, y1, z1 ))
x2 = r2 * cos ( angPos )
y2 = 0.0
z2 = -r2 * sin ( angPos )
path2.append ( pos= ( x2, y2, z2 ))
'''
# ---------------------------method 2:



#translates selected object:
'''
obj = bpy.context.object
obj.location[2] = 5.0
obj.keyframe_insert(data_path="location", frame=10.0, index=2)
obj.location [2] = 1.0
obj.keyframe_insert(data_path="location", frame=20.0, index=2)
'''
#--------------------------------method 3----------------------


'''
#code from:https://blender.stackexchange.com/questions/43086/how-to-rotate-an-object-in-blender-2-74-using-python-script
    
import bpy
from math import radians
import mathutils

Name = 'RotationTest_1'

   


   


   
obj= bpy.ops #selects multiple objects

#selectAll_objects = bpy.ops.object.select_all(action='DESELECT') #selects all objects

context = bpy.context 
scene = bpy.context.scene
OBJECT = bpy.context.object #selects 1 object
objData = OBJECT.data
objData.name = Name
#Location = ob
current_frame = scene.frame_current

context.scene.frame_set(0)  #specify frame
# Testing with selecting 1 object at a time(as multiple doesnt seem to work all the time):
#OBJECT.keyframe_insert(data_path="Location",type='LocRotScale',frame =current_frame, confirm_success=True) #adding keyframe for animation

OBJECT.keyframe_insert(data_path='location',frame =current_frame) #adding keyframe for animation
     
context.scene.frame_set(30) #specify frame
    
#rotating selected object: 
OBJECT.rotation_euler[0] = radians(360)
     
#OBJECT.keyframe_insert(data_path="rotation_euler", type='LocRotScale',frame = current_frame, confirm_success=True) #adding keyframe for animation

OBJECT.keyframe_insert(data_path='location',frame = 30) #adding keyframe for animation
 
#--------applying textures--------------: 
#from==> https://blender.stackexchange.com/questions/157531/blender-2-8-python-add-texture-image
'''

'''
from bpy import context, data, ops


mat = bpy.data.materials.new(name="New_Mat")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("D:\Alessandro\FILESFORSCHOOL\googleAPI\Ex_Files_Azure_Architects_Design_Strategy\Exercise Files\Images\Sasuke Sharigan.jpg")
mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

ob = context.view_layer.objects.active

# Assign it to object
if ob.data.materials:
    ob.data.materials[0] = mat
else:
    ob.data.materials.append(mat)
'''

#------------------method 4:------------------------



'''
#translates selected object:

obj = bpy.context.object
obj.location[2] = 5.0
obj.keyframe_insert(data_path="location", frame=10.0, index=2)
obj.location [2] = 1.0
obj.keyframe_insert(data_path="location", frame=20.0, index=2)
'''
#-------------------------method 5----------------------
'''
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
obj.anim.keyframe_insert(type='LocRotScale',confirm_success=True) #adding keyframe for animation
    
obj2.scene.frame_set(30) #specify frame
#rotating selected object: 
OBJECT.rotation_euler[0] = radians(360)
obj.anim.keyframe_insert(type='LocRotScale',confirm_success=True) #adding keyframe for animation#applying textures: from==> https://blender.stackexchange.com/questions/157531/blender-2-8-python-add-texture-image
'''

#----------------method 6: ----------------
import bpy
from math import radians
from mathutils import Vector

#rotating 

context = bpy.context
Name = 'Euler_RotationX'
# operators don't return object refs.
OBJECT= bpy.ops

scene = context.scene
ob = context.object
ob.name = Name
me = ob.data

# set the objects rotation
context.scene.frame_set(0)

ob.rotation_euler[0] 
ob.keyframe_insert(data_path= 'rotation_euler', frame=0)

context.scene.frame_set(30)
ob.rotation_euler[0] = radians(360)
ob.keyframe_insert(data_path= 'rotation_euler', frame=30.0)

