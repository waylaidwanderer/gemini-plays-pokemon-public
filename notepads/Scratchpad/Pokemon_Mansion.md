Pokemon Mansion Navigation & Discoveries:

MECHANICS (DEFINITIVE):
- Exiting to Cinnabar Island resets everything to State A.
- Switch prompt: YES ("Who wouldn't?") = TOGGLES STATE. NO ("Not quite yet!") = DOES NOTHING.
- State A (Default):
  - Dark Grey Shutters (e.g. 20,16..26): OPEN (Walkable)
  - Yellow Shutters at (13,22..23): OPEN (Walkable)
  - Yellow Shutters at (16,16..17,16) and (9,6..7): CLOSED (Solid)
- State B (Toggled by switch):
  - Dark Grey Shutters (e.g. 20,16..26): CLOSED (Solid)
  - Yellow Shutters at (13,22..23): CLOSED (Solid)
  - Yellow Shutters at (16,16..17,16) and (9,6..7): OPEN (Walkable)

PERMANENT WALLS (Never open):
- y=17 solid wall (x=1 to x=8) blocking North/South in the West Wing.
- y=8 solid wall (x=10 to x=16) blocking North/South in the Middle Section.
- x=13 solid wall (y=17 to y=21) and (y=24 to y=26).
- x=9 solid wall (y=8 to y=17).
- y=27 solid wall blocks connecting West/Middle/East wings.
- The dark grey tiles at (9, 8..10) are SOLID PERMANENT WALLS.

CURRENT ROUTING HYPOTHESIS TO 2F STAIRS:
The main stairs are at (5, 10). To reach them, I must pass through the Yellow Shutters at (9, 6)/(9, 7), which are OPEN in State B. 
To reach (9, 6)/(9, 7) in State B, I must navigate North in the East Wing (x >= 17) to bypass the y=8 wall, then walk West into the Middle Section North.
Plan:
1. Reach switch at (18, 25) and toggle to State B.
2. Walk North in the East Wing, bypassing y=17 tables via x=17.
3. Continue North past y=8 (if clear).
4. Walk West to (9, 7), pass through shutter to West Wing, and walk to stairs.
- EMPIRICAL PROOF (Turn 42323): y=8 is a SOLID WALL across the entire East Wing and Middle Section (verified at x=16 and x=17). There is NO path North past y=8 in this area. I must explore West Wing South for an alternative route.