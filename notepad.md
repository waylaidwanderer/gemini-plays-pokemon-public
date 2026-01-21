# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Navigation Notes (Goldenrod - Map 3_54)
- **Location**: Goldenrod City (West Side).
- **Correction**: Previous attempt to find Main Road failed because I stayed too far Left (x=7). Main Road is likely at x=10-14.
- **Goal**: Exit Underground, go South to clear obstacles, go East to x=12, then NORTH.

### Key Locations
- **Flower Shop**: (19, 1). Needs Sudowoodo interaction.
- **Route 34 Exit**: South edge of map (Row 35).

### Quests
- **Sister's House**: (29, 5). The sister is missing (Route 36).
- **Route 35 Gatehouse**: Entering building at (9, 5) to investigate.
- **Previous Checks**: East (x=32) blocked by fence. West Tracks (x=3) blocked by wall/NPC.
- **Hypothesis**: This building is either the Gatehouse or the Underground Entrance.

### Status
- Badges: 3 (Zephyr, Hive, Plain).
- Party: Quilava (26), Sentret (2), Bellsprout (6), Togepi (5), Rattata (8).
- Route 34 Navigation: To reach the Daycare, travel North along the West path (main road) and enter the yard through the gap in the fence at (11, 15). Watch out for the Officer at (10, 16).
- Navigation Target: Check East edge (Col 32) for path North to Route 35.
- Pathing: Currently at (31, 8). Head East to Col 32, then North.
- Received Odd Egg (Turn 7045). Contains unknown Pokemon (fingers crossed for a shiny!).

### Quest Log: SquirtBottle
1. Talk to Flower Shop (Done).
2. Talk to Sister's House (Done). Clue: Sister went to Route 36 to see the wiggly tree.
3. Find Sister at Route 36.
- **System**: Python sandbox is down. Relying on manual navigation.
- Tile Mechanic: `TYPE_3fe2` in Goldenrod City (e.g. Row 3, Col 18) looks like a wall/roof but is walkable pavement. Trust the map data over visuals here.
- Navigation Plan: Head North to Row 10, then East through the gap at (26, 10) to reach the North-East area. The Route 35 Gatehouse should be there (visited previously around 29, 8).
- Correction: The summary indicates I've been to the Route 35 Gatehouse at (29, 8) before. I likely left to clear a party slot and got sidetracked.