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
- **Verified Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER.
- **Verified Traversable:** FLOOR, GRASS.
- **Verified Warps:** DOOR, CAVE, LADDER, WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (stand on tile, face down, press A).
- **Verified One-Way:**
    - LEDGE / FLOOR_ALLOW_HOP_DOWN: One-way downward traversal. Horizontal movement is permitted.
    - FLOOR_UP_WALL: Complex one-way tile. Can be moved onto from below (Up), but not off of by going Up or Down. Sideways movement is permitted.

### Navigational Learnings
- **Azalea Town Layout:** The town is split by a line of impassable ledges. To get from the southern section to the northern section, one must travel all the way east, loop around north, and then head west.

### Core Mechanic Learnings
- HMs must be used from the PACK menu, not the Pokémon's party menu.
- HM moves cannot be forgotten once taught.

## III. Quest Progression

### Current Hypothesis:
1. **Kurt Reset:** Leaving Kurt's house and returning later might reset his position, allowing me to re-trigger the event where he runs to the well. I can then attempt to follow him.

### Failed Hypotheses Log:
1. **Well Grunt Passable:** The Rocket Grunt at the well isn't blocking the entrance. (Result: False)
2. **Town Reset:** Leaving and re-entering Azalea Town will move the grunt. (Result: False)
3. **Kurt Dialogue:** A second conversation with Kurt after he leaves is the trigger. (Result: False)
4. **Dialogue Order (Grunt then Kurt):** Talking to the grunt, then immediately to Kurt, is the trigger. (Result: False)
5. **Dialogue Order (Kurt then Grunt):** Talking to Kurt *first*, before the grunt, is the trigger. (Result: False)
6. **Gym Grunt Dialogue:** Interacting with the Gym grunt is the trigger. (Result: Partial success, mentioned SLOWPOKETAIL, but no progression.)
7. **SLOWPOKETAIL Clue:** The SLOWPOKETAIL clue would trigger Kurt. (Result: False)
8. **Ilex Forest Puzzle:** The key is a herding puzzle in Ilex Forest. (Result: False)
9. **Ilex Forest Shrine:** The Ilex Forest Shrine is the trigger. (Result: False)
10. **Well Grunt Passable (Physical):** I can walk through the grunt at (31, 9). (Result: False)
11. **Post-Kurt Grunt Talk:** Talking to the well grunt after Kurt leaves is the trigger. (Result: False)
12. **Find Kurt at Well:** Kurt is somewhere near the well entrance. (Result: False, couldn't find him after a thorough search)
13. **Apprentice Dialogue:** The apprentice's dialogue changes after Kurt leaves. (Result: False)
14. **Statue Switch:** The bird statue in Kurt's house is a hidden switch. (Result: False, just a Farfetch'd sound)
15. **Challenge Gym Grunt:** Challenging the Rocket Grunt at the Azalea Town Gym to a battle is the trigger. (Result: False, he only delivered dialogue.)
16. **Hidden Path:** The `area_explorer` tool will find a hidden environmental path. (Result: False. The tool found no reachable unseen tiles.)