# Gem's Pokémon Crystal Notepad

## I. Methodology & Game Mechanics

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Analyze the situation's initial state.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis.
3.  **Test:** Execute the simplest possible action to test the hypothesis.
4.  **Conclude & Document:** Record the result and update this notepad immediately.
5.  **Consider Non-Obvious Triggers:** When stuck, especially if movement is locked on a normally traversable tile, consider that the solution may be a non-movement scripted event (e.g., a phone call, using a key item, etc.).
6.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests.
7.  **Thorough Debugging:** When a tool fails, I must be more thorough in my analysis, checking not just the code's logic but also the inputs and potential engine-side interactions before redefining it.
8.  **Rigorous Tile Testing:** When a new tile type is encountered, I must test movement from all four directions (Up, Down, Left, Right) to fully understand its properties and document them here.

### B. Automation & Agent Usage
*   **Automation First:** For any recurring puzzle type, my first step is to use my available custom tools (`pathfinder`). If a tool fails, my top priority is to fix it **immediately**.
*   **Agent Consultation:** I must use my defined agents when appropriate, especially `navigation_advisor` when stuck.

### C. Tile Traversal Rules (Verified)
*   **Impassable:** WALL, COUNTER, MART_SHELF, PC, BOOKSHELF, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, RADIO, BOOKSHELF, TV, RADIO, ROCK, BUOY
*   **Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA
*   **Warps:** DOOR, CAVE, LADDER, WARP_PANEL, WARP_CARPET_DOWN, WARP_CARPET_LEFT, WARP_CARPET_RIGHT
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL
*   **Conditional (One-Way):** PIT (fall), LEDGE_HOP_RIGHT (verified), LEDGE_HOP_LEFT (verified), LEDGE_HOP_DOWN (verified)
*   **Untested:** VOID (must test when reachable)

### D. HM Usage Rules (Verified)
*   **Fly:** Using Fly from the party menu appears to be bugged, causing unexpected warps to different locations (e.g., New Bark Town, Lake of Rage). It does not function as a standard fast-travel move. **Hypothesis:** This might be a consistent mechanic, not a random bug. **Test:** Systematically use Fly from different cities/routes and document the destination for each origin point to identify any patterns.

### E. Map Marker Best Practices
*   **Link to object_id:** For any on-screen object (especially moving NPCs), I MUST link the map marker to its `object_id`. This ensures the marker stays with the object if it moves, preventing outdated and misleading information. Unlinked markers for mobile objects are a critical failure in data management.

### F. Debugging & Tool Usage (New Methodology)
*   **Tool Failure Protocol:** If a tool fails (e.g., `pathfinder` returns no path), my IMMEDIATE first step is to perform a simple manual test to confirm the task is possible. For pathfinding, this means attempting to walk a few steps in the intended direction. This will prevent wasting time debugging a tool for a task that is impossible due to map layout or other in-game constraints.
*   **Future Agent Idea:** `tool_debugger` - an agent that takes code and an error description to suggest debugging steps or code modifications.
*   **Future Agent Idea:** `trip_planner` - an agent that takes a start and end city/route name and outputs a high-level sequence of maps to traverse. This would handle macro-level navigation planning.

## II. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance.
    *   **Active Hypothesis (CONFIRMED HINT):** The Fisher explicitly told me to go to the Lake of Rage. Resolving the event there should make him move. **Current Action:** Travel to the Lake of Rage.
*   **RED SCALE Investigation:** Mr. Pokémon is the primary person of interest.
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.
*   **Secret Potion Location (Hypothesis Debunked):** The NPC hint pointing to Cianwood City was incorrect. I have verified that the Pharmacist runs a regular shop and does NOT have the Secret Potion. The item must be located elsewhere or require a different trigger.

### B. Passwords & Keys
*   **Team Rocket Hideout (Boss's Room):**
    1. SLOWPOKETAIL
    2. RATICATE TAIL
    3. HAIL GIOVANNI

### C. Solved Puzzles
*   **Cianwood City Stuck Spot (SOLVED):** Was stuck on tile (10, 28). Solution was to trigger and complete the back-to-back phone calls (Mom, then Liz). This confirms it was a scripted event, not a bug.

### D. System Bugs & Glitches
*   **PC Item Management (Mahogany & Violet):** 'DEPOSIT ITEM' and 'TOSS ITEM' from the PC menu are bugged.
*   **Toss Item from Pack (Bugged):** VERIFIED - Function is bugged and does not remove items. Selecting 'TOSS' and confirming the quantity simply returns to the item list without discarding anything.
*   **Giving Items (Bugged):** Giving an item to a Pokémon that is already holding one initiates a swap prompt, but does not free an inventory slot.

## III. Battle and Pokemon Information

### A. Party Held Items
*   **G (FERALIGATR):** BERRY (Assumed)
*   **OM (TOGEPI):** POTION (Verified)
*   **ROCKY (ONIX):** BERRY (Verified)
*   **DYNAMO (ELEKID):** BERRY (Verified)
*   **HOOTIN (HOOTHOOT):** None

### B. Type Effectiveness Chart (Verified in-game)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective

### C. Key Trainer/Pokemon Info
*   **Rival SILVA:** Uses a Croconaw.
*   **Gym Leaders:** Falkner (Flying), Bugsy (Bug), Whitney (Normal), Morty (Ghost), Jasmine (Steel), Chuck (Fighting).

### D. Observed Movesets
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

## IV. Self-Correction & Improvement

### A. Core Directives (Violations & Learnings)
*   **Tool Refinement (VIOLATION):** I failed to immediately fix the `pathfinder` tool after it failed on Route 43. **Correction:** Faulty tools must be fixed immediately, as this is a higher priority than any gameplay action.
*   **Pathfinder Tool Limitations:** The tool does not currently understand HM usage (e.g., SURF, CUT) or automatically detect on-screen NPCs as obstacles. I must manually navigate these transitions for now until the tool is improved.
*   **Schoolboy Alan (Route 36):** My hypothesis that he had an item for me was incorrect. He is in a dialogue loop, which confirms he is a story-gated event. I will not interact with him again until major story progression (e.g., clearing Goldenrod Radio Tower).
*   **Tile Type Hallucination (CORRECTION):** My previous assumption that a FLOOR tile could be impassable was incorrect. Tile collision types are consistent. Being stuck at (10, 28) must be due to an invisible event, object, or game state flag, not a faulty tile.
*   **Pathing Assumptions (VIOLATION):** I incorrectly assumed a land path existed on Route 40. **Correction:** I must trust my `pathfinder` tool's output. If it reports no path, I must test my assumptions by trying alternative routes (e.g., water vs. land) or breaking the problem into smaller, verifiable steps instead of assuming the tool is broken.

### E. Warp Tile Mechanics (Verified)
*   **WARP_CARPET_LEFT (Ilex Forest Azalea Gate):** Activated by moving left *onto* the tile. Other directional movements or pressing 'A' do not work.