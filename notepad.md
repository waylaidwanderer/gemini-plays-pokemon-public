# Johto Progression: The Rock Smash Quest
## Primary Goal: Obtain TM08 Rock Smash
- **Strategy:** Buy TM08 at Goldenrod Dept. Store 5F (¥1000).
- **Quest History:** 
  - Checked Route 36 NPCs (Turns 50430-50490); Fisher (44, 9) gives post-gift dialogue but no item.
  - Checked PC storage (Turn 50513); empty.
  - Conclusion: TM flag set but item missing. Fallback: Purchase at Dept. Store.

## Secondary Goal: Trigger Suicune Sighting in Cianwood City
- **Location:** (14, 10) in Cianwood City.
- **Status:** Blocked by boulders at (4, 19) and (8, 16). Rock Smash mandatory.

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