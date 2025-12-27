# Strategy for Suicune Encounter (Crystal)
1. Prerequisites: Clear Bell and Fog Badge (Obtained).
2. Revised Trigger Sequence (Mandatory Sightings):
   - Burned Tower: Beasts flee. [Done]
   - Cianwood City (North): Suicune observed. [Done]
   - Route 42 (Central Island): Approach Apricorn trees. [In Progress]
   - Route 36 (Sudowoodo junction): Approach junction. [Pending]
   - Tin Tower 1F: Return for battle. (Dialogue with Sages alone is NOT enough).
3. Battle Strategy: Use Sleep Powder (KIMCHI) to prevent Suicune from using Roar. Weaken carefully and capture with Ultra/Great Balls.

# Tile Mechanics (Global)
- FLOOR: Walkable. Standard collision. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable only when using HM03 Surf. [Verified]
- TALL_GRASS: Walkable. Triggers wild encounters. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. [Verified]
- CUT_TREE: Impassable. Can be removed using HM01 Cut. Regrows upon map reload. [Verified]
- WARP_CARPET: Traversable. Triggers map transition. [Verified]
- CAVE: Warp point. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- PC/COUNTER/SIGN: Impassable. Interact from adjacent tile. [Verified]
- FLOOR_UP_WALL: Impassable from below. [Verified]
- VOID: Impassable. Map boundary. [Verified]
- WARP_CARPET_DOWN: Traversable. Triggers exit to overworld. [Verified]
- WARP_CARPET_LEFT/RIGHT: Warp triggered by moving in the direction the carpet faces while standing on it. [Verified]
- STAIRS/LADDER: Warp to a different floor or map. [Verified]

# Trainer Defeats
- Wise Trio (Wise Trio Room): Defeated (Room is empty).
- Sages at (11, 11), (5, 9), (14, 6) (Tin Tower 1F): Lore shared.

# General Lessons
- Suicune Trigger (Crystal): Sightings on Route 42 and 36 are mandatory before the Tin Tower battle. The Sages' dialogue is lore, not the primary trigger.
- Tool Error: Custom tools receive `input_data` directly. Do not use `sys.stdin.read()` for inputs.
- Johto Fly Map: "Up" moves forward in the city list (New Bark -> Cherrygrove -> Violet).