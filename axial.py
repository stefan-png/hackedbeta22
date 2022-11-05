ROOT3 = 1.73205080757

import math 

def _cube_to_axial(cube):
    q = cube[0]
    r = cube[1]
    return (q, r)

def _axial_to_cube(hex):
    q = hex[0]
    r = hex[1]
    s = -q-r
    return (q, r, s)


def _cube_round(frac):
    q = round(frac[0])
    r = round(frac[1])
    s = round(frac[2])

    q_diff = abs(q - frac[0])
    r_diff = abs(r - frac[1])
    s_diff = abs(s - frac[2])

    if q_diff > r_diff and q_diff > s_diff:
        q = -r-s
    elif r_diff > s_diff:
        r = -q-s
    else:
        s = -q-r

    return (q, r, s)

def axial_round(hex):
    return _cube_to_axial(_cube_round(_axial_to_cube(hex)))

def screen_to_axial(vector2, size):
    q = (2.0*vector2[0]/3.0)/size
    r = (-vector2[0]/3.0 + ROOT3*vector2[1]/3.0)/size
    return axial_round((q, r))

def axial_to_screen(axial, size):
    x = (1.5*axial[0])*size
    y = (ROOT3*axial[0]/2.0 + ROOT3*axial[1])*size
    return (x, y)