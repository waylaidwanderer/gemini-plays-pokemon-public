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
- **Knowledge Management:** I must remember to check my World Knowledge Graph for existing nodes/edges before attempting to add new ones to avoid redundant operations. I must be more careful with `destination_entry_point` when creating edges.

## IV. Current Plans & Hypotheses

### Goal: Clear Team Rocket from Slowpoke Well

### Key Clue
- **The map where Kurt lives is named `CharcoalKiln`.** This is not an error. This is the central clue I was ignoring.

### Active Hypothesis
- **The Moltres statue at (5, 6) is a hidden switch.** The 'CharcoalKiln' name and the fiery bird statue are connected.
    - **Plan:**
        1. Move to the tile directly below the statue at (5, 7).
        2. Face up and interact with the statue ('A' button).

### Failed Attempts Log (DO NOT REPEAT)
- **Talking to Kurt:** Failed 5+ times. His dialogue is in a loop and is not the trigger.
- **Talking to Grunt at Well:** Failed 3+ times. He will not move via conversation alone.
- **Talking to Gramps, then Kurt:** Failed. Did not change Kurt's dialogue.
- **Talking to Youngster, then Kurt:** Failed. Did not change Kurt's dialogue.
- **Talking to all NPCs, then Kurt:** Failed. The combination of dialogue flags did not trigger Kurt.