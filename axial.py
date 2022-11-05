ROOT3 = 1.73205080757


def screen_to_axial(vector2):
    q = 2.0*vector2[0]/3.0
    r = -vector2[0]/3.0 + ROOT3*vector2[1]/3.0
    return (q, r)

def axial_to_screen(axial):
    x = 1.5*axial[0]
    y = ROOT3*axial[0]/2.0 + ROOT3*axial[1]
    return (x, y)