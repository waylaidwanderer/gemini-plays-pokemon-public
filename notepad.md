# Gem's Pokémon Crystal Notepad

## I. Game Plan & Goals

### Strategic Notes
- **Party Imbalance:** My party is too reliant on G (Croconaw). The Azalea Town Gym is Bug-type, so I must train my two Hoothoots and my new Togepi. Current plan is to train in Union Cave.
- **Onix's Moveset:** My Onix (ROCKY) lacks a Rock-type move. For now, rely on G and use ROCKY for defensive switching or to use SCREECH.
- **Party Full:** My party is full. I can't catch any new Pokémon until I deposit one in the PC.

### To-Do & Reminders
- **CRITICAL:** If a tool fails, the primary suspect is an impossible request (e.g., pathing to an unreachable location), NOT a bug in the code. I MUST diagnose the reason before attempting to fix the tool.
- **CRITICAL:** Mark all dead ends with '🚫' immediately upon discovery.
- Be more rigorous in testing tile mechanics. Test all directions for one-way tiles.
- Utilize agents like `battle_advisor` even for simple encounters to build good habits.
- Be more flexible with goals. If stuck, pivot to exploration or a different objective.

## II. Battle Intel

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

### Observed Movesets
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE, GROWL, FLASH, FORESIGHT
- Wild Bellsprout: VINE WHIP, GROWTH
- Wild Caterpie: TACKLE, STRING SHOT
- Wild Ekans: (unknown)
- Wild Hoppip: TAIL WHIP, SYNTHESIS
- Wild Rattata: TACKLE, TAIL WHIP
- Wild Wooper: TAIL WHIP, WATER GUN

## III. World Knowledge & Mechanics

### Tile Traversal Rules (Verified)
- **Objects are impassable:** All map objects (items, trees, signs, NPCs, defeated trainers etc.) act as walls.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS:** Traversable, triggers wild encounters.
- **LEDGE:** One-way downward traversal.
- **COUNTER:** Impassable.
- **DOOR/CAVE:** Warp tile, triggered by movement.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING/STATUE/PILLAR:** Impassable scenery.
- **FLOOR_UP_WALL:** One-way traversal. Can only be entered from below (moving up). Impassable from all other directions.
- **WARP_CARPET_DOWN:** Warp tile, triggered by movement.
- **VOID:** Impassable.
- **BUOY:** Impassable scenery.
- **CUT_TREE:** Confirmed impassable without CUT.
- **WATER:** Verified impassable without SURF.

### Tile Traversal Rules (Needs Verification)
- **LONG_GRASS:** Inferred to function like TALL_GRASS.
- **HEADBUTT_TREE:** Impassable by walking. (Hypothesis: may be interactable with the HEADBUTT move).
- **FLOOR_ALLOW_HOP_DOWN:** One-way traversal downward.
- **FLOOR_ALLOW_HOP_RIGHT:** One-way traversal to the right.
- **FLOOR_ALLOW_HOP_DOWN_OR_RIGHT:** One-way traversal down or right.