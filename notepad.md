## Game Mechanics & Systems
*PC Storage*: Currently empty.

## Battle and Pokemon Information
*My Party*: Currently empty.
*Type Effectiveness Chart*: To be built based on battle observations.

## Area and Navigation Insights

### Tile Traversal and Movement Rules (ElmsHouse)
- **FLOOR**: Traversable. (Verified)
- **WALL**: Impassable. (Verified)
- **WINDOW**: Impassable. (Verified)
- **PC**: Impassable. Interacting from an adjacent tile can trigger events. (Verified)
- **TV**: Impassable. (Verified)
- **BOOKSHELF**: Impassable. (Verified)
- **WARP_CARPET_DOWN**: Warp. (Verified)

## Insights & Corrections
- My biggest obstacle is my own memory. I must only trust in-game observation.
- Stunning an NPC can break scripted events, causing dialogue loops.
- The 'Poké Ball machine' was a hallucination.

### Tile Traversal and Movement Rules (ElmsLab)
- **WALL**: Impassable. (Verified)
- **WINDOW**: Impassable. (Verified)
- **FLOOR**: Traversable. (Verified)
- **BOOKSHELF**: Impassable. (Verified)
- **WARP_CARPET_DOWN**: Traversable, acts as a warp tile. (Verified)
### Tile Traversal and Movement Rules (Route29)
- **FLOOR**: Traversable. (Verified)
- **WALL**: Impassable. (Verified)
- **GRASS**: Traversable, likely contains wild Pokémon. (Hypothesis)
- **LEDGE_HOP_DOWN**: One-way ledge that can only be jumped down from above. (Verified)
- **LEDGE_HOP_RIGHT**: One-way ledge that can only be entered by moving right onto it. (Verified)
- **TALL_GRASS**: Traversable, contains wild Pokémon. (Verified)
- **HEADBUTT_TREE**: Impassable. (Verified)
### Additional Tile Rules (Route29)
- **LEDGE_HOP_LEFT**: One-way ledge that can only be entered by moving left onto it. (Verified)
- **CUT_TREE**: Impassable, requires a specific ability/item to remove. (Verified by diagnostic test)

## Route 29 Discoveries
- The southern path is a dead end.
- The western path is blocked by a CUT_TREE.