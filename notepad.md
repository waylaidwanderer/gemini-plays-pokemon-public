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

# Navigation Note
- Path to (10, 15) from north was blocked by Sage at (5, 9). Must detour through column 4.
- Attempt 1 to trigger Suicune: Talking to all Sages. Outcome: Lore shared by 2/3. (IN PROGRESS - Final Sage at 5,9 speaking)
- Attempt 2 to trigger Suicune: Re-entering map. Outcome: No cutscene. (COMPLETED)
- Attempt 3: Accessing central area from 2F. (IN PROGRESS)

# Suicune Tracker Update
- Pokedex Confirmation: Suicune is in Ecruteak City. Entry explicitly states "SUICUNE'S NEST".
- Map Analysis: Central area of 1F (y=4 to y=10, x=6 to x=13) is walled off. Entrance likely from above or hidden.
- Plan: Head to 2F via stairs at (10, 2).

# Pre-Battle Checklist
- Current Ball Inventory: 23 Great Balls, 1 Ultra Ball.
- Status Inducer: XENON (Gastly) with Hypnosis.
- False Swipe: Not available. Using Night Shade (fixed damage) or Lick/Headbutt for chip damage.
- Saving: MUST save before interacting with Suicune.

# Hypothesis Testing Log (Tin Tower Suicune)
1. Hypothesis: Talking to Sages triggers the encounter.
   - Test: Talked to all 3 Sages on 1F.
   - Result: No encounter. Hypothesis denied.
2. Hypothesis: Re-entering the tower triggers the encounter.
   - Test: Exited and re-entered map.
   - Result: No encounter. Hypothesis denied.
3. Hypothesis: Access to central area (Suicune's Nest) is via 2F or hidden path.
   - Observation: 1F center is walled off.
   - Test: Heading to stairs at (10, 2). (Attempt 1, Turn 18950)