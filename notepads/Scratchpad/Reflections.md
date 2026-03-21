[ACTIVE THEORIES & REFLECTIONS]
- Secret Key Location Hypotheses:
  1. In the West Room of B1F (near the 7,15 switch). (FALSE - Turn 47489 proved it's a dead end loop)
  2. Accessed via a completely different pit on 3F (SW corner, South of Y=10) that drops directly into a blocked-off room on 1F or B1F. (ACTIVE)

[Current Plan: The "No Airlock" Strategy]
- Mechanics: The doors at X=9 are CLOSED in State B, requiring State A to access the NW room. The Far East doors at (26, 17) provide a path North to Y=7, bypassing the solid wall at Y=8. The NE switch at (20, 3) toggles states from the North side.
- By Turn 47607, I proved the Far East doors at (26, 17) are CLOSED in State B. Since the Secret Key doors at (9, 7) are ALSO CLOSED in State B, BOTH sets of doors must be OPEN in State A.
- Therefore, the solution is simple: Toggle the Central Switch at (18, 25) to State A, walk up the East corridor, cross West at Y=7, and walk right in.
- Turn 47637: Toggled Central Switch to State A. Currently executing the path to the Secret Key doors.

[Macro & Execution Lessons]
- Massive 40-50 step macros in high-encounter zones fail because encounters interrupt them, causing misalignment. I now use 5-10 step micro-macros and actively verify Game State coordinates.
- Always visually verify facing direction after a battle interruption!
- When caught in a dialogue loop or text box, use `safe_mash_b` or multi-button `press_buttons` calls (e.g., `['A', 'A', 'A']`) instead of single `move_sequence` calls to resolve the interaction efficiently.