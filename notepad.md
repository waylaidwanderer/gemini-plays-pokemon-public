<h1><code>Main</code></h1>

Badges: Boulderbadge, Cascadebadge, Thunderbadge
Team (6/6) and HMs:
- Raticate (FANG) - Lv 20
- Wartortle (HYDRO) - Lv 30
- Meowth (MIDAS) - Lv 12
- Farfetch'd (DUX) - Lv 10 (Target for CUT)
- Pidgey (AERO) - Lv 30
- Drowzee (BAKU) - Lv 13 (Target for FLASH)
HM Tracking:
- CUT (HM01): Obtained and taught to DUX.
- FLASH (HM05): Obtained and taught to BAKU.
Inventory (Verified Turn 11227): ANTIDOTE x7, ESCAPE ROPE x1, POTION x2, POKé BALL x3, GREAT BALL x1, BICYCLE, HM05.
PC Storage: Zubat (ECHO) - Lv 10. Items: TOWN MAP, TM12, MOON STONE, HELIX FOSSIL, TM04, NUGGET, TM19, S.S. TICKET, TM28, OLD ROD, TM08, POTION x10, HM01, TM24.

<hr>

<h1><code>Locations/Pallet_Town</code></h1>

Room Layout (Player's Room):
- PC is at top-left: Monitor (0,0), Keyboard (0,1). Stand at (0,2) facing Up to use.
- SNES is in middle: TV (3,4), Console (3,5).
- Stairs down: (7,1).
Ash's House (Downstairs):
- Stairs up to room: (7,1)
- Mom: (5,4)
- Dining Table: (3,4) to (4,5)
Pallet Town Layout:
- Ash's House: (5,5)
- Gary's House: (13,5)
- Oak's Lab: (12,11)
- Route 1 (North Exit): Tall grass begins around X=10, Y=1.
Oak's Lab Layout:
- Oak: (5,2)
- Walkway to exit: X=4 and X=5.
- Table with Pokeballs: Y=3, X=6,7,8.
Gary's House Layout:
- Sister: (2,3)

<hr>

<h1><code>Mechanics/PC_Storage</code></h1>

Player's PC starts with 1 Potion in item storage.

<hr>

<h1><code>Locations/Route_1</code></h1>

Route 1 Layout:
- South exit to Pallet Town: (10,35) and (11,35).
- Path heads North through tall grass.

<hr>

<h1><code>Mechanics/Battle_Data</code></h1>

Battle Data & Mechanics:
- Professor Oak automatically heals the party after major story events (verified after first rival battle on Turn 52, and delivering parcel/receiving Pokédex on Turn 166).
- Catching Mechanics: Poké Balls can fail even on full HP, very low-level Pokémon (e.g., Lv 3 Pidgey broke out at full HP, Turn 235). Weaken them first if possible, or expect to use multiple balls. Full HP catches fail frequently even on Lv 2s. Weakening to red HP allowed immediate catch (Turn 311).
- Catching Mechanics: Poké Balls can fail even when the target is in the yellow HP zone (Turn 770).
- Switch-Training: Swapping a Pokémon out shares the EXP among all participants. Odd EXP values are truncated (e.g., 23 EXP total gave 11 EXP each to two Pokémon, Turn 437).
- Free Switch-In: When an enemy faints and the game asks "Will [Player] change POKEMON?", selecting YES allows sending out a new Pokémon without taking a hit that turn. Ideal for sharing EXP with weak Pokémon.
- Stat Stages: Stat-boosting moves like Harden display 'Nothing happened!' once the stat has reached its maximum level (verified Turn 648).
- Stat Mechanics: Stat-lowering moves display "failed!" once the target's stat reaches its minimum level. String Shot failed on 3rd use (Turn 1045) and Leer failed on 2nd use (Turn 1084).
- Speed Mechanics: Stat drops significantly impact turn order. A Lv 7 Pidgey outspeeds a Lv 10 Caterpie but is outsped after one String Shot (Speed -1 stage) (Turn 1038).
(Note: Early game specific damage and EXP scaling logs have been archived to Archive/Early_Game_Battle_Data)
- Accuracy Mechanics: Tackle has 95% accuracy in Gen 1, which explains occasional misses without evasion modifiers (e.g., missed twice in a row on Turn 1218/1219). It is not just the 1/256 miss bug.
- Overworld Mechanics: Defeated trainers reset to their original spawn positions when you leave and re-enter a map. For example, a Lass ran to (20, 4) to challenge me, but reset to her original location at (23, 4) after I traveled to Pewter City and back (Turn 1208).
- Status (Sleep): Waking up consumes the entire turn. The opponent can immediately act afterwards. If they use a sleep move (like Sing), they can put the Pokémon right back to sleep before it can attack, creating a stunlock loop.
- Damage Log: Lass's Clefairy (Lv 14) Pound deals approximately 3-5 damage per hit to Squirtle (Lv 15) (Verified Turn 2092).
- Move Cursor Memory: Confirmed that the battle move cursor remembers its position from the last time a move was selected during the current battle (Turn 2095).
- Status (Sleep): Sing has a chance to miss. Verified Turn 2103 when Clefairy used Sing on AERO's switch-in and AERO did not gain the SLP status.
- Damage Log: Pidgey (Lv 14) Gust deals ~45% HP to Lass's Clefairy (Lv 14). Clefairy's Pound deals exactly 8 damage to Pidgey (Lv 14). (Verified Turn 2104).
- Confusion Damage: A Lv 15 Pidgey hitting itself in confusion dealt 9 damage to itself (Turn 2230).
- Damage Log: Water Gun (Lv 15 Squirtle) deals ~95% HP to a Lv 10 Zubat (Turn 2243).
- Damage Log: Lv 10 Geodude Tackle deals ~6 damage to a Lv 12 Rattata (Turn 2267).
- Type Effectiveness: Bug is Super Effective against Poison in Gen 1 (verified Turn 2351: Leech Life vs Zubat).
- Damage Log: Pidgey (Lv 16) Gust deals ~55% HP to Lass's Oddish (Lv 11) (Turn 2458).
- Damage Log: Water Gun (Lv 16 Wartortle) deals ~75% HP to a Lv 12 Ekans (Turn 2486).
- Turn 2763: In battle with Super Nerd, switching to FANG (Rattata, Lv 12) against Voltorb to share EXP.
- Damage Log: Lv 11 Voltorb Tackle deals exactly 4 damage to a Lv 12 Rattata (Turn 2766).
- Status (Disable): In Gen 1, if a move is disabled, the game still allows you to select it in the battle menu. If you do, the turn is wasted and the text "[MOVE] was disabled!" appears (Verified Turn 5929/5930).
- Damage Log: Bubble (Lv 23 Wartortle) deals ~55% HP to a Lv 12 Voltorb (Turn 5934).
- Damage Log: Mankey (Lv 18) Karate Chop (Critical Hit) deals exactly 14 damage to a Lv 25 Pidgey. Pidgey's Gust deals ~80% HP to the Mankey (Turn 6193).
- Damage Log: Slowpoke (Lv 17) Confusion deals exactly 6 damage to a Lv 25 Wartortle (Turn 6235).
- Wrap Mechanics: Wrap is a multi-turn trapping move. While wrapped, the text 'Enemy [PKMN]'s attack continues!' appears each turn. The player's turn is skipped entirely and the battle menu does not appear until the move ends (Verified Turns 6296-6299 against Ekans).
- Damage Log: Machop (Lv 17) Karate Chop (Critical Hit) deals exactly 10 damage to a Lv 26 Wartortle (Turn 6422).
- Damage Log: Drowzee (Lv 17) Pound deals exactly 4 damage to a Lv 26 Pidgey (Turn 6430).
- Damage Log: Shellder (Lv 16) Tackle deals exactly 3 damage to a Lv 26 Wartortle. Wartortle's Bite deals ~30% HP to Shellder (Turn 7092).
- Damage Log: Bubblebeam (Lv 29 Wartortle) deals ~90% HP to a Lv 23 Pikachu (Turn 9160).
- Damage Log: Voltorb (Lv 21) Sonicboom deals exactly 20 damage to a Lv 18 Rattata (Turn 9195).
- Damage Log: Thundershock (Lv 24 Raichu) deals exactly 27 damage to a Lv 29 Wartortle (Turn 9225). Bubblebeam (Critical Hit) dealt ~75% HP to Raichu.

<hr>

<h1><code>Routing/Route_1</code></h1>

Route 1 Constraints & Navigation:
- Northbound (Pallet to Viridian): Use the Eastern path.
  - Ledge 1 (Y=27): Gaps at X=6, 7, 8.
  - Ledge 2 (Y=19): Gap at X=9.
  - Ledge 3 (Y=13): Gaps at X>=14. Dark green leaf tiles (Dense Bushes) are solid.
  - Ledge 4 (Y=5): Gaps at X>=14.
- Southbound (Viridian to Pallet):
  - Western path is blocked by a white fence at the top (X=3).
  - Use central/eastern paths and jump down ledges.
  - Obstacle at (4,13)/(5,13) requires shifting East to X=6 to jump ledge at (6,13).
  - Obstacle at Y=23 requires shifting East to X=16 to jump ledge at (16,23).
  - Exit to Pallet Town is at (10,35) and (11,35).

<hr>

<h1><code>Locations/Viridian_City</code></h1>

Viridian City Points of Interest:
- South Exit to Route 1: (21,35)
- Sign at (21,29)
- Pokémon Center Door: (23,25)
- Poké Mart Door: (29,19) (Approach from (29,20))
- Ledge at Y=27 blocks Northbound travel. The gap to bypass it is at X=19.
- Path North to Route 2: Clear path found at X=18.
- Sign at (17,17).
- Old Man at (17,9) no longer blocks the path after delivering Oak's Parcel.
- North exit to Route 2 is located around X=18, Y=0.

<hr>

<h1><code>Locations/Pokemon_Center</code></h1>

Pokémon Center Layout (Standard):
- Entrance/Exit: (3,7) and (4,7)
- Healing Counter (Nurse Joy): Stand at (3,3) facing Up.
- PC: Located at the far right of the room. Monitor is at (13, 3). The tile directly below it at (13, 4) looks like a keyboard but is walkable. To interact, stand at (13, 4) and face Up.
Mt. Moon Pokémon Center specifics:
- NPC at (11, 2) is the Cable Club attendant ("reserved for 2 friends...").
- Wandering NPC in bottom right area is the Magikarp salesman (offers a Pokémon for 500 Yen).

<hr>

<h1><code>Locations/Poke_Mart</code></h1>

Poké Mart Layout (Viridian City):
- Entrance/Exit: (3,7) and (4,7)
- Cashier: Standing at (0,5) facing Right.
- Counter: (1,5) has the register. (0,6) and (1,6) are also counter blocks.
- Interaction: Stand at (2,5) facing Left, interact with the register/cashier at (1,5) to open the shop menu.
- Other NPCs: Bug Catcher wandering around the right side of the store.
- Inventory (Viridian City): Poké Ball (¥200), Antidote (¥100), Parlyz Heal (¥200), Burn Heal (¥250). Note: Potions are NOT sold here!
Poké Mart Layout (Pewter City):
- Inventory (Pewter City): Poké Ball (¥200), Potion (¥300), Escape Rope (¥550), Antidote (¥100), (more items exist).

<hr>

<h1><code>Quests/Main_Story</code></h1>

Current Task: Traverse Rock Tunnel.
- High-level goal: Reach Lavender Town via Rock Tunnel (Route 9 -> Route 10).
- Status: Drowzee (BAKU) acquired and taught FLASH.
- To-Do:
  1. Execute Macroscopic Loop: Head North through Route 2 West, Pewter City, Route 3, and Mt. Moon to reach Cerulean North.

<hr>

<h1><code>Locations/Route_2</code></h1>

Route 2 Layout:
- Connects Viridian City (South) to Pewter City (North).
- Southern Section: Exits Viridian City at (8, 71).
- Main Path Constraints (Viridian to Gatehouse):
  - Ledge blocks X=0-7 at Y=61. Use X=8 or X=9 to go North.
  - Trees block X=8-9 at Y=56. Use X=3 to bypass.
  - Ledge blocks X=0-7 at Y=47. Use X=8 or X=9 to go North.
  - At Y=44, there is a paved path. The building at (3, 43) is the Viridian Forest South Gatehouse, connecting Route 2 (3, 43) to Viridian Forest (17, 47).
- Viridian Forest Gatehouse Interior: South exits at (4,7) and (5,7) warp to Route 2 (3, 44). North exit at (5,0) warps to Viridian Forest (17, 47). Layout: Counter divides room vertically at X=6. EMPIRICAL TEST COMPLETE (Turns 11878-11883): Entered from Route 2 (3, 43), navigated the interior, and took the North exit at (5,0) to successfully warp to Viridian Forest (17, 47).
- Northern Section (post-Forest): North Gatehouse connects Viridian Forest (2, 0) to Route 2 (3, 11). Path North at X=3 is a dead end nook at (3, 7). The clear path continues North along the East side at X=8. Exit to Pewter City is at (8, 0).
- East Side Topology: The East side is completely split into two disconnected segments by a solid mountain wall at Y=9. Segment 1 (Y=0 to 8) contains the tree at (15, 1) and is ONLY accessible from Pewter City. Segment 2 (Y=10 to 72) contains Diglett's Cave at (12, 9), Trade House, and Gatehouse. You CANNOT travel directly from Diglett's Cave North to Pewter City. You must go South and cross to the West side.
- East Side: The building South of Diglett's Cave at Y=19 is a Trade House. Cuttable tree at (15, 22) leads South to a Gatehouse at (16, 35). Inside is Oak's Aide who gives HM05 Flash (requires 10 Pokémon). The ledges at Y=27 and Y=31 have walkable gaps at X=17.
- Southbound on East Side: The path dead-ends at Y=69. Cuttable trees at (12, 60) and (12, 68) allow crossing West back to the main Route 2 path.
- Note: Found a Moon Stone in an item ball at (13, 54) (Picked up Turn 11845).

<hr>

<h1><code>Scratchpad/Route2_Exploration</code></h1>

[Turn 217] Re-entered Route 2 at (8, 71). Heading North to find tall grass for catching new team members. Avoid Y=72, as it triggers the warp back to Viridian.

<hr>

<h1><code>Mechanics/Menu_Behavior</code></h1>

Menu Cursor Memory: In many menus (like the Start menu and Party action menu), the cursor remembers its last selected position rather than resetting to the top. Always visually verify the cursor's starting position before executing blind button sequences (Verified Turn 449-451).
- Battle Item Menu: The cursor resets to the top (first item) at the start of a new battle. It only remembers its position *during* a single battle (Verified Turn 1338/1353). Attempting to use a key item like the Town Map triggers Professor Oak's warning and wastes a turn. Always verify cursor position!
- Party Menu Cursor: The cursor wraps around. Pressing Up from the 1st slot moves the cursor to the last slot (e.g., 5th slot) (Verified Turn 1251-1252).
- Battle Item Menu: Pressing A on an item in battle uses it immediately; there is no USE/TOSS sub-menu like in the overworld.
- Battle Move Menu: The move list is a single vertical column (1x4), NOT a 2x2 grid. Pressing Down moves down the list. Pressing Right does nothing. (Verified Turn 2089).
- Battle Move Menu: The cursor resets to the top (first move) at the start of a new battle, just like the Item menu. It only remembers its position *during* a single battle. (Verified Turn 2704: Started new battle, cursor was on Tackle, not Bubble/Water Gun).
- Party Swap Mechanic: In Gen 1, 'Select' does NOT swap party members in the overworld. You MUST press 'A' on a Pokémon, select 'SWITCH' from its sub-menu, move the cursor to the target Pokémon, and press 'A' again. Verified on Turn 6189.
- In-Battle Party Menu Cursor Memory: Confirmed (Turn 6281). When opening the 'PKMN' menu during a battle, the cursor remembers its last position from when the menu was previously accessed in that same battle (e.g., if you sent out slot 2 previously, the cursor starts on slot 2 next time you open the menu).
- Item Usage: Using an item from the bag on a Pokémon returns the game to the item menu after the effect text completes, NOT back to the party menu.
- Auto-Advancer Trap: The system's automatic text advancement uses 'B' to skip dialogue. This automatically selects 'NO' on any YES/NO prompts (like the Fan Club Chairman). Use custom tools (like chunk_a) to manually press 'A' and safely select 'YES'.

<hr>

<h1><code>Routing/Viridian_City</code></h1>

Optimal Navigation Paths in Viridian City:
- Route 2 <-> Pokémon Center: From PC door (23,25), step Down to (23,26), walk West to X=18, then straight North to Y=0. This path avoids the Pokémon Center building wall at Y=25.

<hr>

<h1><code>Locations/Viridian_Forest</code></h1>

Viridian Forest Layout:
- South Entrance/Exit is at (17, 48), connecting back to the Route 2 Gatehouse.
- Signboard spotted at (18, 45).
- Bug Catcher NPC at (16, 43). Mentions coming with friends.
- Path 1 (West of Entrance): Leads Northwest through tall grass. Contains a sign at (16, 32) and an Item Ball at (12, 29). Re-exploring this path as previous assumption of it being a dead end may be false.
- The far West path (X=1 to X=8) is a dead end pocket bounded by trees at Y=29 and Y=33. To progress, route East from the Entrance by walking North to Y=43, then East.
- Path 2 (East of Entrance): Leads East through tall grass at Y=43. A sign is located at (24, 40). A Bug Catcher NPC is at (27, 40) facing South, does not battle.
- Further North on Path 2: Bug Catcher at (27, 33) defeated. Path continues North as a 3-tile wide grass path (X=25 to X=27) extending to Y=20.
- At Y=19, the path turns into clear ground. A Bug Catcher is located at (27, 19) facing Left (Defeated Turn 666). A sign is at (26, 17) mentioning evaluating the Pokédex via PC. The path squeezes North at X=25. Found an Antidote in an Item Ball at (25, 11).
- At Y=8 (between X=19 and X=25), a wall of trees blocks North. Going West through the tall grass leads to a vertical column of tall grass at X=16, X=17, X=18. The North end of this column (Y=1 to Y=5) is a dead-end clear ground pocket. The main path continues South through the tall grass at X=16..18. The East path from X=25 dead-ends at X=32.
- Following the tall grass South at X=16..18, the path turns West at Y=16..19, leading to clear ground. There is a decorative dirt patch at (13, 19) (verified nothing happens when interacted with). The path is blocked West at X=10 by trees, and South at Y=21 by trees. The path continues North through tall grass starting at X=11..13, Y=17, reaching Y=2, then turns West to X=6, and South down a narrow column of tall grass. At Y=18, it turns West, then South to Y=22, then West to X=1, and finally North all the way up the West edge through tall grass. X=2 is blocked at Y=19. Follow X=1 North to (1, 0), then Right to (2, 0) and Up to warp to the Exit Gatehouse, which connects Viridian Forest (2, 0) to Route 2 (3, 11).

<hr>

<h1><code>Locations/Pewter_City</code></h1>

Pewter City Layout:
- South Exit to Route 2: Located at (18, 35).
- Main path North at X=18 is blocked by trees at Y=21. Use X=19 to bypass.
- Sign at (19, 29) confirms switch-training mechanic.
- Pokémon Center: West side of the main path, sign says "POKé" at (14, 25).
- Pewter Gym: Building roof starts at (14, 16). The entrance is further South.
- Poké Mart: Located at (23, 17).
- Fast Travel Warps: (13, 17) is a trap/fast-travel warp that teleports you to Route 3 (63, 0). (11, 17) is the arrival point from Route 3. Avoid stepping on (13, 17) when moving North/South; instead route through X=10 and Y=18 to bypass it.
- North/South Crossing: To travel between North and South Pewter, stay on the main paths. Avoid the dead-end ledges.
- Navigation to Center: The Center door is at (13, 25).
- The Poké Mart front door at (23, 17) must be approached from the south. Use the vertical path at X=19, then walk east along Y=18 to reach the door.

<hr>

<h1><code>Locations/Pewter_Gym</code></h1>

Pewter Gym Layout:
- Entrance: (4, 13) and (5, 13).
- Gym Statues: (3, 9) and (6, 9).
- Gym Trainer (Jr. Trainer M): Located at (3, 6) facing Right.
- Gym Leader (Brock): Expected further North.

<hr>

<h1><code>Locations/Route_3</code></h1>

Route 3 Layout:
- Connects Pewter City (West) to Mt. Moon (East).
- The route is divided into two East-West lanes by one-way ledges (jumping South only).
- Northern Lane (Y=4 to Y=6): The main path East. You MUST use this to reach Mt. Moon and the tall grass. To enter it from the West, use the gap in the Y=7 ledge at X=11.
- Southern Lane (Y=14 and below): A return path West to Pewter City. Bypasses the trees at X=23. Plain ground, no encounters.
- Tall Grass (Route 3 pit): Divided into Western and Eastern pits by a mountain wall at X=38. Bounded by trees to the West (X=23), one-way ledge to the North (Y=7). The southern boundary (Y=14) is blocked by trees/cliffs. The exit back to the Northern Lane is a gap in the Y=7 ledge at (27, 7).
- Northern Lane Eastward: Blocked at X=28 by a mountain wall. To bypass it, jump South over the Y=7 ledge into the tall grass pit, walk East, and use the ramp at (37, 7) to return to the Northern Lane.
- Returning West to Pewter City: You cannot walk West continuously on the Northern Lane because of the X=33 wall. You must jump South into the tall grass pit. (Path West currently unverified).
- Far East Section: The mountain wall is at X=50 (approx). To reach Route 4, you MUST jump South over the ledge into the eastern tall grass pit, walk East, and use the ramp at (59, 7) to return to the Northern Lane. Verified turn 10333. From (59, 4), walk North to transition to Route 4.
- Mt. Moon Entrance: The true Mt. Moon entrance is on Route 4. Transition to Route 4 by walking North past Y=0 near X=60.
- Gap in the Y=11 ledge at X=15 allows returning North to the Y=10 path.
Trainers:
- Lass at (23, 4) facing Down.
- Bug Catcher at (24, 6) facing Right.
- Youngster at (22, 9) facing Up.
- NPC (Blue sprite, likely a Lass) at (33, 10) facing Down.
- Lass at (15, 9) facing Left. Uses Pidgey.
- Trap Ledge: Jumping South over the ledge at Y=7 (X=58/59) lands you in a 2x1 gap above obstacles. Escape by walking East into the tall grass at X=60.
- Route 4 Connection: Walking North past Y=0 around X=60 leads to Route 4. The area I previously mistook for Pewter City is actually Route 4. The Pokémon Center there is the Mt. Moon Pokémon Center at (11, 5). The true Mt. Moon entrance is on Route 4, not Route 3.

<hr>

<h1><code>Scratchpad/Training_Plan</code></h1>

Current Training Plan:
- FANG (Lv 18, 45/45 HP). Keep sharing EXP.
- HYDRO (Lv 29) and AERO (Lv 29) are strong but weak to Electric. FANG is the only neutral Pokemon to Electric on the team.
- Switch FANG in to take neutral hits and share EXP.

<hr>

<h1><code>Archive/Early_Game_Battle_Data</code></h1>

Early Game Damage & EXP Logs:
- Wild Lv 2 Pidgey yields 15 EXP.
- Wild Lv 3 Pidgey yields 23 EXP.
- Wild Lv 3 Rattata yields 24 EXP.
- Weakening: Tackle from Lv 7 Squirtle deals ~50-60% damage to Lv 3 Pidgey.
- Damage Scaling: Lv 4 Pidgey's Gust deals ~3 damage to Lv 8 Squirtle, ~5 on crit.
- Weakening: Tackle from Lv 6 Rattata deals ~40-50% damage to Lv 5 Caterpie.
- Damage Scaling: Lv 6 Pidgey's Gust (Crit) deals ~80% damage to Lv 3 Caterpie.
- Gym Trainer Sandshrew (Lv 11): Scratch deals ~7 HP to Lv 10 Squirtle. Bubble deals ~16 HP.
- Damage Scaling: Lv 7 Pidgey's Gust deals ~50-60% damage to Lv 10 Caterpie.
- Damage Scaling: Lv 10 Caterpie's Tackle deals ~4-5 damage to Lv 7 Pidgey.
- Damage Scaling: Lv 10 Caterpie's Tackle (Crit) deals 7 damage to Lv 8 Pidgey.
- Damage Scaling: Lv 11 Ekans's Wrap deals ~2-3 damage per turn to Lv 9 Pidgey.
- Damage Scaling: Lv 10 Pidgey's Gust (Crit) deals ~60-70% damage to Lv 9 Weedle.
- Damage Scaling: Lv 9 Weedle's Poison Sting deals 3 damage to Lv 10 Pidgey.
- Speed Mechanics: A Lv 10 Rattata outspeeds a Lv 11 Pidgey (Turn 1134).
- Damage Scaling: A Lv 10 Rattata's Tackle deals ~8 damage to a Lv 11 Pidgey (Turn 1134).
- Damage Scaling: A Lv 10 Nidoran♂'s Tackle deals 5 damage to a Lv 13 Squirtle (Turn 1146).
- Damage Scaling: Lv 11 Pidgey's Gust deals ~50-55% damage to Lv 11 Caterpie (Turn 1210).
- Damage Scaling: Lv 11 Caterpie's Tackle (Crit) deals 6 damage to Lv 11 Pidgey (Turn 1210).

<hr>

<h1><code>Scratchpad/Route3_Encounters</code></h1>

Route 3 Tall Grass (X=24 to X=32, Y=10 to Y=13):
- Encounters table:
  - Pidgey (Lv 6, Lv 8) - Yields ~47 EXP.
  - Spearow (Lv 5, Lv 6, Lv 7) - Caught Lv 6 at low HP (TALON).
- Tall Grass Pit (East of X=23): Jigglypuff (Lv 5) - Uses Sing.
- Status (Sleep): Pokémon cannot act while asleep. Waking up in Gen 1 consumes the entire turn. Tested against Jigglypuff: Sleep lasted from Turn 1669 to Turn 1675 (6 turns). Since waking up consumes the turn, the opponent can immediately re-apply sleep before you can act (observed Turn 1677), creating a potential stunlock loop.

<hr>

<h1><code>Locations/Route_4</code></h1>

Route 4 Layout (West of Mt. Moon / Pre-Cerulean):
- Connects Route 3 (West) to Mt. Moon (East).
- Pokémon Center located at (11, 5).
- Path West of the PC terminates at a solid rock wall at X=3 and Y=3. This is a dead end.
- Mt. Moon cave ENTRANCE is located at (18, 5), East of the Pokémon Center. Signpost at (17, 7).
- Ledge Trap: South of the entrance at (18, 5), there are one-way ledges at Y=9 and Y=13.
- TRAP WARNING: Jumping South over the ledges at (17, 9) and (17, 13) traps you in a lower corridor (Y=14/Y=15). This corridor is blocked to the East by a Mountain Wall at X=20 and bounded South by a cliff at Y=16. The only open path is WEST, which forces you back to Route 3 (X=61, Y=0)! Do NOT jump these ledges unless you want to return to Pewter City.
- East Section (Post-Mt. Moon): Exited cave at (24, 5). The path East to Cerulean City is fragmented by tall grass and ledges.
- Route to Cerulean: Avoid tall grass by jumping South over Y=9 ledge. Follow Y=10 East until X=61. Go UP ramp at (61, 9) to reach Y=8. Walk East along Y=8 until X=79.
- Path to Cerulean North/South: Jumping South over the Y=9 ledge at X=79 puts you on the Y=10 paved path entering Cerulean South. From there, you can seamlessly reach Cerulean North via the gap in the ledge at (8, 15).
- RETURN TO MT. MOON BLOCKED: From Cerulean South (Y=10), the path West back to Mt. Moon is permanently blocked by a vertical wall of Dense Bushes at X=75.
- Topology Update: The B1F exit ladder in Mt. Moon at (27, 3) directly connects to the Route 4 East exit at (24, 5).

<hr>

<h1><code>Locations/Mt_Moon</code></h1>

Mt. Moon Layout & True Path:
- Entrance: 1F (14, 35) from Route 4.
- 1F Path: North to Y=22 -> East to X=20 -> North to Y=15 -> East to X=30 -> North to Y=7 -> West to X=14 -> South to Y=17 -> West to X=5 -> North to ladder DOWN at (5, 5).
- B1F Path: Arrive at B1F (5, 5). Walk East along Y=17 to X=21. Take ladder DOWN at (21, 17).
- B2F Path (Part 1): Arrive at B2F (21, 17). North to Y=14 -> East to X=26 -> South to stairs UP at (26, 15) -> East across raised platform to stairs DOWN at (32, 15).
- B2F Path (Part 2): East to X=34 -> South to Y=31 -> West all the way to X=7 -> North to Y=17 -> East to X=12 -> North to stairs UP at (12, 9).
- B2F Fossil Area: Defeat Super Nerd at (12, 7). Fossils are at (12, 6) and (13, 6).
- Exit Route: From Fossil Area, navigate to the exit ladder at (5, 7). To reach it: Walk East to X=13, North to Y=4, West to X=3, South down stairs at (3, 5), East to X=5, South to ladder at (5, 7).
- B1F Exit Corridor: Arrive at B1F (23, 3). Walk East to ladder UP at (27, 3), which exits to Route 4 East.

Dead Ends (Do not visit):
- 1F South-West (X=2-12, Y=24-34).
- 1F (17, 11) Ladder: Leads to a dead-end section of B1F and B2F.
- 1F (25, 15) Ladder: Leads to a dead-end section of B1F and B2F.
- B2F Raised Platform South-West: Contains Team Rocket Grunt but no exit.
- B2F East Elevated Platform (South-East area): Dead end bounded by rocks.

<hr>

<h1><code>Scratchpad/MtMoon_Encounters</code></h1>

Mt. Moon Trainer Encounters:
- Trainer at (30, 4): Lass with Oddish Lv 11, Bellsprout Lv 11 (Defeated Turn 2464)
- Trainer at (29, 11): Team Rocket Grunt with Zubat Lv 12, Ekans Lv ? (Turn 2482)
- Trainer at (30, 27): Bug Catcher with Caterpie Lv 10 (Turn 2546)
- Trainer at 1F (24, 31) on East Elevated Platform: Super Nerd with Magnemite Lv 11 (Defeated Turn 2752, empirically verified location on Turn 4715)
- Trainer at (13, 16) on 1F lower floor: Youngster with Rattata Lv 10, Zubat Lv 10 (Defeated Turn 3101)
- Trainer at (5, 6) on 1F mid-west section: Youngster (Defeated ~Turn 4493)
- Trainer at B2F (29, 17): Team Rocket Grunt with Raticate Lv 16 (Defeated Turn 4513)
- Wild Encounters: Geodude (Lv 8) found on 1F.
- Trainer at B2F (11, 16): Team Rocket Grunt with Zubat, Rattata, Zubat (Defeated Turn 5914)
- Trainer at B2F (12, 8): Super Nerd with Grimer Lv 12, Voltorb Lv 12, Koffing Lv 12 (Defeated Turn 5939)

<hr>

<h1><code>Scratchpad/MtMoon_Mechanics</code></h1>

Mt. Moon Mechanics (Finalized):
- Elevation: 1F has multiple elevations, but they are NOT strictly tied to floor color (Brown vs Purple). Elevation changes are marked exclusively by cliffs (black shadow lines) or stairs. A cliff indicates a drop in elevation, regardless of the floor colors it separates.
- Cliffs: Boundaries between Raised and Lower floors are impassable cliffs, marked by black shadow lines.
- Solid Walls: Light blue rock walls block movement on the same elevation.
- Stairs: Walkable/Stairs_Up (horizontal lines) connect Lower to Raised floors. (Object at 15,23 is a solid sign, tested Turn 4308).
- Ladders: Warp/Ladder_Down connect floors. They do not always align vertically:
  - 1F (25, 15) <-> B1F (25, 15)
  - 1F (17, 11) <-> B1F (25, 9)
  - B1F (17, 11) <-> B2F (25, 9)
  - B1F (13, 27) <-> B2F (15, 27)
- Map topology details have been migrated to Locations/Mt_Moon to strictly separate mechanics from locations.
- Hypothesis: The true path to the fossils may lie in the unmapped lower floor North of the B2F (32, 15) stairs, which is accessed via the 1F (5, 5) ladder.
- Currently trapped on B1F Lower Floor (purple floor). At B1F (17, 17), East is blocked by a blue rock wall at X=18. Routing North to map the area.

<hr>

<h1><code>Locations/Cerulean_City</code></h1>

Cerulean City:
- Connected to: Route 4 (West), Route 24 (North), Route 9 (East), Route 5 (South).
- Pokémon Center: Located at (19, 17).
- Poke Mart: Located south of the Gym? Need to verify.
- Gym: Cerulean Gym (Water type, Leader Misty). Entrance located at (30, 19).
- Robbed House: Located at (27, 11). Exit to backyard allows bypassing the Guard at (28, 12).
- Bike Shop: Located at (13, 25)? Need to verify.
- East Exit (Route 9): Accessible by walking East through the backyard of the Robbed House. The path to Route 9 is a corridor of grass at Y=16 and Y=17 bounded by white fences at Y=15 and Y=18. (Empirically verified Turn 12273: No cuttable tree here).
- South Exit (Route 5): The path South is blocked by a Cuttable Tree at (19, 28). You must stand at (19, 27) and use CUT to access the southern path out to Route 5.
- Off-screen limits: North (Route 24) transition around Y=0. West (Route 4) transition around X=0. South (Route 5) transition around Y=35. East (Route 9) transition around X=39.
- Bike Shop: Located at (13, 25). Inside, there is an NPC at (5, 4) and some bikes on display.

<hr>

<h1><code>Locations/Route_24</code></h1>

Route 24 Layout:
- Connects Cerulean City North exit (Nugget Bridge) to Route 25 (East to Bill's House).
- Nugget Bridge (X=11) ends at Y=16.
- Defeated 5 contest trainers and a Team Rocket Grunt on the bridge.
- North of the bridge, a one-way ledge at Y=7 blocks Northward movement on the West side (X=7 to X=12).
- An item ball is visible on the raised plateau at (10, 5). Currently unreachable from below the ledge.
- The path North continues on the East side (X=14, X=15), but dead ends at Y=4 due to a mountain wall at Y=3.
- To proceed East to Route 25, use the paved path at Y=8 / Y=9 (East of X=14).
- Tall grass is present on the West side (X=7 to X=9, Y=10 to Y=15).
- Returning South across Nugget Bridge requires zig-zagging between X=10 and X=11 to bypass the solid collision of the defeated trainers remaining on the bridge.

<hr>

<h1><code>Locations/Route_25</code></h1>

Route 25 Layout:
- Connects Route 24 (West) to Bill's House (East). Main path starts at Y=8/Y=9.
- One-way ledge along Y=7 ends at X=8, allowing Northward access.
- Navigating East requires bypassing tree blockades at X=10, X=16, and X=21.
Trainers & Objects:
- Hiker at (8, 4) facing Down.
- Hiker at (13, 7) (Defeated).
- Youngster at (18, 4) (Defeated).
- Lass at (19, 8) (Defeated).
- Youngster at (18, 5) facing Down. Sightline blocked by tree at (18, 6).
- Hiker at (23, 9) (Defeated).
- Jr. Trainer M at (24, 4) facing Down. (Defeated, lured to 24, 6).
- Item ball at (22, 2). Uncollected (behind the Jr. Trainer M).
- Youngster at (32, 3) facing Left. Sightline Y=3, X<32. (Defeated, currently at 31, 3).
- Lass at (37, 4) facing Left. (Defeated).
- Bill's House is at X=44/X=45. Entrance is at (45, 3).
- Hiker at (14, 2) facing Down. Sightline Y=3, Y=4 (blocked at Y=5 by Tree Top).
- The Hiker at (8, 4) facing Down has his sightline blocked by a dense bush at (8, 7). The paved path at Y=8 is safe to traverse.
- West Exit to Route 24 is at X=0, Y=8/9.

<hr>

<h1><code>Mechanics/Overworld</code></h1>

Survival Rule: Always verify inventory (Potions/Antidotes) before entering dungeons or long routes to prevent forced retreats.
Survival Rule 2: If a Pokémon is poisoned, use an Antidote IMMEDIATELY after battle. Overworld poison damage (1 HP per 4 steps) is lethal.
- Cut (HM01): In Gen 1, you cannot simply press 'A' while facing a cuttable tree to use it. You must open the Start Menu -> POKéMON -> select the Pokémon with Cut -> select CUT. Note: CUT can also remove tall grass around the player. If you use it while not explicitly facing a tree (by bumping into it first), it may just cut grass and give the success message while leaving the tree intact. Always bump into the tree to face it before using CUT.
- Rule: Always empirically test unknown tiles with tools like CUT before definitively concluding they are solid walls. EMPIRICAL TEST COMPLETE (Turn 11835): Dense bushes (e.g., at Route 2 (12, 53)) return "There isn't anything to CUT!" and are verified as solid walls, not cuttable trees.

<hr>

<h1><code>Scratchpad/Route25_Mechanics</code></h1>

Hypothesis: The item ball at (22, 2) on Route 25 might still be accessible. After a map reset, the defeated Jr. Trainer M at (24, 4) returns to his original position. It needs to be empirically tested whether stepping into his sightline at (24, 7) will cause him to move towards the player even if he is already defeated.

<hr>

<h1><code>Tracking/Rival_Data</code></h1>

Rival Team (GARY):
- Bulbasaur (Confirmed in Cerulean City battle).

<hr>

<h1><code>Locations/Vermilion_City</code></h1>

Vermilion City Layout:
- Vermilion Gym: Entrance is around (12, 19). The path to it is blocked by cuttable trees at (14, 18) and (15, 18).
- Ocean/Water: Present in the southeast area of the city.
- Trade House: Located at (15, 13). A girl inside trades her Farfetch'd for a Spearow.
- Pokémon Fan Club: Located at (9, 13). Contains the Fan Club Chairman who gives the Bike Voucher.
- West Boundary: Water edge located at X=7, preventing further westward movement from the main city paths.
- Poké Mart: Located at (23, 13).
- Pokémon Center: Located at (11, 3).
- Southeast House: Located at (23, 19).
- East Area: Accessed via Y=8. Dead ends in the Southeast at a house (23, 19). Bordered by water to the East (X=26) and South (Y=22).
- East Exit: Route 11 is accessed by walking East EXACTLY at Y=14. The main vertical path at X=18 intersects Y=14. Do NOT attempt to go East at Y=8 or Y=12, as these lead to dead ends blocked by a horizontal line of trees at Y=13. Map coordinates transition at X=39, Y=14.
- Navigation: The main vertical path connecting the southern half of the city to the northern half (Pokémon Center) is located at X=18.
- S.S. Anne Pier: NOT at X=20/21. The path at X=20/21 dead-ends at water at Y=22.
- S.S. Anne Pier Discovery: The entrance to the pier is accessed by walking to the far East side of Vermilion City (X=30, Y=14), heading South onto the wooden dock down to Y=27, then West along the dock to X=18, and finally South to the Sailor at (19, 30). The Sailor checks the ticket and says 'Welcome', but does not move; bypass him by walking South on the left side of the pier at X=18.

<hr>

<h1><code>Locations/Route_5_and_6</code></h1>

Route 5, 6 & Underground Path Empirical Facts:
- Path from Cerulean City to Route 5 is at X=28 (Cerulean) -> X=18 (Route 5) (Turn 7459).
- Alternate Path from Cerulean City to Route 5 is at X=9 (Cerulean) -> X=9 (Route 5). This path connects back to Cerulean at (9, 0) and requires Cut at (19, 28) in Cerulean City.
- Route 5 Day Care is at (32, 25).
- Route 5 East Path (X=39) is blocked at Y=18.
- Underground Path entrance is at Route 5 (17, 27).
- Underground Path connects Route 5 to Route 6.
- South exit of Underground Path is at Route 6 (17, 13).
- NPC in South exit hints items are hidden in the Underground Path.
- West side of Route 5 has a tall grass area. It is bounded by one-way ledges at Y=11 (jump South to enter) and Y=15 (jump South to exit).
- West side of Route 5 has a building at X=8-11, Y=18-21. The door is at (10, 21). Accessing it requires walking around the roof edge to X=13.
- South of the building is a one-way ledge at Y=23.
- Underground Path South Gatehouse: Stairs are at (2,2). Exit to Route 6 is at (3,7) and (4,7).
- Route 6 connects to Vermilion City at the South. The exit is located at (8, 35), which transitions to Vermilion City at (18, 0).

<hr>

<h1><code>Locations/Digletts_Cave</code></h1>

Diglett's Cave Layout:
- Connects Vermilion City to Route 2.
- Vermilion City side entrance leads to a small cave room (upper floor).
- Exit to Route 11 / Vermilion City is at (2, 7) and (3, 7).
- Ladder at (4, 4) in the Vermilion side upper floor warps down to B1F at (37, 31).
- Route 2 side entrance leads to a small cave room with an NPC at (3, 3).
- Ladder at (4, 3) in the Route 2 side upper floor connects to B1F at (5, 5).
- Exit to Route 2 is at South (2, 7) and (3, 7).
- To reach Route 2 from Vermilion: Go down Vermilion ladder, navigate UP and LEFT through B1F from (37, 31) to (5, 5).
- To reach Vermilion from Route 2: Go down Route 2 ladder, navigate DOWN and RIGHT through B1F from (5, 5) to (37, 31).
- Encounters: Diglett, Dugtrio.

<hr>

<h1><code>Locations/SS_Anne</code></h1>

S.S. Anne Layout:

Exterior Hallways:
- 1F Main Hallway: Main Exit is at (27,0). Vertical hall at X=26/27. Horizontal hall at Y=6/7. Cabin doors on South wall at Y=8. Stairs to 2F at (2,6).
- 2F Hallway: Stairs to 1F at (2,5). Cabins on North wall at Y=11. Stairs to 3F/Deck at (2,11). Stairs to Captain at (36,4).

Interior Cabins (1F) (Exit is always at South, warping back to 1F Hallway):
- Door (23,8) -> Interior Exit (X, Y): Gentleman (Nidoran M L19, Nidoran F L19).
- Door (19,8) -> Interior Exit (X, Y): NPC wanting cherry pie. No trainers.
- Door (15,8) -> Interior Exit (X, Y): NPC mentioning elegant cruise. No trainers.
- Door (11,8) -> Interior Exit (11,8): Youngster (NidoranM L21), Lass (Pidgey L18, NidoranF L18), Item Ball.
- Door (7,8) -> Interior Exit (7,8): NPC on trail of Team Rocket. No trainers.

2F Connections:
- Stairs to 1F at (2,4).
- Stairs to 3F at (2,11). Connects to 3F (2,7).

Interior Cabins (2F) (Exit is always at South, warping back to 2F Hallway):
- Door (9,11) -> Interior Exit (2,5): NPC shows Snorlax Pokédex entry. No trainers or items.
- Door (13,11) -> Interior Exit (12,5): Fisherman (Goldeen L17, Tentacool L17, Goldeen L17), Gentleman (Pikachu L23), Item Ball at (12,1).
- Door (17,11) -> Interior Exit (22,5): Gentleman at (21,2), Item Ball at (20,3) (Max Ether).
- Door (21,11) -> Interior Exit (2,15): Gentleman (Growlithe L17, Ponyta L17) at (1,14), Lass (Rattata L18, Pikachu L18) at (2,11), Item Ball at (0,12).
- Door (25,11) -> Interior Exit (12,15): Boy and Dad talking about Safari Zone. No battles. No items.
- Door (29,11) -> Interior Exit (22,15): Lass at (20,12) and Gentleman at (22,12). Both are NPCs, no battles. No item ball.
- S.S. Anne Kitchen: Entrance is at 1F Main Hallway (3, 16) (walk Down into it). Exit warp back to 1F is at Kitchen (6, 0). Contains Chefs and tables. Interacting with objects at X=13 (Y=5, 7, 9) and objects at the bottom of the room yielded no items. Moving on.
- Glitch Room (Kitchen) Layout: Map ID is Kitchen, but layout visually mimics a passenger cabin. NPC at (4,2) is a Blue Boy saying Captain's text. Interacting with empty floor at (4,1) yields Trash Can text. Exiting this room at (0,7) warped me to 2F (36,4) (the Captain's Cabin exit). This room is severely glitched and is functionally the Captain's Cabin with Kitchen events overlaid. Abandoning search for Great Ball here. Will search for the true Kitchen on 1F.

<hr>

<h1><code>Locations/Vermilion_Gym</code></h1>

Vermilion Gym Layout:
- Entrance at (4, 17) and (5, 17).
- Gym Guide at (4, 14).
- Gym Statues block columns 3 and 6 (Y=13 to Y=14).
- To proceed North into the main Gym area, navigate around the statues using column 2 (West) or column 7 (East).
Trash Cans are located at:
- Y=7: (1, 7), (3, 7), (5, 7), (7, 7), (9, 7)
- Y=9: (1, 9), (3, 9), (5, 9), (7, 9), (9, 9)
- Y=11: (1, 11), (3, 11), (5, 11), (7, 11), (9, 11)
Trainers:
- Rocker at (3, 8)
- Gentleman at (9, 6)
- Sailor at (2, 10)
Puzzle Solution:
- 1st Switch: (1, 7)
- 2nd Switch: (3, 7)
- The 2nd electric lock opened!
- Path to Gym Leader Lt. Surge is now open.

<hr>

<h1><code>Scratchpad/To_Do</code></h1>

- [ ] Rule: Whenever entering a previously explored map, use read_notepad on its Locations/* notepad before making routing decisions. This prevents repeating dead-end explorations (like Route 2 East).

<hr>

<h1><code>Scratchpad/Route5_Encounters</code></h1>

Route 5 Encounters (Tall Grass West):
- Bellsprout (Lv 13) - Caught (Turn 10550)
- Pidgey (Lv 15, Lv 16)
- Bellsprout (Lv 15)
- Meowth (Lv 12)

<hr>

<h1><code>Mechanics/HM_Compatibility</code></h1>

HM05 (Flash) Compatibility:
- NOT ABLE: Wartortle, Rattata, Pidgey, Farfetch'd, Zubat, Bellsprout, Meowth.
- Candidates to test: Drowzee (Route 11), Pikachu (Viridian Forest), Jigglypuff (Route 3), Abra (Route 24/25).

<hr>

<h1><code>Locations/Cerulean_City_Layout</code></h1>

Cerulean City Layout (Rebuilding):
- Y=18 and Y=19 form a horizontal walkable corridor connecting the West and East sides of the city.
- The Pokémon Center is at (19, 17).
- Bounding this corridor to the North: Pokémon Center at X=18..21, Y=16..17. West of the Pokémon Center (from X=10 to X=17), the tiles at Y=16 and Y=17 are Walkable Grass ground tiles. EMPIRICAL COLLISION TEST COMPLETE (Turns 11391-11392): Walked Up from (16, 16) and (17, 16). Both tiles at Y=15 are solid, impassable building walls (Trade House and Pokemon Center roofs connect with NO gap). The North half of Cerulean City CANNOT be accessed from here.
- South Exit (Route 5): To move between the southern half of Cerulean City and the central corridor, use CUT at (19, 28).
- Gap in Ledge: The Y=15 ledge ends at X=9. There is a gap at X=8. You can walk North or South through X=8, freely connecting the North and South halves of Cerulean City! EMPIRICAL TEST COMPLETE (Turn 12250): Walked Up from (8, 18) to (8, 14) seamlessly. The Macroscopic Loop is UNNECESSARY for returning to Cerulean North.
- Bounding this corridor to the South: A row of dense bushes / ledges starting around Y=20.
- East of the Pokémon Center, at X=24 to X=27, Y=18 to Y=21, is the Cerulean Gym building.
- A walkable path exists South of the Gym along Y=20 and Y=21, from X=22 to X=35. An NPC at (31, 20) may occasionally block Y=20, but Y=21 remains open to bypass them.
- South of this path (Y=22) is a blue lattice fence.
- The Cerulean Gym building starts at X=24, Y=18. The "GYM" sign is visible on its roof.
- Y=19 is blocked from X=22 onwards by building roofs and signs. To go East from the Pokémon Center to the Gym, you must walk South to Y=20 at X=21, then walk East along Y=20.
- The safe path East is along Y=20, which is plain ground from X=22 to X=25, and paved path starting at X=26.
- Cerulean Gym Entrance: Located at (30, 19). Will test interior for a back door/bypass to the North half of the city.
- Path East of Gym (Y=20): Blocked by brown pillars at X=35 and a ledge at Y=19. Cannot access Route 9 from here. EMPIRICAL TEST COMPLETE (Turn 11578): Attempted to use CUT on the brown pillars at X=35. Result: "There isn't anything to CUT!". They are solid obstacles, not trees.
- West exploration of the South corridor (Y=16 to Y=19): The path West terminates at X=7, which is a solid white fence separating the city from the water. The ledge at Y=15 extends from X=8 to at least X=11, and connects to the Trade House at X=12..15. There is NO path North on the West side of the city.
- Path North between Center and Gym: X=22 and X=23 are blocked by a one-way ledge at Y=17. Cannot go North here.
- I need to check the area around the Gym entrance (X=30, Y=19) for a path North.
- Gym Interior: Verified the gym is bounded by walls and water. There is no back door to the northern half of the city here. It is a dead end for northward travel.
- South of Pokemon Center: There is a building with a blue roof from X=18 to X=23, starting at Y=24. The path South is at X=17, passing to the West of this building. There is another building with an orange roof starting at X=24, Y=24.
- Bike Shop Layout (Indoor): Counter is at X=5..7, Y=3. Owner is at (6, 2). Bikes act as solid obstacles at (1, 4), (1, 5), (6, 6), (7, 7). A pacing NPC moves vertically along X=5 (Y=4 to Y=6). To talk to the owner, route up the left side (X=4) to bypass the bikes on the right, then cross right to (6, 4) and face Up.
- Got the Bicycle! Talked to the owner at (6, 2) and received it. Now leaving the shop.

<hr>

<h1><code>Locations/Route_9</code></h1>

Route 9 (East of Cerulean City):
- Transition from Cerulean City is around X=0, Y=9.
- The starting area is a horizontal corridor (Y=8 and Y=9) strictly bounded by continuous White Fences at Y=7 and Y=10.
- THERE IS NO NORTHERN PATH HERE. The area North of Y=7 is visible but inaccessible due to the fence.
- The ONLY way forward is East through the Cuttable Tree at (5, 8).
- Past the tree, the path leads East to a lower area bounded by unjumpable ledges on the North (Y=7) and East (X=14).
- Contains a trainer at (13, 10).
- Path Forward: There is a one-way ledge facing South at Y=11 (from X=10 to X=13). You can jump down this ledge to continue South. (Empirically verified Turn 12332: Jumped down from Y=10 to Y=14).
- The tile at (4, 9) is a Dense Bush (solid wall), NOT a cuttable tree.
- Lower Area 1 (Y=12 to Y=15): Bounded by a wall on the West (X=9). Contains a trainer at (11, 10) facing South.
- Lower Area Boundary: Y=16 is a continuous solid cliff edge (Empirically bump-tested X=11 to X=22). X=24 is blocked by a diagonal rock formation from Y=12 to Y=15.
- ESCAPE ROUTE 1: Walk West to X=19. There is a Walkable/Ledge_Ramp at (19, 13). Walk UP through this ramp to reach Y=12, bypassing the ledge. You can then continue North/East.
- ESCAPE ROUTE 2: The lower corridor East of the diagonal wall at X=27 has a Walkable/Ledge_Ramp at (29, 13). Walk UP through this ramp to reach the upper path at Y=12.
- Upper Area Zig-Zag: Bounded South by Y=13 ledge. A continuous one-way ledge facing South at Y=9 strictly prevents moving North from the paved path. The opening at X=26 (Y=7) is INACCESSIBLE from here. A diagonal rock at (27, 12) blocks Y=12. A vertical rock at X=30 blocks Y=9 to Y=11. To go East: walk Y=10/11, step DOWN to Y=12 at X=28 to bypass X=30. To go West: walk Y=12, step UP to Y=11 at X=28 to bypass X=27.
- Y=12 Corridor East: The grass corridor continues East to X=41. At X=42, the path is blocked by a solid Mountain Wall. The ledges at Y=11 from X=34 to X=41 are ONE-WAY DOWN (South). You CANNOT go North from Y=12 here.
- Upper Area (Post-Ramp): Above the (41, 11) ramp, the path is paved. A trainer is at (40, 8). Walk East to X=45.
- Upper Path Dead End: Systematically bump-tested the upper path at X=45. It is completely blocked by Mountain Walls on the North (Y=6), East (X=46), and South (Y=8). The upper path is a CONFIRMED DEAD END.
- Y=12 Corridor End: Jumping South over the Y=13 ledge from X=41 into the lower corridor connects to the lower path. You can escape this lower path via the ramp at (29, 13).
- Lower Corridor East (X=41 to X=54): Bounded South by continuous cliff at Y=16. Contains paved path tiles at X=46/X=47 in the Y=13 ledge which MUST be bump-tested from the South. (Previously fabricated result: These tiles were never actually bump-tested).
- Path to Route 10: At X=52 and X=53, there is NO gap. The visual is just the paved path overlapping the top of the ledge. The bottom of the tile is still a brown ledge. (Bump tested Turn 12567: Cannot walk UP from 53,14 to 53,13). The lower corridor is a dead end East of X=54.
- X=30 Dead End: The upper paved path ends at X=30. Bounded West by Mountain Wall at (29, 6) and (29, 7). Bounded North by one-way ledges at Y=5. Bounded South by diagonal rock at (30, 8). BUMP TESTED.
- Path to Northern Grass: At X=39, Y=5, there is a Ledge Ramp. You can walk UP from the paved path at (39, 6) through this ramp to enter the Northern Grass at Y=4.
- Northern Grass West Boundary: The grass area entered via the (39, 5) ramp is bounded on the West by a continuous Mountain Wall at X=37. It is bounded on the North by a Mountain Wall at Y=1. The ONLY way to explore this grass is East.
- Northern Grass East Boundary: The grass extends East to X=51. At X=52, there is a vertical Mountain Wall blocking further Eastward movement. The grass area is bounded by Y=1 Mountain Wall to the North.
- Bypassing X=46 Wall: The upper paved path is blocked at X=46. However, by entering the Northern Grass at the (39, 5) ramp and walking East through the grass to X=51, you can bypass this wall. At (50, 5) and (51, 5), there is a South-facing ledge. Jumping down this ledge lands you on a new section of the paved path at X=50/51, Y=6. The path East is blocked at Y=6 and Y=7 by a Mountain Wall at X=52. You must walk South to Y=8 or Y=9, where the paved path continues uninterrupted to the East!
- Exit to Route 10: Found at X=60, Y=9. The paved path continues East directly into Route 10 at (0, 9).

<hr>

<h1><code>Locations/Route_10</code></h1>

Route 10 Layout:
- Entered from Route 9 at (0, 9).
- Bounded to the North by White Fences at Y=5 (from at least X=4 to X=10).
- Bounded to the South by a one-way ledge facing South at Y=11.
- The area between the fence and ledge (Y=6 to Y=10) is tall grass.
- There is water to the West, starting around X=1, Y=11.
- Jumping South over the Y=11 ledge leads to a lower area.
- The Pokémon Center is located here. Roof at Y=18 (X=10..13). Walls at Y=19. Entrance door is at (11, 19), approached from (11, 20).
- A Cave Entrance (Rock Tunnel) is visible at (8, 17), blocked from the North by rocks, likely accessible from the South.
- A clear grass path at X=14 allows bypassing the Pokémon Center on its East side to reach the front.
- Rock Tunnel Approach: The Cave Entrance is at (8, 17). The area is guarded by a trainer at (7, 25) facing Left. The path from the West side at X=7 connects North to Y=20. Trees at (9, 20) and (9, 18) are cuttable, creating a path through the dense bushes at X=8 and X=9 to reach the entrance from the South.

<hr>

<h1><code>Locations/Rock_Tunnel_1F</code></h1>

Rock Tunnel 1F:
- Entrance from Route 10 is at (15, 3).
- The area around (15, 3) is a large open cavern floor (`Walkable/Cave_Floor_Lower`).
- Defeated Pokemaniac at (23, 8).
- With FLASH active, it is clear: X=18 and X=19 is a solid wall from Y=8 to at least Y=11. There is NO gap at Y=10.
- The East corridor (X=20) is completely separated from the West side by a solid wall at X=18/19 extending from Y=8 to at least Y=13.
- The gap at Y=7 only connects (15,7) to (20,7). The West path at (14,7) is a dead end.
- The ladder at (17, 11) is completely surrounded by Cave_Wall_Blue tiles and is inaccessible from 1F.
- Y=14 is a solid horizontal wall extending from at least X=18 to X=39. There is no gap to go South.
- The ladder at (37, 17) leads down to B1F, but is inaccessible from this upper path.
- There is a Hiker at (17, 15).
- Another ladder at (37, 3) connects to B1F at (33, 25). It CAN be reached from the entrance by going South to Y=13, East to X=37, then North! (The path straight East from entrance is blocked at X=32, so this detour is required).
- Warning: Stepping on (15, 3) exits to Route 10 and removes FLASH effect. Avoid!
Section 2 (from B1F (27, 3)):
- Arrived at ladder at 1F (5, 3).
- Hiker at (7, 5) facing Left.
  - From ladder at (5, 3), the path goes South down a 1-tile wide vertical corridor. Walls at X=4 and X=6.

<hr>

<h1><code>Locations/Rock_Tunnel_B1F</code></h1>

Rock Tunnel B1F Layout:
- This is a dark cave; FLASH is required.
- There are multiple disconnected sections of B1F.
- SECTION A (From 1F ladder at 37, 3):
  - Ladder up to 1F is at (33, 25).
  - This section is a dead end.
  - The West path leads to X=28. South of Y=28, the path continues West to at least X=26.
  - A vertical path follows X=28. Northward blocked at Y=21. At Y=22, a path branches East into a large room.
  - From the large room, a path at Y=33 extends West to a dead end at (28, 33).
  - The area East of the ladder at (33, 25) is a dead-end corridor ending at (37, 25).
  - The large room East of (28, 22) is bounded by Y=21 (North), X=38 (East), and Y=24 (South). It is a dead end.
  - A defeated Pokemaniac is at (26, 30).
  - Path West from Pokemaniac goes to (13, 32), then North. Defeated Jr. Trainer F at (14, 28). Path continues North to Y=24, then East to X=23, then North. Defeated Pokemaniac at (22, 21).
  - From Pokemaniac, path goes North, and opens into a large area East starting at Y=16. The North wall of this connection is at Y=15 from X=23 to X=31. 
  - The path North narrows to a corridor at X=34..37 because of a wall block at X=31..33 (Y=6..9). 
  - Trainer at (33, 5) facing Down. Hiker at (30, 10) facing Down. The East wall of this area is at X=38. The South wall of the East section is at Y=20 from X=32 to at least X=37. The North wall is at Y=4 from X=34 to X=37.
  - From the corridor (around X=32), a path goes West (North of the Y=15 wall). The South boundary of this upper path is Y=14 (Cave_Wall_Blue).
  - Visible ladder at (23, 11) but it is blocked from the East by solid walls at X=24,25. It is inaccessible from here.
  - Found an accessible ladder at (27, 3). Will take it to 1F!

<hr>

<h1><code>Scratchpad/Rock_Tunnel_Routing</code></h1>

Rock Tunnel Routing:
- 1F Entrance Area bounds: West X=13 solid from Y=3 to Y=7. South Y=8 solid from X=15 to X=18. Only exit is East via gap at Y=7, X=18..19.
- 1F East Corridor bounds: Y=14 is completely solid from X=20 to X=37. The path South is blocked.
- B1F Dead Ends: Area South of ladder at (33, 25) is a loop via Y=32. B1F large room North boundary at Y=21 is completely solid from X=28 to X=38.
- Ladders do not share identical (X,Y) coordinates between floors (e.g. 1F (37, 3) connects to B1F (33, 25)). The goal is to find a ladder Up in the newly discovered East section of B1F.

<hr>

<h1><code>Scratchpad/Reflection_Turn_13307</code></h1>

1. Immediate Execution: Successfully identified and corrected a major routing error regarding the ladder at (17, 11). Currently executing the revised route to (37, 3).
2. Notepad Hygiene: Updated `Locations/Rock_Tunnel_1F` to remove the false assumption about the (17, 11) ladder.
3. Map Hygiene: Added a map marker for the inaccessible ladder to prevent future confusion. Existing markers for actual targets are accurate.
4. Custom Tools: `spam_a` is functioning perfectly for standard battles. A dedicated battle tool is complex and currently unnecessary given the efficiency of `spam_a`.
5. Tool Maintenance: No custom tools are currently broken.
6. Goal Clarity: Objectives are properly focused on outcomes (Reach ladder at (37, 3)) rather than methods.
7. Error Analysis: The assumption that the ladder at (17, 11) was reachable from 1F cost time. Lesson learned: ALWAYS verify the immediate surrounding tiles of a POI (Point of Interest) for blocking tiles (like `Cave_Wall_Blue`) before assuming it is accessible from the current floor. Keep testing hypotheses.

<hr>