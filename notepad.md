# Suicune Quest Log
- **Start Turn:** 24175 (2025-12-26 20:30)
- **Goal:** Trigger Suicune battle at Tin Tower 1F.
- **Sighting Requirements (Sequential in Crystal):**
  1. Burned Tower: Beasts fled. [Verified]
  2. Cianwood City (North): Sighting. [Verified]
  3. Route 42 (Central Island): Sighting check. [In Progress]
     - *Hypothesis 2:* Re-enter Route 42 from Ecruteak City (West side) to update flags. [Failed - Entered Turn 25051, searched island floor Turn 25056-25065. No sighting.]
  4. Route 36 (Sudowoodo junction): Sighting check. [Next Step]
  5. Tin Tower 1F: Battle Suicune with Clear Bell. [Pending]

# Failed Hypotheses & Troubleshooting
- **Hypothesis 1 (Eusine in Ecruteak PKMN Center):** Searched both floors Turn 25036-25043. Eusine is not present.
- **Hypothesis 2 (Re-enter Route 42 West):** Entered from Ecruteak side, searched entire island floor. No Suicune sighting triggered.
- **Suicune on Route 42 Island (Direct arrival):** Searched all floor tiles (Turn 25009). Suicune was not present. 

# Strategy: Route 36 Check
- If Route 42 sighting is not triggering, check if Suicune has already moved to Route 36. This would imply the Route 42 sighting was either completed previously or skipped by the game engine.
- Destination: Route 36 Sudowoodo junction (West of Violet City).

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