# Gem's Pokémon Crystal Adventure Log

## Game Mechanics & Systems

## Battle and Pokemon Information

### My Party

### PC Storage

### Type Effectiveness Chart

## Area and Navigation Insights

## NPCs and Interactions

## Obstacles and Solutions
- My own memory can be an obstacle. I hallucinated warps in New Bark Town. I must rely only on in-game observation.
- Stunning an NPC (Professor Elm) caused a dialogue loop, preventing a scripted event from progressing. I must be cautious when using `stun_npc` during potential cutscenes.

## Reflection & Self-Correction (Turn 103)
- **Data Hygiene Failures:** I have repeatedly deferred immediate data management tasks, such as marking both sides of a warp (New Bark Town entrance) and documenting new tiles (PC/TV in lab). All data management must be performed immediately.
- **Untested Assumptions:** I have failed to scientifically test tile traversability. I will make it a priority to walk into tiles marked 'untested' to verify if they are truly impassable.

### Tile Traversal and Movement Rules
- **FLOOR**: Traversable.
- **WALL**: Appears impassable. (Untested)
- **STAIRCASE**: Warp. (Verified)
- **BOOKSHELF**: Appears impassable. (Untested)
- **TOWN_MAP**: Appears impassable. (Untested)
- **TV**: Appears impassable. (Untested)
- **DOOR**: Warp. (Verified)
- **WATER**: Appears impassable without Surf. (Untested)
- **HEADBUTT_TREE**: Appears impassable. (Untested)
- **WARP_CARPET_DOWN**: Warp. (Verified)
- **PC**: Appears impassable. (Untested)
- BOOKSHELF: Appears impassable. (Untested)
- TV: Appears impassable. (Untested)
- PC: Appears impassable. (Untested)