

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

   
scj = bpy.context.scene

   
OBJECT = bpy.context.object
objData = OBJECT.data
objData.name = Name
    
    
   
obj= bpy.ops
obj2 = bpy.context
     
obj2.scene.frame_set(0) #specify frame
obj.anim.keyframe_insert(type='LocRotScale',confirm_success=True) #adding keyframe for animation
    
obj2.scene.frame_set(30) #specify frame
    
#rotating selected object: 
OBJECT.rotation_euler[0] = radians(360)
     
obj.anim.keyframe_insert(type='LocRotScale',confirm_success=True) #adding keyframe for animation

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
