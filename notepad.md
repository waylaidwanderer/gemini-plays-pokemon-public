# Gem's Pokémon Crystal Notepad

## I. Game Mechanics

### A. Tile Traversal Rules
*   **WALL/VOID:** Impassable boundary tiles.
*   **FLOOR:** Standard traversable tile.
*   **GRASS/TALL_GRASS:** Traversable; can trigger wild encounters.
*   **DOOR/CAVE/LADDER/WARP_PANEL/WARP_CARPET_UP/WARP_CARPET_DOWN:** Traversable warp tiles. `WARP_CARPET_DOWN` requires facing down to activate.
*   **WATER/SEA:** Traversable only with SURF. Can trigger wild encounters.
*   **LEDGE/FLOOR_UP_WALL:** One-way traversal. Can be jumped down but not climbed up.
*   **PIT:** One-way tile that causes a fall to the floor below.
*   **COUNTER/PC/MART_SHELF/BUOY/WHIRLPOOL:** Impassable obstacles. Interaction with some (PC, counter NPCs) requires standing on an adjacent tile.
*   **TREE:** Small trees can be cut with CUT, leaving an impassable stump.
*   **BOULDER:** Can be moved with STRENGTH.
*   **HEADBUTT_TREE:** Interactable tree for finding Pokémon.
*   **ROCK_SMASH_BOULDER:** Can be crushed with the move ROCK SMASH.

### B. Key Items & HM Usage
*   **SQUIRTBOTTLE:** Used to wake up the Sudowoodo blocking Route 36.
*   **HM01 (CUT):** Cuts small trees. Learned by Feraligatr.
*   **HM02 (FLY):** Allows fast travel. **LOCATION UNKNOWN.**
*   **HM03 (SURF):** Allows travel over water. Learned by Feraligatr.
*   **HM04 (STRENGTH):** Moves large boulders.
*   **HM05 (FLASH):** Illuminates dark caves. Learned by Hoothoot.
*   **HM06 (WHIRLPOOL):** Allows crossing whirlpools. **LOCATION UNKNOWN.**
*   **DIG:** Can be used to escape caves and some buildings, returning to the entrance. Disabled in Cianwood Gym.

### C. Other Systems
*   **Everstone:** A Pokémon holding this item will not evolve.
*   **Phone Calls:** NPCs can call to offer hints, battle rematches, or flavor text.
*   **Happiness:** Increased by haircuts and using items on Pokémon. Required for some evolutions (like Togepi).
*   **Day/Night Cycle:** Affects which Pokémon appear.
*   **Bug-Catching Contest:** Held on Tuesdays, Thursdays, and Saturdays in the National Park.

## II. World & Story

### A. Solved Puzzles
*   **Sprout Tower:** Central pillar blocks direct ascent. Must go up the side ladders to the 3rd floor, then descend via the central ladder to reach the Elder.
*   **Azalea Gym:** A spiderweb platform puzzle. Switches reconfigure the platforms. The correct sequence is left switch, then right switch.
*   **Ilex Forest Farfetch'd:** Chase the Farfetch'd sprite by blocking its path to make it turn. Corner it to return it to its owner.
*   **Goldenrod Gym:** A maze with trainers that appear and disappear. The path is a spiral shape resembling a Clefairy.
*   **Ecruteak Gym:** An invisible path puzzle. Requires careful trial and error to find the safe path to the Gym Leader.

### B. Key NPCs & Quests
*   **Professor Elm:** Gave me my starter and the Pokémon Egg. Main quest giver.
*   **Rival (SILVA):** My recurring rival. Stole a Pokémon from Prof. Elm.
*   **Kurt (Azalea Town):** Makes special Poké Balls from Apricorns.
*   **Day-Care Man (Route 34):** Gave me the ODD EGG.
*   **Sick Miltank (Route 39):** Needs 'lots of BERRIES' to get better.
*   **Sick Ampharos (Olivine Lighthouse):** Needs SECRETMEDICINE from Cianwood City.
*   **Lance (Lake of Rage/Mahogany):** Helped stop Team Rocket's radio signal plot.

## III. Strategy & Learnings

### A. Corrected Assumptions & Critical Lessons
*   **HM02 (Fly) & HM06 (Whirlpool) Hallucinations:** I hallucinated receiving these HMs. I have confirmed by checking my inventory that I DO NOT have them. Their true locations are unknown.
*   **Pathing Logic:** My pathfinder tools failed repeatedly because I was giving them incorrect traversable tile types. I must ensure the `traversable_tiles` argument accurately reflects my current movement state (walking or surfing).
*   **Cianwood Geography:** Cianwood City is split into two landmasses. The southern part where I initially arrived is an island. Progress to the northern part (where the gym is) requires using SURF.

### B. Known Tool Issues
*   **`sokoban_solver` Flaw:** My `sokoban_solver` tool was critically flawed, assuming the player moved with the boulder. I have redefined the tool with the correct logic: the player stays in place after a push.

## IV. Puzzle Solving Methodology (Post-Critique Update)

### A. The Scientific Method for Puzzles
1.  **Observe:** Carefully analyze the puzzle's initial state using the map, object data, and any relevant NPC dialogue. Document these initial observations.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis about a specific mechanic of the puzzle.
3.  **Test:** Execute the simplest possible sequence of actions to test the hypothesis.
4.  **Conclude & Document:** Record the result of the test. Was the hypothesis confirmed or falsified? What was the exact outcome? Update the plan accordingly.
5.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests.

### B. Automation First
- For any recurring puzzle type (e.g., state-based mazes like boulder puzzles), my first step will be to define a custom tool to solve it computationally. Manual trial-and-error is my last resort. If a tool fails, my top priority is to fix it, not to abandon it.

### C. Cianwood Gym Boulder Puzzle (VERIFIED MECHANIC)
1.  **Activation:** Stand adjacent to a boulder and face it. Press 'A'. This brings up the "Want to use STRENGTH?" YES/NO prompt.
2.  **Confirmation:** Select 'YES'. This activates a temporary "push mode" for a single push, confirmed by the message "Boulders may now be moved!".
3.  **Pushing:** After confirmation, walk into the adjacent boulder to push it one tile. The player character does NOT move into the vacated spot. The "push mode" then deactivates, requiring re-activation for the next push.
4.  **Puzzle Trigger:** Walking onto the tile at (8, 6) triggers the appearance of Black Belts, making the puzzle unsolvable. This tile must be avoided.