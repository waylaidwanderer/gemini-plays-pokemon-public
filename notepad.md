# Gem's Pokémon Crystal Notepad

## I. Game Mechanics

### A. Tile Traversal Rules
*   **WALL:** Impassable. Forms the boundaries of maps.
*   **FLOOR:** Standard traversable tile.
*   **LADDER:** A traversable tile that also functions as a warp, moving the player between floors when stepped on.
*   **WARP_PANEL:** A warp tile. Teleports the player to another location. Behavior seems to be one-way.
*   **DOOR:** A warp tile. Leads to other buildings/areas.
*   **GRASS/TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **WATER/SEA:** Traversable only with the HM move SURF. Can trigger wild Pokémon encounters.
*   **BUOY:** Impassable obstacle in water.
*   **WHIRLPOOL:** Impassable obstacle in water. Requires an HM to cross.
*   **TREE:** Small trees can be bypassed with the HM move CUT. Cut trees become impassable stumps.
*   **BOULDER:** Can be moved with the HM move STRENGTH.
*   **LEDGE:** One-way traversal. Can be jumped down but not climbed up.
*   **COUNTER:** Impassable barrier. To interact with an NPC behind a counter, stand on an adjacent floor tile, face the counter, and press 'A'.
*   **PC:** Impassable object. Interact with it from an adjacent tile. 'BILL's PC' is for Pokémon, 'Your Name's PC' is for items.
*   **MART_SHELF:** Impassable object. Acts as a wall within shops.
*   **HEADBUTT_TREE:** An interactable tree that can be shaken with the move Headbutt to find Pokémon.
*   **CAVE:** A type of warp tile, functions like a door to an interior map.
*   **WARP_CARPET_DOWN:** A warp tile that moves the player downwards, usually to exit a building.
*   **WARP_CARPET_UP:** A warp tile that moves the player upwards, usually to enter a building.
*   **VOID:** An impassable boundary tile, functions like a WALL.
*   **PIT:** A one-way tile that causes the player to fall to the floor below when stepped on.

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
*   **Current Plan:** My primary goal is to obtain the SECRETMEDICINE from Cianwood City. I have been unable to ascend the Olivine Lighthouse, and I recall from a previous hint that the medicine is needed to heal the sick Ampharos, which will likely trigger an event with Jasmine. I must exit the lighthouse and travel west across the sea to Cianwood City.

### B. Corrected Assumptions & Critical Lessons
*   **HM02 (Fly) Hallucination:** I hallucinated receiving HM02 from Chuck's wife in Cianwood City. I have confirmed by checking my inventory that I DO NOT have HM02 (Fly). Its true location is unknown.
*   **HM06 (Whirlpool) Hallucination:** I hallucinated receiving HM06 from Lance after defeating Team Rocket. I have confirmed by checking my TM/HM pocket that I DO NOT have HM06 (Whirlpool). Its true location is unknown and the Whirl Islands are currently inaccessible.
*   **Observational Failure & Tool Trust:** My `master_navigator` tool was correct about the buoy wall on Route 41. I must trust the output of my tools over my own visual assessment, as they process the raw game data directly.
*   **Movement Mechanics Update:** My hypothesis that defeated trainer sprites were passable was incorrect. I attempted to walk through a defeated swimmer on Route 41 and was blocked. **Defeated trainer sprites are IMPASSABLE obstacles.**
*   **Pathing Logic:** My `master_navigator` tool failed repeatedly because I was giving it incorrect traversable tile types for my current movement state (e.g., trying to walk on water). I must ensure the `traversable_tiles` argument accurately reflects whether I am walking or surfing.
*   **BUOY:** Impassable obstacle in water.

### C. New Hypotheses & Tests
*   **Movement State Glitch:** The 'walking on water' glitch seems to trigger when moving from land to water. Test: After reaching Cianwood, return to a shore and step on/off the water multiple times to see if the glitch is consistently reproducible.
*   **Movement State Glitch (Surfing):** The game state sometimes reports the player's `movement_state` as 'walking' even when visually surfing on a Pokémon. This can cause pathfinding tools to fail if they are not given 'WATER' as a traversable tile. This seems to be a consistent quirk.
*   **Rival Blockade on Route 40:** I incorrectly assumed I had to battle SILVA to pass him on Route 40. After multiple failed interaction attempts resulting in a dialogue loop, I've realized he might be an optional encounter or simply a non-blocking obstacle on the water. My new strategy is to navigate around him instead of trying to force an interaction.
*   **SECRETMEDICINE Hypothesis:** My primary assumption is defeating Chuck will trigger the pharmacist to give me the medicine. Alternative hypothesis: The medicine is a reward from another NPC who appears *after* the gym battle, or I will receive an item from the gym that unlocks a new area where the medicine is located. Test: After defeating Chuck, I must re-explore all of Cianwood City and talk to every NPC before leaving.
*   **Dialogue Loops:** Interacting with a defeated trainer can sometimes trigger their pre-battle dialogue in a loop without starting a battle. This is a sign that the trainer has already been defeated and interacting with them further is not a valid way to progress. Example: Black Belt Lung in Cianwood Gym.
*   **Cianwood Gym Boulder Puzzle (VERIFIED MECHANIC):**
    1.  **Activation:** Stand adjacent to a boulder and face it. Press 'A'. This *must* bring up the "Want to use STRENGTH?" YES/NO prompt. If it doesn't, the puzzle state may need to be reset by leaving the gym or using the reset tile at (4, 8).
    2.  **Confirmation:** Select 'YES'. This activates a temporary "push mode" for a single push, confirmed by the message "Boulders may now be moved!".
    3.  **Pushing:** Immediately after confirmation, walk into an adjacent boulder to push it one tile. The player character then moves into the tile the boulder previously occupied. The "push mode" then deactivates, requiring re-activation for the next push.

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

### C. Cianwood Gym Boulder Puzzle (New Findings)
- My `puzzle_solver` tool has confirmed that from the initial puzzle state (after stepping on the trigger at (8, 6)), there is **no possible solution** to reach the Gym Leader. 
- **New Hypothesis:** There must be a hidden switch or event within the gym that alters the puzzle state, making it solvable. My next course of action is to systematically re-investigate every interactable object in the gym to find this trigger.
*   **Cianwood Gym Puzzle (External Trigger):** After exhausting all options inside the gym, my new hypothesis is that an external event or NPC interaction in Cianwood City is required to alter the boulder puzzle, making it solvable. I will now leave the gym and re-explore the entire city.