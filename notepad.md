# Gem's Pokémon Crystal Notepad

## I. World & Story

### A. Active Quests & Blockers
*   **Get FIRE STONE from Schoolboy Alan:** My ITEM POCKET is full. I need to fly to a Pokémon Center, store items in the PC, and then return to him on Route 36.
*   **Heal the Sick Miltank (Route 39):** The Miltank in the barn needs 'lots of BERRIES'. I need to find a source of berries.
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance. He insists I go to the Lake of Rage. I have already defeated the Red Gyarados and stopped Team Rocket, but he remains. My hypothesis that the Lake of Rage was the trigger is likely incorrect.

### B. Key NPCs
*   **Professor Elm:** My quest giver in New Bark Town.
*   **Rival (SILVA):** My main rival.
*   **Kurt (Azalea Town):** Crafts special Poké Balls from Apricorns.
*   **Lance:** The Pokémon Champion. Helped me stop Team Rocket in Mahogany Town.
*   **Day-Care Couple (Route 34):** They gave me the ODD EGG.

### B. Solved Puzzles
*   **Sprout Tower:** Central pillar blocks direct ascent. Must go up the side ladders to the 3rd floor, then descend via the central ladder to reach the Elder.
*   **Azalea Gym:** A spiderweb platform puzzle. Switches reconfigure the platforms. The correct sequence is left switch, then right switch.
*   **Ilex Forest Farfetch'd:** Chase the Farfetch'd sprite by blocking its path to make it turn. Corner it to return it to its owner.
*   **Goldenrod Gym:** A maze with trainers that appear and disappear. The path is a spiral shape resembling a Clefairy.
*   **Ecruteak Gym:** An invisible path puzzle. Requires careful trial and error to find the safe path to the Gym Leader.
*   **Cianwood Gym Boulder Puzzle & Bug:** The post-battle dialogue with Chuck is bugged, preventing reward acquisition. Progress is gated by speaking to his wife outside the gym, who provides HM02 (FLY). The boulder puzzle itself requires a multi-step STRENGTH activation for each push, and the player moves into the boulder's previous spot. The gym must be reset by leaving and re-entering to clear blocking trainers.

## II. Game Mechanics

### A. Tile Traversal Rules
*   **WALL/VOID:** Impassable boundary tiles.
*   **FLOOR:** Standard traversable tile.
*   **GRASS/TALL_GRASS:** Traversable; can trigger wild encounters.
*   **DOOR/CAVE/LADDER/WARP_PANEL:** Standard warp tiles.
*   **WARP_CARPET_DOWN:** Warp tile that requires facing down to activate.
*   **WATER/SEA:** Traversable only with SURF. Can trigger wild encounters.
*   **LEDGE/FLOOR_UP_WALL/LEDGE_HOP_DOWN:** One-way traversal. Can be jumped down but not climbed up.
*   **LEDGE_HOP_DOWN:** One-way tile that can be jumped down but not climbed up.
*   **LEDGE_HOP_LEFT:** One-way traversal. Can be jumped left but not entered from the right.
*   **LEDGE_HOP_DOWN:** One-way tile that can be jumped down but not climbed up.
*   **LEDGE_HOP_LEFT:** One-way traversal. Can be jumped left but not entered from the right.
*   **LEDGE_HOP_RIGHT:** One-way traversal. Can be jumped right but not entered from the left.
*   **PIT:** One-way tile that causes a fall to the floor below.
*   **COUNTER/PC/MART_SHELF/BUOY/WHIRLPOOL:** Impassable obstacles. Interaction with some (PC, counter NPCs) requires standing on an adjacent tile.
*   **TREE:** Small trees can be cut with CUT, leaving an impassable stump.
*   **BOULDER:** Can be moved with STRENGTH.
*   **HEADBUTT_TREE:** Interactable tree for finding Pokémon.
*   **ROCK_SMASH_BOULDER:** Can be crushed with the move ROCK SMASH.

### B. Key Items & HM Usage
*   **SQUIRTBOTTLE:** Used to wake up the Sudowoodo blocking Route 36.
*   **HM01 (CUT):** Cuts small trees. Learned by Feraligatr.
*   **HM02 (FLY):** Allows instant travel to previously visited towns. Received from Chuck's wife in Cianwood City after defeating him.
*   **HM03 (SURF):** Allows travel over water. Learned by Feraligatr.
*   **HM04 (STRENGTH):** Moves large boulders. See puzzle methodology for usage.
*   **HM05 (FLASH):** Illuminates dark caves. Learned by Hoothoot.
*   **DIG:** Can be used to escape caves and some buildings, returning to the entrance. Disabled in Cianwood Gym.

### C. Other Systems
*   **Everstone:** A Pokémon holding this item will not evolve.
*   **Phone Calls:** NPCs can call to offer hints, battle rematches, or flavor text.
*   **Happiness:** Increased by haircuts and using items on Pokémon. Required for some evolutions (like Togepi).
*   **Day/Night Cycle:** Affects which Pokémon appear.
*   **Bug-Catching Contest:** Held on Tuesdays, Thursdays, and Saturdays in the National Park.

## III. Puzzle Solving Methodology

### A. The Scientific Method for Puzzles
1.  **Observe:** Carefully analyze the puzzle's initial state using the map, object data, and any relevant NPC dialogue.
2.  **Hypothesize:** Formulate a single, clear, and testable hypothesis about a specific mechanic.
3.  **Test:** Execute the simplest possible sequence of actions to test the hypothesis.
4.  **Conclude & Document:** Record the result of the test. Was the hypothesis confirmed or falsified? Update this notepad accordingly.
5.  **Strategically Mark:** Use map markers to track progress and prevent repeating failed tests.

### B. Automation First
*   For any recurring puzzle type (e.g., state-based mazes like boulder puzzles), my first step will be to define a custom tool to solve it computationally. Manual trial-and-error is my last resort. If a tool fails, my top priority is to fix it, not to abandon it.

### C. Cianwood Gym Boulder Puzzle (VERIFIED MECHANICS)
1.  **Strength Activation (Multi-Step Process):** To push a boulder, you must first be standing on a tile adjacent to it and facing it. Then, press 'A' to bring up the 'Want to use STRENGTH?' YES/NO prompt. Select 'YES' to activate the HM. This puts you in a temporary 'push mode' for a single push, confirmed by the message 'Boulders may now be moved!'.
2.  **The Push:** After confirmation, you must walk into the boulder to push it one tile. **CRITICAL: The player character MOVES INTO THE BOULDER'S PREVIOUS SPOT after a push.** The 'push mode' deactivates immediately, requiring the entire activation process to be repeated for the next push.
3.  **Puzzle Trigger:** Walking onto the tile at (8, 6) triggers the appearance of Black Belts who block paths, making the puzzle unsolvable. This tile must be avoided until the boulders are in their final positions.
4.  **Reset Mechanics:** The puzzle has two reset methods.
    *   **Boulder Reset:** Stepping on the tile at (4, 8) resets **only** the boulders to their initial positions.
    *   **Full Gym Reset:** Leaving the gym and re-entering resets **only** the spawned trainers, not the boulder positions.

## IV. Battle and Pokemon Information

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

### C. Pokémon Locations
*   **Route 29:** Sentret, Pidgey, Hoothoot
*   **Route 30:** Pidgey, Rattata, Caterpie, Metapod, Weedle, Kakuna, Ledyba
*   **Route 31:** Pidgey, Rattata, Bellsprout, Gastly, Hoppip
*   **Dark Cave:** Geodude, Zubat
*   **Sprout Tower:** Rattata, Gastly
*   **Union Cave:** Geodude, Zubat, Onix, Rattata, Sandshrew
*   **Ilex Forest:** Caterpie, Metapod, Weedle, Kakuna, Zubat, Paras, Oddish
*   **Route 34:** Rattata, Abra, Drowzee
*   **National Park:** Pidgey, Caterpie, Weedle, Sunkern, Nidoran♀, Nidoran♂
*   **Route 36:** Growlithe, Nidoran♀, Nidoran♂, Pidgey, Stantler
*   **Route 37:** Pidgey, Pidgeotto, Stantler
*   **Burned Tower:** Rattata, Koffing, Zubat
*   **Route 38:** Rattata, Raticate, Meowth, Magnemite, Farfetch'd, Tauros, Miltank
*   **Route 39:** Rattata, Raticate, Meowth, Magnemite, Farfetch'd, Tauros, Miltank
*   **Olivine Lighthouse:** Rattata, Gastly
*   **Route 40:** Tentacool, Krabby
*   **Route 41:** Tentacool, Tentacruel, Mantine
*   **Mt. Mortar:** Zubat, Geodude, Machop, Marill
*   **Lake of Rage:** Magikarp, Gyarados
*   **Route 43:** Pidgey, Pidgeotto, Flaaffy, Girafarig, Mareep, Natu, Sentret
*   **Route 42:** Mankey, Mareep, Flaaffy, Spearow, Fearow

### D. PC Storage
*   **Items:** BERRY (x1), PSNCUREBERRY (x1), ICE BERRY (x1), MINT BERRY (x1), BURNT BERRY (x1), GREAT BALL (x1), ANTIDOTE (x1), PARLYZ HEAL (x1), AWAKENING (x1), POTION (x1), GUARD SPEC. (x1), X ATTACK (x1), X DEFEND (x1), X SPEED (x1), X SPECIAL (x1), DIRE HIT (x1), POKE BALL (x1), REPEL (x1), ESCAPE ROPE (x1), ETHER (x1), MAX ETHER (x1), REVIVE (x1), NUGGET (x1), PROTEIN (x1), IRON (x1), CARBOS (x1), CALCIUM (x1), HP UP (x1), RARE CANDY (x1), TM39 (SWIFT), TM13 (SNORE), TM41 (THUNDERPUNCH), TM48 (FIRE PUNCH), TM02 (HEADBUTT), TM08 (ROCK SMASH), TM45 (ATTRACT), TM21 (FRUSTRATION), TM27 (RETURN), TM12 (SWEET SCENT), TM35 (SLEEP TALK), TM49 (FURY CUTTER).

## V. Strategy & Learnings

### A. Corrected Assumptions & Critical Lessons
*   **HM06 (Whirlpool) Hallucination:** I previously hallucinated receiving this HM. Its true location is unknown.
*   **Pathing Logic:** My pathfinder tools failed repeatedly because I was giving them incorrect traversable tile types. I must ensure the `traversable_tiles` argument accurately reflects my current movement state (walking or surfing).
*   **Cianwood Geography:** Cianwood City is split into two landmasses. The southern part where I initially arrived is an island. Progress to the northern part (where the gym is) requires using SURF.
*   **Mahogany Gym Block:** The gym is blocked by a Fisher. My hypothesis is that a trigger at the Lake of Rage will move him. An alternative hypothesis is the trigger is elsewhere, possibly related to Schoolboy Alan on Route 36.

## VI. Procedural Learnings & Hypotheses

### A. Procedural Discipline
*   **Immediate Action:** I have previously deferred tasks like tool fixing and marker updates. This is an invalid strategy. All data management and tool refinement must be performed immediately upon discovery.

## VIII. Active Plans

### A. Get Item from Schoolboy Alan (Route 36)
1. **Fly to Route 36:** Travel to Route 36.
2. **Speak to Alan:** Talk to Schoolboy Alan to receive the FIRE STONE.
*   **Agent Idea ('Pathing Advisor'):** Create an agent that analyzes pathing failures. If path_executor fails X times on the same route, the agent could suggest a new strategy (e.g., 'try one-step-at-a-time' or 'investigate if the route is blocked'). This would help break out of loops faster.