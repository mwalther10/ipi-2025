from conversion import (
    degrees_to_radians,
    radians_to_degrees,
    gradians_to_radians,
    radians_to_gradians,
    degrees_to_gradians,
    gradians_to_degrees,
)

INPUT = ["D", "R", "G"]

source_unit = input("Source unit [D / R / G]: ").strip().upper()
if source_unit not in INPUT:
    # check is good practice
    print("Invalid source unit.")
    exit(1)

try:
    value = float(input("Source value: ").strip())
except ValueError:
    print("Invalid source value.")
    exit(1)

target_unit = input("Target unit [D / R / G]: ").strip().upper()
if target_unit not in INPUT:
    # check is good practice
    print("Invalid target unit.")
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

print(
    f"\n{format(value, '.1f')} {source_unit} "
    f"corresponds to {format(result, '.1f')} {target_unit}"
)
