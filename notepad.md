# Global Tile Mechanics
- FLOOR: Traversable. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable via Surf. [Verified]
- HEADBUTT_TREE: Impassable. [Verified]
- CUT_TREE: Impassable. [Verified]
- PC: Standard interaction. [Verified]
- COUNTER: Impassable. Interaction with NPCs behind them must be done from an adjacent tile. [Verified]
- WARP_CARPET: Traversable, triggers map transition. [Verified]
- LEDGE: One-way traversal (hop down/left/right). [Verified]

# Suicune Hunt (Crystal Version)
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood City (Complete)
- Sighting 3: Route 42 Central Island.
    - Status: Not triggered yet.
    - Strategy: Reach island (Surf/Cut). Suicune is a visible sprite at (10, 14) or similar - approach it to trigger the flee event.
- Sighting 4: Route 36 (Sudowoodo junction at (35, 9)).
- Sighting 5: Tin Tower 1F (Final Battle).
- Battle Strategy: Level 40. Induce sleep (XENON/KIMCHI), weaken (GNEISS/Calcifer).

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).

# Timestamps
- Suicune Hunt (Phase 3/4): Started Turn 22256.

# Area Mechanics & Warps
## Ecruteak City (4_9)
- (20, 2): 🚪 To Wise Trio Room (7, 4)
- (20, 3): 🚪 To Wise Trio Room (7, 5)
- (37, 7): 🚪 To Tin Tower 1F (9, 15)
- (35, 26): 🚪 To Route 42 Gatehouse (0, 4)
- (35, 27): 🚪 To Route 42 Gatehouse (0, 5)
- (18, 11): 🚪 To Tin Tower Gatehouse (4, 17)

## Wise Trio Room (4_2)
- (7, 4): 🚪 To Ecruteak City (20, 2)
- (7, 5): 🚪 To Ecruteak City (20, 3)
- (1, 4): 🚪 To Tin Tower Gatehouse (17, 3)

## Tin Tower Gatehouse (4_3)
- (4, 17): 🚪 To Ecruteak City (18, 11)
- (5, 17): 🚪 To Ecruteak City (18, 11)
- (17, 3): 🚪 To Wise Trio Room (1, 4)

## Tin Tower 1F (4_4)
- (9, 15): 🚪 To Ecruteak City (37, 7)

## Route 42
- Island entry via Cut at (24, 13). Trees at Y=13, 14, 16, 17 are impassable.
- (28, 16): Berry Tree (Empty at Turn 21678)
- (27, 16): Berry Tree (Turn 21682)

# Suicune Sighting 3 Details
- Location: Route 42, central island.
- Trigger: Suicune is a visible sprite on the island (approx X=26, Y=15). Approach it to trigger the flee event.
- Prerequisite: Must have Surf and Cut (Ravioli and KIMCHI have these).