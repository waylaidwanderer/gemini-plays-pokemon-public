# Mewtwo Quest Log (Post-Game)
- Started: Turn 111394
- Goal: Enter Cerulean Cave and catch Mewtwo.

## Current status & Progression
- Navigating the corridors of 2F West to find a path to the northwest ladder.

## 2F Exploration Discoveries & Pathing Notes
- Turn 112555: Tested passability of (8, 5) on 2F West. Stood at (9, 5) and pressed Left. Result: Did not change coordinates, received "pressed 1 movement buttons, but visited 0 tiles" system warning. Conclusion: (8, 5) is definitively an impassable rock wall, proving that the Lower Band (Rows 5-7) on the west cannot be accessed from Column 9 on Row 5 on foot.
- Turn 112601: Empirically tested Column 19 passability on foot from the east on 1F. Stood at (20, 15) facing Left, pressed Left to walk onto (19, 15). Result: Coordinate remained (20, 15), received bump warning. This definitively proves that Column 19 is impassable on foot at Row 15. Combined with visual confirmation of solid rock walls (TYPE_2889) on Column 19 from Row 11 down to Row 18, the eastern entrance platform of 1F is indeed completely physically isolated on foot from the western/southern portion of 1F.

- Turn 112986: Discovered that Row 5 contains water across Columns 21-25, blocking on-foot horizontal crossover from Water Ramp 3 at (25, 9) to Ladder 2 at (27, 1) directly. To access Ladder 2 (which sits on the northern landmass at Rows 0-2), we must use Water Ramp 1 at (23, 3) because it lands directly on Row 3/2, which connects horizontally to Column 27 on Rows 0-2!
- Turn 113013: Discovered that on 2F East, we are completely blocked on the small island around (22, 6) and cannot reach Ladder 3 at (19, 7) because of solid rock walls (TYPE_2889) at (23, 6) and (21, 6). The only passable direction from (22, 6) is Down to (22, 7) then Right to (23, 7) (which is the ladder we came from). So we must backtrack down the ladder at (22, 6) / (23, 7) back to 1F.