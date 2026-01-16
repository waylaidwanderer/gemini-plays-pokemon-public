# Johto Progression: The Rock Smash Quest
## Primary Goal: Obtain TM08 Rock Smash
- **Status:** Missing from Bag/PC. Fisher on Route 36 says "smash 'em up!" (Post-gift dialogue).
- **Strategy:**
  1. Fly to Goldenrod City.
  2. Visit Dept. Store 5F and buy TM08 (¥1000).
  3. Teach to GNEISS (Graveler).
- **Quest History:** Checked Route 36 NPCs; PC empty (Turn 50513).
- **Tool Maintenance:** fly_to_city_v1 failed (Turn 50526). Redefining fly_to_city_v2.

## Secondary Goal: Trigger Suicune Sighting in Cianwood City
- **Location:** (14, 10) in Cianwood City.
- **Status:** Blocked by boulders. Rock Smash mandatory.

## Global Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY / HEADBUTT_TREE: Impassable.
- WATER: Requires Surf.
- DOOR / WARP_CARPET: Warp point.
- SMASHABLE_ROCK (Object): Requires Rock Smash.

## Lessons Learned
- **Fisher Dialogue:** "If any rocks are in your way..." is post-gift. Acquisition flag is set even if item is gone.
- **Fly Logic:** Slot 6 (Icarus) is 'Up' x 1 from Slot 1 in Pokémon menu.
- **Arthur (45, 6):** Only gives Hard Stone on Thursdays.