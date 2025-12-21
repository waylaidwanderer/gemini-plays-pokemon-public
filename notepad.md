# Goldenrod Radio Tower Takeover (Started Turn 8588)
## Strategy (HOW)
1. Floor-by-floor sweep (1F -> 4F accessible areas cleared).
2. Find the Director and Card Key in Goldenrod Underground.
3. Use Card Key on 3F (14, 2) to reach upper floors.
4. Defeat Rocket Executives and clear the tower.

## Tower Intel
- **Card Key Slot**: 3F (14, 2).
- **Shutters**: 3F (14, 2), 4F (11, 4), 5F (14, 3).
- **Directory**: 1F Reception, 2F Sales, 3F Personnel, 4F Production, 5F Director's Office.

## Underground Progress (Map 3_53)
- **Status**: Found the Basement Door at (18, 6). It is LOCKED (requires Basement Key).
- **Hypothesis**: Fake Director on 5F has Basement Key. Real Director in Basement has Card Key.
- **NPCs**: Super Nerds Donald/Teru/Eric (Defeated). Haircut Brother, Granny (Shopkeepers).
- **Warps**: Ladder (3, 2) -> North. Ladder (3, 34) -> South. Door (18, 6) -> Basement.

# Global Knowledge
## Tile Mechanics
- **FLOOR**: Standard traversable. Verified.
- **WALL**: Impassable. Verified.
- **COUNTER**: Impassable. Interact from front tile facing the counter. Verified.
- **WARP_CARPET_DOWN/UP/LEFT/RIGHT**: Map transition. Verified.
- **STAIRCASE/LADDER**: Warp points. Verified.
- **POKEBALL TILE**: Decoration (Radio Tower). Verified.
- **BOOKSHELF**: Impassable. Verified.

## Completed Badges
- Zephyr, Hive, Plain, Fog, Storm, Mineral, Glacier.

## Navigation & PC
- **Counter Interaction**: Face the counter, not the NPC.
- **Fly Map (Goldenrod)**: Discrete presses: 4 Ups, 6 Lefts from New Bark Town.
- **PC Storage**: SHUCKIE (Lv15), ROCKY (Lv6), EGG (Lv5), XFDW (Lv16), FRITTATA (Lv5).

## General Lessons Learned
- **Partitioned Layouts**: When a map is split (like Radio Tower 4F), look for alternate stairs on lower floors or Key Items (like Card Key) to open shutters.
- **Object Identity**: During events (like takeovers), NPCs may be replaced by different sprites (e.g., Receptionist replaced by Rocket Grunt). Always interact to verify.
- **Counter Interactions**: To talk to someone behind a counter, stand on the tile directly in front of the counter and face it.
- **Root Hypotheses**: If stuck, re-evaluate the base assumption. The fake Director likely has the Basement Key needed for the Underground.
- **Battle Menu Transitions**: Menu animations in Gen 2 take time. Custom tools that change menus must include at least 1000ms of sleep to ensure the sub-menu is active.

# Switch Room Puzzle (Map 3_54)
- Path to Switch Room: 3_53 (18, 6) Basement Door -> 3_53 (21, 31) -> 3_53 (22, 27) -> 3_54 (23, 3).
- Goal: Find switches 1, 2, and 3 to clear the path to the Warehouse.
- Rival Battle Strategy: Use Calcifer's level advantage. Use Headbutt (Neutral Physical) against Feraligatr to bypass its Fire resistance.