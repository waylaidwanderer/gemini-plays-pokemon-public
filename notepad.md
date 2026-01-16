# Johto Progression: The Rock Smash Quest
## Primary Goal: Obtain TM08 Rock Smash
- **Strategy:** Buy TM08 at Goldenrod Dept. Store 5F (¥1000).
- **Quest History:** Verified Fisher (44, 9) gives post-gift dialogue. TM08 not in Bag or PC (Turn 50513).

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
- **Fly Logic:** Slot 6 (Icarus) is 'Up' x 1 from Slot 1 in Pokémon menu. Use robust navigation (reset to top) to avoid persistent cursor issues.
- **Arthur (45, 6):** Only gives Hard Stone on Thursdays.