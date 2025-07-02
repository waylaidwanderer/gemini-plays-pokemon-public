# Gem's Pokémon Crystal Notepad

## I. Battle Intel

### Type Effectiveness Chart (Verified)
- Normal is not very effective against Water.
- Normal is not very effective against Rock/Ground.
- Water is super effective against Rock/Ground.
- Water is super effective against Ground.
- Flying is super effective against Fighting.

## II. Mechanics & Learnings

### Object Interaction
- **General Rule:** All map objects (NPCs, items, signs) act as walls and are impassable.
- **Defeated Trainers:** Passability is inconsistent. Hiker Daniel & Anthony are passable; POKéMANIAC LARRY is impassable.

### Tile Traversal Rules (Verified)
- **WALL, COUNTER, VOID, etc.:** Impassable scenery.
- **FLOOR, GRASS:** Traversable.
- **DOOR/CAVE/LADDER:** Warp tile.
- **CUT_TREE/WATER:** Impassable without HM.
- **WARP_CARPET_DIRECTION:** Enter from the direction in the name (e.g., move Left for WARP_CARPET_RIGHT).
- **LEDGE / FLOOR_ALLOW_HOP_DOWN:** One-way downward traversal. Horizontal movement is permitted.
- **FLOOR_UP_WALL:** Complex one-way tile. Can be moved onto from below (Up), but not off of by going Up or Down. Sideways movement is permitted.

### Navigational Learnings
- **Azalea Town Layout:** The town is split by a line of impassable ledges. To get from the southern section to the northern section, one must travel all the way east, loop around north, and then head west.

### Core Mechanic Learnings
- HMs must be used from the PACK menu, not the Pokémon's party menu.
- HM moves cannot be forgotten once taught.

## III. Quest Progression: Slowpoke Well

### Failed Hypotheses Log:
1.  **Hypothesis:** The Rocket Grunt at the well isn't blocking the entrance. **Result:** False. My pathfinder confirmed the entrance at (31, 7) is unreachable while the grunt is at (31, 9).
2.  **Hypothesis:** Leaving and re-entering Azalea Town will move the grunt. **Result:** False. The grunt's position did not change.
3.  **Hypothesis:** A second conversation with Kurt after he initially leaves his house is the trigger. **Result:** False. Kurt's dialogue was unchanged.
4.  **Hypothesis:** The trigger is talking to the grunt, then immediately talking to Kurt. **Result:** False. Kurt's dialogue did not change, and he did not move.
5.  **Hypothesis:** The trigger is talking to Kurt *first*, before the grunt. **Result:** False. Kurt's dialogue was unchanged.
6.  **Hypothesis:** Interacting with the Rocket Grunt at the Gym is the trigger. **Result:** Partial success. He mentioned SLOWPOKETAIL, providing a new clue.

### Current Plan:
- **Active Hypothesis:** Now that I have the SLOWPOKETAIL clue from the gym grunt, talking to Kurt will finally trigger him to take action.

## IV. Tool Development
- **DELETED:** The `path_finder` tool was fundamentally flawed. It did not account for all movement restrictions and repeatedly led to dead ends. It has been deleted to prevent further errors.
- **BOOKSHELF, TV, TOWN_MAP, WINDOW:** Verified impassable.
- **Untested but assumed impassable scenery:** RADIO.