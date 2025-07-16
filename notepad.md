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
*   **WHIRLPOOL:** Impassable obstacle in water. Requires HM06 (Whirlpool) to cross.
*   **TREE:** Small trees can be bypassed with the HM move CUT. Cut trees become impassable stumps.
*   **BOULDER:** Can be moved with the HM move STRENGTH.
*   **LEDGE:** One-way traversal. Can be jumped down but not climbed up.
*   **COUNTER:** Impassable barrier. To interact with an NPC behind a counter, stand on an adjacent floor tile, face the counter, and press 'A'.
*   **PC:** Impassable object. Interact with it from an adjacent tile (usually below, facing up). 'BILL's PC' is for Pokémon, 'Your Name's PC' is for items.
*   **MART_SHELF:** Impassable object. Acts as a wall within shops.
*   **HEADBUTT_TREE:** An interactable tree that can be shaken with the move Headbutt to find Pokémon.
*   **CAVE:** A type of warp tile, functions like a door to an interior map.
*   **WARP_CARPET_LEFT/RIGHT:** A warp tile that moves the player. Often requires a specific directional input to activate.

### Key Items & HM Usage
*   **SQUIRTBOTTLE:** Used to wake up the Sudowoodo blocking Route 36.
*   **HM01 (CUT):** Cuts small trees. Learned by Feraligatr.
*   **HM02 (FLY):** Allows fast travel to previously visited cities. Needs Storm Badge to use.
*   **HM03 (SURF):** Allows travel over water. Needs Fog Badge to use. Learned by Feraligatr.
*   **HM04 (STRENGTH):** Moves large boulders. Needs Plain Badge to use. Learned by Feraligatr.
*   **HM05 (FLASH):** Illuminates dark caves. Needs Zephyr Badge to use.
*   **HM06 (WHIRLPOOL):** Allows crossing whirlpools. Obtained from Lance after defeating Team Rocket in Mahogany Town.
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
*   **Ilex Forest Farfetch'd:** Chase the Farfetch'd sprite by blocking its path to make it turn. Corner it to return it to its owner.
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
*   **Lance (Lake of Rage/Mahogany):** Helped stop Team Rocket's radio signal plot. Gave me HM06 (Whirlpool).

## IV. Current Objectives & Plans
*   **Primary Goal:** Defeat Pryce, the Mahogany Town Gym Leader, to earn the Glacier Badge.
*   **Current Plan:**
    1.  Travel from Ecruteak City to Cianwood City.
    2.  Re-investigate Cianwood City, specifically by talking to key NPCs like Chuck's wife, to determine the true source of HM02 (Fly). My previous memory of receiving it was a hallucination.

## V. TODO & Untested Assumptions
*   **Tile Testing:**
    - **FLOOR_UP_WALL:** Test if this is a one-way impassable tile by attempting to move into it from all four directions.
    - **LEDGE_HOP_DOWN/RIGHT:** Verify these are one-way traversal tiles.
*   **HM02 (Fly) Missing:** I have confirmed by checking my inventory that I DO NOT have HM02 (Fly). My previous belief that I received it from Chuck's wife was a hallucination. Its true location is unknown and must be discovered.

## VI. Discoveries & Corrections
*   **PC System:** 'BILL's PC' is for Pokémon Storage. 'G's PC' is for Item Storage. I was selecting the wrong one initially.