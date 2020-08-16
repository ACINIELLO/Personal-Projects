

#translates selected object:
'''
obj = bpy.context.object
obj.location[2] = 5.0
obj.keyframe_insert(data_path="location", frame=10.0, index=2)
obj.location [2] = 1.0
obj.keyframe_insert(data_path="location", frame=20.0, index=2)
'''
#--------------------------------method 1----------------------

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
 
#applying textures: from==> https://blender.stackexchange.com/questions/157531/blender-2-8-python-add-texture-image

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