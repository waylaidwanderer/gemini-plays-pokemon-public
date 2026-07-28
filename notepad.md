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
- **Defeated Youngster Calvin:** Defeated Youngster Calvin on Turn 1325.
- **Defeated Lass Sally:** Defeated Lass Sally on Turn 1348.
- **Healed at Mt. Moon Pokémon Center:** Healed party at (11, 5) on Turn 1422.
- **Entered Mt. Moon:** Entered Mt. Moon 1F at (18, 5) on Turn 1431.
- **Defeated Team Rocket Grunt:** Defeated Team Rocket Grunt at (15, 24) on Turn 1529, earning 330.
- **Obtained HP UP:** Found HP UP at (25, 21) on Turn 1554.
- **Defeated Lass (North-East):** Defeated Lass at (30, 7) on Turn 1641, earning 165.
- **Defeated Team Rocket Grunt:** Defeated Team Rocket Grunt at (29, 11) on Mt. Moon B2F on Turn 1716, earning 360.
- **Obtained Item (Poké Ball):** Found and retrieved Poké Ball at (29, 5) on Mt. Moon B2F on Turn 1722.
- **Defeated Youngster (North-West):** Defeated Youngster at (12, 16) on Mt. Moon 1F on Turn 1779, earning 150.
- **Obtained Item (Moon Stone):** Found and retrieved Moon Stone at (2, 2) on Mt. Moon 1F on Turn 1881.
- **Obtained Item (Moon Stone):** Found and retrieved Moon Stone at (35, 31) on Mt. Moon 1F on Turn 2932.
- **Defeated Bug Catcher Kenton:** Defeated Bug Catcher Kenton at (7, 22) on Turn 2031, earning 110.
- **Obtained Item (Potion):** Found and retrieved Potion at (2, 20) on Mt. Moon 1F on Turn 2068.
- **Defeated Bug Catcher (South-East):** Defeated Bug Catcher at (30, 27) on Mt. Moon 1F on Turn 2697, earning 100.
- **Defeated Super Nerd:** Defeated Super Nerd near (24, 27) on Mt. Moon 1F on Turn 2731, earning 275.

- **Defeated Rival JACK:** Defeated JACK at (20, 6) on Route 24 on Turn 4416, earning 595.
- **Defeated Bug Catcher Cale:** Defeated Bug Catcher Cale at (11, 32) on Route 24 on Turn 4461, earning 140.
- **Defeated Lass Ali:** Defeated Lass Ali at (10, 28) on Route 24 on Turn 4475, earning 210.
- **Defeated Youngster Timmy:** Defeated Youngster Timmy at (11, 25) on Route 24 on Turn 4501, earning 210.
- **Defeated Lass:** Defeated Lass at (10, 22) on Route 24 on Turn 4514, earning 240.
- **Defeated Jr. Trainer♂:** Defeated Jr. Trainer♂ at (11, 19) on Route 24 on Turn 4529, earning 360.
- **Defeated Rocket Grunt:** Defeated Rocket Grunt at (11, 15) on Route 24 on Turn 4558, earning 450.
- **Defeated Youngster Dan:** Defeated Youngster Dan at (18, 5) on Turn 4675, earning Â255.
- **Defeated Lass Robin:** Defeated Lass Robin at (20, 8) on Turn 4697, earning 225.
- **Defeated Hiker Nob:** Defeated Hiker Nob at (23, 9) on Turn 4725, earning 455.
- **Defeated Jr. Trainer♂ Shane:** Defeated Jr. Trainer♂ Shane at (24, 4) on Turn 4734, earning 540.
- **Defeated Lass Haley:** Defeated Lass Haley at (37, 5) on Turn 4758, earning 195.
- **Obtained S.S. TICKET:** Received S.S. TICKET from Bill in his Sea Cottage on Route 25 on Turn 4781.
- **Defeated Hiker Franklin:** Defeated Hiker Franklin at (8, 4) on Turn 4659, earning 525.
- **Defeated Rocket Grunt (Burgled House Backyard):** Defeated Team Rocket Grunt on Turn 4897, earning 510 and obtaining TM28 (Dig).
- **Defeated Jr. Trainer♂ (Route 24 Grass):** Defeated Jr. Trainer♂ on Turn 4992, earning 280.
- **Truffle Leveled Up:** TRUFFLE (Paras) reached Level 13 and learned STUN SPORE on Turn 5032.
- **Defeated Swimmer Horatio (Cerulean Gym):** Defeated Swimmer at (5, 7) inside Cerulean Gym on Turn 5210, earning 80.
- **Defeated Picnicker Diana (Cerulean Gym):** Defeated Picnicker Diana at (5, 3) inside Cerulean Gym on Turn 5233, earning 380.
- **Defeated Gym Leader Misty:** Defeated Cerulean Gym Leader Misty on Turn 5262, obtaining the CASCADEBADGE and TM11 (Bubblebeam).

- **Defeated Bug Catcher (Route 6):** Defeated Bug Catcher on Turn 6172, earning 200.
- **Defeated Jr. Trainer♀ (Route 6):** Defeated Jr. Trainer♀ at (9, 31) on Turn 6185, earning 320.
- **Defeated Jr. Trainer♂ (Route 6):** Defeated Jr. Trainer♂ at (8, 31) on Turn 6211, earning 320.

- **Cut the Gym Bush:** Cut the Gym bush in Vermilion City to open access to the Gym on Turn 6799.
- **Whited Out in Gym:** Whited out against Sailor Dwayne in Vermilion Gym on Turn 6837; returned to Vermilion Pokémon Center and fully restored party.
- **Defeated Sailor Dwayne (Vermilion Gym):** Defeated Sailor Dwayne at (0, 10) in Vermilion Gym on Turn 6863, earning ¥630.
- **Defeated Rocker Harrison (Vermilion Gym):** Defeated Rocker Harrison at (3, 8) in Vermilion Gym on Turn 6886, earning ¥500.
- **Defeated Gentleman Tucker (Vermilion Gym):** Defeated Gentleman Tucker at (9, 6) in Vermilion Gym on Turn 6897, earning ¥1610.
- **Solved Vermilion Gym Puzzle:** Found first switch at (1, 11) and second switch at (3, 11) on Turn 7005, opening the motorized door to Lt. Surge.
- **Defeated Gym Leader Lt. Surge:** Defeated Vermilion Gym Leader Lt. Surge on Turn 7027, obtaining the THUNDERBADGE and TM24 (Thunderbolt).
- **Defeated JR. TRAINER♀ (Route 9):** Defeated JR. TRAINER♀ on Route 9 on Turn 7197, earning ¥360.
- **Obtained Item (TM30):** Found and retrieved TM30 (Teleport) at (10, 15) on Route 9 on Turn 7206.
- **Defeated Hiker (Route 9):** Defeated Hiker at (45, 15) on Route 9 on Turn 7280, earning ¥735.
- **Defeated Bug Catcher Conner:** Defeated Bug Catcher Conner at (40, 8) on Turn 7431, earning ¥320.
- **Defeated JR. TRAINER♂ (Route 9):** Defeated JR. TRAINER♂ at (24, 7) on Turn 7479, earning ¥420.
- **Defeated JR. TRAINER♂ (Route 9):** Defeated JR. TRAINER♂ at (34, 7) on Turn 7528, earning ¥380.

## Party Statistics
- **TESLA (Pikachu):**
  - **Level:** 16
  - **HP:** 40 / 40
  - **Status:** Healthy
- **TRUFFLE (Paras):**
  - **Level:** 14
  - **HP:** 37 / 37
  - **Status:** Healthy
- **GUSTY (Pidgey):**
  - **Level:** 5
  - **HP:** 19 / 19
  - **Status:** Healthy
- **NIBBLES (Rattata):**
  - **Level:** 7
  - **HP:** 22 / 22
  - **Status:** Healthy
- **SHELLBY (Wartortle):**
  - **Level:** 34
  - **HP:** 77 / 92
  - **Status:** Healthy


<hr>

<h1><code>Mechanics/Search_Scripting_Pitfalls</code></h1>

# Search Scripting Pitfalls

## Turn 79 Baseline Drift Pitfall
- **Description:** When running navigation scripts, if you execute a sequence of movements and then a reset sequence without first verifying that the initial movements were successful (e.g. they weren't blocked by a wall, NPC, or wild battle), the actual position of the player will drift from the expected position.
- **Prevention:** Always verify that each step or sequence of steps succeeded (checking GameState coordinates and screen visual) before continuing or executing corrective/reset steps.
## time.sleep() and Concurrent Execution Pitfall
- **Description:** Python's `time.sleep()` does NOT advance the emulator. The emulator is completely paused during Python code execution except when `mgba.press_buttons()` is running. If you use Python loops with `time.sleep()` expecting the player's coordinates to change, the coordinates will never update, leading to infinite loops and script timeouts.
- **Prevention:** Do not use `time.sleep()`. The emulator advances synchronously during `mgba.press_buttons()`. Insert `"sleep <ms>"` directly inside the button list if you need delays, and read coordinates/screenshots only after `mgba.press_buttons()` returns.

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

<h1><code>Locations/Route4</code></h1>

# Route 4 - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **Mt. Moon Exit Door:** Leads out from B1F (27, 3) to Route 4 at (24, 6) facing Down. (Verified at Turn 4002).
- **Upper Road segment (Rows 3-6):** Completely clear dirt path extending east from the exit at (24, 6) to column 37.
- **Vertical Ledge (Column 38):** A vertical one-way ledge facing right. Walk Right from (37, 6) to jump down to (39, 6). (Verified at Turn 4005).
- **Vertical Checkered Cliff (Column 45):** A solid wall on rows 2-9. To bypass it, one must walk south to row 10, jumping down the horizontal ledge at row 9. (Verified at Turn 4007).
- **Horizontal Ledge (Row 9):** A horizontal one-way ledge facing down across columns 44 to at least 61. Can be jumped Down, but cannot be walked Up.
- **Lower Grass Area (Rows 10-15):** Contains tall grass. Bounded on the south by the River at row 16.
- **River Barrier (Row 16+):** Impassable water channel running horizontally, blocking all southward movement. (Verified at Turn 4012).
- **Horizontal Ledge (Row 13):** A horizontal one-way ledge facing down across columns 54-61, and columns 76-79. Bypassed by walking Left to column 53, or by using the walkable gap at column 77. (Verified at Turn 5607).
- **Ledge Gaps (Column 53):** Clear gap in row 13 ledge, allowing the player to walk Up to row 12 from rows 14-15. (Verified at Turn 4016).
- **Ledge Gap (Column 61):** Clear gap in the row 9 ledge. Walking Up from (61, 10) to (61, 9) allows the player to access the upper road of Route 4 (rows 5-8). (Verified at Turn 4020).
- **Vertical Forest/Tree Barrier (Column 62):** A solid vertical line of trees on rows 10-15, blocking direct eastward transit in the lower grass area. Bypassed by taking the gaps at column 53 and column 61 to reach rows 5-8. (Verified at Turn 4015).

<hr>

<h1><code>Locations/CeruleanCity</code></h1>

# Cerulean City - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **West Entrance (from Route 4):** Connects to the paved brick road of Cerulean City at x=0, y=19. (Verified at Turn 4062).
- **Bike Shop:** Large building located south of (13, 15). Roof spans row 24 on columns 12-16. Front of the building is on row 25.
- **Cerulean Gym:** Large building located on the east side, north of the Mart. Sign reads "GYM" at (26, 18) / (27, 18).
- **Poké Mart:** Building located south of the Gym. Sign reads "MART" at (26, 24) / (27, 24) with entrance at (25, 25).
- **Route 24 Bridge (Nugget Bridge Path):** Accessible from the north-center area.

## Northern Bypass to Route 24
- **No South-to-North Direct Passage:** The horizontal barrier at row 15 blocks all columns. The eastern lane on column 33 has a horizontal one-way ledge facing down on row 19, preventing any northward walk. The Burgled House front door is at (27, 11) (north of the barrier), so it is inaccessible from the south side of the city.
- **Route 24 Entrance:** Paved brick road at columns 20-21 on rows 10-13 is completely clear and leads north directly onto Route 24.

## Verified Outside Door & Warp Mappings
| Outside Door | Standard Map Location | Verified Interior Room / Warp Destination | Notes / Functionality |
|--------------|-----------------------|-------------------------------------------|-----------------------|
| (19, 17)     | Pokémon Center        | Pokémon Center                            | Functional Pokémon Center! Stand at (3, 3) and talk to Nurse Joy to heal. |
| (13, 15)     | Melanie's House       | Melanie's House                           | Contains Jynx trade NPC, styled as a house. No healing. |
| (25, 25)     | Poké Mart             | Melanie's House                           | Exiting warps to (25, 25). Contains Jynx trade NPC. |
| (9, 11)      | Badge Guy's House     | Badge Guy's House                         | Contains Badge Guy NPC. Rendered with a misleading Pokémon Center tileset (PC on right, counter on top), but has NO healing function. |
| (13, 25)     | Bike Shop             | Melanie's House                           | Shared interior. Exiting from (2, 8) warps to (13, 25). |
| (27, 21)     | Fighting Dojo         | Unreachable                              | Decorative only. Exposing water canal (24, 22 to 27, 22) blocks southern access. |
| (30, 19)     | Cerulean Gym          | Cerulean Gym                              | Standard Gym interior. Misty is here. |
| (27, 11)     | Burgled House         | Bill's House Interior (Mod Swap)          | Mapped to Bill's House. Entering (27, 11) warps to Bill's House. Exiting Bill's House warps back to (27, 11). |

## Trainers & Defeated Status
- **Team Rocket Grunt (Burgled House Backyard):** Located at (30, 8).
  - **Roster:** Machop (Lv 15), Drowzee (Lv 17)
  - **Status:** Defeated on Turn 4897.
  - **Reward:** ¥510 and TM28 (Dig).

## Verified Southern Barriers (Turn 5421)
- **Route 4 East transition always warps to (0, 18) in Cerulean City:** Transitioning from Route 4 to Cerulean City on rows 0, 3, 4, or 5 always warps the player to (0, 18) on the south side of Cerulean City. The Route 4 Alignment Offset Bypass to the north side (y=12) is NOT functional in this mod.
- **Saffron Road (Columns 16-17) Ledge Block:** Standing at (16, 28) and pressing Down is blocked by the vertical logs at (16, 29). Saffron Road is completely impassable.
- **Row 28 Barrier (MANUALLY VERIFIED):** Row 28 is completely blocked by dark green trees across columns 12-35, and Saffron Road (columns 16-17) is blocked on row 29 by vertical logs at (16, 29) and a signpost at (17, 29). Columns 36 and 37 on row 28 are visually clear of trees. However, reaching columns 36-37 from the south-west side (Saffron Road / Poké Mart area) is **currently impassable and unverified** because column 35 is blocked by logs on rows 20-27 and trees on rows 28-29, and rows 16-23 on columns 32-35 are blocked by the water canal, forming a solid vertical obstruction across all walkable rows.
- **Column 35 Log Barrier (MANUALLY VERIFIED):** Column 35 is completely blocked by a solid wall of vertical logs on rows 23-27, and by trees on rows 28-29. This prevents any direct horizontal passage from the west side of Cerulean City to the eastern lane (columns 36-37) on the south side of the city. (Verified at Turn 5638).

## Verified Southern & Central Barriers (Turn 5769 Update)
- **Column 7 Central Wall:** Empirically verified that column 7 contains a solid vertical wall of grey pillars/walls on rows 12-16, blocking all westward passage to column 0 on those rows.
- **Row 15 Barrier Details:**
  - **Saffron Road Blockage:** Saffron Road (columns 16-17) is completely blocked on row 15 by Melanie's House building (spanning columns 13-17 on row 15).
  - **Ledge Blockage (Columns 8-11):** Column 9 (and columns 8-11) has a horizontal one-way ledge facing down on row 15, which blocks all upward (south-to-north) passage.
- **Row 19 Ledge Blockage:** Columns 32-35 on row 19 have a horizontal one-way ledge facing down, allowing downward jumps but blocking upward passage.
- **Saffron Gym Layout:** Saffron Gym occupies columns 27-31 on rows 16-19.



## Burgled House Backdoor & Backyard Shortcut (Turn 9005-9007 Discovery)
- **Front Door:** (27, 11). Entering warps the player to Bill's House Interior (Mod Swap).
- **Backdoor/Hole in Wall:** Walking north to the top-center (3, 0) inside Bill's House Interior warps the player directly outside to the Backyard of the Burgled House at `(27, 9)`.
- **Bypassing the Column 32 Log Barrier:** This backyard path allows the player to enter the Burgled House front door on the south side at `(27, 11)` (bypassing the Row 15 barriers), exit through the backdoor to `(27, 9)`, and then walk west/east on the north side, completely bypassing the Column 32/33 ledge and log barriers!


<hr>

<h1><code>Locations/Route24</code></h1>

# Route 24 (Nugget Bridge)

## Overworld Layout & Navigation
- **Southern Entrance (from Cerulean City):** Connects to Cerulean City at (20, 0) / (21, 0) transitioning to Route 24 at (10, 35) / (11, 35).
- **Nugget Bridge segment:** Columns 10 and 11 form a paved brick bridge running from row 35 up to row 15. Bounded by water on the left (columns 7-8) and right (columns 15-16).
- **Eastern Path to Route 25:** After clearing the bridge, walking northeast leads to Route 25.

## Trainers & Defeated Status
- **Bug Catcher Cale:** Sits at (11, 31). Defeated on Turn 4461. Reward: ¥140.
- **Lass Ali:** Sits at (10, 28). Defeated on Turn 4475. Reward: ¥210.
- **Youngster Timmy:** Sits at (11, 25). Defeated on Turn 4501. Reward: ¥210.
- **Lass:** Sits at (10, 22). Defeated on Turn 4514. Reward: ¥240.
- **Jr. Trainer♂:** Sits at (11, 19). Defeated on Turn 4529. Reward: ¥360.
- **Rocket Grunt:** Sits at (11, 15). Defeated on Turn 4558. Reward: ¥450.

- **Jr. Trainer♂ (Tall Grass):** Sits at (5, 20) originally, engaged at (5, 17) in the tall grass.
  - **Roster:** Rattata (Lv 14), Ekans (Lv 14)
  - **Status:** Defeated on Turn 4992.
  - **Reward:** ¥280

<hr>

<h1><code>Locations/Route25</code></h1>

# Route 25 - Locations & Landmarks

## Overworld Layout & Navigation
- **Western Entrance (from Route 24):** Transitions from Route 24 at (19, 8) or (19, 9) to Route 25 at (0, 8) or (0, 9).
- **Path structure:** Row 8 is a horizontal paved path. Contains trees/hedges forming a maze, starting from column 10.
- **Grassy Maze segment:** Row 4 is a horizontal path through the grass that can be used to bypass the Hiker at (13, 7) but triggers the Hiker at (8, 4).

## Landmarks & Buildings
- **Bill's Sea Cottage:** Located at the eastern end of Route 25.

## Trainers & Defeated Status
- **Hiker Franklin:** Sits at (8, 4) facing Down.
  - **Roster:** Machop (Lv 15), Geodude (Lv 15)
  - **Status:** Defeated on Turn 4659.
  - **Reward:** ¥525
- **Youngster Joey:** Sits at (14, 2) originally, engaged at (14, 4) facing Down.
  - **Roster:** Rattata (Lv 15), Spearow (Lv 15)
  - **Status:** Defeated on Turn 4668.
  - **Reward:** ¥225
- **Youngster Dan:** Sits at (18, 5) originally, engaged at (18, 4) facing Up.
  - **Roster:** Slowpoke (Lv 17)
  - **Status:** Defeated on Turn 4675.
  - **Reward:** ¥225
- **Lass Robin:** Sits at (18, 8) originally, engaged at (20, 8) facing Left.
  - **Roster:** Nidoran♂ (Lv 15), NidoranF (Lv 15)
  - **Status:** Defeated on Turn 4697.
  - **Reward:** ¥225
- **Hiker Nob:** Sits at (23, 9) originally, engaged at (23, 8) facing Up.
  - **Roster:** Geodude (Lv 13), Machop (Lv 13), Geodude (Lv 13)
  - **Status:** Defeated on Turn 4725.
  - **Reward:** ¥455
- **Jr. Trainer♂ Shane:** Sits at (24, 4) originally.
  - **Roster:** Rattata (Lv 16), Ekans (Lv 16)
  - **Status:** Defeated on Turn 4734.
  - **Reward:** ¥540
- **Lass Haley:** Sits at (37, 4) originally, engaged at (37, 5) facing Down.
  - **Roster:** Oddish (Lv 15), Pidgey (Lv 15)
  - **Status:** Defeated on Turn 4758.
  - **Reward:** ¥195


<hr>

<h1><code>Locations/Route5</code></h1>

# Route 5 - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **Northern Entrance (from Cerulean City Saffron Road):** Connects to Cerulean City at columns 14-15 on row 35 (transitions to Route 5).
- **Western Lane (Columns 10-15):** Clear grass and road running vertically down to Saffron Saffron Road. Bounded on Saffron Saffron Road by a horizontal brick wall at row 33.
- **Vertical Barrier (Column 5):** Solid line of trees (rows 9-15) and logs (rows 16-23) separating the western side (columns 2-4) from the eastern side (columns 6-13).
- **Horizontal Ledge (Row 23):** Downward-facing ledge across columns 6-13. Prevents direct upward movement on those columns.
- **Walkable Gap (Row 24-25, Column 5):** A horizontal gap in the vertical barrier on column 5 at rows 24-25, allowing players to walk freely between the western and eastern sides of Route 5.

## Underground Path Entrance Building
- **Location:** Stands on the eastern side of Route 5 at rows 20-21.
- **Access Route:** Since row 23 has a ledge, the building is accessible from the north side of the ledge. From column 15 (which is open on row 23), walk Up to row 15, Left to column 10, Down to row 20, and walk around to (10, 22) (south doorstep) to walk Up and enter.

<hr>

<h1><code>Locations/Route6</code></h1>

# Route 6 - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **Northern Entrance (from Saffron City Gatehouse / Underground Path):** Exiting the Saffron City Gatehouse at (17, 13) warps the player to Route 6 at (17, 14) facing Down.
- **Main Path (Columns 13-19):** Clear pavement road going south to Vermilion City.
- **Tall Grass Area (Rows 16-18):** Horizontal band of tall grass across the main road, likely containing wild encounters.

## Verified Barriers
- **Row 32 Statues (Saffron City Southern Gatehouse):** Row 32 contains a solid line of grey statues/pillars blocking columns 10-19. This completely blocks Saffron City's southern entrance and forces the player to bypass them by using columns 8-9 (which are clear pavement) to go south.

## Verified Landmarks & Coordinate Log (Route 6)
- **Saffron City Southern Gatehouse Door:** Located at `(10, 7)` on the west side. Exiting the Saffron City Gatehouse warps the player to Route 6 at `(10, 8)` facing Down. Inside, the thirsty guard blocks access to Saffron City.
- **Horizontal Fence Barrier:** Runs horizontally on Row 11 from columns 2 to 15.
- **Fence Gap:** Located at `(7, 11)`. Allows passage north/south between Saffron Gatehouse row 14 and the northern grassy field containing Saffron Southern Gatehouse.
- **Underground Path Entrance Building (Route 6):** Located at columns 16-19, rows 10-13 on the east side.
  - **Entrance Door:** Located at `(17, 13)`. Standing at `(17, 14)` and walking Up enters the building.

<hr>

<h1><code>Locations/VermilionCity</code></h1>

# Vermilion City - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **Northern Entrance:** Connects from Route 6. The transition from Route 6 at y=36 warps the player to Vermilion City at `(18, 0)` due to a +10 horizontal alignment offset (Route 6 x=8 connects to Vermilion City x=18).
- **Visual Grid Alignment:** No coordinate offset in Vermilion City; the visual grid exactly matches internal memory coordinates.

## Verified Outside Door & Warp Mappings
| Outside Door | Standard Map Location | Verified Interior Room / Warp Destination | Notes / Functionality |
|--------------|-----------------------|-------------------------------------------|-----------------------|
| (11, 3)      | Pokémon Center        | Pokémon Center                            | Functional! Nurse Joy is behind the counter at (3, 2). Healed party on Turn 6257. |
| (7, 3)       | House                 | Melanie's House Interior                  | Shared interior warp. Exits to (7, 4). |
| (15, 13)     | House                 | Melanie's House Interior                  | Shared interior warp. Exits to (15, 14). |
| (23, 19)     | Machop House          | Melanie's House Interior                  | Shared interior warp. Exits to (23, 20). |
| (23, 13)     | Poké Mart             | Melanie's House Interior                  | Shared interior warp. Exits to (23, 14). |

## Water, Pond & Hedge Barriers
- **Central Pond Boundaries:**
  - Row 8: Blocks columns 10-15 with soil/water.
  - Row 18: Blocks columns 16-19 with soil/water.
  - Row 22: Blocks columns 20-25 with soil/water.
- **Hedge/Bush Blockages:**
  - Row 18 & 19: Columns 13 and 14 have green hedges/trees that block southward transit to row 20, separating the northern and southern parts of the city.

## S.S. Anne Pier Layout & Map Transitions (Vermilion Dock)
- **Pier Structure:** Consists of two vertical walkable columns: Column 18 and Column 19, running from row 27 down to row 35.
- **Statues/Pillars:** Present on columns 14-17 and columns 20-23 on rows 30 and 31.
- **Boarding Warp Transitions:**
  - **Column 18 (left side):** Walking south on Column 18 past row 35 warps the player to S.S. Anne Entryway (Map 91) at `(14, 0)` (facing Down).
  - **Column 19 (right side):** Walking south on Column 19 past row 35 warps the player to S.S. Anne Entryway (Map 91) at `(14, 2)` (facing Down), right next to the S.S. Anne Deck warp!
- **Sailor Ticket Checker:** Sits at `(19, 30)`. Once ticket is shown, he does not block vertical transit on Column 19 below row 30.

## Vermilion Gym Layout & Geometry
- **Entrance:** Located at `(12, 19)` (connects to Vermilion City at `(12, 20)` after clearing the cuttable bush at `(15, 18)`).
- **Gym Guide:** Stands at `(4, 14)`.
- **Rhydon Statues:** Located at `(3, 13)` / `(3, 14)` and `(6, 13)` / `(6, 14)`.
- **Trash Can Grid (3x5):**
  - Row 11: `(1, 11)`, `(3, 11)`, `(5, 11)`, `(7, 11)`, `(9, 11)`
  - Row 9: `(1, 9)`, `(3, 9)`, `(5, 9)`, `(7, 9)`, `(9, 9)`
  - Row 7: `(1, 7)`, `(3, 7)`, `(5, 7)`, `(7, 7)`, `(9, 7)`
- **Trainers:**
  - **Sailor Dwayne:** Located at `(0, 10)` (facing Right). Roster: Pikachu (Lv 21).
  - **Rocker Harrison:** Located at `(3, 8)` (facing Down). Roster: Voltorb (Lv 20).
  - **Gentleman Tucker:** Located at `(9, 6)` (facing Down). Roster: Pikachu (Lv 23). Defeated on Turn 6897, earning ¥1610.

  - **Gym Leader Lt. Surge:** Located at (5, 1) inside the Vermilion Gym. Roster: Voltorb (Lv 21), Pikachu (Lv 18), Raichu (Lv 24). Defeated on Turn 7027, obtaining the THUNDERBADGE and TM24 (Thunderbolt).

<hr>

<h1><code>Locations/SSAnne</code></h1>

# S.S. Anne - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **Initial Entry (from Pier):** Transitioning from S.S. Anne Pier at (18, 30) warps the player to S.S. Anne Entryway at `(14, 0)` facing Down.
- **Entryway South Warp:** Walking south through the entryway (around row 4) warps the player to the S.S. Anne Deck at `(27, 0)`.
- **Deck Door Warps:**
  - Left Deck Door at `(23, 8)`: Warps the player to S.S. Anne Cabin 2 at `(10, 0)` (facing Down).
  - Right Deck Door at `(31, 8)`: Warps the player to S.S. Anne Cabin 1 at `(0, 0)` (facing Down).

## Cabin 2 Mappings
- **Left Deck Door Connection:** Warps to `(10, 0)` / `(10, 1)`. Contains pink/white checkered carpet of Cabin 2.
- **Wandering NPCs / Barriers:**
  - NPC at (11, 4) facing UP.
  - Desk/Table at (10, 5) and (11, 5).


## S.S. Anne Deck Right-Hand Path
- **Pathway:** Column 36 (rows 6-14) and Column 37 (rows 6-14) form a major vertical walkway on the far right of the S.S. Anne Deck.
- **Staircase Warp:** Standing at (36, 15) and walking Right to (37, 15) warps the player to S.S. Anne 2F at `(27, 5)` (facing Down).

## S.S. Anne 2F Layout & Cabins
- **Entrance Warp:** Warping from Deck (37, 15) places the player at S.S. Anne 2F `(27, 5)` (facing Down).
- **Staircase location:** S.S. Anne 2F `(27, 4)` is the staircase leading back to S.S. Anne Deck.
- **Hallway:** Runs horizontally on rows 4 and 5 from column 27 to at least column 19.
- **Cabin doors:**
  - **Cabin 3 Door:** Located at `(23, 3)`. Entering warps to Cabin 3 Interior at `(12, 15)`.
  - **Cabin 4 Door:** Located at `(19, 3)`. Entering warps to Cabin 4 Interior at `(2, 15)`.

## Cabin 3 Geometry & Mappings
- **Interior Layout:** Map 94 coordinates x=10 to x=13, y=11 to y=15.
- **Warp Exit:** Red carpet door tile is at `(12, 15)`. Walking Down through `(12, 15)` exits back to S.S. Anne 2F at `(23, 4)`.
- **NPCs:**
  - Boy at `(10, 13)` who mentions MACHOKE's STRENGTH.
  - MACHOKE at `(11, 12)` (cries: "Gwoh! Goggoh!").
- **Items:**
  - **Max Potion:** Located on the floor/carpet at `(12, 11)`. Retrieved on Turn 6415.

## Cabin 4 Geometry & Mappings
- **Interior Layout:** Map 94 coordinates x=0 to x=3, y=11 to y=15.
- **Warp Exit:** Red carpet door tile is at `(2, 15)`. Walking Down through `(2, 15)` exits back to S.S. Anne 2F at `(19, 4)`.
- **NPCs & Battle Status:**
  - **Sailor at (2, 11):** Facing Down. Roster: Horsea (Lv 17), Shellder (Lv 17), Tentacool (Lv 17). Defeated on Turn 6437 (earned �510).
  - **Sailor at (0, 13):** Facing Right. Roster: Shellder (Lv 21). Defeated on Turn 6444 (earned �630).


## Cabin 5 Geometry & Mappings
- **Interior Layout:** Map 94 coordinates x=20 to x=23, y=1 to y=5 (estimated based on entrance warp).
- **Warp Exit:** Red carpet door tile is at `(23, 5)`. Walking Down through `(23, 5)` exits back to S.S. Anne 2F at `(15, 4)`.
- **NPCs & Battle Status:**
  - **Boy at (22, 2):** Facing Down.
  - **Sailor at (22, 3):** Defeated on Turn 6467 (earned ¥510).
- **Items:**
  - **Item Ball at (20, 2):** Red/white Pok�ball sitting on floor.

## Cabin 6 Geometry & Mappings
- **Interior Layout:** Map 94 coordinates x=10 to x=13, y=1 to y=5 (estimated based on Cabin 5 offset, or identical structure).
- **Warp Exit:** Red carpet door tile is at `(12, 5)`. Walking Down through `(12, 5)` exits back to S.S. Anne 2F at `(11, 4)`.
- **NPCs & Battle Status:**
  - **Sailor at (12, 3):** Facing DOWN/LEFT. Walks to (11, 3) to challenge player. Dialogue: "Us sailors have POKéMON too!" Defeated on Turn 6497 (earned ¥540).
- **Items:**
  - **Item Ball at (10, 2):** Checkered floor tile mistaken for an item ball (refuted on Turn 6498).
  - **Item Ball at (10, 3):** Checkered floor tile mistaken for an item ball (refuted on Turn 6485).

## Cabin 7 Geometry & Mappings
- **Interior Layout:** Map 94 coordinates x=0 to x=3, y=1 to y=5 (estimated based on entrance warp).
- **Warp Exit:** Red carpet door tile is at `(2, 5)` and `(3, 5)`. Walking Down through `(2, 5)` exits back to S.S. Anne 2F at `(7, 4)`.
- **NPCs & Battle Status:**
  - **Fisherman at (0, 4):** Defeated on Turn 6524 (earned ¥595).
  - **Sailor at (0, 2):** Defeated on Turn 6538 (earned ¥600).
- **Items:**
  - **Item Ball at (0, 3):** Checkered floor tile mistaken for an item ball (refuted on Turn 6528).
## S.S. Anne 1F Hallway (Map 92) Layout & Geometry
- **Main Hallway:** Runs horizontally on rows 6 and 7 across columns 2 to 37. Yellow striped floor tiles.
- **Doors to Cabins:** Located on row 8 at columns:
  - **Cabin 1 Door:** `(31, 8)`
  - **Cabin 2 Door:** `(23, 8)`
  - **Cabin 3 Door:** `(19, 8)`
  - **Cabin 4 Door:** `(15, 8)`
  - **Cabin 5 Door:** `(11, 8)`
  - **Cabin 6 Door:** `(7, 8)`
- **Walkways & Transitions:**
  - **Right Walkway (columns 36-37, rows 8-15):** Connects to the staircase at `(37, 15)` leading up to 2F.
  - **Left Walkway (columns 26-27, rows 0-5):** Connects to the S.S. Anne Entryway (Map 91) at `(27, 0)`.
- **NPCs:**
  - **Sailor at (27, 5):** Stands near the left-hand walkway.
  - **Sailor at (9, 6):** Pacing near Cabin 5/6 area.

## Cabin 8 Geometry & Mappings (Door at 13, 11 on 2F Lower Hallway)
- **Interior Layout:** Map 94 coordinates x=10 to x=13, y=1 to y=5 (estimated based on entrance warp).
- **Warp Exit:** Red carpet door tile is at `(12, 5)` and `(13, 5)`. Walking Down through `(12, 5)` exits back to S.S. Anne 2F at `(13, 12)`.
- **NPCs & Battle Status:**
  - **Fisherman at (13, 4):** Facing LEFT. Dialogue: "Check out what I fished up!" Defeated on Turn 6613 (earned ¥595).
  - **Gentleman at (10, 2):** Facing Right. Pikachu Lv 23. Defeated on Turn 6623 (earned ¥1610).
- **Items:**
  - None (checkered floor pattern has no items).

## S.S. Anne 2F Lower Hallway (Map 94) Layout & Geometry
- **Main Hallway:** Runs horizontally on rows 11, 12, 13 across columns 2 to 37. Yellow striped floor tiles.
- **Physical Walkway Connections:**
  - **Left Walkway (column 2, rows 4-12):** Physically connects the 2F upper hallway (row 4) to the 2F lower hallway (row 12) on the same map. You can walk from upper to lower hallway via this path.
  - **Right Walkway (column 36, rows 6-9):** Runs vertically on column 36. This checkered orange/brown stairwell leads to the Captain's room.
- **Doors to Cabins:** Located on row 11 at columns:
  - **Cabin 7 Door:** `(9, 11)`
  - **Cabin 8 Door:** `(13, 11)` (Warp to Cabin 8 Interior at `(12, 5)`)
  - **Cabin 9 Door:** `(17, 11)`
  - **Cabin 10 Door:** `(21, 11)`
  - **Cabin 11 Door:** `(25, 11)`
  - **Cabin 12 Door:** `(29, 11)`
- **Floor-to-Floor Transitions & Staircases:**
  - **2F Left Staircase:** Located at `(2, 12)` in the lower hallway, warps the player to S.S. Anne 3F at `(19, 3)`.
  - **2F Upper Staircase:** Located at `(27, 4)` in the upper hallway, warps the player back to S.S. Anne Deck.


## Captain's Cabin (Map 95? or interior map) Layout & Geometry
- **Dimensions:** Approx x=0 to x=5, y=0 to y=7.
- **Key Coordinates:**
  - **Captain's Location:** `(4, 2)` (facing Left).
  - **Trash Can:** `(4, 1)` (reading "Yuck! Shouldn't have looked!").
  - **Exit Staircase Warp:** `(0, 7)`. Walking onto `(0, 7)` warps back to S.S. Anne 2F at `(36, 4)`.

## S.S. Anne Pier / Vermilion Dock (Map 95) Layout & Geometry
- **Vertical Left Pier:** Columns 18 and 19 running from row 27 down to row 35. Transitioning south past row 35 warps to S.S. Anne Entryway.
- **Horizontal Pier Connector:** Rows 26 and 27 running from column 18 to column 30.
- **Vertical Right Pier:** Columns 30 and 31 running from row 27 down to row 16, connecting to the Vermilion mainland.
- **Mainland Transition:** Row 15 columns 26-33 is the paved ground of Vermilion City. The transition back into Vermilion City's main overworld is at `(28, 14)` (near the Poké Mart).


<hr>

<h1><code>Locations/Route9</code></h1>

# Route 9 - Spatial Coordinates, Landmarks & Trainer Log

## Overworld Layout & Navigation
- **Western Entrance:** Connects to Cerulean City at `(39, 16)`.
- **Cuttable Bush:** Located at `(5, 8)`. This bush must be cut using HM01 (Cut) to unlock access to the eastern path.
- **Escape Gap (from bottom lane):** Standing at `(19, 14)` and walking UP through `(19, 13)` to `(19, 12)` allows players to exit the lower dead-end pocket and return to the main upper lanes.

## Key Items Found
- **TM30 (Teleport):** Retreived from a Poké Ball at `(10, 15)` inside the southern pocket.

## Trainer Roster & Coordinates
| Trainer Name | Location / Coordinates | Trainer Roster | Earnings / Turn | Notes |
|--------------|------------------------|----------------|-----------------|-------|
| JR. TRAINER♀ | (12, 10) / (13, 10)    | Oddish, Bellsprout (Lv 18) | ¥360 / Turn 7197 | Defeated! |
| Hiker Alan   | (45, 15)               | Geodude, Onix              | ¥735 / Turn 7280| Defeated! |
| JR. TRAINER♂ | (24, 7)                | Growlithe (Lv 21), Charmander (Lv 21) | ¥420 / Turn 7479 | Defeated! |
| Bug Catcher Conner | (40, 8)          | Bug Pokémon (unfought)                | ¥320 / Turn 7431 | Defeated! |
| JR. TRAINER♂ | (34, 7)                | Rattata (Lv 19), Diglett (Lv 19), Ekans (Lv 19), Sandshrew (Lv 19) | ¥380 / Turn 7528 | Defeated! |
## Ledge & Pockets Layout
- **Upper Pavement Lanes (Rows 8, 9, 10):** Main path going east/west.
  - Rows 8 & 9: Completely clear pavement going west from Column 20 to Column 0. Bypasses the trainer at (13, 10) by walking on Row 9.
  - Row 10: Blocked at (9, 10) by a mountain wall. Contains JR. TRAINER♀ at (13, 10) (facing down, defeated).
- **Ledge on Row 11 (Columns 10-19):** Blocks going UP from Row 12 (grass lane) to Row 11 (pavement). This ledge ends at Column 20, which is clear pavement. Note: The boundary at Column 45/46 on Row 6-10 is a solid rock cliff/mountain wall and is NOT a jumpable ledge from the west.
- **Grass Lane (Row 12, Columns 10-19):** Bounded by Row 11 ledge on top and Row 13 ledge on bottom. Blocked on the west (Column 9) by a mountain wall. To return to the upper lanes from here, walk east to Column 20, then walk UP to Row 11/10.
- **Row 13 Ledge & Gap (Columns 20-53):** Blocks going UP from Row 14 (lower pavement) to Row 12 (grass). This ledge has an **empirically verified open gap at Columns 29 and 30** (discovered on Turn 7376, verified on Turn 7451), allowing players to walk UP from (29, 14) to (29, 12).
- **Row 9 Ledge & Gap (Columns 20-25):** Blocks going UP from Row 10 to Row 8. This ledge has an **empirically verified open gap at Column 29** (discovered on Turn 7399), allowing players to walk UP from (29, 10) to (29, 8/9).
- **Lower Pavement Lane (Row 14/15, Columns 10-53):** Bounded by Row 13 ledge on top. Blocked on the west (Column 9) by a mountain wall. Contains Hiker Alan at (45, 15) and Hiker at (16, 15) facing right. Escape Gap is at (19, 14), walking UP through (19, 13) to (19, 12) into the grass lane.
## Empirical Navigation Realities
- **Column 42 Blockage on Row 12:** Empirically verified multiple times that Row 12 is completely blocked at Column 42 by a solid diagonal rock cliff face.
- **Ledge & Mountain Layout:** Row 9 is blocked at Column 42 by a solid rock wall. Columns 26-28 are also blocked on Rows 2-7 by a solid rock wall. Row 14/15 is open but Column 24-27 has a rock wall. Route 10 lower pocket is a dead end blocked by Row 16 rock wall.
- **Geographical Strategy:** Backtracking to Cerulean City on foot from Route 9's eastern sections is possible! On Turn 8921, we successfully backtracked by cutting the bush at (5, 8) and walking west on Rows 2-4 (which are completely clear on Columns 13-22 and do not have any one-way ledge blockages on those upper rows).
## Verified Obstacles & Navigation Limits (Turn 8878)
- **Column 41 Vertical Corridor:** Empirically verified to be completely open vertically with absolutely NO ledges or rock walls from Row 6 down to Row 14, providing a crucial north/south crossing corridor.
- **Row 13 Ledge Lip:** Continuous across Columns 40 to 53, blocking all upward (northward) movement from Row 14/15 on the eastern side.
- **Columns 24-27 Rock Wall on Row 14-15:** Blocks eastward movement on the lower lanes.
- **Column 19 Vertical Ledge on Rows 8-11:** Blocks westward (backtracking) movement on the upper lanes.
- **Column 24/25 Vertical Ledge on Rows 5-6:** Blocks westward (leftward) movement on the upper lanes.
- **Row 17 Water/River Barrier:** Row 17 on Route 9 contains animated river/water tiles (represented by '8788/9392' and '50f8/948d' under dx=0) which completely block foot traversal eastward across Columns 20 to 50.


## ROM Tile Map 2x Coordinate Scaling (Critical)
- **Vertical Scale Factor:** The raw tile map file `route9_tile_map.txt` is exactly **2x scaled** vertically relative to the in-game global coordinate grid reported by the harness.
  - `y_file = y_game * 2`  (maps to file rows `2 * y_game` and `2 * y_game + 1`)
- **Horizontal Scale Alignment:**
  - The horizontal alignment has no offset (dx = 0).
  - `x_file = x_game * 2` (maps to file columns `2 * x_game` and `2 * x_game + 1` since the file represents a 120-column grid, i.e., 60-tile wide map).

- **Route 9 East Pocket (Columns 45-46, Rows 6-7):**
  - **Column 44:** Open pavement. Does NOT block westward (leftward) movement.
  - **Column 46 Rock Wall:** Solid rock wall blocks all eastward (rightward) movement across Column 46 on Rows 4-7.
  - **Row 7 Ledge and Row 8 Diagonal Rock Wall Blockage:** Jumping DOWN from (45, 7) onto (45, 8) is blocked because (45, 8) is a diagonal rock corner tile.
  - **Escape Route:** You can simply walk Left (west) back across Column 44 onto Column 41/42 to exit the pocket. No soft-lock or warp is required.
## Verified Overworld Realities & Escape Routing (Turn 9772)
- **Continuous Ledge on Row 13:** Row 13 is a continuous downward-facing ledge from Column 10 all the way to Column 23, blocking all upward movement on the west/middle sections. Column 29 and Column 30 are the only open gaps in the Row 13 ledge.
- **Continuous Ledge on Row 11:** Row 11 contains a continuous downward-facing ledge from Column 10 to Column 19, blocking all upward movement on these columns.
- **Solid Wall on Column 24:** Column 24 contains a solid rock wall blocking all horizontal movement on Rows 11 to 15. Thus, the lower pocket of Route 9 (Columns 10-23, Rows 12-15) is completely dead-ended going east.
- **Solid Wall on Column 9:** Column 9 contains a solid rock wall blocking all horizontal movement on Rows 10 to 17.

- **Verified Row 9 Escape Corridor:** Row 9 is completely open pavement and grass from Column 29 all the way west to Column 0, providing a clear escape route back to Cerulean City.
- **True Escape Path from Lower Pocket:** To escape the lower pocket, walk to Column 19 on Row 14, walk UP Column 19 (which has no ledge lip on Row 13) to Row 12, walk Right to Column 29 Row 12, walk UP Column 29 through the gap to Row 9, and walk Left on Row 9 all the way to Cerulean City!

<hr>

<h1><code>Locations/Route10</code></h1>

# Route 10 - Map Layout, Ledges & Landmarks

## Overworld Layout & Structure
- **Dimensions:** Height = 36 blocks (144 tiles), Width = 10 blocks (40 tiles).
- **Global Alignment:** Route 10 starts at Column 50 of the global coordinate system.
- **Top Connection:** Connects West to Route 9 at the top-west.

## Verified Landmarks
- **Pokémon Center:** Located on the east side of Route 10, adjacent to the Rock Tunnel entrance. 
  - **Exterior Location:** Entrance Door is at (11, 19) (verified on Turn 10075).
  - **Interior Location:** Nurse Joy is behind the counter at (3, 2). Exiting from (3, 7) warps the player back to Route 10 East at (11, 20).
- **Rock Tunnel Entrance:** Located on Route 10 East at (8, 17) (physically verified on Turn 10283). Walking UP from (8, 18) warps the player into Rock Tunnel 1F at (15, 3).

- **Rock Tunnel South Exit / Lavender Town Connection:** Located at the bottom of Route 10.

## Terrain & Ledges
- **Eastern River:** Columns 54-58 are water/river (specifically Column 54 is the shore, Columns 55-58 are water with animated wave sparkles).
- **Ledge on Row 13:** A horizontal ledge facing DOWN runs across Row 13 (tiles y=12-15) from Columns 50 to 53.
  - Standing below the ledge (Row 14/15), you CANNOT walk UP to Row 12/13.
  - Thus, the pocket at (50, 14) to (53, 15) is a dead end from the south-west, but you can escape by walking Left back to Route 9.

## Navigational Strategy
- Row 8/9 is the open pavement path from Route 9 going east to Column 59 on Route 10.
- Column 52 and 53 on Row 9 are the only columns where you can walk down to the lower level of Route 10 (containing the grass lanes).
- Column 54 is mountain wall on rows 10 to 13, which blocks any eastward traversal on those lower rows.
## Verified Obstacles & Navigation Limits (Turn 8878)
- **Row 16 Rock Wall:** Completely solid and continuous across Columns 50 to 57, making Route 10's lower pocket (Columns 50-53, Rows 14-15) a strict dead end going south.
- **Row 13 Ledge:** Continuous across Columns 50 to 53, blocking all upward (northward) movement to the upper level of Route 10.

## ROM Tile Map 2x Coordinate Scaling (Critical)
- **Scale Factor:** The raw tile map file `route10_tile_map.txt` is exactly **2x scaled** relative to the in-game global coordinate grid reported by the harness.
- **Mapping Formula:** To map from in-game global coordinates `(x_game, y_game)` to the raw file indices `(x_file, y_file)`:
  - `x_file = (x_game - 50) * 2`  (maps to file columns `2 * (x_game - 50)` and `2 * (x_game - 50) + 1` since Route 10 starts at global `x_game = 50`)
  - `y_file = y_game * 2`        (maps to file rows `2 * y_game` and `2 * y_game + 1`)
- **Strict Spatial Consistency:** Each 1x1 in-game overworld tile corresponds to a 2x2 block of raw tiles in `route10_tile_map.txt`. All pathfinding and navigation scripts MUST apply this 2x multiplier before reading from or writing to the file representation.

<hr>