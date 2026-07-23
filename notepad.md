<h1><code>Main</code></h1>

# Pokémon Blue - Crystal Palette Swap Mod Playthrough

## Current Location
- Viridian Forest

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

## Party Statistics
- **SHELLBY (Squirtle):**
  - **Level:** 11
  - **Moveset:** Tackle, Tail Whip, Bubble
  - **HP:** 4 / 32
  - **Status:** Healthy
- **NIBBLES (Rattata):**
  - **Level:** 4
  - **Moveset:** Tackle, Tail Whip
  - **HP:** 5 / 16
  - **Status:** Healthy
- **GUSTY (Pidgey):**
  - **Level:** 5
  - **Moveset:** Gust, Sand-Attack
  - **HP:** 5 / 19
  - **Status:** Healthy

## Inventory
- **Poké Balls:** 4 (3 used to catch NIBBLES, 5 used to catch GUSTY, 2 purchased on Turn 387)
- **Potion:** 0 (1 used during the battle with NIBBLES)




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
- **Conclusion/Hypothesis:** Wild encounters on Route 22 may be disabled or extremely rare at this stage of the game, or the pacing test did not successfully change coordinates on every step (unverified coordinate-by-coordinate traversal). To verify this properly, future tests must explicitly log coordinate changes on each step. Until then, we will avoid hunting for wild Pokémon on Route 22 to focus on progression.

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
  - **East Side (Columns 8 and 9):** A completely clear pavement road with **0% encounter rate**, going straight north to Pewter City.
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

<hr>