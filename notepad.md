# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules
*   **WALL:** Impassable. Forms the boundaries of maps.
*   **FLOOR:** Standard traversable tile.
*   **LADDER:** A warp tile. Moves player between floors.
*   **WARP_PANEL:** A warp tile. Teleports the player to another location. Behavior seems to be one-way.
*   **DOOR:** A warp tile. Leads to other buildings/areas.
*   **GRASS/TALL_GRASS:** Traversable. Can trigger wild Pokémon encounters.
*   **WATER/SEA:** Traversable only with the HM move SURF. Can trigger wild Pokémon encounters.
*   **BUOY:** Impassable obstacle in water.
*   **WHIRLPOOL:** Impassable obstacle in water. Likely requires a specific HM.
*   **TREE:** Small trees can be bypassed with the HM move CUT. Cut trees become impassable stumps.
*   **BOULDER:** Can be moved with the HM move STRENGTH.
*   **LEDGE:** One-way traversal. Can be jumped down but not climbed up.

### Key Items & HM Usage
*   **SQUIRTBOTTLE:** Used to wake up the Sudowoodo blocking Route 36.
*   **HM01 (CUT):** Cuts small trees. Learned by Feraligatr.
*   **HM02 (FLY):** Allows fast travel to previously visited cities. Needs Storm Badge to use.
*   **HM03 (SURF):** Allows travel over water. Needs Fog Badge to use. Learned by Feraligatr.
*   **HM04 (STRENGTH):** Moves large boulders. Needs Plain Badge to use. Learned by Feraligatr.
*   **HM05 (FLASH):** Illuminates dark caves. Needs Zephyr Badge to use.
*   **DIG:** Can be used to escape caves and some buildings, returning to the entrance.

### Other Mechanics
*   **Everstone:** A Pokémon holding this item will not evolve.
*   **Phone Calls:** NPCs can call to offer hints, battle rematches, or flavor text.
*   **Happiness:** Increased by haircuts and using items on Pokémon. Required for some evolutions (like Togepi).
*   **Day/Night Cycle:** Affects which Pokémon appear.
*   **Bug-Catching Contest:** Held on Tuesdays, Thursdays, and Saturdays in the National Park.

## II. Puzzles & Solutions
*   **Sprout Tower:** Central pillar blocks direct ascent. Must go up the side ladders to the 3rd floor, then descend via the central ladder to reach the Elder.
*   **Azalea Gym:** A spiderweb platform puzzle. Switches reconfigure the platforms. The correct sequence is left switch, then right switch.
*   **Ilex Forest Farfetch'd:** Chase the Farfetch'd by stepping on twigs to make it turn. Corner it to return it to its owner.
*   **Goldenrod Gym:** A maze with trainers that appear and disappear. The path is a spiral shape resembling a Clefairy.
*   **Ecruteak Gym:** An invisible path puzzle. Many tiles are pitfalls that return you to the entrance. Requires careful trial and error to find the safe path to the Gym Leader.
*   **Cianwood Gym:** Defeated trainers become obstacles. A switch resets the puzzle. A boulder must be pushed with STRENGTH to clear the path.

## III. Important NPCs & Quests
*   **Professor Elm:** Gave me my starter and the Pokémon Egg. Main quest giver.
*   **Rival (SILVA):** My recurring rival. Stole a Pokémon from Prof. Elm.
*   **Kurt (Azalea Town):** Makes special Poké Balls from Apricorns. Key to the Slowpoke Well quest.
*   **Day-Care Man (Route 34):** Gave me the ODD EGG.
*   **Sick Miltank (Route 39):** Needs 'lots of BERRIES' to get better.
*   **Sick Ampharos (Olivine Lighthouse):** Needs SECRETMEDICINE from Cianwood City. Curing it is required for Jasmine to return to her gym.
*   **Lance (Lake of Rage/Mahogany):** Helps to stop Team Rocket's radio signal plot.

## IV. Current Plans & Hypotheses

### Team Rocket Hideout Puzzle
*   **Observation:** I am in the Team Rocket Hideout in Mahogany Town. The goal is to disable a radio signal. A locked door on B2F requires two passwords, which I have learned are 'SLOWPOKETAIL' and 'RATICATE TAIL'. The hideout has multiple floors and disconnected sections, connected by ladders and warp panels.
*   **Hypothesis 1 (Failed):** The locked door on B2F opens through direct interaction after learning the passwords. (Result: Interaction only yields generic text. No password prompt.)
*   **Hypothesis 2 (Current):** The main switch in the central camera room on B1F at (19, 11) is the primary trigger for the entire hideout. Activating it will disable security systems and open the boss's door.
*   **Test 2a (Complete):** Navigate to the switch at (19, 11) and interact with it. (Result: The switch was turned off.)
*   **Test 2b (Current Plan):** Return to the locked door on B2F at (14, 12) to see if it is now open or prompts for a password. If it remains locked, proceed to B3F to search for a new trigger, as the switch may have only disabled B1F systems.