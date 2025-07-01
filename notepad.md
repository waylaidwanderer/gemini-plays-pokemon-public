# Gem's Pokémon Crystal Notepad

## I. Battle Intel
### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

### Observed Movesets
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE, GROWL, FLASH, FORESIGHT
- Wild Bellsprout: VINE WHIP, GROWTH
- Wild Caterpie: TACKLE, STRING SHOT
- Wild Ekans: LEER, WRAP
- Wild Pidgey: SAND-ATTACK
- Wild Hoppip: TAIL WHIP, SYNTHESIS, SPLASH
- Wild Rattata: TACKLE, TAIL WHIP
- Wild Wooper: TAIL WHIP, WATER GUN
- Wild Zubat: LEECH LIFE
- Wild Sandshrew: SCRATCH, DEFENSE CURL
- Wild Geodude: TACKLE, DEFENSE CURL
- Wild Onix: TACKLE, SCREECH
- Wild Machop: LOW KICK

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
- **HEADBUTT_TREE:** Impassable. Confirmed impassable after path_finder failed.

### One-Way Traversal (Verified)
- **LEDGE / FLOOR_ALLOW_HOP_DOWN:** One-way downward traversal. Horizontal movement (left/right) is permitted.
- **FLOOR_ALLOW_HOP_LEFT:** One-way traversal to the left.
- **FLOOR_ALLOW_HOP_RIGHT:** One-way traversal to the right.
- **FLOOR_ALLOW_HOP_DOWN_OR_RIGHT:** One-way traversal down or right.
- **FLOOR_UP_WALL:** Complex one-way tile. Verified in Union Cave. Can be moved onto from below (by pressing Up). Cannot be moved off of by going Up or Down. Sideways movement (left/right) on and off the tile is permitted.

### Core Mechanic Learnings
- HMs must be used from the PACK menu, not the Pokémon's party menu.
- HM moves cannot be forgotten once taught.

## V. Major Self-Correction (Azalea Town)
- **False Assumption:** I incorrectly assumed the Team Rocket Grunt at (31, 9) was physically blocking the entrance to the Slowpoke Well at (31, 7). 
- **Verification Failure:** I spent multiple turns trying to trigger an event to move him without first verifying if an alternate path existed.
- **Correction:** The grunt is not blocking the warp tile. A clear path exists around him. I must always verify obstacles and not get tunnel vision.
- BED: Impassable (added per system critique, pending verification).
- TABLE: Impassable (added per system critique, pending verification).
- CHAIR: Impassable (added per system critique, pending verification).