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
- [Turn 47720] 50-Turn Reflection: I am currently executing my escape from the B1F Southern trap using Dig. I've realized that the Central Switch is a red herring for solving the Secret Key puzzle. Toggling it to State A traps you in the southern room, meaning you must enter the NW section of B1F from a different location while the Mansion is ALREADY in State A. This strongly points to a second pit on 3F. Once I escape and heal, I will thoroughly explore the 3F West Wing.
- Turn 47729: Decided to use Dig to escape the B1F southern trap. My team's HP is actually fine, but Dig is the fastest way out. The goal now is to return to the Mansion, head straight to 3F, and thoroughly explore the West Wing (South of Y=10) for a second pit that might drop into the isolated NW area of B1F.
- Turn 47738: Successfully used Dig to escape the B1F trap and returned to Cinnabar Island. Healing up before re-entering the Mansion.
- Turn 47750: HALLUCINATION CORRECTED! I just reviewed my notes and realized I ALREADY SOLVED the puzzle! The 'Airlock Puzzle Solution' in my PokemonMansion notes is the correct path. The B1F Central Switch at (18, 25) is a deliberate red herring trap designed to lock you in the south room. I do NOT need to find a second pit on 3F.
- The True Route: Reach 3F, toggle the 3F switch (10, 4) to State B, drop down the 3F pit (16, 14), land on B1F in State B. Walk to the NE Switch (20, 3) via the open Far East doors (26, 17), toggle it to State A to open the Secret Key doors at (9, 7). Executing this now.
- Turn 47772 (50-Turn Reflection): I am successfully executing the "Airlock Puzzle Solution" after correcting a massive hallucination. I realized the B1F Central Switch was a red herring designed to trap me, and I did not need to search for a non-existent "second pit" on 3F. I am now strictly following my empirically verified notes in `Locations/PokemonMansion`. I've also successfully adapted my tool usage, using `press_buttons` for switch toggles to avoid the text-eating desyncs caused by `move_sequence`. Next step is to take the stairs at (21, 23) down to B1F.
- Turn 47777: EMPIRICAL PROOF OVERRIDES NOTES: I am standing at (26, 18) in State B. The Far East doors at (26, 17) are VISUALLY CLOSED (TYPE_a83b). My notes claiming they are open in State B are WRONG. Since both (26, 17) and the Secret Key doors at (9, 7) are closed in State B, there is no "Airlock". I must return to the B1F Central Switch at (18, 25) and toggle it to State A. I predict this will open BOTH doors.