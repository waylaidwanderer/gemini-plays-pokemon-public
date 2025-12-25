# Suicune Strategy (Crystal Version)
- Mechanics Check: In Crystal, Suicune has fixed overworld sprite locations. After the Route 42 encounter, it moves to Tin Tower for a stationary battle.
- Encounter Sequence:
    1. Burned Tower: Trigger beasts to flee. (COMPLETED)
    2. Cianwood City: North end town. (COMPLETED)
    3. Route 42: Island in the middle. (COMPLETED)
    4. Tin Tower: Stationary battle with Clear Bell. (CURRENT)
- Battle Plan: Hypnosis -> weaken. Mean Look is not required as it's a stationary encounter.
- Team: GNEISS (Graveler) for tanking, XENON (Gastly) for Sleep.
- Note: Suicune is level 40. Moves: Rain Dance, Gust, Aurora Beam, Mist.
- Stagnation Plan: If progress stalls, verify access to central area via re-entry or upper floors.

# PC Storage (Box 1)
RICOTTA (RATICATE 16), CINNABAR (GOLDEEN 21), VORTEX (POLIWAG 22), INTERCEPT (YANMA 12), ROCKY (ONIX 6), EGG (CLEFFA 5), XFDW (MEOWTH 16), FRITTATA (TOGEPI 5), SHUCKIE (SHUCKLE 15), Blarney (SUDOWOODO 20).

# Training Plan (XENON)
- Target: Level 35-40. Location: Route 39 (near Moomoo Farm).

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- WATER: Walkable with Surf.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable; removable with Cut.
- TALL_GRASS: Walkable; wild encounters.
- CAVE/DOOR/WARP: Walkable; warp.
- LEDGE: One-way (hop down).
- COUNTER: Impassable; interact from adjacent tile.

# Tin Tower 1F Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- WARP_CARPET_DOWN: Exit warp.
- Trigger: Entering the map with the Clear Bell after defeating the Wise Trio.
- Wise Trio: Defeated.
- Central Area: Unreachable from floor level; completely walled off (y=4 to y=10, x=6 to x=13).
- Warp (10, 2): Identified as warp in XML; behavior unverified.

# Battle & Equipment History
- Amulet Coin: Equipped to XENON.
- Sage Lore: All Sages have shared their lore.
- Suicune: Stationary encounter in Crystal. Strategy: Hypnosis -> Weaken.

# Event Trigger Progress (Tin Tower Suicune)
- Condition: Defeat Wise Trio. (VERIFIED: COMPLETED)
- Condition: Talk to all 3 Sages on 1F in a single session.
    1. Sage ID 5 (5, 9): Talked (Turn 18963).
    2. Sage ID 6 (11, 11): Talked (Turn 18966).
    3. Sage ID 7 (14, 6): TARGET (Current).
- Attempt 2: Resetting map via exit/re-entry. (Failed)
- Observation: Central area (Suicune's Nest) is walled off. Entrance likely from above or hidden.
- Note: Stairs at (10, 2) are currently inactive (not listed in map warps).