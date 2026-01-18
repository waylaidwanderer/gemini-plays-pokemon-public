# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026 at 5:08 PM PST

### Current Objectives & Strategy
- **Main Quest**: Journey to Azalea Town.
- **Immediate Goal**: Head South to Route 32.
- **Status**: Leaving Violet City.
- **Location**: Route 32 (10_1).
- **Accomplishments**: Defeated Falkner (Zephyr Badge), Sprout Tower Cleared, Received Togepi Egg.
- **Next Steps**: Route 32 -> Union Cave.

### Violet City Information
- **Pokemon Center**: (31, 25) - Visited.
- **Poke Mart**: (10, 17) - Visited.
- **Gym**: (18, 16) - Falkner (Flying type).
- **Sprout Tower**: (23, 5).
- **School**: (30, 17).

### Contacts
- **Youngster Joey**: Route 30 (3, 28).

### Route 30/31 Recap
- Passed Cherrygrove City.
- Defeated Rival (Silver).
- Delivered Mystery Egg to Elm.
- Route 31 Lower Path was the key to Violet City.
- Dark Cave entrance at Route 31 (34, 5).

### Reflection (Turn 3164)
- **Status**: Stuck on Route 32 (Southbound).
- **Blockages**: West (Row 72), Center (Row 76), East (Row 86) all blocked by `TYPE_fea1`.
- **Hypothesis**: `TYPE_fea1` might be a ledge, or there is a crossover path I missed (e.g. at Row 74).
- **Action**: Running BFS to find the valid path.
### Tile Mechanics
- **TYPE_3fe2**: Walkable Ground.
- **TYPE_fed7**: Walkable Grass/Ledge Top.
- **TYPE_2889**: Tree/Wall (Impassable).
- **TYPE_80fc**: Bush (Solid Obstacle).
- **TYPE_c453**: Ledge (Jumpable South).
- **TYPE_fea1**: Blockage/Wall (Confirmed impassable at Rows 72, 76, 86).

### Planned Route to Union Cave (The Zig-Zag)
1. Go South to Row 74.
2. Cross East to X=10 (avoid Row 76 blockage).
3. Go South to Row 82.
4. Cross West to X=7 (via Row 82).
5. Go North to Row 77.
6. Cross West to X=4 (via Row 77).
7. Go South on X=4 to Union Cave.
- **Battle Note**: Cursor remembers last move (Ember/BR). To reuse Ember, just press 'A'. Blind navigation is risky due to wrapping.
### Boss Battle: Falkner
- **Status**: Defeated on Turn 2770.
- **Result**: Earned Zephyr Badge (Enables Flash) & TM31 (Mud-Slap).
- **Strategy**: Quilava's Ember was effective despite accuracy drops.
### Exploration Notes
- **Route 32**: Found Repel at (3, 30). Backtracking East to find a valid path South.
- **Route 32**: Defeated Camper Roland (3, 43) and Youngster Gordon (4, 60).
- **Route 32 Maze Solution**:
  - **East Side (Col 10-12)**: Blocked South at Row 86 (Wall).
  - **Middle (Col 6-9)**: Blocked South at Row 76 (Bushes/Wall).
  - **West Side (Col 4)**: Open path South to Union Cave.
  - **The Path**: Go North to Row 74, cross Left to Col 7, go North to Row 71, cross Left to Col 4, then head South.
- **Blocked Paths**: Row 86 (East), Row 76 (Middle), Row 78 (Col 9 Wall), Row 83 (Col 5 Wall).

- **Miracle Seed**: Obtained from NPC on Route 32 (Turn 2861).
- **Recent Catch**: Zubat "Jet" (Box 1).
- **Key Items**: Obtained Old Rod from Fishing Guru in Route 32 Pokemon Center.