import navigate_safari

# We are in Area 1 (East) at (12, 22)
waypoints = [
    (8, 22),  # Move left to column 8
    (8, 8),   # Walk up column 8
    (12, 8),  # Move right to northern plateau west stairs
    (12, 6),  # Climb stairs to northern plateau
    (17, 6),  # Walk right along northern plateau
    (17, 8)   # Descend east stairs to ground
]

steps, transitioned = navigate_safari.navigate_chunk(waypoints, "area1", max_steps=32)
print(f"Completed chunk: steps={steps}, transitioned={transitioned}")
