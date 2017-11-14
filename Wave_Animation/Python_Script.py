import math

node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

freq = node.evalParm("freq")
phase = node.evalParm("phase")
amp = node.evalParm("amp")

points = geo.points()

for p in points:
    pos = p.position()
    x = pos[0]
    z = pos[2]
    y = pos[1]+math.sin(z*phase+(hou.frame()*freq))*amp
    p.setPosition((x,y,z))
    
    
