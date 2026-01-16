# Cianwood City Progression
## Strategy: Trigger Suicune Sighting at (14, 10)
- **Start Turn:** 50283 (Thursday, Jan 15, 2026, 10:30 PM PST)
- **Status:** In Progress. Verified that Rock Smash is required for the land bypass.
- **Route:** Wall Gap (5, 34) -> Terrace Ascent (4, 30), (4, 20) -> Northern Loop (14, 10).

## Strategy: Finding TM08 Rock Smash
- **Start Turn:** 50283
- **Status:** Searching for the TM. Pokefan M (18, 33) is the primary source in Crystal after defeating Leader Chuck.
- **Plan:**
  1. Investigate Lugia Speech House (15, 37). (Current: Talking to NPCs)
  2. Stun Pokefan M (Sprite ID 2) and talk to him from the front.
  3. Re-verify Route 36 NPC if Cianwood fails.

## Global Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY: Impassable.
- WATER: Requires Surf.
- DOOR / WARP_CARPET: Warp point.
- LEDGE_HOP_DOWN: One-way South jump.
- FLOOR_UP_WALL: One-way North climb.
- SMASHABLE_ROCK (Object): Impassable. Requires Rock Smash.

## General Lessons
- **NPC Interaction:** Chasing moving NPCs is inefficient. Wait in their path or use `stun_npc` to ensure the interaction triggers.
- **Rock Smash Verification:** Confirmed via pathfinder (Turn 50310) that the land route to Suicune is blocked by boulders.

## Failed Hypotheses
- Pokefan M (18, 33): Hint only (Turn 50278, 50281). Likely requires specific positioning or post-Chuck trigger.
- Pokefan F (10, 46): Hint only.
- Mania (2, 4): Dead end (asks for Shuckle).
- Lass (14, 44): Dead end (talks about Chuck).

## Strategy: The Eastern Water Route (Surf)
- **Goal:** Reach Suicune at (14, 10) without Rock Smash.
- **Steps:**
  1. Navigate to the Surf spot at (12, 28).
  2. Surf North to (14, 16).
  Land West on the plateau at (13, 16).
  4. Walk North to (14, 10).