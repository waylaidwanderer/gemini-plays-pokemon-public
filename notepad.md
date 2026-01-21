# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Navigation Notes (Goldenrod - Map 11_2)
- **Current Location**: Backtracking East from x=6.
- **Target**: North-East Corner (Row 0, Col 32+).
- **Correction**: The West side (x=6) at Row 8 is a dead end. The "Main Road" tracks are blocked by an NPC at (3, 16).
- **Hypothesis**: The Exit to Route 35 is in the North-East corner, past the Sister's House (x=29, y=5). Heatmap shows Row 0-1 there are unseen.

### Key Locations
- **Flower Shop**: (19, 1). Needs Sudowoodo interaction.
- **Gym**: (24, 7).
- **Sister's House**: (29, 5).

### Key Locations
- **Flower Shop**: (19, 1). Needs Sudowoodo interaction.
- **Route 34 Exit**: South edge of map (Row 35).

### Quests
- **Sister's House**: (29, 5). The sister is missing (Route 36).
- **Route 35 Gatehouse**: East Side (x=31) is a dead end.
- **New Lead**: Gap to West Corridor (x=16) found at Row 8.
- **Plan**: Exit Sister's House -> Go to Main Road (18, 8) -> Go West to x=16 -> Go North to Gatehouse.
- **Fact**: Sister is at Route 36 (Sudowoodo).

### Status
- Badges: 3 (Zephyr, Hive, Plain).
- Party: Quilava (26), Sentret (2), Bellsprout (6), Togepi (5), Rattata (8).
- Route 34 Navigation: To reach the Daycare, travel North along the West path (main road) and enter the yard through the gap in the fence at (11, 15). Watch out for the Officer at (10, 16).
- Navigation Target: Check East edge (Col 32) for path North to Route 35.

- Received Odd Egg (Turn 7045). Contains unknown Pokemon (fingers crossed for a shiny!).

### Quest Log: SquirtBottle
1. Talk to Flower Shop (Done).
2. Talk to Sister's House (Done). Clue: Sister went to Route 36 to see the wiggly tree.
3. Find Sister at Route 36.
- **System**: Python sandbox is down. Relying on manual navigation.
- Tile Mechanic: `TYPE_3fe2` in Goldenrod City (e.g. Row 3, Col 18) looks like a wall/roof but is walkable pavement. Trust the map data over visuals here.
- Navigation Plan: Go South to the Ilex Forest Gatehouse area (Row 41+). Look for a path to wrap around to the West side of the route.
- Task: Find Floria at Route 36.