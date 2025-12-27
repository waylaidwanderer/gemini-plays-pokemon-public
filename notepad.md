# Suicune Quest Log
- **Goal:** Trigger Suicune battle at Tin Tower 1F.
- **Sighting Requirements (Sequential in Crystal):**
  1. Burned Tower: Beasts fled. [Verified]
  2. Cianwood City (North): Sighting. [Verified]
  3. Route 42 (Central Island): Sighting check. [In Progress]
     - *Hypothesis 1 (Eusine in Ecruteak PKMN Center):* [Failed - Turn 25036-25043]
     - *Hypothesis 2 (Re-enter Route 42 West):* [Failed - Turn 25051-25065]
     - *Hypothesis 4 (Mahogany Approach - East):* [Failed - Entered Turn 25081, searched island Turn 25101-25104. No sighting.]
  4. Route 36 (Sudowoodo junction): Sighting check. [Failed - Turn 25074]
  5. Tin Tower 1F: Battle Suicune with Clear Bell. [Pending]

# Strategy: Mahogany Approach
- Enter Route 42 from Mahogany Town (East side).
- Note: Central island requires CUT at (24, 13) to access sighting area.

# Tile Mechanics (Global)
- **FLOOR:** Traversable. Standard walking surface.
- **WALL:** Impassable. Boundary or obstacle.
- **WATER:** Traversable only with HM03 Surf.
- **TALL_GRASS:** Traversable. Triggers wild encounters.
- **HEADBUTT_TREE:** Impassable. Can be interacted with using Headbutt.
- **CUT_TREE:** Impassable. Removed using HM01 Cut. Regrows when the map is reloaded (e.g., after warping or flying).
- **FRUIT_TREE:** Impassable. Interact to obtain berries/apricorns.
- **WARP_CARPET:** Traversable. Triggers map transition/warp when walking "off" the map edge or onto the specific tile.
- **LEDGE:** One-way traversable (down/right/left as indicated). Hop over to descend.
- **DOOR/STAIRS/LADDER:** Traversable. Triggers map transition.
- **PC/COUNTER/SIGN:** Impassable. Interact from an adjacent tile.

# NPC Registry
- Route 36: Lass (50, 8), Fisher (44, 9).
- Route 42: Fisher Tully (25, 6), Hiker Benjamin (14, 10), Pokemaniac Shane (28, 11).

# PC Storage
- Box 1: BRIMSTONE, HELIODOR, COBALT, QUARTZ, DIVA, PENDULUM, JASPER, UNAKITE, EGG, AMETHYST, AZURITE, HEMATITE, KENYA, TOGEPI, LUCID, BELLADONNA, TRUFFLE, LAPIS.

# Lesson: Tree Cutting
- To use CUT, face the tree and press A. When prompted "Want to use CUT?", press A again (default is YES). Do NOT press Down, as that selects NO.
- Verified: CUT tree at (24, 13) on Route 42 cleared successfully Turn 24899.
- *Hypothesis 5 (Wise Trio Check):* [In Progress - Turn 25117] Consulting the Wise Trio to verify if the Suicune quest has progressed or if a sighting was missed.
- *Observation (Tin Tower Shook):* Turn 24187 - Sage mentioned the tower shook. This is a key indicator.

- *Observation (Tin Tower Shook):* Turn 25133 & 25137 - Sage mentioned the tower shook. Confirmed current turn event.
- *Verified Tile Mechanics:*
  - FLOOR: Verified traversable Turn 25141.
  - WALL: Verified impassable Turn 25141.
  - LADDER/WARP: Verified triggers transition upon entry Turn 25129.
- *Strategy (Suicune Encounter):* [Turn 25150] Heading to Tin Tower 1F via Ecruteak City (20, 2). Plan to lead with GNEISS (Lv44) for durability or KIMCHI (Lv21) for Sleep Powder.
- *Status:* "Tin Tower shook" event triggered. Wise Trio Room explored, no Sages found. Proceeding to tower base.
- *Observation (Wise Trio Room Empty):* [Turn 25151] Explored 64/64 tiles. No NPCs present. Sages must have moved after the Tin Tower shook.
- *Observation (Tin Tower Shook):* Turn 25133 & 25137 - Sage mentioned the tower shook. This usually indicates Suicune is present.
- *Navigation (Tin Tower Path):* [Turn 25159] Confirmed path from (20, 2) to (37, 7) is reachable within the restricted area: (20, 2) -> (29, 2) -> (29, 4) -> (33, 4) -> (33, 7) -> (34, 7) -> (34, 8) -> (35, 8) -> (35, 9) -> (37, 9) -> (37, 7).
- *Plan:* Proceeding to Tin Tower 1F to check for Suicune. Leading with KIMCHI (Lv21) for Sleep Powder. GNEISS (Lv44) and Calcifer (Lv45) are backup for durability.
- *Verified Tile Mechanics:*
  - FLOOR: Verified traversable Turn 25141.
  - WALL: Verified impassable Turn 25141.
  - LADDER/WARP: Verified triggers transition upon entry Turn 25129.
  - DOOR: Verified as targetable warp point at (37, 7).