# Cianwood City Progression
## Strategy: Trigger Suicune Sighting at (14, 10)
- **Status:** In Progress. Verified that Rock Smash is required for the land bypass.
- **Route:** Wall Gap (5, 34) -> Terrace Ascent (4, 30), (4, 20) -> Northern Loop (14, 10).

## Strategy: Olivine Lighthouse Progress
- **Status:** Completed (16 badges obtained). Pharmacist at (2, 3) is now a regular shopkeeper.

## Strategy: Finding TM08 Rock Smash
- **Start Turn:** 50283
- **Status:** Searching for the TM. Pokefan M (18, 33) only hints. Pharmacy was a dead end.
- **Remaining Leads:**
  1. Investigate Lugia Speech House (15, 37). (Next)
  2. Re-check Gym Leader Chuck (8, 43) or his wife outside.
  3. Fly to Route 36 to find the NPC near where Sudowoodo was.

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
## Strategy: The Eastern Water Route (Surf)
- **Start Turn:** 50338
- **Goal:** Reach Suicune at (14, 10) without Rock Smash.
- **Steps:**
  1. Navigate to the Surf spot at (12, 28).
  2. Surf North into the water pocket (West of the buoy line).
  3. Surf North to (14, 16).
  4. Land West on the plateau at (13, 16).
  5. Walk North to the trigger point at (14, 10).
- **Verification:** Pathfinder (Turn 50310) confirmed land route requires Rock Smash. Water pocket is continuous from Row 27 to Row 16.