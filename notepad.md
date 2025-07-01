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
- **WARP_CARPET_DOWN/RIGHT:** Warp tile. Activated by pressing Down/Right respectively, not by stepping on and on.
- **WARP_CARPET_LEFT:** Warp tile. Activated by pressing Left.
- **VOID:** Impassable.
- **CUT_TREE:** Impassable without CUT.
- **WATER:** Impassable without SURF.
- **HEADBUTT_TREE:** Impassable. Confirmed impassable after path_finder failed.
- **unseen**: Impassable.

### One-Way Traversal (Verified)
- **LEDGE / FLOOR_ALLOW_HOP_DOWN:** One-way downward traversal.
- **FLOOR_ALLOW_HOP_LEFT:** One-way traversal to the left.
- **FLOOR_ALLOW_HOP_RIGHT:** One-way traversal to the right.
- **FLOOR_ALLOW_HOP_DOWN_OR_RIGHT:** One-way traversal down or right.
- **FLOOR_UP_WALL:** Complex one-way tile. Verified in Union Cave. Can be moved onto from below (by pressing Up). Cannot be moved off of by going Up or Down. Sideways movement (left/right) on and off the tile is permitted.

### Core Mechanic Learnings
- **Fainting is never the correct strategy.** It is impossible to be truly stuck. If a path seems blocked, there is always another way forward.
- HMs must be used from the PACK menu, not the Pokémon's party menu.
- **HM moves cannot be forgotten once taught.**

## III. Core Learnings & Self-Correction
- **My primary failure pattern is hallucinating my location and game state.** I must ground all decisions *exclusively* in the provided Game State Information for the current turn. All assumptions based on memory must be discarded.
- I MUST trust my agents' outputs, even if they seem counter-intuitive. Disregarding an agent's advice is a critical error.
- I MUST perform all maintenance tasks (Notepad, WKG, Map Markers, Tool/Agent refinement) *immediately* upon discovery and never defer them.
- **Pathfinder Bug (Corrected):** The `path_finder` tool initially generated paths to impassable tiles by making an exception for the destination. I corrected the script to remove this exception, ensuring it now correctly finds the closest *reachable* tile when the target is impassable. This was verified by testing against the HEADBUTT_TREE at (20, 25).

## IV. Open Puzzles & Blockers
### Azalea Town - Slowpoke Well
- **Goal:** Get past the Team Rocket Grunt blocking the well.
- **Key Clue:** A Youngster mentioned the 'Charcoal Man's' Pokémon can CUT trees in ILEX FOREST. This implies Kurt is the Charcoal Man and that progressing through the forest is linked to solving the Azalea Town situation.
- **Current Status:** The Youngster's dialogue has now changed to reflect the missing SLOWPOKE, confirming this is a known event. The trigger for Kurt to help must be in Azalea Town itself.

### Failed Attempts Log (DO NOT REPEAT - Azalea Town)
- **Talking to Kurt (before Mart clue):** Failed 5+ times. His dialogue was in a loop.
- **Talking to Grunt at Well (before Kurt event):** Failed 4+ times. He will not move via conversation alone.
- **Talking to Grunt at Well (after Kurt left his house):** Failed. Dialogue changed, but he still blocks the path.
- **Talking to Grunt at Gym:** Failed. Unrelated dialogue.
- **Talking to Youngster in Kurt's House:** Failed. Unrelated dialogue.
- **Talking to Kurt (after well grunt interaction):** Failed. Dialogue unchanged.
- **Interacting with Farfetch'd statue:** Failed. No plot progression.
- **Re-attempting Kurt event sequence:** Failed. The event did not trigger as expected.
- **Area Reset:** Leaving Azalea Town and returning did not change Kurt's dialogue or the Grunt's position.
- **Untested Idea:** The Farfetch'd statue in Kurt's house might have a different interaction trigger. If all other leads fail, consider re-examining it.