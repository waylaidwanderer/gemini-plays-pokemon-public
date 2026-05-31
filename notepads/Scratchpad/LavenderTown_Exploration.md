# Scratchpad for Lavender Town and Pokémon Tower Exploration
- **Turn 37559**: Standing at (8, 6) on Map 0_4 (Lavender Town) facing Right.
- **Immediate Goal**: Walk east to column 14, then walk Up to (14, 5) to enter the Pokémon Tower.
- **Route to Tower Entrance (14, 5)**:
  - (8, 6) -> (9, 6) (Right)
  - (9, 6) -> (10, 6) (Right)
  - (10, 6) -> (11, 6) (Right)
  - (11, 6) -> (12, 6) (Right)
  - (12, 6) -> (13, 6) (Right)
  - (13, 6) -> (14, 6) (Right)
  - (14, 6) -> (14, 5) (Up)
- **Observations**:
  - NPC (SPRITE_cdfc) is standing at (12, 7) or (13, 7) facing Left. Wait, last turn he was reported at (12, 7). He seems to be moving.
  - Socratic Challenge Note: GEMMY has BITE. In Gen 1, BITE is a Normal-type move. It has NO effect on Ghost-types (Gastly, Haunter) in the Pokémon Tower. We must use DIG or other non-Normal moves!

## Pokémon Tower Combat Strategy (Turn 37562)
- **Problem**: Pidgeotto's GUST and general Normal-type moves do absolutely 0 damage to Ghost/Poison Pokémon (Gastly, Haunter) in Pokémon Tower.
- **Combat Readiness**:
  - **GEMMY (BLASTOISE, Level 44)**: Knows DIG (Ground-type, PP: 10), which deals super-effective damage to Ghost/Poison types. Will be our primary sweeper in the tower.
  - **SPARKY (PIKACHU, Level 24)**: Knows THUNDERBOLT (Electric-type, PP: 15), which deals neutral damage. Can be used for cleanup or back-up.
  - **Other Moves**: Do not use BITE (GEMMY) or TACKLE (BUGGY, ROCKY) as they are Normal-type in Gen 1 and will deal no damage.
- **Execution Tracking**:
  - Start Turn: 37562
  - Date/Time: Sunday, May 31, 2026 at 7:05 AM PDT