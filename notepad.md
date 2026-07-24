<h1><code>Main</code></h1>

# Pokémon Blue - Crystal Palette Swap Mod Playthrough

## Verified Map Coordinates & Layouts
- Detailed coordinate files are organized in the `Locations/` directory.
- Refer to `Locations/PalletTown_And_Route1` for Pallet Town and Route 1 layouts.
- Refer to `Locations/ViridianCity` for Viridian City layouts.

## Rules & Learnings
- **mgba.get_coordinates() Warning:** Returns `{'x': 0, 'y': 0}` in some emulator/harness states. Do NOT trust it for spatial tracking in scripts. Use the injected `GameStateInformation` coordinate report in the system prompt instead.
- **Map Transition Verification:** Always verify map transitions visually (checking surrounding objects/NPCs) and by watching for the `SYSTEM NOTE: Map Transition Detected` injection, rather than assuming a movement was successful.

<hr>

<h1><code>Locations/PalletTown_And_Route1</code></h1>

# Pallet Town & Route 1 - Map Coordinates & Layouts

## Player's House - Bedroom (2F)
- **PC Location:** (0, 1) - Keyboard is at (0, 1), Monitor at (0, 0).
  - Standing at (0, 2) facing Up or (1, 1) facing Left lets you access it.
  - Contains **1x Potion** (Withdrawn).
- **Staircase (to 1F):** (7, 1)
  - **Mechanic / Collision:** Walking Up from (7, 2) to (7, 1) is blocked. To warp downstairs, you must enter from the Left: (6, 1) -> (7, 1).

## Player's House - Living Room (1F)
- **Staircase (to 2F):** (7, 1)
- **Front Door Exit:** (2, 7) (door mat).
  - Walking Down from (2, 7) exits to Pallet Town.
  - (3, 7) is a wall/blocked at the bottom (y=8 is wall).
- **Table / Chairs:** In the middle-right area.
- **Mom:** Sitting at the table.

## Pallet Town (Overworld)
- **Red's House Door:** (5, 5). Exiting Red's house spawns the player at (5, 6) facing Down.
- **Oak's Lab Door:** (12, 11). Exiting Oak's Lab spawns the player at (12, 12) facing Down.
- **Route 1 Entrance:** Tall Grass starts at (10, 1) and (11, 1).
  - Attempting to step onto (10, 1) or (11, 1) triggers Professor Oak's event.
  - Fences line the north boundary from x=4 to x=9 at y=1, blocking direct passage north except through the tall grass gap at x=10-11.

## Route 1
- **Bottom Entrance (from Pallet Town):** (10, 35) and (11, 35).
- **Northern Entrance (from Viridian City):** (10, 0) and (11, 0).
- **Tree Line at y=13:** Blocks x=10-13.
  - *Bypass/Gap:* Walk through x=8 (left corridor, clear ground) or x=14 (right corridor).
- **Ledge at y=5:** One-way ledge (jumpable going south). Blocks x=4-13.
  - *Bypass/Gap:* Walk through clear right-side corridor at columns 14 to 17.
- **Ledge at y=19:** One-way ledge (jumpable going south).
- **Tree Line at y=23:** Blocks x=5-11.
  - *Bypass/Gap:* Walk through tall grass corridor at x=12 and x=13.
- **Ledge at y=27:** One-way ledge (jumpable going south).
- **Grey Fence Stones at y=32:** Blocks x=5-9 and x=12-17.
  - *Bypass/Gap:* Walk through tall grass corridor at x=10 and x=11 (this is the only entrance/exit to/from Pallet Town).
- **Northern Segment Layout (near Viridian City exit):**
  - **Fences:** Row 1 has solid gray fence stones from x=3 to x=9, and x=12 to x=18 (blocking direct passage north except through the gap).
  - **Clear Path:** Columns 10 and 11 are clear ground (gray with vertical dots) from row 0 to row 4, forming the main north-south road to/from Viridian City.
  - **Decorative Lawn:** Columns 5 to 9 and 12 to 15 on rows 2 and 3 contain checkered green decorative lawn, which has a 0% encounter rate. The actual tall grass (leafy texture) only starts at row 6.

## Daisy's House (Blue's House)
- **Daisy's House Door (Pallet Town):** (13, 5). Exiting Daisy's house spawns the player at (13, 6) facing Down.
- **Inside Daisy's House Layout:**
  - **Daisy:** Sits at (2, 3) behind a table.
  - **Table with Book/Map:** Located at (3, 3).
  - **Player standing position to talk to Daisy:** Standing at (2, 4) facing Up.
  - **Exit Warp/Door Mats:** (2, 7) and (3, 7). Walking Down from (2, 7) or (3, 7) warps you back to Pallet Town.

<hr>

<h1><code>Locations/ViridianCity</code></h1>

# Viridian City - Locations & Landmarks

## Overworld
- **Southern Entrance (from Route 1):** (20, 35) and (21, 35).
- **Ledge at y=27:** Blocks upward passage across the main entrance road.
  - **Walkable Gap:** (19, 27) is a grassy/dirt opening. Walking through (19, 28) -> (19, 27) -> (19, 26) lets the player bypass the ledge and head north.
- **Pokémon Center Entrance:** (23, 25).
  - Exiting spawns the player at (23, 26) facing Down.
- **Poké Mart Entrance:** (29, 19).
  - Exiting spawns the player at (29, 20) facing Down.
  - Triggers OAK's PARCEL quest upon entry.

## Pokémon Center (Inside)
- **Nurse Joy:** Behind the counter at (3, 2).
  - Counter is at (3, 3).
  - Talking to her from (3, 4) facing Up heals the party to full health.
- **NPC Girl:** Sits on the left side of the room.
  - Sits at (0, 4) behind a desk.
  - Standing at (1, 4) facing Left and talking to her gives dialogue about Pokémon Centers.
- **Exit Door:** at (3, 7) and (4, 7). Walking Down from (3, 7) exits back to Viridian City at (23, 26).

## Poké Mart (Inside)
- **Clerk:** Sits at (0, 5) behind the counter.
- **Counter:** Located at (1, 5).
- **Player standing position to buy/sell:** Standing at (2, 5) facing Left.
- **Exit Door:** at (3, 7) and (4, 7). Walking Down from (3, 7) exits back to Viridian City at (29, 20).

## Western Boundary & Cliff Barrier
- **Cliff Barrier:** A solid, vertical checkered brown cliff barrier runs at column 3, blocking access to the west (columns 0, 1, 2) from the main city.
  - **Checkered Cliff Tiles (Blocked):** (3, 19), (3, 20), (3, 21), (3, 22), (3, 23), (3, 24).
  - **Diagonal Cliff Transition (Blocked):** (3, 18).
- **Walkable Gap / Route 22 Path:**
  - **Clear Ground Opening:** (3, 16) and (3, 17) are clear ground (unblocked), allowing the player to walk Left from column 4 to columns 0, 1, 2 (the path to Route 22).
  - **Coordinates:** Walking Left through (4, 16) -> (3, 16) -> (2, 16) -> (1, 16) -> (0, 16) leads directly to Route 22.

## Northern Boundary & Route 2 Exit (Row 1)
- **Fence Obstruction:** (19, 1) has a decorative fence that blocks straight upward movement on column 19.
- **Clear Bypass (Column 18):** Column 18 is completely clear. Walking through (19, 2) -> (18, 2) -> (18, 1) -> (18, 0) allows the player to bypass the fence and exit north to Route 2.

<hr>

<h1><code>Progression_And_Party_Stats</code></h1>

# Progression & Party Stats

## Key Progression Milestones
- **Pokédex:** Obtained from Professor Oak in Oak's Pokémon Lab on Turn 128.
- **Town Map:** Obtained from Daisy in Daisy's House on Turn 137.
- **Caught First Companion:** Caught NIBBLES (Rattata, Level 3) on Route 1 on Turn 318.
- **Caught Second Companion:** Caught GUSTY (Pidgey, Level 3) on Route 1 on Turn 350.
- **Caught Third Companion:** Caught TESLA (Pikachu, Level 3) in Viridian Forest on Turn 894.
- **Caught Fourth Companion:** Caught TRUFFLE (Paras, Level 10) on Mt. Moon B1F on Turn 1482.
- **Defeated Gym Junior Trainer:** Defeated Pewter Gym Junior Trainer on Turn 979.
- **Defeated Gym Leader Brock:** Defeated Pewter Gym Leader Brock on Turn 1024, obtaining the BOULDERBADGE and TM34 (Bide).
- **Pewter Poké Mart Shopping:** Purchased Poké Balls, Potions, and Antidote on Turn 1033.
- **Route 3 Entrance:** Entered Route 3 on Turn 1041.
- **Defeated Youngster Calvin:** Defeated Youngster Calvin on Turn 1325.
- **Defeated Lass Sally:** Defeated Lass Sally on Turn 1348.
- **Healed at Mt. Moon Pokémon Center:** Healed party at (11, 5) on Turn 1422.
- **Entered Mt. Moon:** Entered Mt. Moon 1F at (18, 5) on Turn 1431.
- **Defeated Team Rocket Grunt:** Defeated Team Rocket Grunt at (15, 24) on Turn 1529, earning ¥330.
- **Obtained HP UP:** Found HP UP at (25, 21) on Turn 1554.
- **Defeated Lass (North-East):** Defeated Lass at (30, 7) on Turn 1641, earning ¥165.
- **Defeated Team Rocket Grunt:** Defeated Team Rocket Grunt at (29, 11) on Mt. Moon B2F on Turn 1716, earning ¥360.
- **Obtained Item (Poké Ball):** Found and retrieved Poké Ball at (29, 5) on Mt. Moon B2F on Turn 1722.
- **Defeated Youngster (North-West):** Defeated Youngster at (12, 16) on Mt. Moon 1F on Turn 1779, earning ¥150.
- **Obtained Item (Moon Stone):** Found and retrieved Moon Stone at (2, 2) on Mt. Moon 1F on Turn 1881.
- **Defeated Bug Catcher Kenton:** Defeated Bug Catcher Kenton at (7, 22) on Turn 2031, earning ¥110.
- **Obtained Item (Potion):** Found and retrieved Potion at (2, 20) on Mt. Moon 1F on Turn 2068.
- **Discovered Direct Cavern Crossing:** Verified that row 27 is completely open across column 16 and columns 22-23 on Turn 2335, and columns 20-21 are completely open vertically on Turn 2297, providing a direct route to the eastern cavern.

## Party Statistics
- **SHELLBY (Wartortle):**
  - **Level:** 19
  - **Moveset:** Tackle (31/35 PP), Tail Whip (30/30 PP), Bubble (29/30 PP), Water Gun (25/25 PP)
  - **HP:** 50 / 54
  - **Status:** Healthy
- **TRUFFLE (Paras):**
  - **Level:** 11
  - **Moveset:** Scratch (35/35 PP)
  - **Stats:** Attack 24, Defense 17, Speed 13, Special 18
  - **HP:** 30 / 30
  - **Status:** Healthy
- **TESLA (Pikachu):**
  - **Level:** 8
  - **Moveset:** ThunderShock (28/30 PP), Growl (40/40 PP)
  - **Stats:** Attack 12, Defense 10, Speed 19, Special 12
  - **HP:** 22 / 24
  - **Status:** Healthy
- **GUSTY (Pidgey):**
  - **Level:** 5
  - **Moveset:** Gust, Sand-Attack
  - **HP:** 19 / 19
  - **Status:** Healthy
- **NIBBLES (Rattata):**
  - **Level:** 7
  - **Moveset:** Tackle, Tail Whip, Quick Attack
  - **HP:** 22 / 22
  - **Status:** Healthy

## Inventory
- **Poké Balls:** 6 (used 1 to catch TRUFFLE on Turn 1482)
- **Potion:** 1 (used on TRUFFLE on Turn 1671, found 1 at (2, 20) on Mt. Moon 1F on Turn 2068)
- **Antidote:** 2 (found 1 on Turn 576, purchased 1 at Pewter Poké Mart on Turn 1036)
- **HP UP:** 1 (found on Turn 1554)
- **Moon Stone:** 1 (found on Turn 1881)
- **TM01 (Mega Punch):** 1 (found in inventory on Turn 1878)
- **TM12 (Water Gun):** 1 (found at (5, 32) on Mt. Moon 1F on Turn 2018)

<hr>

<h1><code>Mechanics/Search_Scripting_Pitfalls</code></h1>

# Search Scripting Pitfalls

## Turn 79 Baseline Drift Pitfall
- **Description:** When running navigation scripts, if you execute a sequence of movements and then a reset sequence without first verifying that the initial movements were successful (e.g. they weren't blocked by a wall, NPC, or wild battle), the actual position of the player will drift from the expected position.
- **Prevention:** Always verify that each step or sequence of steps succeeded (checking GameState coordinates and screen visual) before continuing or executing corrective/reset steps.

<hr>

<h1><code>Locations/Route22</code></h1>

# Route 22 - Locations & Landmarks

## Layout & Landmarks
- **Eastern Entrance (from Viridian City):** (39, 8) (warp/transition spawn point).
- **Tall Grass Area:** Row 6 and Row 7 have tall grass starting from x=36 to x=44 (and possibly more).

## Wild Encounter Investigations (Turn 303)
- **Empirical Test:** Paced for 68 steps inside Route 22's tall grass (x=36 to 44, y=6 to 7) on Turn 221-230.
- **Result:** 0 wild encounters triggered.
- **Conclusion/Hypothesis:** Wild encounters on Route 22 may be disabled or extremely rare at this stage of the game, or the pacing test did not successfully change coordinates on every step (unverified coordinate-by-coordinate traversal). To verify this properly, future tests must explicitly log coordinate changes on each step. 

<hr>

<h1><code>Mechanics/Naming_Screen_Offset</code></h1>

# Naming Screen Column Offset Mechanic

## Discovery & Explanation
- In the nickname naming screen, there is a visual shift in the rendering of the letter grid. The letters and symbols are shifted to the right by exactly one column relative to the game ROM's internal cursor mapping.
- This creates a consistent 1-column horizontal offset between where the cursor visually points and what character is actually entered when "A" is pressed.
- **Rule:** The character entered is always the one situated exactly **one column to the right** of the cursor's visual position.

## Accurate Mapping & Selector Table
- To select a character at **Visual Column Y**, the player must place the cursor at **Visual Column Y-1** (which corresponds to internal Column Y-1):
  - **Visual Column 1** ('A', 'J', 'S', 'x', '-', 'lower'): Place cursor at **Column 0** (the empty column on the far left).
  - **Visual Column 2** ('B', 'K', 'T', '(', '?', 'case'): Place cursor at **Column 1** (pointing at 'A'/'J'/'S').
  - **Visual Column 3** ('C', 'L', 'U', ')', '!'): Place cursor at **Column 2** (pointing at 'B'/'K'/'T').
  - **Visual Column 4** ('D', 'M', 'V', ':', '♂'): Place cursor at **Column 3** (pointing at 'C'/'L'/'U').
  - **Visual Column 5** ('E', 'N', 'W', ';', '♀'): Place cursor at **Column 4** (pointing at 'D'/'M'/'V').
  - **Visual Column 6** ('F', 'O', 'X', '[', '/'): Place cursor at **Column 5** (pointing at 'E'/'N'/'W').
  - **Visual Column 7** ('G', 'P', 'Y', ']', '.'): Place cursor at **Column 6** (pointing at 'F'/'O'/'X').
  - **Visual Column 8** ('H', 'Q', 'Z', 'PK', ','): Place cursor at **Column 7** (pointing at 'G'/'P'/'Y').
  - **Visual Column 9** ('I', 'R', 'MN', 'END'): Place cursor at **Column 8** (pointing at 'H'/'Q'/'Z' / between ',' and 'END').

## Important Navigation & Wrap-Around Mechanics
- **Horizontal Wrapping:** Row 2 and Row 4 wrap around when you press "Left" at Column 1 ('S' or '-') or "Right" at Column 8 ('Z' or 'END').
- Wrapping left from Column 1 moves the cursor to Column 8.
- Wrapping right from Column 8 moves the cursor to Column 1.
- **B Button:** Universal backspace. Deletes the last character without moving the cursor.

<hr>

<h1><code>Locations/Route2</code></h1>

# Route 2 - Locations & Landmarks

## Overworld Layout
- **Southern Entrance (from Viridian City):** Player transitions to Route 2 at (8, 71) or (8, 72).
- **Clearing / Paths:**
  - Column 8 and 9 are clear paths.
  - Tall Grass starts at Column 10 to 13 on the right side.
- **Left Side Boundary:** Solid row of trees starts at Column 6.

## Ledge Barrier & Walkable Gap (Row 61)
- **Ledge Blockages:** Row 61 has a horizontal ledge blocking Columns 2-6 and Columns 8-11.
- **Walkable Gap / Ramp:** (7, 61) is a visually distinct, solid brown tile that is completely walkable. Standing at (7, 62) and walking Up to (7, 61) allows the player to bypass the ledge and access the northern area of Route 2.
- **Pavement Road Above Ledge:** Starts at y=58 and y=59 across columns 4-9.

## Viridian Forest Southern Gatehouse (Warp Building)
- **Southern Entrance (from Route 2 south):** Door is at (3, 43) on Route 2. Entering warps the player inside the gatehouse at (4, 7) facing Up.
- **Inside Gatehouse Layout:**
  - **Exits:** Southern door mat is at (4, 7) and (5, 7). Northern door is at (5, 0).
  - **NPCs:** Girl with blue hair on the right, wandering NPC on the left.
- **Northern Exit (to Viridian Forest):** Walking Up through the doorway at (5, 0) inside the gatehouse warps the player to Viridian Forest at (17, 47) facing Up.

## Northern Segment (Above Viridian Forest)
- **Northern Gatehouse Exit:** Exiting the Northern Gatehouse north puts the player on Route 2 at (3, 11).
- **Pewter City Boundary:** Route 2 north transitions to Pewter City at (8, 0) or (9, 0) going north.
- **Layout & Walkable Path:**
  - **West Side / Center (Columns 3 to 7):** Contains tall grass with wild encounters from row 3 up to row 11.
  - **East Side (Columns 8 and 9):** A completely clear pavement road going straight north to Pewter City. Pavement terrain has a 0% encounter rate by design in the game engine.
  - **Transitioning to Safe Path:** Standing at the Northern Gatehouse exit at (3, 11), walk up to (3, 7), then walk Right to column 8. There is no fence or ledge blocking access from the grass to column 8, allowing the player to safely walk up to Pewter City.

<hr>

<h1><code>Locations/ViridianForest</code></h1>

# Viridian Forest - Locations & Landmarks

## Overworld Layout
- **Southern Entrance (from Route 2 Gatehouse):** Player transitions to Viridian Forest at (17, 47) facing Up.
- **Entry Area:**
  - **Signpost 1:** Located at (18, 45).
  - **Wandering NPC:** Near (16, 43) (friendly, says "I came here with some friends! They're out for Pokémon fights!").

## Path Branches & Layout Topology (Verified Turn 448-481)
- **Central Clear Corridor:**
  - Columns 16 & 17 are clear green grass from row 33 to row 39.
- **Winding Left Path (West Side) - Dead End/Ledge Boundary:**
  - **Horizontal Connector:** Rows 30 & 31 have a clear horizontal corridor from columns 2 to 6.
  - **Vertical Connector:** Columns 6 & 7 form a clear vertical corridor from row 30 to row 36.
  - **Column 1 Dead-End Pocket:** (1, 30) is a 1x1 pocket blocked by trees on the Left (0, 30 is tree stump), Up (1, 29 is tree), and Down (1, 31 is tree).
  - **Left Edge Ledge Barrier:** The far-left path is blocked for northward traversal by a one-way ledge facing down.
  - **Item (Poké Ball):** Visible at (12, 29) on an upper ledge, currently inaccessible from the south.
- **East Path (Main Progression Route):**
  - **Entrance to East Path:** Walk Right from (17, 41) through columns 18 to 22 (dense tall grass area, rows 40-41) to reach the eastern segment of the forest.
  - **Tree Stump Barrier:** (24, 40) has a tree stump blocking direct access at row 40. Walk via row 41.
  - **Friendly NPC:** Sits at (27, 40) facing Left. (Says: "I ran out of POKé BALLs to catch POKéMON with! You should carry extras!")

## Defeated Trainers
- **Bug Catcher Rick:** Sits at (30, 33) originally, engaged at (26, 33) on Turn 488-510.
  - **Roster:** Weedle (Lv 6), Caterpie (Lv 6)
  - **Reward:** ¥60
- **Bug Catcher at (30, 19):** Engaged at (26, 19) on Turn 527-561.
  - **Roster:** Weedle (Lv 7), Kakuna (Lv 7), Weedle (Lv 7)
  - **Reward:** ¥70
- **Signpost at (26, 17):** Identified on Turn 527.
- **Tall Grass Corridor (East Segment):** Columns 25, 26, 27 form a 3-tile wide path going north from row 40 up to at least row 24, filled completely with tall grass.

## Northern Forest Layout (Verified Turn 574-603)
- **Top-Right Corner Pathway:**
  - Column 25/26 forms a clear vertical corridor from row 18 up to row 8.
  - Row 8 is clear from column 24 to column 30.
  - Columns 31 & 32 form a clear vertical corridor going north from row 8 up to row 1.
- **Top-Horizontal Corridor:**
  - Row 1 & 2 form a clear horizontal corridor going west from column 32 to column 16.
- **Tree Canopy Barriers:**
  - Column 15 forms a solid vertical barrier of tree canopies on rows 0-15, blocking direct leftward movement.
  - Column 14 is also blocked on rows 1-15.
- **Crossover/Opening to West Side:**
  - Row 16 & 17 on columns 14 & 15 are clear grass, allowing passage from the central corridor (columns 16/17) to the west corridor (columns 12/13).
- **Items & Landmarks:**
  - **Antidote:** Located at (25, 11) (collected on Turn 576).


## West Side Layout & Crossovers (Verified Turn 604-620)
- **Top-West Pocket Corridor:**
  - Columns 6, 7, 8 form a clear vertical corridor running from row 5 down to row 24.
  - The doormat pattern at (7, 5) was verified to be **non-warping** (regular walkable terrain).
- **Crossover Corridor (Row 24/25):**
  - Standing at (7, 24), the player can walk Left to columns 4 and 5 (which are clear grass on rows 22-25, bypassing row 21 and above which are tree canopies).
  - To bypass the blocked fence/stump at (4, 24), walk via row 25: Left to (5, 24), Down to (5, 25), Left to (4, 25) -> (3, 25).
- **Western Vertical Corridor:**
  - Columns 1, 2, 3 form a clear vertical corridor of clear grass going north from row 25.
  - This corridor provides a completely safe, non-grass (0% encounter) route north to the northern exit area.


<hr>

<h1><code>Locations/PewterCity</code></h1>

# Pewter City - Locations & Landmarks

## Overworld Layout
- **Southern Entrance (from Route 2):** Player transitions to Pewter City at (18, 35) or (19, 35) facing Up.
- **Main South Road:** Columns 18 and 19 are a clear pavement road going north from row 35.

## Pokémon Center
- **Exterior Location:** Entrance Door is at (13, 25) in Pewter City. "POKé" sign is at (14, 25).
- **Inside Layout:** Matches the Viridian City Pokémon Center exactly.
  - Nurse Joy is behind the counter at (3, 2).
  - Standing at (3, 4) facing Up and interacting heals the party.
  - Exit door mats are at (3, 7) and (4, 7).

## Poké Mart
- **Exterior Location:** Entrance Door is at (23, 17) in Pewter City. "MART" sign is at (24, 17).
- **Inside Layout:** Matches the Viridian City Poké Mart exactly.
  - Clerk is behind the counter at (0, 5).
  - Standing at (2, 5) facing Left to shop.
  - Exit door mats are at (3, 7) and (4, 7).

## Pewter City Gym
- **Exterior Location:** Entrance Door is at (16, 17) in Pewter City. "GYM" sign is at (15, 16).

## Newly Discovered Topography & Boundaries (Turns 937-948)
- **Pewter City Gym Building Footprint:** Occupies columns 12-17, rows 14-17.
  - Roof at row 14 and 15 (columns 12-17) is solid and blocked.
  - Walls and windows at row 16 and 17 (columns 12-15, 17) are blocked.
  - Entrance Door is at (16, 17) (door mat/access is at (16, 18)).
- **Ledge Barrier at Row 21:**
  - A horizontal one-way ledge facing down runs at row 21 across the city, blocking northward passage.
  - **Walkable Gap / Ramp:** Column 19 is a completely clear pavement street that allows safe northward/southward passage across row 21.
- **Column 18 Post Fence:**
  - Column 18 contains solid wooden posts at rows 18-21, blocking direct horizontal transit between the main street (column 19) and the Gym area (columns 12-17).
  - (18, 17) is clear turf, allowing horizontal passage north of the posts.
- **Column 11 Fence:**
  - Column 11 contains a solid fence at rows 16 and 17, blocking direct downward transit to row 18 on that column.
- **Column 10 Safe North-South Path:**
  - Column 10 is completely clear of fences and tree canopies. It serves as the primary north-south connector on the west side of the Gym, running between row 13 and row 18.
- **Optimal Gym Navigation Path (From South to Gym Door):**
  1. Walk north along column 19 (the main street) to row 13.
  2. Walk Left along row 13 to column 10 (10, 13).
  3. Walk Down column 10 to row 18 (10, 18).
  4. Walk Right along row 18 to column 16 (16, 18).
  5. Walk Up into the Gym door at (16, 17).

<hr>

<h1><code>Locations/Route3</code></h1>

# Route 3 - Locations & Landmarks

## Overworld Layout & Navigation
- **Western Entrance (from Pewter City):** Player transitions from Pewter City (39, 18) to Route 3 at (0, 10) facing Right.
- **Initial Segment Tall Grass Corridor (Rows 8 to 11):**
  - **Tall Grass:** Columns 2 to at least 11 contain tall grass on rows 8 to 11.
  - **Obstacles:** 
    - Stone posts are located at (4, 8) and (4, 11).
    - Trees are located at (9, 10) and (9, 11), blocking direct horizontal movement on rows 10 and 11.
  - **Bypass for Trees:** Walk north to row 8 or 9 (which are tall grass) to bypass the trees on column 9 and continue going east.
- **Ledges:** 
  - Row 7 has a horizontal one-way ledge facing down, blocking northward movement.
  - Row 12 has a horizontal ledge.

- **Ledge Barrier at Row 11 / Access to Eastern Area:**
  - **Ledge Blockage:** Row 11 has a horizontal ledge blocking Columns 10-14 and Columns 16-19.
  - **Tree Blockage:** Column 17 contains a solid vertical row of trees from row 6 to row 11, blocking direct horizontal transit on rows 8-10.
  - **Walkable Gap / Ramp:** (15, 11) is a completely clear, walkable dirt ramp. Walking through (15, 9) -> (15, 10) -> (15, 11) -> (15, 12) allows the player to bypass the ledge and access the clear path going east on row 12.
- **Ledge Barrier at Row 7 / Access to Upper Road:**
  - **Ledge Blockage:** Row 7 has a horizontal ledge blocking Columns 10 and Columns 12-20.
  - **Walkable Gap / Ramp:** (11, 7) is a completely clear, walkable dirt ramp. Standing at (11, 8) and walking Up to (11, 7) lets the player access the upper road of Route 3!

- **Eastern Obstacles and Stairs (Columns 20-25):**
  - **Forest Barrier (Column 23):** Column 23 contains a solid vertical line of trees from row 8 to row 13, blocking direct eastward passage.
  - **Tree blockages on Columns 24-27:** Forest/trees extend eastwards on rows 10-13, forming a solid block.
  - **Cliff Face (Row 14):** A solid brown checkered cliff runs horizontally on row 14 across columns 14 to 24, blocking downward transit.
  - **Walkable Staircase (Column 25):** (25, 14), (25, 15), and (25, 16) is a walkable staircase that cuts through the cliff face, allowing vertical transit.
  - **Upper Road Eastward Path:** Accessible by walking east along the upper road (rows 5-6) which bypasses the trees and ledges completely.

## Landmarks & Buildings
- **Mt. Moon Pokémon Center:** Entrance Door is at (11, 5) on Route 3. "POKé" sign is at (12, 5). Warps inside at (3, 7).
- **Mt. Moon Cave Entrance:** Cave mouth is at (18, 5) on Route 3. Walking into (18, 5) warps the player inside Mt. Moon 1F at (14, 35).

## Trainers & Defeated Status
- **Lass Janice:** Sits at (16, 9) originally, engaged at (15, 9) on Turn 1057.
  - **Roster:** Pidgey (Lv 9), Pidgey (Lv 9)
  - **Status:** Defeated on Turn 1094.
  - **Reward:** ¥135
- **Bug Catcher Greg:** Sits at (10, 6) facing Right. Engaged at (11, 6) on Turn 1124.
  - **Roster:** Caterpie (Lv 10), Weedle (Lv 10), Caterpie (Lv 10)
  - **Status:** Defeated on Turn 1161.
  - **Reward:** ¥100
- **Youngster Ben:** Sits at (14, 4) originally, walked to (14, 5). Engaged at (14, 6) on Turn 1166.
  - **Roster:** Rattata (Lv 11), Ekans (Lv 11)
  - **Status:** Defeated on Turn 1184.
  - **Reward:** ¥165
- **Bug Catcher James:** Sits at (19, 5) originally. Engaged at (18, 5) on Turn 1248.
  - **Roster:** Weedle (Lv 9), Kakuna (Lv 9), Caterpie (Lv 9), Metapod (Lv 9)
  - **Status:** Defeated on Turn 1271.
  - **Reward:** ¥90
- **Lass Robin:** Sits at (20, 4) originally. Engaged at (19, 4) on Turn 1278.
  - **Roster:** Rattata (Lv 10), Nidoran♂ (Lv 10)
  - **Status:** Defeated on Turn 1289.
  - **Reward:** ¥150
- **Bug Catcher Colbert:** Sits at (24, 6) originally. Engaged at (24, 5) on Turn 1301.
  - **Roster:** Caterpie (Lv 11), Metapod (Lv 11)
  - **Status:** Defeated on Turn 1311.
  - **Reward:** ¥110
- **Youngster Calvin:** Sits at (22, 9) originally. Engaged at (22, 8) on Turn 1319.
  - **Roster:** Spearow (Lv 14)
  - **Status:** Defeated on Turn 1325.
  - **Reward:** ¥210
- **Lass Sally:** Sits at (33, 10) originally. Engaged at (33, 8) on Turn 1341.
  - **Roster:** Jigglypuff (Lv 14)
  - **Status:** Defeated on Turn 1348.
  - **Reward:** ¥210

<hr>

<h1><code>Mechanics/UI_And_Border_Rendering</code></h1>

# UI and Border Rendering Mechanics

## Numeric Display Frame Border Quirk (Gen 1)
- **Description:** In numeric displays rendered near the right edge of the screen (such as the Poké Mart shop MONEY window), the vertical border of the frame is drawn using a tile that visually resembles a small, bold digit "1".
- **Visual Appearance:** On the far right of the MONEY window, column 19 on row 0 or row 1 contains this border tile. It renders directly to the right of the actual numbers, which can easily be misread as an extra digit "1" at the end of the money amount.
- **Rule/Verification:** Always ignore the rightmost vertical line in the MONEY display box when reading quantities. For example, if the screen displays "401" followed by the border "1", the actual amount of money is **¥401**, NOT ¥4011.
- **History:** This visual misreading occurred on Turn 1034 (reading ¥170 as ¥1701, or ¥1701 as ¥17011) and was repeated on Turn 1222 (reading ¥401 as ¥4011). Creating this permanent documentation prevents future hallucinations of this border pattern.

<hr>

<h1><code>Locations/MtMoon_B1F</code></h1>

# Mt. Moon B1F

## Platform 1 (Middle-Right)
- **Access:** Ladder from Mt. Moon 1F at (25, 15).
- **Landing:** Mt. Moon B1F at (25, 15).
- **Layout:**
  - Walkable floor columns 24-27, rows 14-27.
  - Connecting corridor at row 26/27 going left to columns 13-23.
- **Ladders:**
  - (25, 15): Leads back to Mt. Moon 1F.
  - (13, 27): Located at the bottom-left of the platform.
- **Items:** None.
- **Trainers:** None.

## Connector Corridor (North-West)
- **Access:** 
  - Eastern Ladder: at (25, 9) leading up to Mt. Moon 1F at (17, 11).
  - Western Ladder: at (17, 11) leading down to Mt. Moon B2F at (25, 9).
- **Layout:** 
  - Walkable floor is a horizontal corridor across columns 14 to 22 on rows 8 to 11.
  - Row 10 is completely clear, allowing safe horizontal transit to bypass the western ladder warp at (17, 11).
- **Ladders:**
  - (25, 9): Leads up to Mt. Moon 1F.
  - (17, 11): Leads down to Mt. Moon B2F.
- **Items:** None.
- **Trainers:** None.

## Connector Corridor (North-West-2)
- **Access:**
  - Northern Ladder: at (5, 5) leading up to Mt. Moon 1F at (5, 5).
  - Southern/Eastern Ladder: at (21, 17) leading down to Mt. Moon B2F at (21, 17).
- **Layout:**
  - Vertical segment from (5, 5) down to (5, 16).
  - Horizontal segment from (5, 16) east to (21, 16), which goes south to (21, 17).
- **Ladders:**
  - (5, 5): Leads up to Mt. Moon 1F.
  - (21, 17): Leads down to Mt. Moon B2F.
- **Items:** None.
- **Trainers:** None.

<hr>

<h1><code>Locations/MtMoon_1F</code></h1>

# Mt. Moon 1F - Locations & Landmarks

## Overworld Layout & Navigation
- **Southern Entrance (from Route 3):** Player transitions to Mt. Moon 1F at (14, 35) facing Up.
- **Ladders:**
  - (25, 15): Leads to Mt. Moon B1F Platform 1.
  - (17, 11): Newly observed ladder on the north-western side.
  - (5, 5): Leads to Mt. Moon B1F Connector Corridor (North-West-2) at (5, 5).
  - Note on Southern Warp: When exiting B1F at (13, 27), the game places the player at the landing coordinate (15, 27) on 1F. There is no interactive warp tile at (15, 27) or (13, 27) on 1F; it is a one-way landing spot from B1F.

## Signposts & Points of Interest
- **Signpost at (15, 23):** Reads: "Beware! ZUBAT is a blood sucker!"
- **HP UP at (25, 21):** Retrieved on Turn 1554.
- **Potion at (2, 20):** Found and retrieved Potion at (2, 20) on Turn 2068.
- **TM12 (Water Gun) at (5, 32):** Found and retrieved TM12 at (5, 32) on Turn 2018.

## Trainers & Defeated Status
- **Lass Miriam:** Sits at (16, 23).
  - **Roster:** Clefairy (Lv 14)
  - **Status:** Defeated on Turn 1448.
- **Team Rocket Grunt:** Standing at (15, 24).
  - **Roster:** Sandshrew (Lv 11), Rattata (Lv 11), Zubat (Lv 11)
  - **Status:** Defeated on Turn 1529.
  - **Reward:** ¥330
- **Lass (North-East):** Sits at (30, 6) originally, engaged at (30, 7).
  - **Roster:** Oddish (Lv 11), Bellsprout (Lv 11)
  - **Status:** Defeated on Turn 1641.
  - **Reward:** ¥165
- **Youngster (North-West):** Sits at (12, 16) originally, engaged at (14, 16) on Turn 1763.
  - **Roster:** Rattata (Lv 10), Rattata (Lv 10)
  - **Status:** Defeated on Turn 1779.
  - **Reward:** ¥150
- **Bug Catcher Kenton:** Sits at (7, 22) originally, engaged at (7, 24) facing Down.
  - **Roster:** Weedle (Lv 11), Kakuna (Lv 11)
  - **Status:** Defeated on Turn 2031.
  - **Reward:** ¥110
- **Hiker (Top-Left):** Sits at (5, 6) originally, engaged at (5, 7) facing Down.
  - **Roster:** Geodude (Lv 10)
  - **Status:** Undefeated (encountered on Turn 1889).

## Verified Layout Details & Barriers
- **Central Wall & Ledge Barrier:** Rows 20 and 21 form a solid horizontal rocky wall across columns 14 to 29, EXCEPT for columns 20 and 21 which are completely open and clear, allowing direct northward (upward) movement between the southern area (row 25) and the northern area (row 15). There is no ledge blocking upward movement on columns 20 and 21.
- **Raised Platform (West Side):** Columns 12 and 13 on rows 20 to 28 form an elevated platform.
  - The eastern edge (column 13) has a solid wall on rows 22 and 26 (experimentally tested), but row 27 is a completely walkable gap/staircase allowing passage to the west side (verified on Turn 2451).
  - Row 28 is a horizontal elevated platform segment that blocks column 14, meaning column 14 is a dead-end at row 27.
- **Stony Floor (South-West):** Row 29 is a completely walkable stony floor across columns 10 to 19, which is situated below the platform.
- **Northwest Pocket (Ladder area):** (17, 11) is a ladder, and (17, 12) is the floor tile below it. This forms a small 1x2 pocket that is blocked on the left by rock walls at column 16, blocked on the right by rock walls at column 18, and blocked on the south by rock walls on row 13. The pocket exits to the LEFT (west) on row 12! The path goes (17, 12) <--> (16, 12) <--> (15, 12) <--> ... into the main cavern on columns 12-16.
- **Western Cavern Barriers (Rows 18-19):** Systematic, tile-by-tile testing (completed on Turn 2165-2166) confirmed that rows 18 and 19 form a solid, impassable horizontal rock wall across columns 2 to 9 on the west side. All columns (2, 3, 4, 5, 6, 7) are completely blocked.
- **Central/Southern Cavern Blockages & Pathing:**
  - **No Direct Middle Crossing:** Column 16 has a solid vertical wall blocking rows 26 to 29 (except row 25 which is open on column 16).
  - **Columns 22-23 Barrier:** Solid vertical rock wall on columns 22 and 23 across rows 21 to 29 (EXCEPT rows 24 to 27 which are completely open and walkable, as verified on Turn 2428).
  - **Row 26 Wall:** Row 26 is a solid rock wall across columns 16 to 23, blocking any downward movement from row 25.
  - **Result:** Rows 30 to 35 are completely open and walkable across column 16, allowing direct horizontal crossing between the western cavern and the eastern cavern!
  - **Eastern Cavern Access Route (Direct & Verified):**
    - Walk north from the entrance (14, 35) to row 25.
    - Walk east along row 25 to column 20 or 21 (completely open across column 16).
    - Walk north along column 20/21 directly to row 15 (completely open, no ledges or walls!).
    - Walk east along row 15 directly to the ladder at (25, 15).
    - This is the fastest, most direct route, entirely bypassing all rock walls and northern detours!

<hr>

<h1><code>Locations/MtMoon_B2F</code></h1>

# Mt. Moon B2F

## Overworld Layout & Navigation
- **Access Ladders:**
  - (25, 9): Leads up to B1F at (17, 11) (accessed from the starting platform).
  - (21, 17): Leads up to B1F at (21, 17) (accessed from the vertical chamber).
- **Starting Platform & Chambers (Isolated Area):**
  - **Starting Platform:** Columns 24 to 28, rows 8 to 11. Bounded by rock walls on row 7. Elevated above row 12 by an impassable one-way ledge/cliff face on row 11 (columns 24-28). You can jump down to row 12, but cannot walk back Up.
  - **Vertical Chamber:** Columns 20 to 23, rows 14 to 19. Bounded by rock walls on columns 18-19 on the left and column 24 on the right. This chamber is at the lower level. It connects to the starting platform's ledge on row 12.
  - **Upper Niche:** Columns 20 to 22, rows 5 to 7. Bounded by rock walls on row 4, column 19, and column 23. Elevated above the vertical chamber by an impassable one-way ledge/cliff face on row 11 (columns 20-22).
  - **Wall Blockage:** Columns 18-19 form a solid, vertical rock wall dividing this starting platform area from the main B2F cavern. It is completely solid on all rows (including row 12), meaning this entire top-right area of B2F is a self-contained closed loop with no overworld path to the main B2F cavern.

## Items
- **Poké Ball (Top-Right):** Sits at (29, 5) (Retrieved on Turn 1722).

## Trainers
- **Team Rocket Grunt:** Sits at (29, 11). Defeated on Turn 1716. Reward: ¥360. Roster: Zubat (Lv 12), Ekans (Lv 12).

<hr>