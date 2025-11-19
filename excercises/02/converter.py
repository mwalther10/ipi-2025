from conversion import degrees_to_radians, radians_to_degrees, gradians_to_radians, radians_to_gradians, degrees_to_gradians, gradians_to_degrees

INPUT = ["D", "R", "G"]

print("Source unit [D / R / G]:")
source_unit = input().strip().upper()
if source_unit not in INPUT:
    print("Invalid source unit.")
    exit(1)
print("Target unit [D / R / G]:")
target_unit = input().strip().upper()
if target_unit not in INPUT:
    print("Invalid target unit.")
    exit(1)
print("Value to convert:")
try:
    value = float(input().strip())
except ValueError:
    print("Invalid value.")
    exit(1)
if source_unit == target_unit:
    result = value
elif source_unit == "D" and target_unit == "R":
    result = degrees_to_radians(value)
elif source_unit == "R" and target_unit == "D":
    result = radians_to_degrees(value)
elif source_unit == "G" and target_unit == "R":
    result = gradians_to_radians(value)
elif source_unit == "R" and target_unit == "G":
    result = radians_to_gradians(value)
elif source_unit == "D" and target_unit == "G":
    result = degrees_to_gradians(value)
elif source_unit == "G" and target_unit == "D":
    result = gradians_to_degrees(value)
print(f"{format(value, '.1f')} {source_unit} corresponds to {format(result, '.1f')} {target_unit}")
