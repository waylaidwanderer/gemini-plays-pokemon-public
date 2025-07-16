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

### Key Items & HM Usage
*   **SQUIRTBOTTLE:** Used to wake up the Sudowoodo blocking Route 36.
*   **HM01 (CUT):** Cuts small trees. Learned by Feraligatr.
*   **HM02 (FLY):** Allows fast travel. **LOCATION UNKNOWN.**
*   **HM03 (SURF):** Allows travel over water. Learned by Feraligatr.
*   **HM04 (STRENGTH):** Moves large boulders. Learned by Feraligatr.
*   **HM05 (FLASH):** Illuminates dark caves. Learned by Hoothoot.
*   **HM06 (WHIRLPOOL):** Allows crossing whirlpools. **LOCATION UNKNOWN.**
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
*   **Ecruteak Gym:** An invisible path puzzle. Requires careful trial and error to find the safe path to the Gym Leader.
*   **Cianwood Gym:** Defeated trainers become obstacles. A switch resets the puzzle. A boulder must be pushed with STRENGTH to clear the path.

## III. Important NPCs & Quests
*   **Professor Elm:** Gave me my starter and the Pokémon Egg. Main quest giver.
*   **Rival (SILVA):** My recurring rival. Stole a Pokémon from Prof. Elm.
*   **Kurt (Azalea Town):** Makes special Poké Balls from Apricorns.
*   **Day-Care Man (Route 34):** Gave me the ODD EGG.
*   **Sick Miltank (Route 39):** Needs 'lots of BERRIES' to get better.
*   **Sick Ampharos (Olivine Lighthouse):** Needs SECRETMEDICINE from Cianwood City.
*   **Lance (Lake of Rage/Mahogany):** Helped stop Team Rocket's radio signal plot. 

## IV. Current Objectives & Plans
*   **Current Plan:** My previous attempts to reach Mahogany Town via the eastern land route have failed. I am currently blocked. My new primary hypothesis is that the Fast Ship S.S. Aqua in Olivine City is now operational since I have restored power to the lighthouse. I will travel to the Olivine Port to investigate this possibility. If the ship is not running, I will reconsider exploring Mt. Mortar.

## V. Lessons Learned & Corrected Assumptions
*   **HM02 (Fly) Hallucination:** I hallucinated receiving HM02 from Chuck's wife in Cianwood City. I have confirmed by checking my inventory that I DO NOT have HM02 (Fly). Its true location is unknown.
*   **HM06 (Whirlpool) Hallucination:** I hallucinated receiving HM06 from Lance after defeating Team Rocket. I have confirmed by checking my TM/HM pocket that I DO NOT have HM06 (Whirlpool). Its true location is unknown and the Whirl Islands are currently inaccessible.
*   **Observational Failure & Tool Trust:** My `master_navigator` tool was correct about the buoy wall on Route 41. I must trust the output of my tools over my own visual assessment, as they process the raw game data directly.
*   **Movement Mechanics Update:** My hypothesis that defeated trainer sprites were passable was incorrect. I attempted to walk through a defeated swimmer on Route 41 and was blocked. **Defeated trainer sprites are IMPASSABLE obstacles.**
*   **Pathing Logic:** My `master_navigator` tool failed repeatedly because I was giving it incorrect traversable tile types for my current movement state (e.g., trying to walk on water). I must ensure the `traversable_tiles` argument accurately reflects whether I am walking or surfing.
*   **VOID:** An impassable boundary tile, functions like a WALL.
*   **WARP_CARPET_UP:** A warp tile that moves the player upwards, usually to enter a building.