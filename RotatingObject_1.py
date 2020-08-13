#code from: Blender 3D - Physically Realistic Animation textbook

from visual import *
import math

# ---------------------------option 1:

'''
this program makes an object and rotates it
pmb, 10/24/02
'''

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

# ---------------------------option 2: