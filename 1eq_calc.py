import sympy
from fractions import Fraction

print('Insert coordinates of two points from a plane on the following fields to find information about them.')
print('\nPoint A')
xa, ya = float(input('X: ')), float(input('Y: '))
print('\nPoint B')
xb, yb = float(input('X: ')), float(input('Y: '))

def formatNum(num):
    if num % 1 == 0:
        return int(num)
    else:
        return Fraction(num).limit_denominator()

def formatAng(ang):
    if ang < 0:
        return ang + 180
    else:
        return ang

x_delta = xb - xa
y_delta = yb - ya

if x_delta == 0:
    print('\nBoth points cannot have the same X value!')
else:
    a_coeff = y_delta / x_delta
    b_coeff = ya - a_coeff * xa
    root_hyp = sympy.sqrt(formatNum(x_delta)**2 + formatNum(y_delta)**2)
    decimal_hyp = sympy.N(sympy.sqrt(x_delta**2 + y_delta**2))
    a_angle = sympy.N(sympy.atan(a_coeff) * 180 / sympy.pi)
    
    print('\nFunction: F(x)=' + str(formatNum(a_coeff)) + 'x+' + str(formatNum(b_coeff)))
    if type(root_hyp) == sympy.core.numbers.Integer:
        print('Distance between both points: ' + str(root_hyp))
    else:
        print('Distance between both points: ' + str(root_hyp) + ' (aprox. ' + str("{:.2f}".format(decimal_hyp)) + ')')
    print('Angle: ' + str("{:.2f}".format(formatAng(a_angle))) + '°')