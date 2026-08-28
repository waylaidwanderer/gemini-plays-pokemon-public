# Pokémon Mansion 1F - Map & Navigation Log

## Layout & Spatial Boundaries (Verified State A)
- **Entrance Warp:** Entering from Cinnabar Island at `(6, 3)` warps the player to `(5, 27)` inside 1F West. Stepping DOWN on `(5, 27)` inside 1F West exits the Mansion back to Cinnabar Island at `(6, 3)`.
- **North-South Shutter Gates (Row 8/9):** Completely CLOSED across Columns 5, 6, 7 in State A on 1F West, preventing vertical traversal from Row 7 to Row 8 on the West side.
- **Solid Horizontal Wall (Row 9, Columns 3-9):** A solid permanent horizontal wall separates the southern hallway (Row 10-14) from the northern hallway (Row 5-8) on 1F West. This blocks vertical traversal on Columns 3, 4, 5, 6, 7, 8, and 9, meaning vertical crossing can only occur on Columns 10, 11, 12, or 13, which are completely open floor.
- **Solid Separation Wall (Column 18):** Column 18 is a solid permanent wall separating 1F West from 1F East, blocking all horizontal traversal between the two halves of the floor.
- **Warp to 2F West:** The staircase at `(5, 10)` on 1F West warps the player UP to 2F West. This staircase is accessed from the South side (standing at `(6, 10)` and stepping LEFT onto `(5, 10)`).
- **Horizontal Openness (Row 7):** Row 7 on 1F West is completely open horizontally from Column 5 to Column 17.
## State-Dependent Spatial Barriers (Verified)
- **Row 5 Column 21 Shutter Gate (1F East):** CLOSED in State A, OPEN in State B (verified Turns 56673-56699).
- **B1F East Stairs Gate at (22, 2) (1F East):** CLOSED in State A, OPEN in State B (verified Turn 56693).