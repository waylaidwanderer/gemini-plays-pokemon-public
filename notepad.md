# Global Tile Mechanics
- FLOOR: Traversable. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable via Surf (Ravioli). [Verified]
- HEADBUTT_TREE: Impassable. [Verified]
- CUT_TREE: Impassable. Requires HM01 Cut (KIMCHI). [Verified]
- PC: Standard interaction. [Verified]
- COUNTER: Impassable. Interaction with NPCs behind them must be done from an adjacent tile. [Verified]
- WARP_CARPET: Traversable, triggers map transition. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- FRUIT_TREE: Impassable. [Verified]
- DOOR: Traversable, triggers map transition. [Verified]
- TALL_GRASS: Traversable, triggers wild encounters. [Verified]

# Suicune Hunt (Crystal Version)
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood City (Complete)
- Sighting 3: Route 42 Central Island Grove.
    - Status: In Progress. Previous search (Turns 22580-22640) unsuccessful.
    - Strategy: Use Surf to reach island, use Cut to enter grove. Perform 100% tile coverage sweep.
- Sighting 4: Route 36 (Sudowoodo junction).
    - Status: Locked. Requires Sighting 3.
- Sighting 5: Tin Tower 1F (Final Battle). Requires Clear Bell (Obtained).
- Battle Strategy: Level 40. Induce sleep (XENON/KIMCHI), weaken (GNEISS/Calcifer).

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).

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
- Island entry via Cut at (24, 13).
- (28, 16): Berry Tree
- (27, 16): Berry Tree
## Violet City (10_5)
- (27, 23): Ledge gap. Allows passage north without hopping the ledge.

# Lessons Learned & Failures
- FLY Map Navigation (Turns 22696-22709): Attempted to move cursor with D-pad for 14 turns without success. FLY map cursor movement is not 1:1 with D-pad presses and may require specific logic or repeated inputs. Avoided for now by walking.
- Suicune Trigger Hypothesis (Route 42): Sighting 3 is triggered by approaching the central island grove with three Apricorn trees. Exhaustive sweep of the island is the current priority.

# Area Mechanics & Warps (Continued)
## Route 36 (10_3)
- (35, 9): Sudowoodo junction. Previously blocked by Sudowoodo. Sighting 4 location.
- "WEIRD_TREE" tiles are Sudowoodo-like sprites. Interaction requires Squirtbottle if they block the path. [Hypothesis]