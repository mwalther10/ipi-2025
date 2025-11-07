p = float(input("p = "))
q = float(input("q = "))

p_half = p / 2
p_half_negative = -p_half
root = (p_half**2 - q) ** 0.5

print("x1 = " + str(p_half_negative + root))
print("x2 = " + str(p_half_negative - root))
##############################

# alternative with math module
import math

p_half = p / 2
p_half_negative = -p_half
root = math.sqrt(math.pow(p_half, 2) - q)

print("x1 = " + str(p_half_negative + root))
print("x2 = " + str(p_half_negative - root))
