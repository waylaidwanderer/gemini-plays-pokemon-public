# Gem's Pokémon Crystal Notepad

## I. Methodology & Game Mechanics

### A. The Scientific Method for Puzzles & Unknowns
1.  **Observe:** Analyze the situation's initial state.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis.
3.  **Test:** Execute the simplest possible action to test the hypothesis.
4.  **Conclude & Document:** Record the result and update this notepad.
5.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests.

### B. Automation & Agent Usage
*   **Automation First:** For any recurring puzzle type, my first step is to use my available custom tools. If a tool fails, my top priority is to fix it.
*   **Agent Consultation:** I must use my defined agents when appropriate, especially `navigation_advisor` when stuck.

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

### B. System Bugs & Glitches
*   **PC Item Management:** 'DEPOSIT ITEM' and 'TOSS ITEM' are bugged in Violet City.
*   **Toss Item from Pack:** Function is bugged and does not remove items.
*   **Giving Items:** Swaps items instead of freeing an inventory slot.
*   **Schoolboy Alan (Route 36) Bug:** NPC script is stuck.

## III. Battle and Pokemon Information

### A. Type Effectiveness Chart (Verified in-game)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective

### B. Key Trainer/Pokemon Info
*   **Rival SILVA:** Uses a Croconaw.
*   **Gym Leaders:** Falkner (Flying), Bugsy (Bug), Whitney (Normal), Morty (Ghost), Jasmine (Steel), Chuck (Fighting).

### C. PC Storage
*   **Items:** PSNCUREBERRY, ICE BERRY, MINT BERRY, BURNT BERRY, GREAT BALL, and various healing/battle items and TMs.