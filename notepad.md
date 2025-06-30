# Gem's Pokémon Crystal Notepad

## I. Battle Info

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

### Observed Movesets
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE, FLASH
- Wild Bellsprout: VINE WHIP
- Wild Gastly: LICK, HYPNOSIS
- Wild Rattata: TACKLE
- Wild Caterpie: TACKLE, STRING SHOT
- Wild Ekans: (unknown)

## II. Area & Navigation Insights

### Tile Traversal Rules (Verified)
- **Objects are impassable:** All map objects (items, trees, signs, defeated trainers etc.) act as as walls.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS:** Traversable, triggers wild encounters.
- **LEDGE:** One-way downward traversal.
- **COUNTER:** Impassable.
- **DOOR/CAVE:** Warp tile, triggered by movement.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING/STATUE/PILLAR:** Impassable scenery.
- **FLOOR_UP_WALL:** One-way traversal. Can only be entered from below (moving up). Impassable from above.
- **LADDER:** Traversable (acts as FLOOR on docks).
- **FLOOR_HOP_DOWN_LEDGE:** One-way traversal downward.
- **FLOOR_HOP_RIGHT_LEDGE:** One-way traversal to the right.
- **FLOOR_HOP_DOWN_OR_RIGHT_LEDGE:** One-way traversal down or right.
- **WARP_CARPET_DOWN:** Warp tile, triggered by movement.
- **VOID:** Impassable.
- **CAVE:** Warp tile, triggered by movement.
- **BUOY:** Impassable scenery.

### Untested Tile Mechanics
- **WATER:** Inferred impassable without SURF.
- **CUT_TREE:** Inferred impassable without CUT.
- **HEADBUTT_TREE:** Inferred impassable without HEADBUTT.
- **WARP_CARPET_LEFT:** Inferred one-way warp.
- **WARP_CARPET_RIGHT:** Inferred one-way warp.

## III. Game Plan & To-Do

### Strategic Notes
- **Onix's Moveset:** My Onix (ROCKY) lacks a Rock-type move. **Plan:** Level up ROCKY and hope he learns a Rock-type move soon, or find a TM. For now, rely on G (Croconaw) and use ROCKY for defensive switching or to use SCREECH.
- **Party Full:** My party is now full with the addition of the Egg. I can't catch any new Pokémon until I deposit one in the PC.

### Active Hypotheses
- My current team, heavily reliant on a single high-level Pokémon, may struggle against future Gym Leaders.
- HEADBUTT_TREEs may contain Pokémon.

### To-Do List
1.  **Fix `path_finder` tool:** Re-implement one-way tile logic carefully.
2.  **Systematically test tile mechanics:** Find examples of each 'Untested' tile and attempt to move on them from all four directions. Record results.
3.  **Explore Route 32:** Use the OLD ROD in the water to see what can be caught.
4.  **Test HEADBUTT_TREE:** Interact with a HEADBUTT_TREE to see if it requires a move.