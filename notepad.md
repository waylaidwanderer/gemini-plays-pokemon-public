# Global Tile Mechanics
- FLOOR: Traversable. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable via Surf. [Verified]
- HEADBUTT_TREE: Impassable. [Verified]
- CUT_TREE: Impassable. Requires HM01 Cut. [Verified]
- PC: Standard interaction. [Verified]
- COUNTER: Impassable. Interaction with NPCs behind them must be done from an adjacent tile. [Verified]
- WARP_CARPET: Traversable, triggers map transition. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into (e.g. LEDGE_HOP_DOWN blocks movement from the South). [Verified]
- FRUIT_TREE: Impassable. [Verified]
- DOOR: Traversable, triggers map transition. [Verified]
- TALL_GRASS: Traversable, triggers wild encounters. [Verified]

# Suicune Hunt (Crystal Version)
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood City (Complete)
- Sighting 3: Route 42 Central Island Grove.
    - Status: Verification failed. Systematic sweep (Turns 22580-22640) found no sprite.
    - Plan: Return to Route 42 for exhaustive search near Apricorn trees.
- Sighting 4: Route 36 (Sudowoodo junction at (35, 9)).
    - Status: Not found. Walked to junction, no sprite appeared.
    - Hypothesis: Route 42 sighting is mandatory and was not successfully triggered.
- Sighting 5: Tin Tower 1F (Final Battle). Requires Clear Bell (Obtained).
- Battle Strategy: Level 40. Induce sleep (XENON/KIMCHI), weaken (GNEISS/Calcifer).

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).

# Timestamps
- Suicune Hunt (Phase 3/4): Started Turn 22256.
- Route 42 Island Sweep: Started Turn 22580. Ended Turn 22640.
- Route 36 Verification: Started Turn 22665. Ended Turn 22681.
- Current Status: Returning to Route 42.

# Area Mechanics & Warps
## Ecruteak City (4_9)
- (20, 2): 🚪 To Wise Trio Room (7, 4)
- (37, 7): 🚪 To Tin Tower 1F (9, 15)
- (35, 26): 🚪 To Route 42 Gatehouse (0, 4)
- (18, 11): 🚪 To Tin Tower Gatehouse (4, 17)

## Wise Trio Room (4_2)
- (7, 4): 🚪 To Ecruteak City (20, 2)
- (1, 4): 🚪 To Tin Tower Gatehouse (17, 3)

## Tin Tower Gatehouse (4_3)
- (4, 17): 🚪 To Ecruteak City (18, 11)
- (17, 3): 🚪 To Wise Trio Room (1, 4)

## Tin Tower 1F (4_4)
- (9, 15): 🚪 To Ecruteak City (37, 7)

## Route 42
- Island entry via Cut at (24, 13). Trees at Y=13, 14, 16, 17 are impassable.
- (28, 16): Berry Tree (Empty at Turn 21678)
- (27, 16): Berry Tree (Turn 21682)
- Note: Preparation: Healing at Violet City PC complete. Gastly's Mean Look PP restored (5/5). Moving to Route 42.
- Island Sweep #2 (Exhaustive): Started Turn 22684. Objective: 100% tile coverage of the central island grove.