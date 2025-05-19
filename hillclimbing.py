import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return -x ** 2 


def hill_climbing(init_x, max_iterations = 1000, step_size = 0.9):
  current_x = init_x
  iteration = 0
  current_y = f(current_x)

  x_values = [current_x]
  y_values = [current_y]

  while iteration < max_iterations:
    neighbor_x = current_x + step_size * np.random.uniform(-1, 1)
    neighbor_y = f(neighbor_x)

    if neighbor_y > current_y:
      current_x = neighbor_x
      current_y = neighbor_y
      x_values.append(current_x)
      y_values.append(current_y)

    iteration += 1
  return current_x, f(current_x), x_values, y_values

inital_x = float(input("Enter the inital value for x: "))
 
best_x, y, x_values, y_values = hill_climbing(inital_x)

original_x_values = np.linspace(min(x_values), max(x_values), 1000)
original_y_values = [f(x) for x in original_x_values]
plt.plot(original_x_values, original_y_values)
plt.plot(x_values, y_values)
plt.title("Hill Climbing Algorithm")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
