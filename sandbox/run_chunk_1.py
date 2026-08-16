import navigate_safari

# We are in Area 1 (East) at (13, 24)
waypoints = [
    (20, 24), # Walk right along southern ground
    (20, 20), # Climb stairs to southern plateau
    (12, 20), # Walk left along southern plateau
    (12, 22)  # Descend stairs to ground level
]

steps, transitioned = navigate_safari.navigate_chunk(waypoints, "area1", max_steps=22)
print(f"Completed chunk: steps={steps}, transitioned={transitioned}")
