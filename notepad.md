# Cianwood City Progression
## Strategy: Trigger Suicune Sighting at (14, 10)
- **Status:** In Progress. Verified that Rock Smash is required for the land bypass.
- **Route:** Wall Gap (5, 34) -> Terrace Ascent (4, 30), (4, 20) -> Northern Loop (14, 10).

## Strategy: Finding TM08 Rock Smash
- **Start Turn:** 50283
- **Status:** Searching for the TM. Pokefan M (18, 33) only hints.
- **Remaining Leads:**
  1. Investigate Lugia Speech House (15, 37).
  2. Re-check Gym Leader Chuck (8, 43) or his wife outside.
  3. Route 36 (if Cianwood is a dead end).

## Strategy: Olivine Lighthouse Progress
- **Start Turn:** 50332
- **Goal:** Obtain SecretPotion for Amphy.
- **Status:** Talking to Pharmacist at (2, 3) in Cianwood Pharmacy.

## Global Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY: Impassable.
- WATER: Requires Surf.
- DOOR / WARP_CARPET: Warp point.
- LEDGE_HOP_DOWN: One-way South jump.
- FLOOR_UP_WALL: One-way North climb.
- SMASHABLE_ROCK (Object): Impassable. Requires Rock Smash.

## General Lessons
- **NPC Interaction:** Chasing moving NPCs is inefficient. Wait in their path or use `stun_npc` to ensure the interaction triggers. (Learned Turns 50301-50314).
- **Rock Smash Verification:** Confirmed via pathfinder (Turn 50310) that the land route to Suicune is blocked by boulders.

## Failed Hypotheses
- Pokefan M (18, 33): Hint only.
- Pokefan F (10, 46): Hint only.
- Mania (2, 4): Dead end (asks for Shuckle).
- Lass (14, 44): Dead end (talks about Chuck).