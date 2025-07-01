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
### Tile Traversal Rules (Verified)
- **Objects are impassable:** All map objects (NPCs, items, signs) act as walls.
- **Defeated Trainers:** Passability is inconsistent and must be tested individually.
    - Hiker Daniel at (4, 6) in Union Cave is PASSABLE.
    - POKéMANIAC LARRY at (4, 21) in Union Cave is IMPASSABLE.
    - Firebreather Bill at (14, 16) in Union Cave is PASSABLE.
    - Hiker Anthony at (6, 13) on Route 33 is PASSABLE.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS / LONG_GRASS:** Traversable, triggers wild encounters.
- **COUNTER:** Impassable.
- **DOOR/CAVE/LADDER:** Warp tile.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING/STATUE/PILLAR:** Impassable scenery.
- **WARP_CARPET_DOWN/RIGHT:** Warp tile.
- **VOID:** Impassable.
- **CUT_TREE:** Impassable without CUT.
- **WATER:** Impassable without SURF.
- **HEADBUTT_TREE:** Impassable.
- **unseen**: Impassable.

### One-Way Traversal (Verified)
- **LEDGE / FLOOR_ALLOW_HOP_DOWN:** One-way downward traversal.
- **FLOOR_ALLOW_HOP_LEFT:** One-way traversal to the left.
- **FLOOR_ALLOW_HOP_RIGHT:** One-way traversal to the right.
- **FLOOR_ALLOW_HOP_DOWN_OR_RIGHT:** One-way traversal down or right.
- **FLOOR_UP_WALL:** Complex one-way tile. Verified in Union Cave. Can be moved onto from below (by pressing Up). Cannot be moved off of by going Up or Down. Sideways movement (left/right) on and off the tile is permitted.

### Unverified Mechanics & Assumptions
- **BUOY:** Assumed impassable. (NEEDS VERIFICATION)

### Core Mechanic Learnings
- **Fainting is never the correct strategy.** It is impossible to be truly stuck. If a path seems blocked, there is always another way forward.
- HMs must be used from the PACK menu, not the Pokémon's party menu.
- **HM moves cannot be forgotten once taught.**

## III. Tool Development & Self-Critique
- **New Methodology:**
    1.  **Observe:** If a tool fails or behavior is unexpected, my first step is ALWAYS to verify the specific game mechanic through direct, in-game observation.
    2.  **Document:** I will IMMEDIATELY update the 'Tile Traversal Rules' in this notepad with my verified findings. This notepad is my source of truth.
    3.  **Implement:** Only after the mechanic is fully documented will I modify a tool's code to reflect this verified knowledge.
    4.  **Test:** I will then perform a single, definitive test of the tool. If it fails, I will restart the process from step 1, rather than guessing at code changes.
- **Agent Trust:** I MUST trust my agents' outputs, even if they seem counter-intuitive. My `strategic_advisor` correctly identified the path forward when my own visual assessment failed. Disregarding an agent's advice is a critical error.
- **Knowledge Management:** I must remember to check my World Knowledge Graph for existing nodes/edges before attempting to add new ones to avoid redundant operations.

## IV. Plans & Puzzles
### Current Puzzle: Stuck in Kurt's House
- **Goal:** Trigger event for Kurt to confront Team Rocket or find the exit.
- **Hypotheses from `puzzle_solver` agent (to be tested):
  1. ~~Speak to NPCs in a specific order (Kurt -> Youngster -> Kurt).~~ (Failed)
  2. Stand on exit warp, turn, and talk to Kurt.
  3. ~~After talking to Kurt, immediately interact with Farfetch'd/Radio.~~ (Failed)
  4. After talking to Kurt, walk to the far side of the room and then back to the exit.
  5. Systematically check every tile of the Bookshelf.
  6. Bump into Farfetch'd from all four directions.