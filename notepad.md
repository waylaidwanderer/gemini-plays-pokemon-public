# Gem's Pokémon Crystal Notepad

## I. Game Plan & Objectives
- **Primary Objective:** Get the Hive Badge from the Azalea Town Gym.
- **Current Plan:** Navigate Route 32 to reach the Union Cave entrance at (6, 79).

## II. Battle Intel
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

### Type Effectiveness Chart (Verified)
- Normal is not very effective against Water.
- Normal is not very effective against Rock/Ground.
- Water is super effective against Rock/Ground.
- Water is super effective against Ground.

## III. Mechanics & Learnings
### Tile Traversal Rules
- **Objects are impassable:** All map objects (NPCs, items, signs) act as walls.
- **Defeated Trainers:** Passability is inconsistent. Each must be tested.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS / LONG_GRASS:** Traversable, triggers wild encounters.
- **COUNTER:** Impassable.
- **DOOR/CAVE:** Warp tile.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING/STATUE/PILLAR:** Impassable scenery.
- **WARP_CARPET_DOWN/RIGHT:** Warp tile.
- **VOID:** Impassable.
- **CUT_TREE:** Impassable without CUT.
- **WATER:** Impassable without SURF.
- **HEADBUTT_TREE:** Impassable by walking.
- **unseen**: Impassable.

### One-Way Traversal (Verified)
- **LEDGE / FLOOR_ALLOW_HOP_DOWN:** One-way downward traversal.
- **FLOOR_ALLOW_HOP_LEFT:** One-way traversal to the left.
- **FLOOR_ALLOW_HOP_RIGHT:** One-way traversal to the right.
- **FLOOR_ALLOW_HOP_DOWN_OR_RIGHT:** One-way traversal down or right.

### Unverified Mechanics & Assumptions
- **BUOY:** Assumed impassable. (NEEDS VERIFICATION)
- **LADDER:** Assumed impassable. (NEEDS VERIFICATION)
- **FLOOR_UP_WALL:** Assumed one-way upward traversal. (NEEDS VERIFICATION)

### Core Mechanic Learnings
- **Fainting is never the correct strategy.** It is impossible to be truly stuck. If a path seems blocked, there is always another way forward. This is a fundamental rule.
- HMs must be used from the PACK menu, not the Pokémon's party menu.

## V. Tool Development & Self-Critique
- **path_finder Debugging:** My previous debugging process was critically flawed. I wasted dozens of turns modifying the tool based on incorrect assumptions about game mechanics (`COUNTER`, `FLOOR_UP_WALL`) instead of verifying the mechanics first. I also failed to recognize I was in a large, inescapable dead-end area, incorrectly blaming the tool for my own lack of map awareness.
- **New Methodology:**
    1.  **Observe:** If a tool fails or behavior is unexpected, my first step is ALWAYS to verify the specific game mechanic through direct, in-game observation.
    2.  **Document:** I will IMMEDIATELY update the 'Tile Traversal Rules' in this notepad with my verified findings. This notepad is my source of truth.
    3.  **Implement:** Only after the mechanic is fully documented will I modify a tool's code to reflect this verified knowledge.
    4.  **Test:** I will then perform a single, definitive test of the tool. If it fails, I will restart the process from step 1, rather than guessing at code changes.
- **Agent Testing:** I have defined a `move_advisor` agent but have not used it. I MUST prioritize using this agent at the next opportunity (e.g., finding a TM) to evaluate its effectiveness.
- **Knowledge Management:** I must remember to check my World Knowledge Graph for existing nodes/edges before attempting to add new ones to avoid redundant operations.