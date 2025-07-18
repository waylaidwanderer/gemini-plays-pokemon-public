# Gem's Pokémon Crystal Notepad

## I. Methodology & Game Mechanics

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Analyze the situation's initial state.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis.
3.  **Test:** Execute the simplest possible action to test the hypothesis.
4.  **Conclude & Document:** Record the result and update this notepad.
5.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests.

### B. Automation & Agent Usage
*   **Automation First:** For any recurring puzzle type, my first step is to use my available custom tools (`pathfinder`, `puzzle_solver`, `sokoban_solver`). If a tool fails, my top priority is to fix it.
*   **Agent Consultation:** I must use my defined agents when appropriate, especially `navigation_advisor` when stuck and my new `pathing_monitor` to detect loops.

### C. Tile Traversal Rules (Verified)
*   **Impassable:** WALL, VOID, COUNTER, MART_SHELF, BUOY, WHIRLPOOL, PC
*   **Traversable:** FLOOR, GRASS, TALL_GRASS
*   **Warps:** DOOR, CAVE, LADDER, WARP_PANEL
*   **HM Required:** WATER/SEA (SURF), CUT_TREE (CUT), BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH)
*   **Conditional:** PIT (one-way fall), WARP_CARPET (directional)

### D. Tile Mechanics (Pending Tests)
*   **LEDGE/LEDGE_HOP:** Believed to be one-way. **Test:** Attempt to move up/sideways against a ledge at the next opportunity.
*   **FLOOR_UP_WALL:** Impassable from below. **Test:** Attempt to move onto from above/sides at the next opportunity.

## II. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance. **Hypothesis:** Defeating Team Rocket in their hideout was the trigger. **Test:** Speak to the Fisher at (6, 14) in Mahogany Town after arriving.
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.
*   **Schoolboy Alan (Route 36) Bug:** NPC script is stuck. I need to test if tossing an item resolves it.

### B. System Bugs & Glitches
*   **PC Item Management:** 'DEPOSIT ITEM' and 'TOSS ITEM' are bugged in Violet City.
*   **Toss Item from Pack:** Function is bugged and does not remove items.
*   **Giving Items:** Swaps items instead of freeing an inventory slot.
*   **Fly Command:** Using Fly can cause a game-breaking glitch/hallucination. Avoid using it unless absolutely necessary.

## III. Battle and Pokemon Information

### A. Type Effectiveness Chart (Verified in-game)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective

### B. Key Trainer/Pokemon Info
*   **Rival SILVA:** Uses a Croconaw.
*   **Gym Leaders:** Falkner (Flying), Bugsy (Bug), Whitney (Normal), Morty (Ghost), Jasmine (Steel), Chuck (Fighting).

## IV. Appendices & Data

### A. Observed Movesets
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

### B. Pokémon Locations (Summary)
*   **Early Routes (29-31):** Common Normal/Flying/Bug types.
*   **Caves (Dark, Union, Mt. Mortar):** Rock/Ground/Poison types (Geodude, Zubat, Onix).
*   **Forests (Ilex):** Bug/Grass types.
*   **Mid Routes (34-39):** More variety, including Fire, Psychic, and Steel types.
*   **Water Routes (40-41, Lake of Rage):** Water types (Tentacool, Magikarp, Gyarados).
*   **Late Routes (42-43):** Electric and Psychic types appear more frequently.

### C. Pending Mechanic Tests
*   **Objective:** Verify the behavior of `LEDGE` and `FLOOR_UP_WALL` tiles.
*   **Method:** At the next encounter with these tiles, attempt to move against their presumed one-way direction and document the result.
*   **Specific Target:** Test the `FLOOR_UP_WALL` tile at **(39, 12)** on Route 42 once the area is accessible.

### C. PC Storage
*   **Items:** PSNCUREBERRY (x1), ICE BERRY (x1), MINT BERRY (x1), BURNT BERRY (x1), GREAT BALL (x1), ANTIDOTE (x1), PARLYZ HEAL (x1), AWAKENING (x1), POTION (x1), GUARD SPEC. (x1), X ATTACK (x1), X DEFEND (x1), X SPEED (x1), X SPECIAL (x1), DIRE HIT (x1), POKE BALL (x1), REPEL (x1), ESCAPE ROPE (x1), ETHER (x1), MAX ETHER (x1), REVIVE (x1), NUGGET (x1), PROTEIN (x1), IRON (x1), CARBOS (x1), CALCIUM (x1), HP UP (x1), RARE CANDY (x1), TM39 (SWIFT), TM13 (SNORE), TM41 (THUNDERPUNCH), TM48 (FIRE PUNCH), TM02 (HEADBUTT), TM45 (ATTRACT), TM21 (FRUSTRATION), TM27 (RETURN), TM12 (SWEET SCENT), TM35 (SLEEP TALK), TM49 (FURY CUTTER).

## V. Current Exploration Plans

### A. Route 42 Invisible Barrier
*   **Objective:** Systematically map the boundaries of the invisible barrier at x=35.
*   **Method:**
    1.  Move along the x=34 column, attempting to move right into x=35 at each y-coordinate.
    2.  Mark each confirmed impassable tile at x=35 with a '🚫' marker.
    3.  Once the southern and northern extents of the barrier are found, search for a path around it.

### B. Pending Mechanic Tests
*   **Objective:** Verify the behavior of `LEDGE` and `FLOOR_UP_WALL` tiles.
*   **Method:** At the next encounter with these tiles, attempt to move against their presumed one-way direction and document the result.