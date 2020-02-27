def is_power_of(number, base):
  # Base case: when number is smaller than base.
  print(number, base)
  if number == 1:
    return True
    # If number is equal to 1, it's a power (base**0).
  elif number < base:
    return False
  # Recursive case: keep dividing number by base.
  print("calling function with number {} and base {}".format(number, base))
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
