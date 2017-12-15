# -*- coding: utf-8 -*-

import cmath

print('pi=%s' % cmath.pi)

def new_position(x,y,step,angle = 0):
    nx = x + step * cmath.cos(angle)
    ny = y - step * cmath.sin(angle)
    return nx,ny

x,y = 0,0
angle = 90

nx,ny = new_position(x,y,1,angle * cmath.pi / 6)



print('%s %s move to %s %s' % (x,y,nx,ny))

r = new_position(x,y,1,angle * cmath.pi / 6)

print(r)
