Pokemon Mansion Navigation & Discoveries:

MECHANICS (DEFINITIVE):
- Exiting to Cinnabar Island resets everything to State A.
- Switch prompt: YES = TOGGLES STATE. NO = DOES NOTHING.
- State A (Default):
  - Dark Grey Shutters (e.g. 20,16..26): OPEN (Walkable)
  - Yellow Shutters (Vertical, e.g. 13,22..23): OPEN (Walkable)
  - Yellow Shutters (Horizontal, e.g. 14,16..15,16, 18,16..19,16, 9,6..7, 26,17): CLOSED (Solid)
- State B (Toggled by switch):
  - Dark Grey Shutters (e.g. 20,16..26): CLOSED (Solid)
  - Yellow Shutters (Vertical, e.g. 13,22..23): CLOSED (Solid)
  - Yellow Shutters (Horizontal, e.g. 14,16..15,16, 18,16..19,16, 9,6..7, 26,17): OPEN (Walkable)

PERMANENT WALLS (Never open):
- y=17 solid wall (x=1 to x=8) blocking North/South in the West Wing.
- y=8 solid wall (x=10 to x=24) blocking North/South in the Middle Section and East Wing.
- x=13 solid wall (y=17 to y=21) and (y=24 to y=26).
- x=9 solid wall (y=8 to y=17).
- y=27 solid wall blocks connecting West/Middle/East wings.
- The dark grey tiles at (9, 8..10) are SOLID PERMANENT WALLS.
- The tiles at y=17 (x=14..15 and x=18..19) are permanent solid objects (statue bases/tables), NOT yellow shutters. There is a permanent open gap at x=16 and x=17.

CURRENT ROUTING GOAL:
Take stairs at 1F (23, 22) up to 2F East. Ensure Mansion is in State B.
On 2F, walk to (21, 18), avoiding drop hole at (21, 23).
Walk Up through gap at (21, 17) to (21, 16).
Walk Right to x=26, then North to (26, 6) bypassing y=8 wall.
Walk West to (9, 6) and pass through OPEN yellow shutters into West Wing.
Navigate West Wing North to reach stairs to 3F at (6, 1).