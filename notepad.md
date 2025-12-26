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
    - Strategy: Use Surf to reach island, use Cut to enter grove. Perform 100% tile coverage sweep.
    - Status: Island sweep complete (Turn 22782). No trigger.
    - Hypothesis: Trigger is on the water surrounding the island or the eastern path toward Mahogany Town.
- Sighting 4: Route 36 (Sudowoodo junction). Status: Locked until Sighting 3 is cleared.
- Sighting 5: Tin Tower 1F (Final Battle). Requires Clear Bell (Obtained).
- Battle Strategy: Level 40. Induce sleep (XENON/KIMCHI), weaken (GNEISS/Calcifer).

# PC Storage Inventory
- Box 1: RICOTTA (RATICATE), CINNABAR (GOLDEEN), VORTEX (POLIWAG), INTERCEPT (YANMA), ROCKY (ONIX), EGG (CLEFFA), XFDW (MEOWTH), FRITTATA (TOGEPI), SHUCKIE (SHUCKLE), Blarney (SUDOWOODO).

# Lessons Learned & Failures
- FLY Map Navigation: Attempted to move cursor with D-pad without success. FLY map cursor movement is not 1:1 with D-pad presses and may require specific logic or repeated inputs.
- Suicune Trigger Hypothesis (Route 42): Sighting 3 is triggered by approaching the central island area. Exhaustive island sweep failed. Next: Check water and eastern land path.

# Area Mechanics & Warps
## Ecruteak City (4_9)
- (20, 2): 🚪 To Wise Trio Room (7, 4)
- (37, 7): 🚪 To Tin Tower 1F (9, 15)
- (35, 26): 🚪 To Route 42 Gatehouse (0, 4)
- (18, 11): 🚪 To Tin Tower Gatehouse (4, 17)

## Route 42 (2_5)
- (0, 8/9): 🚪 To Ecruteak Gatehouse
- (10, 5): 🚪 To Mount Mortar 1F Outside (Western)
- (28, 9): 🚪 To Mount Mortar 1F (Central)
- (46, 7): 🚪 To Mount Mortar (Eastern)
- (27, 16): Apricorn Tree (GRN)
- (28, 16): Apricorn Tree (PNK)
- (29, 16): Apricorn Tree (YLW)
- (40, 10): ☠️ Fisher Tully
- (47, 8): ☠️ Pokemaniac Shane
- (49, 9): ☠️ Hiker Benjamin
- (4, 10), (7, 5), (45, 9), (54, 8): 🪧 Signs

## Route 36 (10_3)
- (35, 9): Sudowoodo junction. Sighting 4 location.
- "WEIRD_TREE" tiles (Sudowoodo) require Squirtbottle if blocking path.

## Violet City (10_5)
- (27, 23): Ledge gap. Allows passage north without hopping the ledge.

# Timestamps
- Suicune Hunt (Phase 3/4): Started Turn 22256.
- Island Sweep #2 (Exhaustive): Started Turn 22724. Ended Turn 22782. Result: No trigger.