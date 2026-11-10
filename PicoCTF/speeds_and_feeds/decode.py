import matplotlib.pyplot as plt
import re

# Read G-code from file
with open("gcode.txt", "r") as f:
    gcode = f.readlines()

x_coords = []
y_coords = []
current_x = 0
current_y = 0

for line in gcode:
    line = line.strip()
    if line.startswith(('G0', 'G1')):  # Only consider movement commands
        # Find X and Y values using regex
        x_match = re.search(r'X(-?\d+\.?\d*)', line)
        y_match = re.search(r'Y(-?\d+\.?\d*)', line)
        
        if x_match:
            current_x = float(x_match.group(1))
        if y_match:
            current_y = float(y_match.group(1))
        
        x_coords.append(current_x)
        y_coords.append(current_y)

# Plot the toolpath
plt.figure(figsize=(10, 10))
plt.plot(x_coords, y_coords, marker='o', markersize=2)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Toolpath Visualization")
plt.show()
