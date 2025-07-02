# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER.
- **Traversable:** FLOOR, GRASS.
- **Warps:** DOOR, CAVE, LADDER, WARP_CARPET_RIGHT, WARP_CARPET_DOWN.
- **Unverified Warps:** WARP_CARPET_LEFT (Activation method unknown. Hypothesis: requires entry from the right).
- **One-Way Down:** LEDGE / FLOOR_ALLOW_HOP_DOWN (Horizontal movement is permitted).
- **Complex One-Way:** FLOOR_UP_WALL (Can be entered from below, but not exited up or down. Sideways movement is permitted).

### Key Learnings
- HMs must be used from the PACK menu.
- HM moves are permanent.
- All map objects (NPCs, items, signs) act as walls.

## II. Quest Progression

### Current Objective: Obtain HM01 (Cut)
- **Hypothesis:** The key to progressing is in Ilex Forest. An NPC in Azalea mentioned a 'Charcoal Man' whose Pokémon can use CUT. This is the only remaining lead after being blocked at the Slowpoke Well.
- **Plan:** Enter Ilex Forest and search for the Charcoal Man and his Farfetch'd.

### Blocked Path: Slowpoke Well
- **Status:** The path to the well is blocked by a Rocket Grunt at (31, 9) who will not move.
- **Summary of Failed Attempts:**
  1. Talking to the grunt repeatedly.
  2. Triggering the Kurt event and returning (grunt does not move).
  3. Leaving and re-entering Azalea Town.
  4. Entering and exiting a different building in town.
  5. Searching for alternate entrances (none found).
  6. Speaking to Kurt's apprentice after Kurt leaves (no new info).
- **Conclusion:** The trigger for this event is not in Azalea Town itself. Progress must be made elsewhere first, likely in Ilex Forest.