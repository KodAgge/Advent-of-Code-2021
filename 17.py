import math

TARGET_X_MIN = 282
TARGET_X_MAX = 314
TARGET_Y_MIN = -80
TARGET_Y_MAX = -45
# TARGET_X_MIN = 20
# TARGET_X_MAX = 30
# TARGET_Y_MIN = -10
# TARGET_Y_MAX = -5

# Part 1
print(f"Answer part 1: {TARGET_Y_MIN * (TARGET_Y_MIN + 1) / 2}")

# Part 2
def smallest_x_stop_before_x_min():
    return int(-1/2 + math.sqrt(1/4 + 2 * TARGET_X_MIN))

velocity_count = 0
for v_x_0 in range(smallest_x_stop_before_x_min()+1, TARGET_X_MAX + 1):
    for v_y_0 in range(TARGET_Y_MIN, -TARGET_Y_MIN + 1):
        x, y = 0, 0
        x_velocity, y_velocity = v_x_0, v_y_0
        while y >= TARGET_Y_MIN and x <= TARGET_X_MAX:
            x += x_velocity
            y += y_velocity
            x_velocity = max(x_velocity - 1, 0)
            y_velocity -= 1
            if y >= TARGET_Y_MIN and y <= TARGET_Y_MAX:
                if x >= TARGET_X_MIN and x <= TARGET_X_MAX:
                    velocity_count += 1
                    break
print(f"Answer part 2: {velocity_count}")