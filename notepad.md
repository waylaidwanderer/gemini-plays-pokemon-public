# Johto Progression: The Rock Smash Quest
## Primary Goal: Obtain TM08 Rock Smash
- **Start Turn:** #50565
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
- STAIRCASE: Warp point (stairs/elevator).
- COUNTER: Impassable; interact from adjacent tile.
- SMASHABLE_ROCK (Object): Requires Rock Smash.

## Lessons Learned
- **Fisher Dialogue:** "If any rocks are in your way..." is post-gift. flag set even if item gone.
- **Arthur (45, 6):** Only gives Hard Stone on Thursdays.
- **Menu Navigation:** The "Switch items?" confirmation box is modal; B button does not close it. Use A on NO to exit.
- **Fly Map:** Cursor snaps to towns. Relative positions: New Bark (East), Cherrygrove (West of New Bark), Violet (North of Cherrygrove), Azalea (South), Goldenrod (West/North of Azalea), Olivine (West), Cianwood (Far West).
- **Tool Alert:** fly_to_city_v2 is unreliable due to incorrect menu navigation logic. Use manual menu_navigator_refined_v2 sequences for Flying.
- **Coordinates:** Notepad coordinates (e.g., New Bark 14, 10) refer to the World Map/Town Map grid, not the Fly Map cursor position.