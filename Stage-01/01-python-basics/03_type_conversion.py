x = "100"
y = int(x)

print(type(x))
print(type(y))

x = 25
y_float = float(x)
y_string = str(x)
y_bool = bool(x)    # non-zero = true

print(f"Values: float {y_float} string {y_string} bool {y_bool}")

x = 0
y_bool = bool(x)    # zero = false

print(y_bool)

x=""
print(bool(x))      # Empty string = false

print(bool("False"))    # Non-empty = true