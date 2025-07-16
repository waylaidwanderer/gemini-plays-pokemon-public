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
*   **COUNTER:** Impassable. Acts as a barrier, often with an NPC behind it.
*   **PC:** Impassable object. Interact with it from an adjacent tile (usually below, facing up).
*   **MART_SHELF:** Impassable object. Acts as a wall within shops.
*   **HEADBUTT_TREE:** An interactable tree that can be shaken with the move Headbutt to find Pokémon.
*   **CAVE:** A type of warp tile, functions like a door to an interior map.
*   **WARP_CARPET_LEFT:** A warp tile that moves the player. Often requires a specific directional input (e.g., 'Down') to activate.

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
*   **Lance (Lake of Rage/Mahogany):** Helped stop Team Rocket's radio signal plot. Gave me HM06 (Whirlpool).

## IV. Current Objectives & Plans
*   **Primary Goal:** Defeat Pryce, the Mahogany Town Gym Leader, to earn the Glacier Badge.
*   **Current Obstacle:** A Fisher is blocking the gym entrance at (6, 14). All leads in Mahogany Town have been exhausted.
*   **Hypothesis 1:** The trigger is exploring the Whirl Islands. This requires catching a Pokémon that can learn Fly.
*   **Hypothesis 2 (Alternative):** The trigger is healing the sick Miltank on Route 39. This would require gathering berries.
*   **Current Plan:** Travel to Mahogany Town to heal and buy Poké Balls. Return to Route 42 to catch a flying-type Pokémon. Once I can fly, I will test Hypothesis 2 by flying to Route 39 and healing the Miltank before attempting Hypothesis 1.

## V. Failed Hypotheses & Corrected Misconceptions
*   **Mahogany Gym Blockade:** The trigger for the Fisher to move is NOT defeating Team Rocket or talking to any of the local NPCs post-Team-Rocket.
*   **RAGECANDYBAR:** The Mahogany Town 'shop' is a front for Team Rocket and does not sell any items. The RAGECANDYBAR cannot be purchased to move the Fisher.
*   **FLOOR_UP_WALL:** A one-way impassable tile. Appears to be the top of a ledge, cannot be traversed from below.

## VI. Glitched Encounters
*   **Route 42 Glitch:** While surfing on Route 42, I was pulled into a glitched battle on an unknown map (ID: 242_255). My party, Pokedex, and money were all corrupted. The opponent was a glitched, pink, unicorn-like Pokémon.
*   **WARP_CARPET_RIGHT:** (Hypothesis) A warp tile that likely moves the player right when activated.
*   **LEDGE_HOP_DOWN:** (Hypothesis) A one-way traversal tile, allowing movement down but not up.
*   **LEDGE_HOP_RIGHT:** (Hypothesis) A one-way traversal tile, allowing movement right but not left.

### Tasks
*   Fix the `master_navigator` tool. It fails on simple indoor paths and must be debugged.