# ******* 2 ********

def sphere(radius):
    v = (4 / 3) * (3.1416) * (radius * radius * radius)
    print(round(v,2))   # take upto 2 digits after decimal.
    return v


radius = int(input("Enter the radius of the sphere: "))
sphere(radius)
