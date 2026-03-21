[ACTIVE THEORIES & REFLECTIONS]
- Secret Key Location Hypotheses:
  1. In the West Room of B1F (near the 7,15 switch). (FALSE - Turn 47489 proved it's a dead end loop)
  2. Accessed via a completely different pit on 3F (SW corner, South of Y=10) that drops directly into a blocked-off room on 1F or B1F. (ACTIVE)

[The "Central Switch Trap" Revelation]
- Turn 47701: Discovered that in State A, the Central Doors at (16, 16) and (17, 16) are CLOSED.
- The Central Switch is at (18, 25), which is South of these doors.
- The ONLY way to reach the Northern half of B1F (to access the Far East corridor or the NE Switch) is by crossing North through (16, 16).
- Therefore, toggling the Mansion to State A from the Central Switch TRAPS YOU in the southern room!
- The B1F Central Switch is a red herring/trap. It cannot be used to solve the puzzle, because you cannot leave the room while the necessary doors are open.
- The True Path MUST be a second pit on 3F that drops directly into the isolated NW section of B1F, bypassing the electronic doors entirely!
- Next steps: Escape this trap (toggle back to State B to open the doors, or use Dig), heal, and explore the West Wing of 3F.

[Macro & Execution Lessons]
- Massive 40-50 step macros in high-encounter zones fail because encounters interrupt them, causing misalignment. I now use 5-10 step micro-macros and actively verify Game State coordinates.
- Always visually verify facing direction after a battle interruption!
- When caught in a dialogue loop or text box, use `safe_mash_b` or multi-button `press_buttons` calls (e.g., `['A', 'A', 'A']`) instead of single `move_sequence` calls to resolve the interaction efficiently.