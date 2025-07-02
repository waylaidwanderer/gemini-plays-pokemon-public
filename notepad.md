# Gem's Pokémon Crystal Notepad

## I. Battle Intel

### Type Effectiveness Chart (Verified)
- Normal is not very effective against Water.
- Normal is not very effective against Rock/Ground.
- Water is super effective against Rock/Ground.
- Water is super effective against Ground.
- Flying is super effective against Fighting.

## II. Game Mechanics

### Object Interaction
- **General Rule:** All map objects (NPCs, items, signs) act as walls and are impassable.
- **Defeated Trainers:** Passability is inconsistent. Hiker Daniel & Anthony are passable; POKéMANIAC LARRY is impassable.

### Tile Traversal Rules
- **Verified Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER (to be fully verified).
- **Verified Traversable:** FLOOR, GRASS.
- **Verified Warps:** DOOR, CAVE, LADDER, WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (enter from direction in name).
- **Verified One-Way:**
    - LEDGE / FLOOR_ALLOW_HOP_DOWN: One-way downward traversal. Horizontal movement is permitted.
    - FLOOR_UP_WALL: Complex one-way tile. Can be moved onto from below (Up), but not off of by going Up or Down. Sideways movement is permitted.

### Navigational Learnings
- **Azalea Town Layout:** The town is split by a line of impassable ledges. To get from the southern section to the northern section, one must travel all the way east, loop around north, and then head west.

### Core Mechanic Learnings
- HMs must be used from the PACK menu, not the Pokémon's party menu.
- HM moves cannot be forgotten once taught.

## III. Quest Progression

### Current Hypotheses:
1. The 'Charcoal Man' is a specific NPC in Azalea Town who will provide the HM for CUT.
2. The Slowpoke Well event needs a different trigger than just talking to Kurt.
3. The Rocket Grunt blocking the Azalea Gym might have new dialogue now that the Slowpoke Well event is active.

### Failed Hypotheses Log:
1. **Hypothesis:** The Rocket Grunt at the well isn't blocking the entrance. **Result:** False.
2. **Hypothesis:** Leaving and re-entering Azalea Town will move the grunt. **Result:** False.
3. **Hypothesis:** A second conversation with Kurt after he initially leaves his house is the trigger. **Result:** False.
4. **Hypothesis:** The trigger is talking to the grunt, then immediately talking to Kurt. **Result:** False.
5. **Hypothesis:** The trigger is talking to Kurt *first*, before the grunt. **Result:** False.
6. **Hypothesis:** Interacting with the Rocket Grunt at the Gym is the trigger. **Result:** Partial success. He mentioned SLOWPOKETAIL.
7. **Hypothesis:** The SLOWPOKETAIL clue from the gym grunt would trigger Kurt to take action. **Result:** False.
8. **Hypothesis:** The key is a herding puzzle in Ilex Forest involving twigs. **Result:** False.
9. **Hypothesis:** The Ilex Forest Shrine is the trigger. **Result:** False.

### Quest Progression - Azalea Town (Update)
- My `path_finder_plus` tool confirmed that there is no path to the Slowpoke Well entrance at (31, 7).
- The path is blocked by the Rocket Grunt at (31, 9). This is a quest-based obstacle, not a navigation error.
- New Hypothesis: I must interact with the Rocket Grunt at (31, 9) again now that Kurt has left his house to trigger the next step.