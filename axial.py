ROOT3 = 1.73205080757

import math 


def screen_to_axial(vector2, size):
    q = (2.0*vector2[0]/3.0)*size
    r = (-vector2[0]/3.0 + ROOT3*vector2[1]/3.0)*size
    return (q, r)

def axial_to_screen(axial, size):
    x = (1.5*axial[0])*size
    y = (ROOT3*axial[0]/2.0 + ROOT3*axial[1])*size
    return (x, y)