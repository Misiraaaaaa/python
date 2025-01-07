from graphics.rectangle import area as rectarea,perimeter as rectperimeter
from graphics.circle import area as circlearea,perimeter as circleperimeter
from graphics.threedgraphics.sphere import area as spherearea, volume as spherevolume
from graphics.threedgraphics.cuboid import area as cuboidarea, volume as cuboidvolume
print("rectangle area : ",rectarea(4,5))
print("rectangle perimeter : ",rectperimeter(4,5))
print("circle area :", circlearea(7))
print("circle perimeter :", circleperimeter(7))
print("sphere area :", spherearea(6))
print("sphere volume :", spherevolume(6))
print("cuboid area :", cuboidarea(2,3,4))
print("cuboid volume :", cuboidvolume(2,3,4))