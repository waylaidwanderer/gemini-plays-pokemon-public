import safari_helper

waypoints = [
    (20, 23),
    (20, 19),
    (12, 20),
    (12, 22),
    (12, 8),
    (12, 6),
    (0, 5)
]

print("Starting Safari Part 1 navigation...")
for wp in waypoints:
    print(f"Going to waypoint: {wp}")
    safari_helper.navigate_to(wp[0], wp[1])

print("Transition completed or sequence finished!")
