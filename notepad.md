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
- **HEADBUTT_TREE:** Impassable.
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

## III. Tool Development & Self-Critique
- **New Methodology:**
    1.  **Observe:** If a tool fails or behavior is unexpected, my first step is ALWAYS to verify the specific game mechanic through direct, in-game observation.
    2.  **Document:** I will IMMEDIATELY update the 'Tile Traversal Rules' in this notepad with my verified findings. This notepad is my source of truth.
    3.  **Implement:** Only after the mechanic is fully documented will I modify a tool's code to reflect this verified knowledge.
    4.  **Test:** I will then perform a single, definitive test of the tool. If it fails, I will restart the process from step 1, rather than guessing at code changes.
- **Agent Trust:** I MUST trust my agents' outputs, even if they seem counter-intuitive. My `quest_strategist` correctly identified the path forward when my own visual assessment failed. Disregarding an agent's advice is a critical error.
- **Knowledge Management:** I must remember to check my World Knowledge Graph for existing nodes/edges before attempting to add new ones to avoid redundant operations. I must be more careful with `destination_entry_point` when creating edges.
- **path_finder:** Cannot see or account for off-screen objects. Paths generated may be physically impossible if a known, but off-screen, obstacle is in the way. I must manually verify paths against my map markers.

## IV. Open Puzzles & Blockers
### Azalea Town - Slowpoke Well
- **Goal:** Get past the Team Rocket Grunt blocking the well.
- **Key Clue:** A Youngster mentioned the 'Charcoal Man's' Pokémon can CUT trees in ILEX FOREST. This implies Kurt is the Charcoal Man and that progressing through the forest is linked to solving the Azalea Town situation.
- **Current Status:** I have confirmed Ilex Forest is a dead end for now. This suggests the trigger for Kurt to help must be in Azalea Town itself.

### Failed Attempts Log (DO NOT REPEAT - Azalea Town)
- **Talking to Kurt (before Mart clue):** Failed 5+ times. His dialogue was in a loop.
- **Talking to Grunt at Well (before Kurt event):** Failed 4+ times. He will not move via conversation alone.
- **Talking to Grunt at Well (after Kurt left his house):** Failed. Dialogue changed, but he still blocks the path.
- **Talking to Grunt at Gym:** Failed. Unrelated dialogue.
- **Talking to Youngster in Kurt's House:** Failed. Unrelated dialogue.
- **Talking to Kurt (after well grunt interaction):** Failed. Dialogue unchanged.
- **Interacting with Farfetch'd statue:** Failed. No plot progression.
- **Re-attempting Kurt event sequence:** Failed. The event did not trigger as expected.

## V. Immediate Tasks & Tests
- **Verify Tile Mechanics:**
    - **FLOOR_ALLOW_HOP_DOWN_LEFT:** Seen in Ilex Forest. Behavior to be verified.
    - **FLOOR_ALLOW_HOP_DOWN_RIGHT:** Test the 'right' hop functionality.
- **Fix Warp Markers:** Backtrack to Ilex Forest entrance and Ilex Forest Gate to place the missing '🚪' markers.
## Self-Critique Update (Azalea Town)
- **Major Misunderstanding:** I wasted significant time trying to get past the Rocket Grunt at (31, 9), believing he was blocking the Slowpoke Well. The well entrance is at (31, 7) and was never blocked. This was a critical failure in map reading and problem assessment. I must be more careful in analyzing the map visually before assuming a path is blocked.
- **Hallucination & Tunnel Vision:** I had a critical failure where I hallucinated my position (believing I was at (31, 7) when I was at (30, 9)) and wasted turns. I also stubbornly resisted the conclusion that the path was blocked by the grunt, trying to find a way around a non-existent opening. I must trust my tools and observations more, and be quicker to re-evaluate when I'm stuck.
## Self-Critique Update (Azalea Town - Part 3)
- **Corrected Misunderstanding:** After my `path_finder` tool confirmed it, I now understand the true nature of the blockage. While the Rocket Grunt at (31, 9) is not standing directly in front of the well entrance at (31, 7), the surrounding terrain (walls and one-way ledges) makes the path through the grunt the *only* possible way to access the well. My pathfinder is correct: the path is impossible. Therefore, the grunt *is* the puzzle, and I have exhausted all direct attempts to solve it.
## Self-Critique Update (Azalea Town - Part 4)
- **Pattern of Failure:** I am repeatedly hallucinating my location and the status of game events (e.g., believing Kurt had left, believing the well was unblocked, believing the path to Ilex was blocked). This leads to wasted turns and flawed strategies. I must rely ONLY on the current game state information provided each turn and stop making assumptions based on memory. I also need to test simple, direct event sequences before attempting complex workarounds.

## VI. AI Observer Feedback (Self-Critique)
- **Tool Quality:** My `path_finder` tool required numerous rewrites. I need to focus on writing higher-quality, more robust code from the beginning to avoid this cycle of failure and repair.
- **WKG Data Entry:** I have a pattern of making data entry errors (coordinates, entry points) when updating my World Knowledge Graph. I must be more meticulous to ensure the graph's reliability.