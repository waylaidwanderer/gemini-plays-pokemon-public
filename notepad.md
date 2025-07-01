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
- **WARP_CARPET_DOWN/RIGHT:** Warp tile. Activated by pressing Down/Right respectively, not by stepping off and on.
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
- **path_finder:** Cannot see or account for off-screen objects. Paths generated may be physically impossible if a known, but off-screen, obstacle is in the way. I must manually verify paths against my map markers.

## IV. Current Plans & Hypotheses

### Goal: Clear Team Rocket from Slowpoke Well

### Key Clue
- **Cooltrainer in Azalea Mart:** Mentioned Kurt makes custom Poké Balls.
- **The map where Kurt lives is named `CharcoalKiln`.** This is a strong hint towards crafting/forging.

### Active Hypothesis
- **I need to trigger a crafting event with Kurt.** The combination of the 'CharcoalKiln' map name and the NPC dialogue is too strong a coincidence. Since Kurt is not in his house, I must find him. The most logical place is at the Slowpoke Well, where he went to confront Team Rocket.
    - **Plan:**
        1. Find a way to the Slowpoke Well entrance at (31, 7). The direct path from the south is blocked.
        2. Explore the west side of Azalea Town for an alternate route.
        3. If no route is found, re-investigate Kurt's house to see if anything changed after learning about the custom balls.

### Failed Attempts Log (DO NOT REPEAT)
- **Talking to Kurt (before Mart clue):** Failed 5+ times. His dialogue was in a loop.
- **Talking to Grunt at Well (before Kurt event):** Failed 4+ times. He will not move via conversation alone.
- **Talking to Grunt at Well (after Kurt left his house):** Failed. Dialogue changed, but he still blocks the path.
- **Talking to Grunt at Gym:** Failed. Unrelated dialogue.
- **Talking to Youngster in Kurt's House:** Failed. Unrelated dialogue.
### New Clue (Azalea Town)
- **Youngster west of town:** Mentioned the 'Charcoal Man's' Pokémon can CUT down the trees in ILEX FOREST. This confirms Kurt is the Charcoal Man and I need to find a way to get the HM Cut or a Pokémon that knows it from him to proceed west into the forest.

- **VOID:** Impassable.
- **Talking to Kurt (after well grunt interaction):** Failed. Dialogue unchanged.
- **WARP_CARPET_LEFT:** Warp tile. Activated by pressing Left, not by stepping off and on.