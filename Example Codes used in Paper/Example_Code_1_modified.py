Equilateral = 0
Scalene = 1
Right_Triangle=2

def triangle_type(a, b, c):
  if a < b + c and b < a + c and c < a + b:
    if  a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
      return Right_Triangle
    if a == b == c:
      return Equilateral
    return Scalene
  return None