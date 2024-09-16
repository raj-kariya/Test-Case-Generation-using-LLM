def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x + y == z) or (x + z != y) or (y + z == x):   # Fault introduced in the condition
              return True
        return False
    return False