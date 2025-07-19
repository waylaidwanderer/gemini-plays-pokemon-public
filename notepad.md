# Gem's Pokémon Crystal Notepad

## I. Methodology & Game Mechanics

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Analyze the situation's initial state.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis.
3.  **Test:** Execute the simplest possible action to test the hypothesis.
4.  **Conclude & Document:** Record the result and update this notepad immediately.
5.  **Consider Non-Obvious Triggers:** When stuck, especially if movement is locked on a normally traversable tile, consider that the solution may be a non-movement scripted event (e.g., a phone call, using a key item, etc.).
6.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests.
7.  **Rigorous Tile Testing:** When a new tile type is encountered, I must test movement from all four directions (Up, Down, Left, Right) to fully understand its properties and document them here. The test must be performed IMMEDIATELY upon discovery.

### B. Tile Traversal Rules (Verified)
*   **Impassable:** WALL, COUNTER, MART_SHELF, PC, BOOKSHELF, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, RADIO, ROCK, BUOY
*   **Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA
*   **Warps:** DOOR, CAVE, LADDER, WARP_PANEL, WARP_CARPET_DOWN, WARP_CARPET_LEFT, WARP_CARPET_RIGHT
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL
*   **Conditional (One-Way):** PIT (fall), LEDGE_HOP_RIGHT (verified), LEDGE_HOP_LEFT (verified), LEDGE_HOP_DOWN (verified)
*   **VOID (Impassable - verified)**
*   **Untested:** RADIO, INCENSE_BURNER

### C. HM Usage Rules (Verified)
*   **Fly:** Using Fly from the party menu appears to be bugged, causing unexpected warps to different locations. It does not function as a standard fast-travel move.

### D. Map Marker Best Practices
*   **Link to object_id:** For any on-screen object (especially moving NPCs), I MUST link the map marker to its `object_id`. This ensures the marker stays with the object if it moves, preventing outdated and misleading information. Unlinked markers for mobile objects are a critical failure in data management.

## II. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance. Hypothesis: I must find and speak to Lance at the Lake of Rage to progress the story.
*   **RED SCALE Investigation:** Mr. Pokémon is the primary person of interest.
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.
*   **Secret Potion Location (Hypothesis Debunked):** The NPC hint pointing to Cianwood City was incorrect. The Pharmacist runs a regular shop and does NOT have the Secret Potion.

### B. Passwords & Keys
*   **Team Rocket Hideout (Boss's Room):
    1. SLOWPOKETAIL (Confirmed)
    2. RATICATE TAIL
    3. HAIL GIOVANNI

### C. Solved Puzzles
*   **Cianwood City Stuck Spot (SOLVED):** Was stuck on tile (10, 28). Solution was to trigger and complete the back-to-back phone calls (Mom, then Liz).
*   **Team Rocket Base Arrow Maze (In Progress):** Safe tiles found so far: (5, 3), (5, 4), (4, 4), (3, 4), (1, 3), (1, 2), (1, 1), (2, 1), (4, 1), (5, 2), (4, 5), (3, 3), (2, 3), (2, 2).

### D. System Bugs & Glitches
*   **PC Item Management (Mahogany & Violet):** 'DEPOSIT ITEM' and 'TOSS ITEM' from the PC menu are bugged.
*   **Toss Item from Pack (Bugged):** VERIFIED - Function is bugged and does not remove items.
*   **Giving Items (Bugged):** Giving an item to a Pokémon that is already holding one initiates a swap prompt, but does not free an inventory slot.

## III. Battle and Pokemon Information

### A. Type Effectiveness Chart (Verified in-game)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective

### B. Observed Movesets
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
*   **Tool Refinement (VIOLATION):** I failed to immediately fix the `pathfinder` tool. **Correction:** Faulty tools must be fixed immediately.
*   **Pathfinder Tool Limitations:** The tool does not currently understand HM usage (e.g., SURF, CUT) or automatically detect on-screen NPCs as obstacles. I must manually navigate these transitions for now until the tool is improved.
*   **Schoolboy Alan (Route 36):** My hypothesis that he had an item for me was incorrect. He is in a dialogue loop, which confirms he is a story-gated event.
*   **Tile Type Hallucination (CORRECTION):** My previous assumption that a FLOOR tile could be impassable was incorrect. Tile collision types are consistent. Being stuck at (10, 28) must be due to an invisible event, object, or game state flag, not a faulty tile.
*   **Pathing Assumptions (VIOLATION):** I incorrectly assumed a land path existed on Route 40. **Correction:** I must trust my `pathfinder` tool's output.
*   **Ilex Forest Shrine:** A Lass in the Route 34 Gate mentioned a shrine honoring a grass-type protector of the forest.
*   **TM12 (Sweet Scent):** Given by Teacher in Route 34 Ilex Forest Gate. Attracts wild Pokémon.

## V. Automation & Tool Development

### A. Pathfinder Tool Issues & Strategy
*   **Known Bug:** The `pathfinder` tool currently fails on long, complex paths, especially those involving multiple terrain transitions (e.g., land -> water -> land).
*   **Current Workaround:** I must break down long-distance navigation into smaller, simpler segments.

### B. Future Tool Ideas
*   **Maze Solver:** A tool to systematically explore and map out unknown mazes with special tile mechanics, like the invisible arrow tiles in the Team Rocket Base.
*   **Team Rocket Arrow Maze (Hypothesis):** The arrow tiles have a consistent, repeatable effect. **Test:** After mapping a tile's behavior, I must re-test it later to confirm the outcome is identical. This will rule out more complex puzzle logic where tile behavior might change.