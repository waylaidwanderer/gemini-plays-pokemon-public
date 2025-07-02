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
- **Defeated Trainers:** Passability is inconsistent and must be tested individually.
    - Hiker Daniel at (4, 6) in Union Cave is PASSABLE.
    - POKéMANIAC LARRY at (4, 21) in Union Cave is IMPASSABLE.
    - Firebreather Bill at (14, 16) in Union Cave is PASSABLE.
    - Hiker Anthony at (6, 13) on Route 33 is PASSABLE.

### Tile Traversal Rules (Verified)
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS / LONG_GRASS:** Traversable, triggers wild encounters.
- **COUNTER:** Impassable.
- **DOOR/CAVE/LADDER:** Warp tile.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING/STATUE/PILLAR:** Impassable scenery.
- **WARP_CARPET_DIRECTION** (e.g., _DOWN, _RIGHT): Warp tile. To activate, move *onto* the tile from the direction indicated in its name (e.g., move Left to enter a WARP_CARPET_RIGHT tile).
- **VOID:** Impassable.
- **CUT_TREE:** Impassable without CUT.
- **WATER:** Impassable without SURF.
- **HEADBUTT_TREE:** Impassable. Confirmed impassable after path_finder failed and by attempting to walk into one at (9, 28).

### One-Way Traversal (Verified)
- **LEDGE / FLOOR_ALLOW_HOP_DOWN:** One-way downward traversal. Horizontal movement (left/right) is permitted.
- **FLOOR_ALLOW_HOP_LEFT:** One-way traversal to the left.
- **FLOOR_ALLOW_HOP_RIGHT:** One-way traversal to the right.
- **FLOOR_ALLOW_HOP_DOWN_OR_RIGHT:** One-way traversal down or right.
- **FLOOR_UP_WALL:** Complex one-way tile. Verified in Union Cave. Can be moved onto from below (by pressing Up). Cannot be moved off of by going Up or Down. Sideways movement (left/right) on and off the tile is permitted.

### Core Mechanic Learnings
- HMs must be used from the PACK menu, not the Pokémon's party menu.
- HM moves cannot be forgotten once taught.

## III. Current Plans

### Finding the Farfetch'd
**Hypothesis:** The main path through Ilex Forest was missed when I jumped down the ledge at (22, 22). The Farfetch'd is likely located on the path I skipped.

**Plan:**
1. Backtrack to the area just before the ledge, around coordinates (22, 21).
2. Explore the path that continues north from that point, which I previously ignored.
3. Systematically search this new area for the Farfetch'd or any other clues.

## IV. Tool Development
- **BUG:** `path_finder` tool is unreliable. It led me to a dead end at (33, 7) in Azalea Town. It doesn't correctly identify all impassable tiles. Needs to be fixed.