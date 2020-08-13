#code from: Blender 3D - Physically Realistic Animation textbook

from visual import *
import math
#
# this program makes an object and rotates it
# this version is like rotator1, but draws
# ANGULAR velocity and acceleration vectors
# pmb, 10/24/02
#
# make axes
xaxis = cylinder ( pos=(0,0,0), axis=(5,0,0), radius=0.025, color=color.red )
yaxis = cylinder ( pos=(0,0,0), axis=(0,5,0), radius=0.025, color=color.green )
zaxis = cylinder ( pos=(0,0,0), axis=(0,0,5), radius=0.025, color=color.blue )
# label axes
xlabel = label ( pos= (5,0,0),text='X',height=10, border=5 )
ylabel = label ( pos= (0,5,0),text='Y',height=10, border=5 )
zlabel = label ( pos= (0,0,5),text='Z',height=10, border=5 )
#
# make a box
whiteBox = box(pos=(0,0,0), length= 5.0, height=1.0, width=0.1, color=color.white)
#
# setup for rotation
t = 0.0
dt = 0.05
angPos = 0.0
angVel = 0.0
angAxis = ( 0,1,0 )
#
# draw angular vel and acc?
drawAngAcc = 1
rPoint = 2.0
if drawAngAcc:
angAccVec =arrow(pos=( 0,0,0 ),axis=( 0,1,0 ),shaftwidth=0.15,color=color.red )
angVelVec =arrow(pos=( 0,0,0 ),axis=( 0,1,0 ),shaftwidth=0.15,color=color.blue )
#
# main loop
while 1:
rate(20)
t = t+ dt
# find angular velocity
angAcc = 2 * 3.14159/100.0
angVel = angVel + angAcc * dt
angPos = angPos + angVel * dt
# the vpython "rotate" takes CHANGES to omega as argument, not omega
whiteBox.rotate( angle= angVel * dt, axis = angAxis )
# draw acc, vel if wanted
if ( drawAngAcc ):
# draw ang velocity
angVelVec.axis = vector ( 0,1,0 ) * angVel
# draw ang acc
angAccVec.pos = angVelVec.axis
angAccVec.axis = vector( 0,angAcc,0 ) * 5.0