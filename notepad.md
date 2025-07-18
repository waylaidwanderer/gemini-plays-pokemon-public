# Gem's Pokémon Crystal Notepad

## I. Methodology & Game Mechanics

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Analyze the situation's initial state.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis.
3.  **Test:** Execute the simplest possible action to test the hypothesis.
4.  **Conclude & Document:** Record the result and update this notepad.
5.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests.
6.  **Thorough Debugging:** When a tool fails, I must be more thorough in my analysis, checking not just the code's logic but also the inputs and potential engine-side interactions before redefining it.

### B. Automation & Agent Usage
*   **Automation First:** For any recurring puzzle type, my first step is to use my available custom tools (`pathfinder`). If a tool fails, my top priority is to fix it.
*   **Agent Consultation:** I must use my defined agents when appropriate, especially `navigation_advisor` when stuck.

### C. Tile Traversal Rules (Verified)
*   **Impassable:** WALL, VOID, COUNTER, MART_SHELF, BUOY, WHIRLPOOL, PC, BOOKSHELF, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, RADIO
*   **Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA
*   **Warps:** DOOR, CAVE, LADDER, WARP_PANEL, WARP_CARPET_DOWN, WARP_CARPET_LEFT, WARP_CARPET_RIGHT
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH)
*   **Conditional (One-Way):** PIT (fall), LEDGE_HOP_RIGHT (verified), LEDGE_HOP_LEFT (verified), LEDGE_HOP_DOWN (verified)

### D. HM Usage Rules (Verified)
*   **Fly:** Using Fly from the party menu appears to be bugged, causing unexpected warps to different locations (e.g., New Bark Town, Lake of Rage). It does not function as a standard fast-travel move. **Hypothesis:** This might be a consistent mechanic, not a random bug. **Test:** Systematically use Fly from different cities/routes and document the destination for each origin point to identify any patterns.

## II. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance.
    *   **Active Hypothesis (CONFIRMED HINT):** The Fisher explicitly told me to go to the Lake of Rage. Resolving the event there should make him move. **Current Action:** Re-investigating the Lake of Rage.
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.
*   **Schoolboy Alan (Route 36) Blocker (CONFIRMED):** NPC is in a dialogue loop ('I'll call you when I find something'). This is confirmed to be a story-gated event, not a bag issue. Do not interact again until after major story progression (e.g., clearing Goldenrod Radio Tower).
*   **Invisible Barrier on Route 42:** Re-investigate the supposed barrier at (35, 6), (35, 7), and (35, 8). Systematically test movement from all adjacent water tiles to map the exact collision.

### B. Pending Mechanic Tests
*   **FLOOR_UP_WALL:** Impassable from below. **Test:** Attempt to move onto from above/sides at the next opportunity.
*   **CUT_TREE (cut):** Believed to be impassable after being cut. **Test:** Attempt to walk onto a cut tree stump.

### C. Passwords & Keys
*   **Team Rocket Hideout (Boss's Room):**
    1. SLOWPOKETAIL
    2. RATICATE TAIL
    3. HAIL GIOVANNI

### D. Archived Hypotheses
*   **Mahogany Town Gym Block:**
    *   **Hypothesis 1 (Failed):** Defeating Team Rocket in their hideout was the trigger. **Result:** The Fisher still blocks the path.

### E. System Bugs & Glitches
*   **PC Item Management (Mahogany & Violet):** 'DEPOSIT ITEM' and 'TOSS ITEM' from the PC menu are bugged.
*   **Toss Item from Pack (Bugged):** VERIFIED - Function is bugged and does not remove items. Selecting 'TOSS' and confirming the quantity simply returns to the item list without discarding anything.
*   **Giving Items (Bugged):** Giving an item to a Pokémon that is already holding one initiates a swap prompt, but does not free an inventory slot.
*   **Self-Correction:** My own positional tracking errors have led to navigation issues, which I previously misidentified as game glitches. I must be more diligent in verifying my coordinates before acting.

## III. Battle and Pokemon Information

### A. Type Effectiveness Chart (Verified in-game)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective

### B. Key Trainer/Pokemon Info
*   **Rival SILVA:** Uses a Croconaw.
*   **Gym Leaders:** Falkner (Flying), Bugsy (Bug), Whitney (Normal), Morty (Ghost), Jasmine (Steel), Chuck (Fighting).
*   **Rocket Grunt (TeamRocketBaseB2F):** RATTATA (x2), ZUBAT
*   **Rocket Executive (TeamRocketBaseB3F):** ZUBAT (Lv22), RATICATE (Lv24), KOFFING (Lv22)

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

### D. Tool Limitations & Strategy
*   **pathfinder:** Previously had multiple bugs related to coordinate handling and ledge traversal. All are now believed to be fixed.
*   **Prioritize Specialized Tools:** I must remember to check for and use pre-existing specialized tools (e.g., `puzzle_solver`, `sokoban_solver`) for their intended puzzles before attempting manual solutions or building new tools.