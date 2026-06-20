# Mewtwo Quest Log (Post-Game)
- Started: Turn 111394
- Goal: Enter Cerulean Cave and catch Mewtwo.

## Current status & Progression
- Exiting Nugget Bridge at Row 12 to Surf south along the water canal on Column 8.

## 2F Exploration Discoveries & Pathing Notes
- Turn 112555: Tested passability of (8, 5) on 2F West. Stood at (9, 5) and pressed Left. Result: Did not change coordinates, received "pressed 1 movement buttons, but visited 0 tiles" system warning. Conclusion: (8, 5) is definitively an impassable rock wall, proving that the Lower Band (Rows 5-7) on the west cannot be accessed from Column 9 on Row 5 on foot.
- Turn 112601: Empirically tested Column 19 passability on foot from the east on 1F. Stood at (20, 15) facing Left, pressed Left to walk onto (19, 15). Result: Coordinate remained (20, 15), received bump warning. This definitively proves that Column 19 is impassable on foot at Row 15. Combined with visual confirmation of solid rock walls (TYPE_2889) on Column 19 from Row 11 down to Row 18, the eastern entrance platform of 1F is indeed completely physically isolated on foot from the western/southern portion of 1F.
- Turn 112769: Navigated South down Route 24 water canal, currently at (8, 28) on the water. Planning to surf Down to (8, 32) and then head West to reach the western canal leading to Cerulean Cave.
- Turn 112813: Scientific Test Plan for Northern Water Canal Column 13/14 passability on Rows 4-5.
  - **Hypothesis**: The northern water canal on Rows 4-5 is open and passable horizontally, allowing us to surf directly from the eastern water canal (Column 25) to the western water canal (Column 8), bypassing the 2F/1F platforms entirely.
  - **Test Procedure**:
    1. Surf on 1F using Water Ramp 3 at (25, 9) to enter the water at (25, 10).
    2. Surf North up the eastern water canal to Row 5 (25, 5).
    3. Surf West along Row 5 (or Row 4) from Column 25 towards Column 8.
    4. Record the outcome at Column 13 to prove or disprove passability.
- Turn 112818: Preparing to test Row 5 Column 13 blockage. We navigated next to Column 13 at (14, 5).
  - **New Discovery**: Rows 6 and 7 on Column 13 are completely open, passable water (TYPE_4e8c)!
  - **New Plan**: Surf Down 1 step to (14, 6) and then Left along Row 6 to reach the western canal at Column 10. This allows us to bypass the rock wall on Rows 4-5. We will test Column 13 Rows 4 and 5 later.