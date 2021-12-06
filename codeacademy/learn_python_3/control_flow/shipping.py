# Program to estimate shipping costs based on 3 types

# Initial value, not needed when converting control flows to functions
weight = 0

# Ground Shipping
def ground_shipping(weight):
  if weight <= 2.0:
    ground_cost = 1.5 * weight + 20
  elif weight <= 6.0:
    ground_cost = 3.0 * weight + 20
  elif weight <= 10.0:
    ground_cost = 4.0 * weight + 20
  else:
    ground_cost = 4.75 * weight + 20
  return ground_cost

# 8.4 lbs should cost $53.60
# 8.4 * $4.00 + $20.00 = 53.60
assert ground_shipping(8.4) == 53.6

premium_cost = 125.0

# print(f"Ground Shipping Premium ${premium_cost:.2f}")

# Drone Shipping
def drone_shipping(weight):
  if weight <= 2.0:
    drone_cost = 4.5 * weight
  elif weight <= 6.0:
    drone_cost = 9.0 * weight
  elif weight <= 10.0:
    drone_cost = 12.0 * weight
  else:
    drone_cost = 14.25 * weight
  return drone_cost

# 1.5 lbs should cost $6.75 
# 1.5 * $4.50 + $0.00 = $6.75
assert drone_shipping(1.5) == 6.75

# prices for 4.8 lbs
print(f'Ground Shipping ${ground_shipping(4.8):.2f}')
print(f"Ground Shipping Premium ${premium_cost:.2f}")
print(f'Drone Shipping ${drone_shipping(4.8):.2f}')

# prices for 41.5 lbs
print(f'Ground Shipping ${ground_shipping(41.5):.2f}')
print(f"Ground Shipping Premium ${premium_cost:.2f}")
print(f'Drone Shipping ${drone_shipping(41.5):.2f}')
