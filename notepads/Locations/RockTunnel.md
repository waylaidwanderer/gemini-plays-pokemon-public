# Rock Tunnel Geographical Records (Map 0_82) (Updated Turn 23479)

## Socratic Challenge (The Impassable Floor Contradiction) Answer:
- In Mt. Moon B2F, TYPE_2770 is the primary passable cavern floor. However, on Rock Tunnel 1F, we attempted to step onto (4, 22) (labeled TYPE_2770) and collided (0 tiles visited), concluding that TYPE_2770 is impassable. 
- *Physical Contradiction Explained*: The tile type ID itself does not change its collision properties dynamically. In Gen 1, collision is determined by the tileset's collision byte map. If TYPE_2770 is passable in Mt. Moon, it must share the same tile index or metatile index in the cavern tileset. 
- Wait, are Mt. Moon and Rock Tunnel using the exact same cavern tileset? Yes, both use the "cave" tileset.
- However, our collision at Rock Tunnel 1F (4, 22) was not because of TYPE_2770 itself. Let's look closer at (4, 22) on 1F: row 22 is the southern boundary wall on 1F! The tile at (4, 22) is visually a wall or part of the border. But why was it labeled TYPE_2770? The overlay labels are based on automated tile type classification which might map visually distinct cavern border tiles to the same index (such as a solid black tile or cave wall corner that has a different collision bit).
- Specifically, the border tile of the cavern tileset is a solid block, which is impassable. Thus, (4, 22) is part of the solid cave border/wall, causing direct collision. The collision rule is consistent because the tile ID under the hood for that specific wall/border tile has the impassable bit set.

## Socratic Challenge (Southeast B1F Sweep) Answer:
- In Locations/RockTunnel (line 123), we documented a plan to systematically sweep B1F Columns 34-37 on Rows 30-33 to search for a new ladder or exit.
- *Physical Execution Verification*: We actually did NOT physically execute this 4x4 grid sweep yet! We only walked along Row 33 (from Column 37 to Column 2 on Turn 21591-21625) and tested Columns 2-4 on Rows 31-33 (the bottom-left quadrant). We completely skipped sweeping the rest of Columns 34-37 on Rows 30-32!
- Therefore, the true exit ladder (Ladder 4 in vanilla Rock Tunnel, which leads to 1F bottom-right exit) could very likely be hiding in this unexplored southeastern quadrant of B1F!
- We are currently standing at (33, 15) and will immediately head to (33, 30) and sweep Columns 34-37 on Rows 30-33 systematically!

## Overview & Major Connections:
- **1F Entrance/Exit**: Connects to Route 10 at (15, 3) (verified on Turn 20628). Map Marker '🚪' placed at (15, 3).
- **Ladders**:
  - Ladder A: Located at (17, 11) on 1F (visually observed but blocked from the western starting chamber).

---

## Rock Tunnel 1F Layout & Discoveries:
- **Chamber 1 (Western Starting Area)**:
  - Bounded on the West by Column 13.
  - Rows 4-7 are passable corridors extending East from Column 14 to at least Column 28.
- **Solid Wall Barriers**:
  - Column 18-19 has a continuous solid rock wall (TYPE_2889) extending from Row 8 to at least Row 15, blocking direct South movement on those columns.
  - Rows 14 and 15 form a completely solid horizontal barrier of rock across Columns 18-33.
  - Column 17 is blocked at Rows 8 and 9 by TYPE_2889 solid rock, isolating the Western Chamber from the (17, 11) ladder.
- **Eastern Corridor (Rows 10-13)**:
  - Connects to the western chamber and Pokémaniac's area.
  - Extends East from Column 20 to at least Column 33 as a wide, open corridor.

---

## Rock Tunnel B1F Layout & Discoveries (Updated Turn 23041):
- **Chamber 1 (B1F Starting Chamber)**:
  - Bounded on the North by Row 21 (solid wall TYPE_2889).
  - Bounded on the East by Column 38 (solid wall TYPE_2889).
  - Bounded on the West by Columns 26-27 (continuous solid rock wall TYPE_2889 extending from Row 21 to Row 30).
  - The ladder to 1F is located at (33, 25).
  - Passages: The main exploration route leads South (beyond Row 29) on Columns 28-34. Exploration of the West-facing passage is blocked at Row 30 by the extension of the solid Column 26-27 rock wall, but we have successfully bypassed this wall at Row 31 (X=26, Y=31) (verified on Turn 20872).
- **Southern B1F Corridor (Rows 30-33, Columns 2-37)**:
  - Discovered on Turn 21591-21592.
  - Bounded on the North by Row 29 (solid rock TYPE_2889) for Columns 2-13 and 21-27. Column 14 at Row 29 is potentially passable (TYPE_3fe2).
  - Bounded on the South by Row 34 (solid rock TYPE_2770/TYPE_2889) for all columns 2-37.
  - Bounded on the West by Column 1 (solid rock TYPE_2889) for Rows 29-35.
  - This forms a wide, 4-tile-tall horizontal corridor (Rows 30-33) extending from the eastern Starting Chamber (Column 37) all the way West to Column 2 (completely mapped on Turn 21626).
- **Western Connecting Passage (Rows 24-29, Columns 14-20)**:
  - Discovered and physically verified on Turns 21665-21685.
  - Connects the Southern Corridor (Rows 30-33) to the Western Bypass Corridor (Columns 20-25).
  - Specific path:
    - Column 14, Row 28 is blocked by the defeated Jr. Trainer ♀ sprite.
    - However, Column 15 is fully open and passable on Rows 24-29, allowing complete bypass of the trainer blockage!
    - At Row 24, Columns 14-20 are completely open (TYPE_3fe2), connecting directly to Column 20 (Western Bypass Corridor).
  - This provides a secondary, fully open pathway connecting the Southern B1F corridor directly to the upper B1F areas and the eastern starting chamber!
- **Upper Bypass Corridor (Proven Connection)**:
  - Verified on Turn 21081 via the Systematic Upper Connection Testing Protocol.
  - Rows 18 and 19 form a completely open, passable corridor extending from Column 20 to at least Column 29.
  - This corridor runs directly over the top of the solid Column 26-27 rock wall (which ends at Row 20).
  - It connects the Western vertical/horizontal bypass corridor (Columns 20-25, Rows 21-25) directly to the Eastern starting chamber's Column 29 boundary.
  - This is a verified loop-free corridor, allowing direct, unobstructed travel between the starting chamber and the far western regions of B1F!

## B1F Systematic Layout Tracking & Exploration Protocol:
- **Intersection Tracking**: Every branching path will be logged by its coordinate (X, Y) with all available directions.
- **Loop Identification**: We will cross-reference newly reached coordinates against our existing logs. If a coordinate is already logged, we classify it as a circular loop. If not, it is a new path.
- **Notepad Management Milestone**: Upon reaching the next ladder on B1F or exiting to Lavender Town, we will unload "Locations/Route9" and "Locations/Route10" to maintain a clean notepad environment and prevent hitting the 10-loaded-notepad limit.

---

## Trainer Battles Database (Updated Turn 21239):
### Rock Tunnel 1F:
1. **Pokémaniac (Turn 20677)**:
   - Location: (22, 8) on 1F.
   - Opponent: CUBONE Lv 23 (Ground).
   - Strategy: Switched SPARKY immediately to GEMMY (Wartortle) Lv 31.
   - Result: Defeated!

2. **Hiker (Turn 21239)**:
   - Location: (5, 17) on 1F (walks south to intercept player at 5, 18).
   - Dialogue: "Hmm. Maybe I'm lost in here..."
   - Opponent: ONIX Lv 20, ONIX Lv 20, GEODUDE Lv 20.
   - Strategy: Lead with GEMMY (Wartortle) Lv 32, use WATER GUN (4x super-effective).
   - Result: Defeated on Turn 21251!

3. **Hiker (Turn 21295)**:
   - Location: (16, 14) on 1F (intercepts player at 16, 15).
   - Dialogue: "Outsiders like you need to show me some respect!"
   - Opponent: GEODUDE Lv 21, GRAVELER Lv 21.
   - Strategy: Lead with GEMMY (Wartortle) Lv 33, use WATER GUN (4x super-effective).
   - Result: Defeated on Turn 21310!

### Rock Tunnel B1F:
2. **Pokémaniac / Jr. Trainer ♀ Sofia (Turn 20872)**:
   - Location: (26, 31) on B1F.
   - Dialogue: "I draw POKéMON when I'm home."
   - Opponent: SLOWPOKE Lv 25 (Water/Psychic).
   - Strategy: Lead with SPARKY (Pikachu) Lv 23, switch to GEMMY (Wartortle) Lv 31.
   - Result: Defeated on Turn 20925! GEMMY finished Slowpoke with a critical hit BITE.

3. **Jr. Trainer ♀ (Turn 20976)**:
   - Location: (16, 28) on B1F (walks east to intercept player at 17, 28).
   - Dialogue: "I don't often come here, but I will fight you."
   - Opponent: ODDISH Lv 22, BULBASAUR Lv 22.
   - Strategy: Lead with GEMMY (Wartortle) Lv 31, use BITE to defeat.
   - Result: Defeated on Turn 20989! GEMMY gained EXP and remains in perfect health.

4. **Pokémaniac (Turn 21028)**:
   - Location: (20, 21) on B1F (walks east to intercept player at 24, 21).
   - Dialogue: "Do you know about costume players?"
   - Opponent: CHARMANDER Lv 22, CUBONE Lv 22.
   - Strategy: Lead with GEMMY (Wartortle) Lv 32, use WATER GUN (super-effective) to defeat.
   - Result: Defeated on Turn 21038! GEMMY leveled up to 32 and learned no new moves.

5. **Hiker (Turn 21137)**:
   - Location: (35, 5) on B1F (walks east to intercept player at 36, 5).
   - Dialogue: "Hit me with your best shot!"
   - Opponent: MACHOP Lv 20, ONIX Lv 20.
   - Strategy: Lead with GEMMY (Wartortle) Lv 32. Use BITE on Machop and WATER GUN (4x super-effective) on Onix.
   - Result: Defeated on Turn 21147! Got ¥700.

---

## Wild Encounters Database:
- **Scientific Tracking Methodology (Established Turn 20858)**:
  - We log every wild encounter inside Rock Tunnel here.

| Species | Levels | Encounter Count | Matchup Strategy | Notes & Verification |
|---------|--------|-----------------|------------------|----------------------|
| ZUBAT   | 15,17,18| 4               | Thundershock/Run | Turn 20733 (Lv17), Turn 20784 (Lv18), Turn 21107 (Lv17), Turn 21281 (Lv15) |
| GEODUDE | 17     | 2               | Run              | Turn 21331 (Lv17), Turn 21412 (Lv17)                                         |
| MACHOP  | 15     | 4               | Run              | Turn 21349 (Lv15), Turn 21361 (Lv15), Turn 21407 (Lv15), Turn 21451 (Lv15)   |

### Southeast B1F Exploration Plan & Socratic Answer (Turn 21807):
- **Socratic Question 1 (Southeast Exploration Protocol)**: Upon backtracking to Ladder A at (33, 25), we will systematically explore the unmapped Southeast area of B1F (specifically Columns 34-37 on Rows 30-33) to search for a new ladder or exit.
  - **Exploration Path**:
    1. From (33, 25), walk South on Column 33 to (33, 30).
    2. Walk East to (37, 30) to test Columns 34-37.
    3. Walk Down Column 37 to Y=33, and then walk West back to Column 33 to sweep the entire 4x4 grid (Columns 34-37, Rows 30-33).
    4. If a ladder or passage is discovered, we will log its exact coordinates and place a map marker immediately.

### B1F Middle-Right Corridor Verified Layout & Discoveries (Resolved Turn 22081):
- **Empirical Status**: Fully Resolved!
- **Verified Corridor**: Rows 10-13 on Columns 26-37 form a wide, completely open, passable corridor (TYPE_3fe2).
- **Vertical Connection**: There is a wide vertical gap on Columns 32-35 across Rows 14 and 15 connecting this upper corridor directly to the lower area (Rows 16-17 on Columns 26-35).
- **Obstacles**:
  - Row 14 & 15 form a completely solid rock barrier (TYPE_2770, TYPE_2889) across Columns 26-31.
  - Column 30 has a Hiker at (30, 12) who walks down to (30, 13) to intercept. He was successfully defeated on Turn 22049.

6. Hiker (Turn 22042):
   - Location: (30, 12) on B1F (walked down to intercept player at 30, 13).
   - Dialogue: "My POKéMON techniques will leave you crying!"
   - Opponent: GEODUDE Lv 25.
   - Strategy: Lead with GEMMY (Wartortle) Lv 33, use WATER GUN (4x super-effective).
   - Result: Defeated on Turn 22049! Received money and registered map marker '☠️' at (30, 12).

### Socratic Question (The Middle Corridor Connection & 4th Ladder) - Resolved Turn 22085:
- **Socratic Question**: Does this middle-right corridor connect directly to the middle-left corridor (Columns 17-23, Rows 10-13) to form a single continuous East-West highway across B1F? If so, where is the 4th ladder (leading to the south-east exit area of 1F)?
- **Empirical Status**: Fully Resolved!
- **Direct Connection Finding**:
  - Columns 24 and 25 on Rows 9-15 are completely solid rock walls (TYPE_2889/TYPE_2770), dividing the eastern Middle-Right Corridor from the western Middle-Left Corridor on these rows.
  - However, Columns 24 and 25 on Rows 16 and 17 are completely open and passable (TYPE_3fe2), forming a direct horizontal connection between the eastern and western sides of B1F!
- **Connecting Path**: From (26, 13), we can walk East to (32, 13), Down to (32, 16), West to (23, 16), and Up to B1F Ladder C at (23, 11). However, Row 16 has a solid wall blockage at Column 18-19, meaning the eastern Middle-Right zone is completely isolated from the western system on Rows 16-17.
- **The 4th Ladder Search**:
  - Since the Middle-Right Corridor (Rows 10-13) and its vertical connector (Columns 32-35) connect to B1F Row 16, let's explore if there's a 4th ladder along this connection.
  - **B1F Rows 16-17 Corridor (Columns 14-37) - Resolved Turn 22174**:
    - **Verification**: Fully verified that Rows 16-17 from Column 14 to Column 37 form a wide open, passable corridor (TYPE_3fe2) with a solid blockage at Column 18-19.
    - **The 4th Ladder Finding**: Visually and physically verified that no ladder exists at (37, 17) or any other Column 32-37 coordinate on Rows 16-17 on B1F.
    - **East-West Blockage**: Physically proved on Turn 22203 that Column 18-19 is completely blocked on Row 16 by solid rock wall TYPE_2889. Therefore, B1F Rows 16-17 do not form a direct, continuous horizontal connection across the entire map, and the eastern Middle-Right zone remains isolated from the western system on Row 16.

### Transition Protocol to Lavender Town (Overwatch Alignment):
- **Objective**: Prevent context bloat and ensure high-efficiency database management.
- **Trigger**: Upon exiting Rock Tunnel onto Route 10 South / Lavender Town.
- **Step-by-Step Procedure**:
  1. **Unload Completed Notepads**: Unload the following 5 notepads immediately:
     - `Locations/RockTunnel`
     - `Locations/Route10`
     - `Scratchpad/RockTunnel_Pathfinding`
     - `Scratchpad/Route9_Route10_RockTunnel_Strategy`
     - `Mechanics/PikachuTrainingAndGrindingPlan` (or save its core strategy to Main/Archive and unload)
  2. **Initialize Lavender Town Database**: Create and load:
     - `Locations/LavenderTown_PointsOfInterest` (for verified POIs/NPCs/buildings)
     - `Scratchpad/LavenderTown_Exploration` (for live exploration notes)
  3. **Employ Regional Database Agent**: Call the custom `regional_database_agent` to systematically parse and compress all raw exploration logs, landmark coordinates, and points of interest for Lavender Town, Route 10 South, and surrounding areas to prevent context memory bloat.
  4. **Establish Strategic Map Markers**: Define markers for the Lavender Pokémon Center, Pokémon Tower, and Volunteer House.