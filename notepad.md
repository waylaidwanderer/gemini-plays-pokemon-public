# Suicune Strategy (Crystal Version)
- Mechanics Check: Suicune is a stationary overworld encounter at Tin Tower 1F.
- Prerequisites & Verification:
    1. Burned Tower flee event. (COMPLETED)
    2. Cianwood City encounter (North end). (COMPLETED)
    3. Route 42 encounter (Middle island). (STATUS: UNVERIFIED - MUST CHECK)
    4. Defeat Wise Trio at Tin Tower Entrance. (COMPLETED)
    5. Possess Clear Bell. (COMPLETED: In Key Items)
- Current Status: Pokedex shows Suicune in Ecruteak City.
- Encounter Trigger: If prerequisites are met, Suicune stands in the center of Tin Tower 1F. If it's missing, a prerequisite is likely incomplete.
- Battle Plan: Hypnosis (XENON) -> Weaken (Night Shade/Lick/Headbutt).
- Team: XENON (Gastly 21), GNEISS (Graveler 44).

# Tin Tower Investigation Strategy
- Goal: Determine why Suicune is not appearing on 1F.
- Step 1: Verify Route 42 encounter. (Action: Check Pokedex status and use tracker agent).
- Step 2: Search Ecruteak City Pokemon Center (23, 27) for Eusine.
- Step 3: Search Tin Tower Entrance (3_3) for Eusine or missed Wise Trio dialogue.
- Step 4: If still missing, re-explore Route 42 island.

# PC Storage (Box 1)
RICOTTA (RATICATE 16), CINNABAR (GOLDEEN 21), VORTEX (POLIWAG 22), INTERCEPT (YANMA 12), ROCKY (ONIX 6), EGG (CLEFFA 5), XFDW (MEOWTH 16), FRITTATA (TOGEPI 5), SHUCKIE (SHUCKLE 15), Blarney (SUDOWOODO 20).

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- WATER: Walkable with Surf.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable; removable with Cut.
- TALL_GRASS: Walkable.
- CAVE/DOOR/WARP: Walkable; warp.
- LEDGE: One-way (hop down).
- COUNTER: Impassable; interact from adjacent tile.

# Tool & Agent Usage
- suicune_tracker_v2: Use to verify milestone completion.
- check_map_area: Use to scan for Eusine/Sages in buildings.
- find_path_v2: Use for overworld navigation.