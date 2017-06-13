#ZERO DIVISION ERROR
a = 4 / 0			#BUG, division by zero
a = True / False #BUG, division by zero

import fractions

def method():
  return 0

fractions.Fraction(a,0)  #BUG, division by zero
fractions.Fraction(2,method())  #BUG, division by zero