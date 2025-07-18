# Gem's Pokémon Crystal Notepad

## I. Methodology & Game Mechanics

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Analyze the situation's initial state.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis.
3.  **Test:** Execute the simplest possible action to test the hypothesis.
4.  **Conclude & Document:** Record the result and update this notepad.
5.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests.

### B. Automation & Agent Usage
*   **Automation First:** For any recurring puzzle type, my first step is to use my available custom tools (`pathfinder`). If a tool fails, my top priority is to fix it.
### B. Tile Traversal Rules (Verified)
*   **Impassable:** WALL, VOID, COUNTER, MART_SHELF, BUOY, WHIRLPOOL, PC, BOOKSHELF, HEADBUTT_TREE, CUT_TREE (uncut)
*   **Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS
*   **Warps:** DOOR, CAVE, LADDER, WARP_PANEL, WARP_CARPET_DOWN (directional), WARP_CARPET_LEFT, WARP_CARPET_RIGHT
*   **HM Required:** WATER/SEA (SURF), BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH)
*   **Conditional (One-Way):** PIT (fall), LEDGE_HOP_RIGHT, LEDGE_HOP_LEFT, LEDGE_HOP_DOWN

### D. Tile Mechanics (Pending Tests)
*   **LEDGE_HOP_RIGHT:** One-way, impassable from the left. (Verified on Route 29)
*   **LEDGE/LEDGE_HOP (General):** Believed to be one-way. **Test:** At the next opportunity, attempt to move against `LEDGE_HOP_LEFT` and `LEDGE_HOP_DOWN` to confirm one-way traversal.
*   **FLOOR_UP_WALL:** Impassable from below. **Test:** Attempt to move onto from above/sides at the next opportunity.
*   **HEADBUTT_TREE:** Believed to be impassable. **Test:** Attempt to walk into a HEADBUTT_TREE tile at the next opportunity.

## II. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance.
    *   **Active Hypothesis:** The trigger is resolving the Team Rocket situation at the Goldenrod Radio Tower. **Test:** Fly to Goldenrod City and investigate the Radio Tower.
    *   **Alternative Hypothesis:** The trigger might involve speaking to another key NPC, like Kurt in Azalea Town, after clearing the hideout.
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.
*   **Schoolboy Alan (Route 36) Bug:** NPC script is stuck. I need to test if tossing an item resolves it.

### B. Archived Hypotheses
*   **Mahogany Town Gym Block:**
    *   **Hypothesis 1 (Failed):** Defeating Team Rocket in their hideout was the trigger. **Result:** The Fisher still blocks the path.
    *   **Hypothesis 2 (Failed):** A missed event trigger exists at the Lake of Rage. **Result:** All NPCs have repeating dialogue, and Lance is gone.

### C. System Bugs & Glitches
*   **PC Item Management (Mahogany & Violet):** 'DEPOSIT ITEM' and 'TOSS ITEM' from the PC menu are bugged.
*   **Toss Item from Pack (Bugged):** VERIFIED - Function is bugged and does not remove items. Selecting 'TOSS' and confirming the quantity simply returns to the item list without discarding anything.
*   **Giving Items (Bugged):** Giving an item to a Pokémon that is already holding one initiates a swap prompt, but does not free an inventory slot.
*   **Fly HM (Bugged):** The Fly map is unresponsive, preventing destination selection. **Alternative Hypothesis:** The bug might be location-specific. **Test:** Attempt to use Fly in a different city.
*   **Self-Correction:** My own positional tracking errors have led to navigation issues, which I previously misidentified as game glitches. I must be more diligent in verifying my coordinates before acting.

## III. Battle and Pokemon Information

### A. Type Effectiveness Chart (Verified in-game)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective

### B. Key Trainer/Pokemon Info
*   **Rival SILVA:** Uses a Croconaw.
*   **Gym Leaders:** Falkner (Flying), Bugsy (Bug), Whitney (Normal), Morty (Ghost), Jasmine (Steel), Chuck (Fighting).

### C. Observed Movesets
*   **Youngster Joey's RATTATA:** Tackle, Tail Whip
*   **Falkner's PIDGEY:** Tackle
*   **Falkner's PIDGEOTTO:** Tackle, Gust
*   **Bugsy's METAPOD:** Harden
*   **Bugsy's KAKUNA:** Harden
*   **Bugsy's SCYTHER:** Fury Cutter, Leer
*   **Whitney's CLEFAIRY:** Doubleslap, Encore
*   **Whitney's MILTANK:** Rollout, Stomp, Attract
*   **Morty's GASTLY:** Lick, Spite
*   **Morty's HAUNTER:** Curse, Hypnosis, Dream Eater
*   **Morty's GENGAR:** Shadow Ball, Hypnosis, Dream Eater
*   **Jasmine's MAGNEMITE:** Thunderbolt, Thunder Wave, Supersonic
*   **Jasmine's STEELIX:** Iron Tail, Screech, Rock Throw
*   **Chuck's PRIMEAPE:** Leer, Rage, Karate Chop
*   **Chuck's POLIWRATH:** Hypnosis, Mind Reader, Dynamicpunch

## IV. Future Development & Testing

### A. Agent & Tool Ideas
*   **inventory_manager (Agent):** To help decide which items to discard when my bag is full.
*   **path_tester (Tool):** To systematically test the traversability of tiles around a given coordinate to map out invisible walls or complex collision.

### B. Pending Investigations
*   **Objective:** Re-investigate the 'Invisible Barrier' on Route 42.
*   **Hypothesis:** The barrier is not a true invisible wall, but a result of flawed pathing or a misunderstanding of water tile traversal.
*   **Method:** Return to the marked coordinates at (35, 6), (35, 7), and (35, 8). Systematically attempt to move onto each of these three tiles from all adjacent, traversable water tiles to the south, west, and east. Document the result of each attempt to map the exact collision boundaries and disprove the 'invisible wall' theory.
*   **Impassable:** BOOKSHELF

### D. Passwords & Keys
*   **Team Rocket Hideout (Boss's Room):**
    1. SLOWPOKETAIL
    2. RATICATE TAIL

### D. Tool Limitations
*   **pathfinder:** Cannot distinguish between on-screen and off-screen objects. It treats all previously seen objects from the map XML as permanent obstacles, making it unreliable for pathing through areas with moved or temporary NPCs/objects.