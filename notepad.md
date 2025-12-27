# Suicune Quest Strategy (Crystal Version)
- **Status:** Possession of Clear Bell confirmed. Sightings on Route 42 and 36 complete.
- **Narrative Flag:** Gatehouse Sage confirmed "The TIN TOWER shook! A POKéMON must have returned to the top!"
- **Current Objective:** Trigger the Wise Trio battle in Map 4_2.
- **Problem:** Wise Trio Room (4_2) is empty despite "shook" dialogue.
- **Hypothesis:** One or more NPCs in the Gatehouse (4_1) must be spoken to in a specific sequence to trigger the Trio's appearance in 4_2.
- **Plan:**
  1. Return to the Gatehouse (4_1).
  2. Use `run_code` to identify all objects in 4_1.
  3. Talk to every NPC in 4_1.
  4. Check 4_2 for the Wise Trio.
  5. If successful, defeat Gaku, Masa, and Koji.

## Tile Mechanics - Global
- **FLOOR**: Standard walkable tile.
- **WALL / VOID**: Impassable.
- **WATER**: Requires SURF.
- **LADDER / STAIRS / DOOR**: Warp.

## Trainer & Party Info
- **Lead:** XENON (Gastly) Lv21 (Hypnosis/Mean Look).
- **Party:** Gastly, Pidgey, Graveler, Krabby, Gloom, Typhlosion.