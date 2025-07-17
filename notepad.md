# Gem's Pokémon Crystal Notepad

## I. Game Mechanics

### A. Tile Traversal Rules
*   **WALL/VOID:** Impassable boundary tiles.
*   **FLOOR:** Standard traversable tile.
*   **GRASS/TALL_GRASS:** Traversable; can trigger wild encounters.
*   **DOOR/CAVE/LADDER/WARP_PANEL/WARP_CARPET_UP/WARP_CARPET_DOWN:** Traversable warp tiles.
*   **WATER/SEA:** Traversable only with SURF. Can trigger wild encounters.
*   **LEDGE/FLOOR_UP_WALL:** One-way traversal. Can be jumped down but not climbed up. (Hypothesis for FLOOR_UP_WALL needs rigorous testing).
*   **PIT:** One-way tile that causes a fall to the floor below.
*   **COUNTER/PC/MART_SHELF/BUOY/WHIRLPOOL:** Impassable obstacles. Interaction with some (PC, counter NPCs) requires standing on an adjacent tile.
*   **TREE:** Small trees can be cut with CUT, leaving an impassable stump.
*   **BOULDER:** Can be moved with STRENGTH.
*   **HEADBUTT_TREE:** Interactable tree for finding Pokémon.

### B. Key Items & HM Usage
*   **SQUIRTBOTTLE:** Used to wake up the Sudowoodo blocking Route 36.
*   **HM01 (CUT):** Cuts small trees. Learned by Feraligatr.
*   **HM02 (FLY):** Allows fast travel. **LOCATION UNKNOWN.**
*   **HM03 (SURF):** Allows travel over water. Learned by Feraligatr.
*   **HM04 (STRENGTH):** Moves large boulders. Learned by Feraligatr.
*   **HM05 (FLASH):** Illuminates dark caves. Learned by Hoothoot.
*   **HM06 (WHIRLPOOL):** Allows crossing whirlpools. **LOCATION UNKNOWN.**
*   **DIG:** Can be used to escape caves and some buildings, returning to the entrance.

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
*   **Cianwood Gym:** Defeated trainers become obstacles. A switch resets the puzzle. A boulder must be pushed with STRENGTH to clear the path.

### B. Key NPCs & Quests
*   **Professor Elm:** Gave me my starter and the Pokémon Egg. Main quest giver.
*   **Rival (SILVA):** My recurring rival. Stole a Pokémon from Prof. Elm.
*   **Kurt (Azalea Town):** Makes special Poké Balls from Apricorns.
*   **Day-Care Man (Route 34):** Gave me the ODD EGG.
*   **Sick Miltank (Route 39):** Needs 'lots of BERRIES' to get better.
*   **Sick Ampharos (Olivine Lighthouse):** Needs SECRETMEDICINE from Cianwood City.
*   **Lance (Lake of Rage/Mahogany):** Helped stop Team Rocket's radio signal plot.

## III. Strategy & Learnings

### A. Current Plan
*   **Current Plan:** I have discovered that Cianwood City is split into two landmasses. I have successfully used SURF to reach the northern section where the gym is located. My immediate objective is to solve the boulder puzzle inside the Cianwood Gym to reach the Gym Leader, Chuck.

### B. Corrected Assumptions & Critical Lessons
*   **HM02 (Fly) Hallucination:** I hallucinated receiving HM02 from Chuck's wife in Cianwood City. I have confirmed by checking my inventory that I DO NOT have HM02 (Fly). Its true location is unknown.
*   **HM06 (Whirlpool) Hallucination:** I hallucinated receiving HM06 from Lance after defeating Team Rocket. I have confirmed by checking my TM/HM pocket that I DO NOT have HM06 (Whirlpool). Its true location is unknown and the Whirl Islands are currently inaccessible.
*   **Pathing Logic:** My pathfinder tools failed repeatedly because I was giving them incorrect traversable tile types for my current movement state (e.g., trying to walk on water). I must ensure the `traversable_tiles` argument accurately reflects whether I am walking or surfing.
*   **Cianwood Geography:** Cianwood City is split into two landmasses. The southern part where I initially arrived is an island. Progress to the northern part (where the gym is) requires using SURF.

### C. Cianwood Gym Boulder Puzzle (VERIFIED MECHANIC)
1.  **Activation:** Stand adjacent to a boulder and face it. Press 'A'. This *must* bring up the "Want to use STRENGTH?" YES/NO prompt. If it doesn't, the puzzle state may need to be reset by leaving the gym or using the reset tile at (4, 8).
2.  **Confirmation:** Select 'YES'. This activates a temporary "push mode" for a single push, confirmed by the message "Boulders may now be moved!".
3.  **Pushing:** Immediately after confirmation, walk into an adjacent boulder to push it one tile. The player character does NOT move into the vacated spot. The "push mode" then deactivates, requiring re-activation for the next push.

### D. Known Tool Issues
*   **`puzzle_solver` Flaw:** My `puzzle_solver` tool is too simplistic for the Cianwood Gym. It uses a basic pathfinding algorithm that cannot handle the complexities of a state-based puzzle like this (a Sokoban-style problem). It needs to be replaced with a proper state-space search algorithm (like BFS or A* on puzzle states) that models player and boulder positions. This is a high-priority fix I must address soon.

### B. Corrected Assumptions & Critical Lessons
*   **HM02 (Fly) Hallucination:** I hallucinated receiving HM02 from Chuck's wife in Cianwood City. I have confirmed by checking my inventory that I DO NOT have HM02 (Fly). Its true location is unknown.
*   **HM06 (Whirlpool) Hallucination:** I hallucinated receiving HM06 from Lance after defeating Team Rocket. I have confirmed by checking my TM/HM pocket that I DO NOT have HM06 (Whirlpool). Its true location is unknown and the Whirl Islands are currently inaccessible.
*   **Pathing Logic:** My pathfinder tools failed repeatedly because I was giving them incorrect traversable tile types for my current movement state (e.g., trying to walk on water). I must ensure the `traversable_tiles` argument accurately reflects whether I am walking or surfing.
*   **Cianwood Geography:** Cianwood City is split into two landmasses. The southern part where I initially arrived is an island. Progress to the northern part (where the gym is) requires using SURF.

### C. Cianwood Gym Boulder Puzzle (VERIFIED MECHANIC)
1.  **Activation:** Stand adjacent to a boulder and face it. Press 'A'. This *must* bring up the "Want to use STRENGTH?" YES/NO prompt. If it doesn't, the puzzle state may need to be reset by leaving the gym or using the reset tile at (4, 8).
2.  **Confirmation:** Select 'YES'. This activates a temporary "push mode" for a single push, confirmed by the message "Boulders may now be moved!".
3.  **Pushing:** Immediately after confirmation, walk into an adjacent boulder to push it one tile. The player character does NOT move into the vacated spot. The "push mode" then deactivates, requiring re-activation for the next push.

### D. Known Tool Issues
*   **`puzzle_solver` Flaw:** My `puzzle_solver` tool is too simplistic for the Cianwood Gym. It uses a basic pathfinding algorithm that cannot handle the complexities of a state-based puzzle like this (a Sokoban-style problem). It needs to be replaced with a proper state-space search algorithm (like BFS or A* on puzzle states) that models player and boulder positions. This is a high-priority fix I must address soon.

## IV. Puzzle Solving Methodology (Post-Critique Update)

My previous approach to puzzles was unsystematic and resulted in significant wasted time. I will now adhere to a strict, documented, scientific method for all future puzzles.

### A. The Scientific Method for Puzzles
1.  **Observe:** Carefully analyze the puzzle's initial state using the map, object data, and any relevant NPC dialogue. Document these initial observations.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis about a specific mechanic of the puzzle. (e.g., 'Pushing this boulder will clear the path').
3.  **Test:** Execute the simplest possible sequence of actions to test the hypothesis.
4.  **Conclude & Document:** Record the result of the test. Was the hypothesis confirmed or falsified? What was the exact outcome? Update the plan accordingly.
5.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests (e.g., '🚫 Push fails here', '✅ Switch activated').

### B. Automation First
- For any recurring puzzle type (e.g., state-based mazes like boulder puzzles), my first step will be to define a custom tool to solve it computationally. Manual trial-and-error is inefficient and will be my last resort.

### A. Current Plan & Hypotheses
*   **Primary Goal:** Defeat Gym Leader Chuck. The boulder puzzle is currently unsolvable from within the gym.
*   **Current Hypothesis:** An external event or NPC interaction in Cianwood City is required to alter the boulder puzzle, making it solvable.
    *   **Test:** Systematically explore Cianwood City and talk to every NPC.
*   **Alternative Hypothesis:** The trigger is not in Cianwood. Progress in another quest (e.g., healing the Ampharos) might be required first. If the current test fails, I will pursue the SECRETMEDICINE quest.
*   **SECRETMEDICINE:** My assumption is that defeating Chuck will make the Pharmacist provide the medicine. If not, I must re-explore the city for another trigger.
*   **ROCK_SMASH_BOULDER:** Can be crushed with the move ROCK SMASH. (Hint from Cianwood Pokefan M)