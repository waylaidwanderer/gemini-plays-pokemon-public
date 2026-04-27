<h1><code>Main</code></h1>

Badges: Boulderbadge, Cascadebadge, Thunderbadge, Rainbowbadge, Soulbadge, Marshbadge
Team (6/6) and HMs:
- Pidgeot (AERO) - Lv 40
- Blastoise (HYDRO) - Lv 54 (SURF, STRENGTH)
- Farfetch'd (DUX) - Lv 11 (Target for CUT)
- Raticate (FANG) - Lv 24
- Meowth (MIDAS) - Lv 12
- Drowzee (BAKU) - Lv 13 (Target for FLASH)
HM Tracking:
- CUT (HM01): Obtained and taught to DUX.
- FLY (HM02): Obtained and taught to AERO.
- SURF (HM03): Obtained and taught to HYDRO. (Requires Soulbadge - Koga)
- STRENGTH (HM04): Obtained and taught to HYDRO. (Requires Rainbowbadge - Erika)
- FLASH (HM05): Obtained and taught to BAKU.
Inventory: MASTER BALL, TM46, IRON, CALCIUM, MAX POTION, CARBOS, TM14, FULL RESTORE.
PC Storage: Zubat (ECHO) - Lv 10, Snorlax (TITAN) - Lv 30, NidoranF (NINA), Exeggcute (OMELET), Hitmonlee (BRUCE) - Lv 30. Items: TOWN MAP, TM12, HELIX FOSSIL, TM04, NUGGET x2, TM19, S.S. TICKET, TM28, OLD ROD, TM08, TM24, HM01, MOON STONE x2, HM05, TM10, SILPH SCOPE, TM21, POKE FLUTE, HM04, HM03, TM06, TM40.
- Active PC Box: Box No. 2 (Switched on Turn 28224).

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
- Gift Pokémon (e.g., Hitmonlee from the Fighting Dojo) are sent directly to the currently active PC Box if the player's party is full. Verified Turn 28642.

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
- Move Cursor Memory: Confirmed that the battle move cursor remembers its position from the last time a move was selected during the current battle (Turn 2095).
- Status (Sleep): Sing has a chance to miss. Verified Turn 2103 when Clefairy used Sing on AERO's switch-in and AERO did not gain the SLP status.
- Type Effectiveness: Bug is Super Effective against Poison in Gen 1 (verified Turn 2351: Leech Life vs Zubat).
- Turn 2763: In battle with Super Nerd, switching to FANG (Rattata, Lv 12) against Voltorb to share EXP.
- Status (Disable): In Gen 1, if a move is disabled, the game still allows you to select it in the battle menu. If you do, the turn is wasted and the text "[MOVE] was disabled!" appears (Verified Turn 5929/5930).
- Wrap Mechanics: Wrap is a multi-turn trapping move. While wrapped, the text 'Enemy [PKMN]'s attack continues!' appears each turn. The player's turn is skipped entirely and the battle menu does not appear until the move ends (Verified Turns 6296-6299 against Ekans).
- Ghost types are immune to Normal-type moves (e.g. Mega Punch, Tackle). (Verified Turn 17558 against a Gastly).

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

Gen 1 Menu Behaviors:
- Start Menu: Wraps around (Up from top goes to bottom). Remembers cursor position between uses.
- Party Menu: Remembers cursor position between uses.
- Because of wrapping and memory, blind macros for menus (like spamming Up to reach the top) DO NOT WORK. You must visually confirm cursor position.
- Overworld Item Menu: The cursor DOES NOT wrap around. Pressing Up at the top item (slot 1) does nothing. You must manually scroll down to reach items at the bottom. (Verified Turn 22113)
- Main Battle Menu Layout:
FIGHT  PKMN
ITEM   RUN
- The cursor ALWAYS resets to FIGHT at the start of every turn. It does NOT remember its position.
- Pressing Right from FIGHT goes to PKMN. Pressing Down from FIGHT goes to ITEM.
- Yes/No Prompts: The default cursor position for many Yes/No prompts (like "Press it?" for switches, or "Toss this item?") is "NO". To select "YES", you must explicitly input 'Up' before pressing 'A'. For the Mansion switch: YES outputs "Who wouldn't?". NO outputs "Not quite yet!".

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
Survival Rule 3: Anti-Softlock - If physically trapped by ledges/obstacles with no walking exit, immediately use FLY, TELEPORT, DIG, or ESCAPE ROPE instead of pacing.
- Cut (HM01): In Gen 1, you cannot simply press 'A' while facing a cuttable tree to use it. You must open the Start Menu -> POKéMON -> select the Pokémon with Cut -> select CUT. Note: CUT can also remove tall grass around the player. If you use it while not explicitly facing a tree (by bumping into it first), it may just cut grass and give the success message while leaving the tree intact. Always bump into the tree to face it before using CUT.
- Rule: Always empirically test unknown tiles with tools like CUT before definitively concluding they are solid walls. EMPIRICAL TEST COMPLETE (Turn 11835): Dense bushes (e.g., at Route 2 (12, 53)) return "There isn't anything to CUT!" and are verified as solid walls, not cuttable trees.
- To use stairs in the Dept Store, step on the stairs tile and press the directional button facing the stairs (e.g., 'Up' for stairs that go up). Just stepping on the tile is not enough.
- Cycling Road (Route 17) Forced Movement Mechanic: The route features a downward slope that automatically forces the player to move South (Down). This forced movement can happen rapidly without any player input, causing the Y-coordinate to increase. This appears to cover the entirety of Route 17. (Verified Turn 22607).
- Cuttable Trees (Mechanic): Cuttable trees respawn when you leave and return to the area/map. Verified Turn 22795.
- Escape Rope (Item): Does not work inside Gyms. Triggers Professor Oak's warning message (Verified Turn 28083).
- Cuttable Trees (Mechanic): Opening and closing the Pokédex (or potentially viewing stats) reloads the overworld and causes cuttable trees to respawn immediately. Verified Turn 28361.
- Silph Co Elevator: The elevator IS OPERABLE without the Card Key. The panel must be interacted with by standing at (3,1) and facing Up.
- Defeated Team Rocket Grunts in Silph Co do NOT disappear when you leave the floor or reload the map. They act as permanent physical obstacles. Confirmed empirically on 9F.
- Elevators: To exit an elevator, you must walk DOWN off the map from the threshold tiles at (1, 3) or (2, 3). Just stepping on them does not trigger the warp.
- Elevator Protocol: MENU LAYOUT: 1F is at the TOP, 11F is at the BOTTOM. To go to higher floors (e.g., from 1F to 5F), press DOWN. To go to lower floors, press UP. DO NOT blind press. Open the menu, visually verify cursor, calculate inputs.
- Strict Elevator Protocol (to avoid dropped inputs): 1. Face panel and press A. 2. Press Select (Wait 1 turn for menu text). 3. Press Down N times. 4. Press Select (Wait 1 turn to verify cursor). 5. Press A to confirm. 6. Press Select (Wait 1 turn for travel animation). 7. Exit elevator.
- Card Key: Stand facing a locked yellow door and press 'A' to open it. It removes the door permanently (Verified Turn 34137).
- Elevator Menus: The cursor ALWAYS starts on 1F. The reason inputs were "dropped" was because the "Which floor do you want?" text box takes time to animate. Directional inputs made during this animation are ignored. You MUST wait one full turn after pressing A on the panel before pressing Down.
- Shutter Walls: Grey walls with horizontal lines (e.g., at Silph Co 3F (17, 8) and (17, 9)) are actually locked doors! Stand facing them and press 'A' with the Card Key to open them (Verified Turn 35599).

<hr>

<h1><code>Tracking/Rival_Data</code></h1>

Rival Team (GARY):
- Bulbasaur (Confirmed in Cerulean City battle).
Encounter 4 (Pokemon Tower 2F): Defeated.
Team: Pidgeotto Lv 25, Gyarados Lv 23, Growlithe Lv 22, Kadabra Lv 20, Ivysaur Lv 25.
Encounter 5 (Silph Co): Expected here, unverified location.

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
- Route 10 South of Rock Tunnel:
- Exit is at (8, 53).
- Sign at (9, 55).
- Area is bounded South by a cliff at Y=58 (X=6..13).
- To proceed to Lavender Town, go East to X=14/15, then South over a one-way ledge at Y=57 to reach the grass area below.
- After jumping the ledge at Y=57, there is another one-way ledge South at Y=61.
- South of Y=61 is a large patch of tall grass.
- Path south into Lavender Town is on the West side (X=10..11) to bypass the purple fence/structure at Y=66.

<hr>

<h1><code>Locations/Rock_Tunnel_1F</code></h1>

Rock Tunnel 1F:
- Entrance from Route 10 is at (15, 3).
- The path South from the Entrance area is blocked by a solid horizontal wall at Y=8 spanning from X=14 to X=20. To bypass it and go South, you must go East at Y=6 or Y=7 to X=21+.
- The area around (15, 3) is a large open cavern floor (`Walkable/Cave_Floor_Lower`).
- Defeated Pokemaniac at (23, 8).
- With FLASH active, it is clear: X=18 and X=19 is a solid wall from Y=8 to at least Y=11. There is NO gap at Y=10.
- The East corridor (X=20) is completely separated from the West side by a solid wall at X=18/19 extending from Y=8 to at least Y=13.
- The gap at Y=7 only connects (15,7) to (20,7). The West path at (14,7) is a dead end.
- The ladder at (17, 11) CAN be reached from the West! From (16, 11) it is accessible.
- Y=14 is a solid horizontal wall extending from at least X=18 to X=39. There is no gap to go South.
- There is a Hiker at (17, 15).
- Another ladder at (37, 3) connects to B1F at (33, 25). It CAN be reached from the entrance by going South to Y=13, East to X=37, then North! (The path straight East from entrance is blocked at X=32, so this detour is required).
- Warning: Stepping on (15, 3) exits to Route 10 and removes FLASH effect. Avoid!
Section 2 (from B1F (27, 3)):
- Arrived at ladder at 1F (5, 3).
- Hiker at (7, 5) facing Left.
  - From ladder at (5, 3), the path goes South. It is NOT a 1-tile corridor. X=2 to X=5 are Walkable.
  - At Y=6, the path opens up Eastward (Y=6 to Y=9 are walkable). The open area at X=6..11, Y=6..9 is a dead end with no hidden paths or ladders (Verified Turn 16335).
  - The West wall is at X=1. The East wall is at least past X=10.
  - At X=6, Y=10 to at least Y=14 is a Cave_Wall_Blue boundary.
  - Path continues South down X=2..5. Hiker at (5, 16) facing Down. Can be bypassed on the left.
  - South boundary is solid Cave_Wall_Blue at Y=22 (Verified from X=1 to X=22).
  - The path turns North at X=2..5. X=1 is a solid wall at Y=17..25.
  - At Y=20..21, a long horizontal corridor also goes East. It hits a wall at X=22.
  - A path goes North from the corridor at X=9..11, but dead-ends (North wall at Y=6, East boundary at X=12 is solid Cave_Wall_Blue verified at Turn 14065).
- From the South corridor (Y=20..21), a path goes North at X=14..17.
- This path leads to the Hiker at (17, 15) and continues North to the ladder at (17, 11).
- The path is bounded by solid walls: West at X=13 (from at least Y=10 to Y=15), East at X=18 (from Y=8 to Y=15).
- Therefore, the ladder at (17, 11) is a dead-end branch from the South corridor.
- Path North from (21, 20) dead-ends at a wall at (21, 15).
- The path East from the Entrance at Y=1 and Y=2 is blocked by a solid wall at X=18. (Verified Turn 16439).
- The connection between East and West is via the gap at Y=7. From the Entrance, go South to Y=7, East to X=20, South to Y=13, then East to X=37.
- VISUAL CUE: A Hiker sprite was seen at (22, 24) from (21, 21). Since the wall at Y=22 is solid, there must be another path leading to the area South of Y=22.
- The path West from the Entrance (15, 3) is blocked at X=13 by a cliff face separating the lower floor (X>=14) from a raised platform (X<=13).
Section 3 (From B1F (3, 3)):
- Arrived at ladder at 1F (37, 17).
- Bounded North by solid wall at Y=16. Bounded East by solid Cave_Wall_Blue at X=38 (verified near Y=17..24). Bounded West by solid Cave_Wall_Blue at X=31 (verified near Y=20..24).
- Jr. Trainer F at (37, 21) facing Up. Defeated.
- Hiker at (32, 24) facing Up. Defeated.
- The path continues South between X=32 and X=37.
- At Y=28, the path turns West. Bounded South by Cave_Wall_Blue at Y=32+.
- Path goes West to X=26, then turns North up X=26.
- The path North up X=26 DEAD-ENDS at a wall at Y=23. The path instead turns WEST at Y=24..27.
- Jr. Trainer F at (22, 24) facing Right. Defeated.
- Path from (22, 24) goes West to X=14.
- At X=14, path goes South to Y=28.
- At Y=28, path goes West to X=11.
- Found a sign at (11, 29) on 1F! It is an obstacle.
- The area around X=9..16, Y=24..31 is a large open room.
- The room is bounded West by a cliff at X=8, and South by a cliff at Y=32.
- Found a ladder at 1F (15, 33)! This is likely the exit.

<hr>

<h1><code>Locations/Rock_Tunnel_B1F</code></h1>

Rock Tunnel B1F Layout:
- This is a dark cave; FLASH is required.
Warp Pairings:
- 1F (37, 3) <-> B1F (33, 25)
- 1F (17, 11) <-> B1F (23, 11)
- 1F (5, 3) <-> B1F (27, 3)
- 1F (37, 17) <-> B1F (3, 3)

- SECTION A (From 1F ladder at 37, 3):
  - Ladder up to 1F is at (33, 25).
  - This section is a dead end.
  - The West path leads to X=28. South of Y=28, the path continues West to at least X=26.
  - A vertical path follows X=28. Northward blocked at Y=21. At Y=22, a path branches East into a large room.
  - From the large room, a path at Y=33 extends West to a dead end at (28, 33).
  - The area East of the ladder at (33, 25) connects to a vertical path at X=37. This Southern segment of X=37 extends North to a DEAD END at Y=21 (solid Cave_Wall_Blue), and South to Y=32, connecting to the Pokemaniac area (26, 30).
  - The Northern segment of X=37 (explored earlier) runs from Y=16 North to Y=2. It does NOT connect to the Southern segment due to the wall at Y=21.
  - The large room East of (28, 22) is BOUNDED by a solid wall at Y=21 from at least X=28 to X=37! It is a dead end to the North.
  - NEW TOPOLOGY (Turn 16284): The Southeast corridor at Y=32/33 connects from the Pokemaniac at (26, 30) East to X=37, and then goes NORTH directly to the ladder at (33, 25). This forms a complete loop. There are NO hidden ladders in the Southeast quadrant of B1F.
  - A defeated Pokemaniac is at (26, 30).
  - Path West from Pokemaniac goes to (13, 32), then North. Defeated Jr. Trainer F at (14, 28). Path continues North to Y=24, then East to X=23, then North. Defeated Pokemaniac at (22, 21).
  - From Pokemaniac, path goes North, and opens into a large area East starting at Y=16. The North wall of this connection is at Y=15 from X=23 to X=27.
  - Pokemaniac at (33, 5) facing Right. Hiker at (30, 10) facing Down. There is a 4x4 solid wall block at X=30..33, Y=6..9. You can bypass it via X=29 or X=34. The East wall of this area is at X=38. The South wall of the East section is at Y=20 from X=32 to at least X=37.
  - The path at Y=2 from X=37 goes West to X=26, then turns South to (26, 3). It does NOT continue West past X=25. X=25 is a solid Cave_Wall_Blue at Y=2 and Y=3.
  - Therefore, the Y=2 path is just a northern loop connecting Section A to the ladder at (27, 3). It does not lead to the Northwest quadrant.
  - From the corridor (around X=32), a path goes West (North of the Y=14 wall). The South boundary of this upper path is Y=14 (Cave_Wall_Blue).
  - This West path goes to X=26 and turns North. It goes up X=26 to (26, 3), then East to ladder at (27, 3). THIS CONNECTS SECTION A AND D!
  - The path also goes South down X=26 from Y=3. However, this path DEAD-ENDS at a solid wall at (26, 14). It DOES NOT connect to the open area at Y=16.
  - Investigated (37, 16) and (37, 17) - dead end corner, no ladder.
  - Explored West from (23, 16) to (20, 16). The path South of (20, 16) at X=20 dead-ends at a solid wall at Y=19/20. The path West from Pokemaniac at (22, 21) leads to the Hiker at (20, 21). (19, 21) is a solid Cave_Wall_Blue. There is NO path West of the Hiker.
SECTION C (From 1F ladder at 17, 11):
- The ladder at B1F (23, 11) leads to a path that goes West at Y=12/13. It is NOT a dead end! This is the main path to the Northwest quadrant.

SECTION D (From 1F ladder at 5, 3):
- Arrived at B1F ladder at (27, 3).
- Path goes West from the ladder at (27, 3) to (26, 3), where it is blocked from going further West by a wall at X=25.
- The path turns South down X=26.
- Investigated (37, 16) - it is a fake ladder/just a tile.
- Turn 15682 hallucination corrected: There is NO gap at (21, 15). (21, 15) is a solid Cave_Wall_Blue. I misremembered the gap at (21, 20) going South.
- Far Southwest corner (X=2..11, Y=30..35) is a DEAD END pocket. North boundary is solid Cave_Wall_Blue at Y=29.
- The path North from the Southwest is at X=15..17 (bypassing Jr. Trainer F at 14,28). X=12 and X=13 are blocked to the North by Cave_Wall_Blue at Y=29.
- The Y=24 corridor has NO branching paths West. X=13 is a solid wall from Y=23 to Y=28 (Verified Turn 16399).
- The Cave_Wall_Blue boundary at Y=23 is solid from X=13 to X=19. The path North from the Y=24 corridor is open via X=20..26 back to the Pokemaniac and the B1F East Area! There is NO one-way ledge here.
- The open area starting at Y=16 is bounded North by a solid wall at Y=14/15. To reach the upper path at Y=13, go East to X=32+.
- The path South down X=26 dead-ends at a solid wall at (26, 14). The West wall of this X=26 corridor is solid from Y=3 to Y=14.
- The path West at Y=16 from X=23 is blocked at X=19 and X=18 by solid walls. It does not connect to the West.
- Northwest Quadrant:
  - From B1F (23, 11), path goes West to at least X=11.
  - Defeated Jr Trainer F at (11, 13).
  - Open area around X=4..11, Y=8..13.
  - Pokemaniac at (6, 10) facing Down.
  - Found another ladder at B1F (3, 3)!
  - Pokemaniac at (3, 5) facing Down guards the ladder.
  - Defeated another trainer (Pokemaniac?) around (2, 11).

<hr>

<h1><code>Locations/Lavender_Town</code></h1>

Lavender Town Layout:
- Entered from Route 10 (North).
- Transition from Route 10 is around X=9..11, Y=0.
- Pokemon Center is at (3, 5). Roof is purple/blue checkered.
- Volunteer Pokemon House (Mr. Fuji) is at (7, 9).
- House with statues is at (7, 13).
- Another building is at (15, 13).
- Pokemon Tower is likely the large structure in the north/east.

<hr>

<h1><code>Locations/Pokemon_Tower</code></h1>

Pokemon Tower Warps & Layout:
1F:
- Entrance from Lavender Town.
- Stairs UP to 2F at (18, 9).
2F:
- Defeated Rival Gary at (14, 5).
- Stairs DOWN to 1F are exactly at (18, 9).
- Stairs UP to 3F are at (3, 9).
3F:
- Stairs DOWN to 2F at (3, 9).
- Stairs UP to 4F at (18, 9).
- Main path is West via the gap at (17, 13) or navigating around grave markers.
4F:
- Stairs DOWN to 3F at (18, 9).
- Stairs UP to 5F at (3, 9).
- Channelers at (14, 9) and (3, 7).
5F:
- Stairs DOWN to 4F at (3, 9).
- Stairs UP to 6F at (18, 9).
- X=7 is a solid vertical wall of grave markers separating West/East, with a gap at Y=13.
- Main East-West path is at Y=4.
- Nugget found at (12, 1).
- Ghost encounters require Silph Scope to attack.
6F:
- Stairs DOWN to 5F at (18, 9).
- Channelers at (15, 5), (9, 6), (13, 10).
- Open horizontal path across the floor at Y=7.
- Need to systematically map the grave marker gaps to reach the West side.
7F:
- Stairs DOWN to 6F at (10, 16).

<hr>

<h1><code>Locations/Route_8</code></h1>

Route 8 Layout:
- Located West of Lavender Town.
- Lavender Town West Gate fence is at X=54.
- Route is blocked by a solid white fence block spanning X=47 to X=50 (from at least Y=4 to Y=11).
- A path West appears to open up at Y=12.
- Hostile trainer (Lass) at (51, 12) was defeated, opening the path at Y=12.
- A large building at X=43 (likely Saffron Gate) blocks Westward movement.
- The area is bounded South by a wall at Y=14.
- Heading North through the tall grass at X=44-46 to find a path around the building or to the Underground Path.
- Turn 17879 Reflection: Discovered a path going North (Y=0 to Y=3) alongside a building roof at X=38..41. Defeated a Super Nerd at (42, 6). Continuing West through the tall grass North of the building.
- A vertical line of trainers at X=26 (Gambler at Y=3, Super Nerd at Y=4, Hiker at Y=5) blocks the path.
- A white fence corners at (17, 11), going North up X=17 and East along Y=11 to X=21. The Underground Path building is at X=14..15.

<hr>

<h1><code>Locations/Route_7</code></h1>

Route 7 Layout:
- Underground Path building is at X=4..7. Door at (5, 13). Sign at (3, 13).
- Paved path goes West from the building to X=2, and East towards Saffron City.
- The West boundary of the southern area is a solid wall of Trees/Hedges at X=1 (Y=4 to Y=15).
- Bounded North by one-way ledges (facing South) at Y=11 (X=2..3).
- At Y=7, there is a cliff edge, but a walkable ledge ramp exists at (4, 7) allowing passage North!
- North of Y=7, the paved path continues and turns West at Y=2 and Y=3, opening past the X=1 tree line towards Celadon City.

<hr>

<h1><code>Locations/Celadon_City</code></h1>

Celadon City Layout:
- Entered from Route 7 on the East side around (49, 11).
- The Pokémon Center is at (41, 9). It's a large building with a "POKE" sign on the roof (X=40..43, Y=8..9).
- Building at (24, 9) contains a Clefairy and an NPC.
- The main street (Y=10) has a one-way ledge directly north of it at Y=9. There is a gap in the ledge at X=20 (green grass) allowing Northward movement.
- The gap at X=20, Y=9 leads to a 2-wide alley (X=20, 21) that dead-ends at trees at Y=3. It does not connect to the northern street.
- There is NO gap between buildings at X=31. The buildings block North/South movement here.
- The main open path to the northern part of the city is located on the East side, at X=44 and X=45, just right of the Pokemon Center.
- The northernmost alley (Y=2) connects to the middle street (Y=5) ONLY at X=32.
- The middle street (Y=5) connects to the main street (Y=10) ONLY at X=45.
- The main street (Y=10, Y=11) is blocked at X=13 by the Celadon Dept. Store. The southern paths (Y=14, Y=17) dead-end at trees near X=2 and do NOT lead to Route 16.
- The correct path to Route 16 is via a paved path on the western edge of the city at Y=18. This leads directly to Route 16 at X=39.
- The Gym is definitely located in the southern area, accessible by cutting the tree at (35, 32). My previous assumption that it was on the upper path was incorrect.
- To reach the Gym, cut the tree at (35, 32), walk West along the grassy path (Y=32..34) all the way to X=5, then walk North through the gap in the ledge.
- Routing Clarification (Turn 28307): The Gym is in an enclosed area ABOVE the ledge at Y=31. However, this enclosed area cannot be reached from the main city streets because it is walled off by buildings and other ledges. The ONLY way into this enclosure is to cut the tree at (35, 32), walk West along the southern grassy path below the ledge to X=5, and then use the ramp at (5, 31) to jump UP over the ledge into the Gym enclosure. This is why the cuttable tree is required.

<hr>

<h1><code>Locations/Celadon_Dept_Store</code></h1>

Celadon Dept Store Layout:

1F: Service Counter
- Entrance at (16, 7)
- Stairs UP at (12, 1)

2F: Trainer's Market
- Stairs DOWN at (12, 1), UP at (16, 1)
- NPC gave TM18 (Counter).

3F: TV Game Shop
- Stairs DOWN at (16, 1), UP at (12, 1)
- NPC at (8, 2) talks about Graveler.
- No item vendors on this floor.

4F: Wiseman Gifts
- Stairs DOWN at (12, 1), UP at (16, 1)
- NPC at (17, 5) mentions buying a POKé DOLL.
- Sign mentions Element STONEs on sale.
- Left Clerk sells:
  - POKé DOLL (¥1000)
  - FIRE STONE (¥2100)
  - THUNDERSTONE (¥2100)
  - WATER STONE (¥2100)

5F: Drug Store
- Stairs DOWN at (16, 1), UP at (12, 1)
- Right Clerk sells:
  - X ACCURACY (¥950)
  - GUARD SPEC. (¥700)
  - DIRE HIT (¥650)
  - X ATTACK (¥500)
  - X DEFEND (¥550)
  - X SPEED (¥350)
  - X SPECIAL (¥350)
- Left Clerk sells:
  - HP UP (¥9800)
  - PROTEIN (¥9800)
  - IRON (¥9800)
  - CARBOS (¥9800)

Rooftop: Vending Machines
- Stairs DOWN at (12, 1)
- Elevator at (14, 1)
- Vending Machines sell:
  - FRESH WATER (¥200)
  - SODA POP (¥300)
  - LEMONADE (¥350)
- Thirsty Girl (Little Girl NPC):
  - Give FRESH WATER -> TM13 (Ice Beam)
2F Right Clerk sells:
  - TM32 (¥1000)
  - TM33 (¥1000)
  - TM02 (¥2000)
  - TM07 (¥2000)
  - TM37 (¥2000)
  - TM01 (¥3000)
  - TM05 (¥3000)
  - TM09 (¥3000)
  - TM17 (¥3000)
2F Left Clerk sells:
  - GREAT BALL (¥600)
  - SUPER POTION (¥700)
  - REVIVE (¥1500)
  - ANTIDOTE (¥100)
  - BURN HEAL (¥250)
  - ICE HEAL (¥250)
  - AWAKENING (¥200)
  - PARLYZ HEAL (¥200)

<hr>

<h1><code>Locations/Rocket_Hideout</code></h1>

Rocket Hideout Layout:
Entrance: Game Corner (17, 4). Warps to B1F (21, 2).

B1F Layout:
- Main Area Stairs UP: (21, 2) [Exit to Game Corner].
- Main Area Stairs DOWN: (23, 2) [Leads to B2F Main Area].
- East Area Stairs DOWN: (21, 24) [Leads to B2F East Area].
- Path opened by Grunt at (12, 6) loops back to the South Area and is a dead-end.
- Defeated Grunts: (16, 25), (26, 8).
- East Area contains the Elevator doors at (24, 20) and (25, 20). You exit at (24, 19)/(25, 19). The Yellow Grid Doors at (24, 16) and (25, 16) are walkable floors, allowing passage North through the Y=16 wall. The path East via X=28 is blocked at Y=16. We can explore North to find a way back to the B1F Main Area.

- B2F Main Area: Accessed from B1F stairs at (23, 2), arriving at B2F (27, 8). Contains Spin Maze start at (2, 9). Connects directly to the Stairs DOWN to B3F at (21, 8) via the southern path (Walk South to Y=15, Left to X=21, Up to Y=8). Thus, the B3F stairs are NOT isolated behind the Spin Maze.
- B2F Isolated Area: Contains Stairs UP to B1F at (21, 21) [Leads to B1F (21, 24)]. Reached via the Spin Maze.
- B2F Grunt at (26, 12) tells me I need the LIFT KEY. He is not hostile.
- Spin maze in South/West.
- Defeated Grunt: (20, 14), (18, 17).
B2F Spin Maze Complete: Start (2, 9) -> Stop (8, 11) -> Walk to (10, 14) -> Left to (9, 14) vv -> Stop (9, 16) -> Walk to (10, 16) -> Down to (10, 17) >> -> Stop (14, 15) -> Walk to (16, 15) -> Up to (16, 14) ^^ -> Stop (16, 13) -> Walk Right/Up to B3F Stairs at (21, 8).

B3F Layout:
- Divided by horizontal walls at Y=4 and Y=8.
- North Section (Y < 4): Contains Stairs DOWN to B4F at (16, 2). NO GAP CONNECTS IT TO MIDDLE. Y=4 wall is completely solid. Must be accessed via Elevator.
- Middle Section (Y=5 to 7): Contains Stairs UP to B2F at (25, 6).
- South Section (Y > 8): Contains Y=9 corridor, Spin Maze, East Area.
- Gap in Y=8 wall is at (20, 8), connecting South Section to Middle Section.
- Stairs DOWN to B4F: (19, 18) [Access via B3F Spin Maze].
- Stairs UP from B4F: (19, 18) [Leads to B3F (19, 18)].
- B3F Spin Maze forward path: Start (13, 11) -> (12, 11) << -> Stop (10, 11) -> Down to (10, 13) >> -> Stop (14, 13) -> Left to (12, 13) -> Down to (12, 16) -> Left to (9, 16) -> Down to (9, 18) -> Right to (11, 18) >> -> hits (15, 18) vv -> Stop (15, 22). From (15, 22): Walk Left to (11, 22), bypass Grunt at (10, 22) via (11, 21)->(10, 21)->(9, 21)->(9, 22). From (9, 22), Down to (9, 25), Right to gap at (13, 25), East to (18, 25), Up to B4F Stairs at (19, 18).
- B3F Spin Maze Escape path: From (12, 13) -> Left to (10, 13) >> -> Stop (14, 13) -> Right to (16, 13) ^^ -> Stop (16, 11) -> Right to Main Area.
- East Area is a dead end with TM10 at (26, 17).
- Item: Rare Candy at (20, 14).
- Defeated Grunt: (26, 8), (11, 2).
B3F Spin Maze Return Path (from 19,18 back to Main Area): Start (19, 18) -> Left/Up to (18, 16) ^^ -> Stop at (18, 15) Normal Floor -> Left/Up to (16, 13) ^^ -> Stop at (16, 11) Stop Tile -> Right to (20, 11) -> Up to Main Area.

B4F Layout:
- West Area (Accessed via B3F 19,18 stairs): Contains Lift Key at (10, 2).
- East Area: Contains Grunts at (23, 12) and (26, 12) guarding Giovanni's doors at (24, 11). Elevator is at (24, 16).
- North Area (Isolated): Contains Stairs UP to B3F at (16, 2).
- PROOF OF NO CONNECTION: The wall at X=21 is completely solid (verified Turn 20770). I can physically see the Grunt at (23, 12) from the West side, but solid wall tiles at (21, 10) to (21, 12) block all access. Therefore, the East Area of B4F CANNOT be reached by walking from the West Area. It MUST be accessed via the Elevator from another floor (likely B2F East Area).
- Turn 20641: Corrected visual misidentification. The "Gold Platform" at (24, 9) is actually just a Chair (`Obstacle/Chair_Down`) facing downwards, matching the visual glossary. It is a solid obstacle. There is no elevator at (24, 9).
- Giovanni is located at B4F East Area (25, 3). Defeated on Turn 21348. He drops an item ball at (25, 2), presumably the Silph Scope.

<hr>

<h1><code>Locations/Route_16</code></h1>

Route 16:
- Connected to Celadon City on the East. The transition from Celadon City (2, 18) places you at Route 16 (39, 10).
- The route is split into an upper and lower section. The lower section leads to a sleeping Snorlax blocking the way at (26, 10). The upper section is accessed by cutting a tree at (34, 9).
- Arrived on Route 17 (Cycling Road). The West lane (X=1) ends at a body of water at Y=124. Need to find a way to cross to the East lanes.

<hr>

<h1><code>Mechanics/Town_Map_Connections</code></h1>

Town Map Navigation Rules:
- The Town Map interface is node-based, not a free-roaming grid.
- The cursor snaps directly between valid city/town nodes.
- Do NOT guess long sequences of directional inputs. Instead, use single steps to systematically map and verify the connections between cities.
- TODO: Systematically map the directional connections between visited cities (e.g., 'From Pewter City, pressing Down goes to Viridian City') to ensure reliable future travel.
Fly Map Confirmed Connections:
- Pallet Town: Up->Viridian, Down->Fuchsia, Right->None, Left->None
- Viridian City: Up->Pewter, Down->Pallet, Right->None, Left->None
- Pewter City: Down->Viridian, Up->Cerulean, Right->None, Left->None
- Cerulean City: Down->Pewter, Up->None, Left->None, Right->None
- Fuchsia City: Up->Pallet, Down->None, Left->None, Right->None
- Fly Destination Unlock: A city or town only appears on the Fly map after you have visited its local Pokémon Center. (Discovered Turn 28531 when Celadon City was missing from the map because its Pokémon Center hadn't been visited during the visit).

<hr>

<h1><code>Locations/Fuchsia_City</code></h1>

Fuchsia City:
- Safari Zone is located at the top center of the city. Entrance at (18, 3).
- To access the main city from the south, cut the tree at (18, 19).
- Poke Mart is at (5, 13).
- Bill's Grandpa's House is at (11, 27).
- Pokemon Center is at (19, 27).
- Fuchsia City Gym is at (5, 27).
- Voltorb encounter trap (looks like an item ball) at (25, 6) behind brown pillars.
- Good Rod: Fishing Guru's older brother is in the house at (31, 27). He offers the Good Rod. Need bag space to receive it (Discovered Turn 23068).
- Quest Hook: Safari Zone Warden lost his false teeth (mentioned by a Lass on Turn 23050).
- Safari Zone Warden's House front door is at (27, 27), back door at (22, 13) (leads to a small back room with an NPC and an item blocked by a boulder). Warden is missing his teeth and speaks gibberish. Finding them is required.
- Cuttable trees in Fuchsia City found at (18, 19), (22, 7), and (16, 11). To access Safari Zone from the south, cut the tree at (22, 7).
- WARNING: Fuchsia City is split horizontally into North and South by a wall of buildings, rocks, and ledges at Y=25. Finding the path North is my current goal.
- One-way ledge at X=23 (facing East) between Pokemon Center and Warden's House. If you jump East, you cannot walk West back.
- ROUTE (South to North): The far western edge (X=1) is a fenced-off path leading to Route 18. It does not connect to the northern half of the city. The only way to move between the North and South halves of Fuchsia City is by using CUT on the trees at (18, 19) or (22, 7).
- ROUTE (Center to Gym): Verified Turn 27868. Walk South from the Pokemon Center to Y=28, walk West along Y=28 to X=5, then walk Up to enter the Gym at (5, 27). No CUT required.

<hr>

<h1><code>Locations/Safari_Zone</code></h1>

Safari Zone (Center Area):
- Entrance is at the South.
- The North transition to the North Area is located at (14/15, 0).
Step Count Tracker:
- Remaining steps are displayed in the top-left of the START menu (e.g., 34/500 means 34 steps remaining).
- The Safari Zone session ends automatically when steps hit 0.
- Far SW corner (X=2, Y=17) is a dead end blocked by bushes and hedge fences.
- Rest House located at (17, 19).
- Path North of the central area has a solid dense bush wall at Y=9 (Tested around X=22-27 on Turn 24093). Must explore further East/West to see if the wall ends.
- Center Area bounds: West edge at X=0 (Y=14 to 22) is blocked by dense bushes and trees.
- Center Area has a large lake in the middle (X=17 to 21, Y=12 to 15). The West side of the lake is blocked at Y=15/16 spanning from X=0 to at least X=17 by dense bushes and a building. There is NO path North on the West side of the lake.
- Path North from East of the lake (X=22 to X=29): Empirically tested all tiles along Y=9 (Turns 25648-25655). Every single tile from X=22 to X=29 is blocked by solid bushes. There is NO direct path North from the East side of the Center Area. The Center -> East -> North -> West route is definitively MANDATORY.

- The EXIT from the Safari Zone Center Area back to the Gatehouse is at X=14/15, Y=26. Walking Down at Y=25 triggers the exit prompt.
- Access West Area: Walking South at Y=25 transports you to the Gatehouse. You cannot walk behind the entrance fence. Path must be elsewhere.
- Center Area West boundary (X=0, Y=14 to Y=25) is completely blocked by dense bushes, trees, and buildings. There is no transition to the West Area along this edge.
- The gap at X=20/21, Y=14 is a dead end. Walking further East reveals a path North at (23, 14) that simply loops back to the East Area transition at (29, 10). There is no path to the North Area here.

<hr>

<h1><code>Locations/Safari_Zone_East</code></h1>

Safari Zone (East Area):
- Transition from Center Area (X=29, Y=10) leads to East Area (X=0, Y=22).
- Rest House is at (25, 11).
- Stairs up to the central plateau are at (20, 21).
- Mapping started Turn 26000. Verified route documented in Routing/Safari_Zone.

<hr>

<h1><code>Routing/Safari_Zone</code></h1>

Safari Zone East Area Route (Verified Turns 27109-27145):
- Waypoint 1: Head East from the Center Area entrance (29, 10), then North to climb the stairs at (20, 21).
- Waypoint 2: Walk West across the plateau and descend the stairs at (12, 21).
- Waypoint 3: Walk North along the western grass path to Y=7, then East to climb the stairs at (12, 7).
- Waypoint 4: Walk East across the northern plateau and descend the stairs at (17, 7).
- Waypoint 5: Walk East, then North past the Rest House, and walk West along the upper path (Y=3).
- Waypoint 6: Walk down around the signpost at (6, 4) to Y=5, then walk West to the transition at (0, 5) to reach the North Area.

Safari Zone North Area Route:
- Waypoint 1: Head west from the East Area entrance (39, 31).
- Waypoint 2: To bypass the vertical line of bushes at X=17, climb the stairs to the plateau at (22, 23).
- Waypoint 3: Walk west across the plateau and descend the stairs at (16, 27).
- Waypoint 4: Proceed north/west to explore the rest of the area and find the true transition to the West Area.

<hr>

<h1><code>Locations/Safari_Zone_North</code></h1>

Safari Zone (North Area):
- Transition from East Area (X=0, Y=4/5) leads to North Area at (39, 31).
- East path from (39, 31) loops back to the East Area.
- West path from (39, 31) leads through a large grassy lower level.
- Upper plateau accessible via stairs at (22, 23).
- The lower level path West is blocked by a vertical line of dense bushes at X=17 (spanning Y=28 to Y=33). Successfully bypassed this wall by taking stairs up to the plateau at (22, 23) and stairs down at (16, 27) (Verified Turn 25935).
- Rest House entrance located at (38, 28).
- Stairs down from the western edge of the plateau are at (16, 27).
- South transition at (20/21, Y=35) likely leads to Center Area at (14/15, 0) (unverified).
- The transition South of X=8, Y=35 leads to an ISOLATED DEAD END trench in the West Area. Do not use this transition.
- The true transition to the main West Area is at X=2, Y=35, leading to (21, 0) in the West Area.
- Sign at (13, 31) reads "AREA 2", indicating the North Area is considered Area 2.
- The pond and bushes block Westward movement between Y=8 and Y=17. A line of bushes at X=5 blocks Westward movement from Y=20 downwards. Actively searching for a gap in the X=5 wall to reach the West Area.
- The plateau in the North Area contains a rock wall around X=26. Stairs at (28, 27) access the East section of the plateau, which ends at a one-way ledge at Y=23. Stairs at (22, 23) access the West section.

<hr>

<h1><code>Locations/Safari_Zone_West</code></h1>

Safari Zone (West Area):
- Transition from North Area (Walking South at X=8, Y=35) leads to West Area at (26, 0).
- The trench accessed from North Area (8, 35) is an ISOLATED DEAD END. True transition to West Area is elsewhere in North Area.
- Rest House located at (24, 22).
- Secret House located at (11, 11).
- Warden's Teeth (Item Ball) at (19, 7).
- Topology: U-shaped HIGH PLATEAU surrounds a central LOW TRENCH.
- East Plateau: Southern section accessed via stairs from trench at (21, 17) is a dead end blocked by a ledge. Warden's Teeth must be accessed via a different path on the plateau.

<hr>

<h1><code>Archive/Damage_Logs</code></h1>

Damage Logs:
- Lass's Clefairy (Lv 14) Pound deals approximately 3-5 damage per hit to Squirtle (Lv 15) (Verified Turn 2092).
- Pidgey (Lv 14) Gust deals ~45% HP to Lass's Clefairy (Lv 14). Clefairy's Pound deals exactly 8 damage to Pidgey (Lv 14). (Verified Turn 2104).
- Confusion Damage: A Lv 15 Pidgey hitting itself in confusion dealt 9 damage to itself (Turn 2230).
- Water Gun (Lv 15 Squirtle) deals ~95% HP to a Lv 10 Zubat (Turn 2243).
- Lv 10 Geodude Tackle deals ~6 damage to a Lv 12 Rattata (Turn 2267).
- Pidgey (Lv 16) Gust deals ~55% HP to Lass's Oddish (Lv 11) (Turn 2458).
- Water Gun (Lv 16 Wartortle) deals ~75% HP to a Lv 12 Ekans (Turn 2486).
- Lv 11 Voltorb Tackle deals exactly 4 damage to a Lv 12 Rattata (Turn 2766).
- Bubble (Lv 23 Wartortle) deals ~55% HP to a Lv 12 Voltorb (Turn 5934).
- Mankey (Lv 18) Karate Chop (Critical Hit) deals exactly 14 damage to a Lv 25 Pidgey. Pidgey's Gust deals ~80% HP to the Mankey (Turn 6193).
- Slowpoke (Lv 17) Confusion deals exactly 6 damage to a Lv 25 Wartortle (Turn 6235).
- Machop (Lv 17) Karate Chop (Critical Hit) deals exactly 10 damage to a Lv 26 Wartortle (Turn 6422).
- Drowzee (Lv 17) Pound deals exactly 4 damage to a Lv 26 Pidgey (Turn 6430).
- Shellder (Lv 16) Tackle deals exactly 3 damage to a Lv 26 Wartortle. Wartortle's Bite deals ~30% HP to Shellder (Turn 7092).
- Bubblebeam (Lv 29 Wartortle) deals ~90% HP to a Lv 23 Pikachu (Turn 9160).
- Voltorb (Lv 21) Sonicboom deals exactly 20 damage to a Lv 18 Rattata (Turn 9195).
- Thundershock (Lv 24 Raichu) deals exactly 27 damage to a Lv 29 Wartortle (Turn 9225). Bubblebeam (Critical Hit) dealt ~75% HP to Raichu.

<hr>

<h1><code>Routing/Fuchsia_Gym</code></h1>

Fuchsia Gym Invisible Wall Maze:
- (7, 15): Wall (from 7, 16)
- (10, 12): Wall (from 9, 12)
- Juggler at (9, 7). Path so far: (7, 16) -> (7, 15) Wall -> (8, 15) -> (9, 12) -> (10, 12) Wall -> (9, 10) -> (8, 10) -> (8, 9) -> (9, 9) -> (9, 8) (Battle).

<hr>

<h1><code>Scratchpad/Fuchsia_Routing</code></h1>

- Hydro is poisoned and I have no Antidotes. Need to monitor his HP and use Potions, or find a healing spot.

<hr>

<h1><code>Locations/Fuchsia_Gym</code></h1>

Fuchsia Gym Invisible Walls:
Walls: (0,4), (0,6), (2,6), (2,8), (2,12), (3,2), (3,6), (3,8), (3,12), (4,3), (4,4), (4,5), (4,8), (4,12), (5,3), (5,8), (5,12), (6,6), (6,7), (6,12), (7,2), (7,3), (7,4), (7,5), (7,12), (10,10).
Clear paths explored:
- (5,17) North to Y=13
- Right side: (9,14) up to (9,10), Left to (8,10) up to (8,5).
- Right to (9,4) up to (9,1), Left to (0,1), Down to (0,3), Right to (3,3).
- (4,1) Down to (4,2).
- (5,1) Down to (5,2), Right to (6,2), Down to (6,5), Left to (5,5), Down to (5,7), Left to (4,7), Up to (4,6).
Defeated Trainers: Juggler(1,12), Tamer(8,3), Juggler(7,8), Juggler(8,6), Juggler(8,13), Tamer(3,5).
Visible Trainers: Juggler(2,7), Koga(4,10).

<hr>

<h1><code>Scratchpad/Fly_Map_Exploration</code></h1>

Fly map exploration:
- Cerulean:

<hr>

<h1><code>Locations/Saffron_City</code></h1>

Saffron City:
- City accessed via Route 5 Gatehouse.
- Fighting Dojo is at (26, 3).
- Official Saffron Gym is at (34, 3), but the door is currently blocked by a Team Rocket Grunt at (34, 4).
- Pokemon Center is at (9, 29).
- Many houses are blocked by Team Rocket Grunts, such as at (7, 5) and (13, 11).
- House at (17, 29) has its door blocked by a Team Rocket Grunt.
- Poke Mart is at (25, 11).
- Mr. Psychic's House is at (29, 29).
- Silph Co. building is located centrally, north of the southern row of houses. The confirmed entrance is the door at (18, 21) (Verified Turn 30423).
Layout:
- Central Crossroad: (20, 17)
- North-South Main Road: X=20 (Connects Route 5 & 6)
- East-West Main Road: Y=17 (Connects Route 7 & 8)
- Southern East-West Road: Y=30

<hr>

<h1><code>Scratchpad/Battle_Hypotheses</code></h1>

- To select RUN: Down, Right, A (or Right, Down, A). (Hypothesis based on Turn 28615-28616 mistake)

<hr>

<h1><code>Locations/Silph_Co</code></h1>

Silph Co Map IDs & Main Corridor Coords:
- 1F (0_207): UP(26,0). Elev(20,0).
- 2F (0_208): DOWN(26,0), UP(24,0). Elev(20,0).
- 3F (0_209): DOWN(24,0), UP(26,0). Elev(20,0).
- 4F (0_210): DOWN(26,0), UP(24,0). Elev(20,0).
- 5F (0_211): DOWN(14,0), UP(16,0). Elev(18,0).
- 6F (0_212): DOWN(22,0), UP(16,0). Elev(18,0).
- 7F (0_213): DOWN(14,0), UP(16,0). Elev(18,0).
- 8F (0_233): DOWN(16,0), UP(14,0). Elev(18,0).
- 9F (0_215): DOWN(8,0), UP(10,0). Elev(12,0).
- 10F (0_216): DOWN(9,0). Elev(13,0). No stairs UP in open area.
- 11F (0_217): DOWN(9,0). Elev(13,0).

<hr>

<h1><code>Locations/Silph_Co_Warps</code></h1>

Silph Co Warp Pad Data (MUST include Turn # for proof):
- 4F (11, 7) <-> 9F (9, 11) (Verified 2-way Turn 34857)
- 4F (11, 5) <-> 3F (3, 3) (Verified Turn 34402)
- 4F (17, 11) <-> 9F (13, 7) (Verified 2-way)
- 3F (3, 15) <-> 4F (3, 15) (Verified Turn 33532)
- 5F (27, 3) <-> 7F (21, 15) (Verified)
- 2F (9, 15) <-> 5F (23, 3) (Verified Turn 35083)
- 2F (13, 3) <-> 8F (3, 15) (Isolated room with TM09) (Verified Turn 35583)
- 3F (23, 11) <-> 3F (27, 15) (Verified Turn 33692)
- [REMOVED FALSE ENTRY]
- 3-Way Warp Cycle: 6F (17, 15) -> 4F (9, 15) -> 8F (17, 15) -> 6F (17, 15) (Verified Turn 34474)
- 9F (13, 15) <-> 10F (3, 15) (Verified Turn 34522)
- 7F (11, 9) <-> 7F (3, 11) (Intra-floor warp, verified Turn 35015)
- 8F (11, 5) -> 2F (27, 15) (One-way, Verified Turn 35834)
- 5F (3, 3) <-> 3F (11, 5) (Verified Turn 35047)
- 4F (17, 3) -> 3F (3, 3) (Verified Turn 35366)
- 3F (11, 11) <-> 7F (5, 3) (Verified Turn 35603)
- 7F (5, 7) <-> 11F (3, 2) (Verified Turn 35638)

<hr>

<h1><code>Locations/Silph_Co_Stairs</code></h1>

Silph Co Stair Connections (Empirically Verified):
- 1F UP(26,0) <-> 2F DOWN(26,0) (Verified Turn 30894)
- 2F UP(24,0) <-> 3F DOWN(24,0) (Verified Turn 30902)
- 3F UP(26,0) <-> 4F DOWN(26,0) (Verified Turn 30907)
- The corridor between stairs is NEVER blocked. To climb:
  - 1F->2F: Take (26,0)
  - 2F->3F: Walk Left to (24,0) and take UP.
  - 3F->4F: Walk Right to (26,0) and take UP.
- 4F UP(24,0) <-> 5F DOWN(14,0) (Verified Turn 31164)
- 5F UP(16,0) <-> 6F DOWN(22,0) (Verified Turn 30846)
- 6F UP(16,0) <-> 7F DOWN(14,0) (Verified Turn 30843)
- 7F UP(16,0) <-> 8F DOWN(16,0) (Verified Turn 31289)
- 8F UP(14,0) <-> 9F DOWN(8,0) (Verified Turn 32179)
- 9F UP(10,0) <-> 10F DOWN(9,0)

<hr>

<h1><code>Locations/Silph_Co_5F</code></h1>

5F Layout:
- Elevator at (20, 0). Stairs UP at (16, 0). Stairs DOWN at (26, 0) -> 4F (24, 0).
- Northern Corridor: Runs E-W along Y=1. Blocked on the West by a solid wall at X=7, separating the Northwest corner from the rest of the corridor. Contains a Scientist at (8, 3).
- Enclave (X=16..23, Y=3..6): Accessed via Warp Pad at (23, 3) from 2F (9, 15). Contains Juggler at (20, 6) and Scientist at (21, 6). Desks at Y=4 block direct south access from the pad; must use the gap at X=19. Dead end.
- Eastern Corridor: Contains warp pad at (27, 3), and chairs at (27, 7) and (27, 11) (not warp pads). Corridor at X=28 runs South connecting to the Southern Corridor.
- Path South (West): Accessed from the Southwest Room. Runs north and dead-ends at Y=4 (blocked from Northern Corridor). Contains an Item Ball at (8, 5).
  - Southern Corridor (Y=16) runs east from X=9, but is BLOCKED at X=14 by a solid wall.
- Doors: Locked yellow door at (25, 9) leads West into the massive continuous Southwest room. (There is NO door at 25, 13; the area is wide open from Y=12 to Y=13).
- Southwest Room: Spans from X=1 to X=24, Y=4 to Y=17. Connects directly to the Eastern Corridor at Y=12 and Y=13. Contains Potted Plant at (7, 14)/(7, 15) and (2, 6). Checkered floor tiles at (10, 17) and (11, 17). No warp pads found inside the room itself.

<hr>

<h1><code>Locations/Silph_Co_7F</code></h1>

7F Layout (Verified):
- Elevator at (18, 0). Stairs UP at (16, 0), DOWN at (14, 0).
- Northern corridor runs East-West.
- Vertical corridor at X=14 is blocked by NPC at (14, 5).
- Vertical corridor at X=16 runs from Y=1 to Y=15, bounded by walls at X=15 and X=17. Connects to South-East area.
- South-East Area: Contains Grunt at (19, 14) and Warp Pad at (21, 15).
- Central Area North (X=7..12, Y=2..13): Contains Worker at (10, 2), Grunt at (11, 4), Warp Pad at (11, 5), Warp Pad at (11, 9). A short partition wall at Y=7 (X=10..12) requires walking around via X=9 to travel between the top and bottom halves. Bounded North by desks at Y=1, East by wall at X=13, and South by desks at Y=13. Completely enclosed. Accessible ONLY via the Warp Pad at (11, 5) from 2F (27, 15).
- Isolated West Room (X=1..6, Y=1..12): Accessible ONLY via Warp Pad at (3, 11) which connects to 7F (11, 9). Blocked from the south by a solid wall at Y=13. Contains defeated Grunt at (3, 8) and an NPC (Silph Worker) at (4, 2). Path North is at X=1.
- Warp Pads:
  - (11, 9) <-> 7F (3, 11)
  - (21, 15) <-> 5F (27, 3)

<hr>

<h1><code>Locations/Silph_Co_8F</code></h1>

8F Layout (Updating):
- Elevator at (18, 0). Stairs DOWN to 7F at (16, 0). Stairs UP to 9F at (14, 0).
- Northern corridor (Y=1 to Y=3) is blocked at X=11 by a solid vertical wall. It DOES NOT connect to the west side.
- Movement south from the elevator is via X=15 through the gap at Y=4. X=16 through X=20 are blocked at Y=4.
- Path south: Walk down X=15 to reach the Southern Corridor. The warp pad to 2F is located at (3, 15).
- Corridor at X=14/X=15 runs South. It is bounded by a solid wall at X=13, separating it from the Central Area East.
- Central Area East (X=11..12, Y=5..9): Contains warp pads at (11, 5) and (11, 9). Currently inaccessible from X=14.
- Gap at (12, 14) leads west to the Central Area. Defeated Grunt at (12, 15).
- Locked yellow doors at (10, 10)/(10, 11) and (11, 10)/(11, 11). Desks at Y=13 from X=10 to X=13.
- Gap at X=8/9 (Y=14) leads North from the Southern Corridor into the central-western area.
- Isolated West Room (X=1..6, Y=1..12): Accessible ONLY via Warp Pad at (3, 11) which connects to 8F (11, 9). Blocked from the south by a solid wall at Y=13. Contains an NPC (Silph Worker) at (4, 2) who says "I wonder if SILPH is finished...". Path North is at X=3.
Warp Pads:
- (11, 9) <-> 8F (3, 11) (Intra-floor warp, verified Turn 35810)
- (11, 5) -> 2F (27, 15) (One-way warp, verified Turn 35861)
- (3, 15) <-> 2F (13, 3) (Verified Turn 35583)

<hr>

<h1><code>Locations/Silph_Co_9F</code></h1>

9F Layout:
- Elevator at (12, 0). Stairs UP to 10F at (10, 0). Stairs DOWN to 8F at (8, 0).
- Defeated Grunt at (10, 2) permanently blocks the path south along X=10.
- Desks at Y=4 block path south along X=11..13.
- The Central Room is totally isolated from the Elevator area. It can only be accessed via the warp pad at (9, 11) from 4F (11, 7).
- Western Corridors:
  - Corridor at X=1 runs from Y=1 to Y=7.
  - Corridor at X=6 runs from Y=1 to Y=7.
  - Horizontal corridor at Y=7 connects X=1 to X=6.
  - Vertical corridor at X=3 connects Y=7 to Y=9.
  - Horizontal corridor at Y=9 connects X=1 to X=6. Locked yellow doors at (10, 8) and (11, 8).
  - Corridor at X=1 runs from Y=10 to Y=16.
  - Corridor at X=6 runs from Y=9 to Y=16.
  - Defeated Grunt at (1, 9) blocks movement along X=1.
  - Horizontal corridor at Y=16 connects X=1 to X=6. No items or warps in this entire southwest block.
- Eastern side of northern corridor ends at a wall at X=15. No paths south.
- 9F open areas are fully explored.
- Warp pad at (13, 7) <-> 10F (17, 11). (17, 11) is in an isolated room containing beds.
- Locked yellow doors at (10, 8) and (11, 8).
- Central Room (South of doors at Y=8): Bounded by walls at X=7 and X=15. Block of desks from (10, 12) to (11, 14) and (12, 10) to (13, 12). Contains pacing Grunts and Warp Pads at (13, 15) and (9, 11). (Accessed by opening door at 10, 8).

<hr>

<h1><code>Locations/Silph_Co_10F</code></h1>

10F Layout (Verified):
- Elevator at (13, 0). Stairs DOWN to 9F at (9, 0).
- Northern corridor runs E-W along Y=1 from X=13 to X=1. The path turns South at X=1.
- Eastern corridor at X=14 is blocked by a wall at Y=4. The East Area cannot be accessed from the Northern Corridor.
- SW Area: Accessed via Warp Pad at (3, 15) from 9F (13, 15). Contains a FULL HEAL at (3, 9).
- Isolated Eastern Room: Contains beds and Warp Pad at (17, 11).

<hr>

<h1><code>Locations/Silph_Co_4F</code></h1>

4F Layout (Verified):
- Elevator at (20, 0). Stairs UP at (24, 0) -> 5F (26, 0). Stairs DOWN at (26, 0) -> 3F (26, 0).
- Northern corridor DOES NOT connect East and West sides. Blocked by solid vertical wall at X=18.
- The eastern area (X>=21) is connected via the northern corridor.
  - Horizontal wall at Y=4 blocks X=21..23 and X=26..28. Gap is at X=24 and X=25.
  - X=24 and X=25 are blocked by desks from Y=7 to Y=14. The path south is at X=23.
  - Contains a Grunt at (26, 10).
- Central Room: Bounded by walls at X=7 (west) and X=20 (east). X=18 is a solid vertical wall with a gap at Y=14. X=10 is a solid wall from Y=6 to Y=13, but open from Y=14 to Y=16, connecting the East and West sides. Horizontal wall at Y=12 blocks direct access from the north, gap is at X=12/X=13. Grunt at (14, 6).
  - Y=14 horizontal corridor allows movement from X=11 to X=19.
  - East partition contains warp pad at (17, 11) (accessed via X=19 corridor -> Left -> Up into room).
  - West partition contains warp pad at (11, 7) (part of 4-way cycle). Solid wall at Y=8 restricts direct access from south; bypass via gap at X=12/13.
  - Warp pad at (11, 5) <-> 3F (3, 3). Bounded by walls at Y=6 and X=15. Does NOT lead to East Central Room.
- Western Area (X=1 to X=8): Accessed via gap at X=5, Y=12. Wall at X=9 separates this from the Central Room. 
  - X=1 and X=8 are clear vertical paths from Y=1 to Y=11.
  - Central block of desks from X=2 to X=7 (Y=4 to Y=9).
  - The southern part contains warp pad at (3, 15) <-> 3F (3, 15).
- IMPORTANT: The East half (containing pads 17, 11 and 11, 7) is accessible from the 4F elevator by walking South down the X=19 corridor to Y=14, crossing West to X=11, and walking North.

<hr>

<h1><code>Locations/Silph_Co_6F</code></h1>

6F Layout (Verified):
- Elevator at (18, 0). Stairs UP to 7F at (16, 0). Stairs DOWN to 5F at (22, 0).
- Eastern wall at X=15 separates the floor. Pass through gap at (15, 3), then go DOWN to Y=4/5 to pass through the gap at X=12 to reach the central area and bypass the Grunt at (13, 1).
- Team Rocket Grunt at (13, 1).
- Locked yellow doors at (20, 4) and (21, 4) block access to the Eastern Area.
- Eastern Area: Contains an item ball at (24, 11). Connects to a room at X=17..21, Y=12..16 via locked doors at (20, 12) and (21, 12).
- Room at X=17..21, Y=12..16 contains Scientist at (21, 13) and Warp Pad at (17, 15).
- Central Room: Accessed via locked doors at (10, 6) and (11, 6). Contains Silph Worker at (10, 8), defeated Grunt at (7, 10), and defeated Juggler at (13, 13). (Verified NO warp pad exists here on Turn 35035).
- West Room: Located west of X=16 corridor. Partitioned by desks at Y=15. Southern Corridor (Y=16) connects the X=16 corridor to the West Room (X=1..6). Found CALCIUM at (1, 9). Contains Scientist at (2, 13), defeated Grunt at (3, 8) and an NPC (Silph Worker) at (4, 2). Warp pad at (3, 11) connects to 7F (11, 9).
- Northern part of West Room (Y=2..7) is separated by a solid wall at X=6. Contains desks at X=4..5, Y=4..5. Contains Grunt at (3,7) facing Up, Grunt at (1, 5) facing Right, and Warp Pads at (5,3) and (5,7). Accessed via Warp Pad at (5,3).
- Warp Pads:
  - (11, 9) <-> 7F (3, 11) (Verified 2-way Turn 34931)
  - (17, 15) <-> 4F (9, 15)
- 6F (5, 7) <-> 11F (3, 2) (Verified Turn 35638)

<hr>

<h1><code>Locations/Silph_Co_2F</code></h1>

2F Layout (Verified):
- Stairs DOWN to 1F at (24, 0).
- Stairs UP to 3F at (26, 0).
- Northern Corridor (Y=1..3): Runs from X=12 to X=28. Blocked on the West by a wall at X=11. Blocked on the South by desks at Y=4. Contains Warp pad at (13, 3) connecting to ?F (3, 15) (TM09 room).
- Eastern area (X=24..28) has a gap in the desks at Y=4 around X=24/X=25.
- Central/Southern Area: Accessed via gap at (24, 4). Contains a Grunt at (24, 7) facing Down.
- West Area (X=1..10): Divided by a yellow wall at X=6 (Y=1..3).
  - X=1..5, Y=1..2 is an empty isolated area behind brown desks at Y=3.
  - X=7..10, Y=1..3 contains Silph Worker at (10, 1) who gives TM36. Accessed via the open southern area at Y=11.
- Southwest Area: Contains Scientist at (5, 12) facing Down, and Warp Pad at (9, 15).
- Southeast Area (X=23..28, Y=9..15): Connected to the rest of the Southern Area via Y=12/Y=13. Contains NPC at (24, 13). Potted plants block Y=14. Warp pad at (27, 15).

<hr>

<h1><code>Locations/Silph_Co_11F</code></h1>

11F Layout:
- Elevator at (13, 0). Stairs DOWN at (9, 0).
- A vertical corridor at X=14/X=15 runs south from the elevator area!
- Northern corridor runs west from elevator. The area south of Y=3 is walled off and inaccessible from the elevator. It contains a Scientist at (10, 5), and warp pads at (3, 2) and (10, 4).
- X=14/15 corridor leads south and dead-ends at Y=16. It contains a Grunt at (15, 9) but no items or warp pads.
- 11F (3, 2) <-> 7F (5, 7) (Verified Turn 35638)
The area accessible from (3, 2) has a vertical corridor from X=1 to X=3 that leads South.
- Shutter doors at (6, 13) and (7, 13) can be opened with the Card Key.
- Boardroom: South of the shutter doors is the Boardroom, containing Giovanni (defeated) and the Silph President at (7, 5). A solid wall at X=4 separates the Boardroom from the western corridor, spanning from Y=4 down to Y=13.
- Gap at (4, 14) connects the Boardroom to the western corridor at X=3.

<hr>

<h1><code>Locations/Silph_Co_3F</code></h1>

3F Layout:
- Elevator at (20, 0). Stairs UP at (26, 0) -> 4F (26, 0). Stairs DOWN at (24, 0) -> 2F (24, 0).
- Northern Corridor (Y=1..3): Runs from X=1 all the way East to the elevator/stairs area. Contains warp pad at (3, 3). Bounded on the South by a solid wall at Y=4.
- Empty Room: Spans X=1..5, Y=10..11. Accessed via locked doors at (4, 10) and (5, 10) from the Central Area. Contains NO items or warp pads.
- Gap at X=19 leads to a southern corridor. Solid wall at X=17 blocks West access from Y=6 to Y=13, EXCEPT for the shutter walls at (17, 8) and (17, 9) which can be opened with the Card Key! The southern corridor at Y=14/15 connects the East and West sides.
- Central Area: Accessed via Warp Pad at (11, 5) from 5F (3, 3).
  - Divided by a solid wall at X=10 from Y=6 downwards, AND a row of desks at Y=6 from X=11 to X=14.
  - West side (X=8/9): Contains Silph Worker at (8, 3). Path South along X=10 needs testing.
  - East side (X=11..13): Contains Scientist at (13, 9) and Warp Pad at (11, 11).
- Locked doors at (4, 10) and (5, 10) are located in the SW corner.
- Warp pad at 3F (3, 15) <-> 4F (3, 15).
- Warp pad at (23, 11) <-> 3F (27, 15) (Intra-floor warp, Verified Turn 33693). (23, 11) is blocked from the south by a row of desks at Y=13.
- NPCs: Silph worker at (20, 7), Grunt at (24, 8).
- Warp pad at (11, 11) <-> 6F (5, 3) (Verified Turn 35603). There is a yellow machine at (11, 9).
- Locked yellow doors found at (4, 10) and (5, 10). They are INACCESSIBLE from the southern corridor due to the solid wall at Y=13. They must be accessed from within the central area.
- 3F Central Area West Side path: From X=9, Y=4, path goes South to Y=12, then West to X=6, then North to access the locked doors at (4, 10) and (5, 10).

<hr>

<h1><code>Scratchpad/Warp_Network</code></h1>

Unverified/Untested Warp Pads:
- 11F (10, 4) (Inaccessible from elevator)

Isolated Rooms/Areas:
- 11F: Northern corridor from elevator is a dead end at X=4. Warp pads at (3, 2) and (10, 4) must be reached from other floors.

<hr>

<h1><code>Scratchpad/Warp_Network}৪৩}</code></h1>



<hr>

<h1><code>Locations/Saffron_Gym</code></h1>

Saffron Gym (3x3 Grid):
BL, BM(Start), BR
ML, MM(Sabrina), MR
TL, TM, TR

Connections:
1. BM R(11,15) <-> BR BR(19,17)
2. BR TL(15,15) <-> TR TR(19,3)
3. TR TL(15,3) <-> MR TL(15,9)
4. MR TR(19,9) <-> BR TR(19,15)
5. BR BL(15,17) <-> BL TR(5,15)
6. BL TL(1,15) <-> TR BR(19,5)
7. TR BL(15,5) <-> TL TL(1,3)
8. TL TR(5,3) <-> TM TR(11,3)
9. TL BR(5,5) <-> ML BL(1,11)
10. ML TR(5,9) <-> TM BL(9,5)
11. TM TL(9,3) <-> MR BL(15,11)
12. MR BR(19,11) <-> ML TL(1,9)
13. ML BR(5,11) <-> BL BR(5,17)
14. BL BL(1,17) <-> TM BR(11,5)
15. TL BL(1,5) <-> MM BR(11,11)

Path to Sabrina: BM(R) -> BR(TL) -> TR(BL) -> TL(BL) -> Sabrina!

Unmapped:
BM: L(7,15)

Defeated:
BM(10,15), BR(17,15), TR(17,1), MR(17,7), BL(3,13), TL(3,1), ML(3,7)

<hr>

<h1><code>Locations/Cinnabar_Island</code></h1>

Cinnabar Island:
- Cinnabar Gym: Entrance at (18, 3).
- Pokemon Lab: Entrances around the island, including (6, 9).
- Pokemon Center: Entrance at (11, 11).
- Poke Mart: Entrance at (15, 11).
- Pokemon Mansion: Entrance at (6, 3).

<hr>

<h1><code>Locations/Pokemon_Mansion</code></h1>

Pokemon Mansion:
- Layout 1F:
  - Entrance is a long hallway heading North.
  - Stairs UP to 2F at (5, 10).
  - Drop landing from 2F at (7, 10).
  - Yellow shutter at (16, 7)/(17, 7) is OPEN in State B (Verified Turn 37048).
  - East wing has no stairs to B1F. Thoroughly explored to dead ends at (21, 15) and (28, 7).
  - Can cross between East/West wings via passage at y=6/y=7 when shutter at (16, 7)/(17, 7) is OPEN (State B). Dark grey shutters block y=5 and y=8.
- Layout 2F:
  - Stairs DOWN to 1F at (5, 10).
  - 2F (7, 10) is an INVISIBLE drop hole. Falls to 1F.
  - Stairs UP to 3F at (6, 1) (leads from 3F to 2F North isolated section).
- Layout 3F:
  - Stairs DOWN to 2F North at (6, 1).
- Layout B1F:
  - B1F is largely unexplored. (Previous notes were a hallucination of 1F).
- Turn 36585-36588: Tested the Switch Statues at (12, 9) and (12, 11) from multiple sides (right, south, left if possible). Pressing A on them did not trigger any switch or text. Not all statues in the mansion are switches.
- EMPIRICAL PROOF (Turn 37975-37978): The switch statue at 3F (10, 4) toggles YELLOW shutters globally. Verified by pressing it and observing the yellow shutter at 3F (15, 10)/(15, 11) change from closed to open.
  - Known Yellow Shutter: 3F (15, 10)/(15, 11).
  - Known Yellow Shutter: 3F (15, 6)/(15, 7).
- Switch Statue at 1F (2, 5) IS functional when interacted with by standing at (2, 6) and facing Up (Tested Turn 38839). It toggles global states.
- Statues previously noted at y=11 were coordinate hallucinations. Actual y is 5.
- Hypothesis: Dark Grey shutters (e.g. 15,2 and 15,4) are permanent walls unaffected by switches. Needs rigorous testing.
- Stairs at 3F (25, 14) lead to an isolated 4x2 dead-end room on 2F.
- Layout 2F (Northern Section):
  - Reached via 3F stairs at (6, 1).
  - Permanent dark grey shutter at (9, 4)/(9, 5) blocks Westward movement.
  - A Diary/Book is located at (18, 2). Not stairs.
  - Yellow Shutter at (18, 8)/(19, 8) is CLOSED in State A.
- Drop from 3F (19, 14) leads to 2F at (19, 14) (Verified Turn 37124).
- Found a gap in the rubble on 2F at y=3, allowing crossing from the western side (x=18) to the eastern side (x=25).
  - HOWEVER, 2F East is permanently blocked by a solid wall at y=8, preventing access to y=3 from the 1F (23, 22) stairs.
- B1F South has an IDENTICAL visual layout to 1F South, including the checkered floor, statues, and even a Scientist NPC. However, B1F does NOT have tables and chairs. This similarity can cause severe confusion. ALWAYS check the stairs to confirm floor.
- EMPIRICAL PROOF (Turn 38877): The switch statue at 1F (2, 5) toggles the global shutter state. I verified that after pressing it, the yellow shutters at 1F (24, 13)/(25, 13) became open, allowing passage South through the East Wing.
- Drop from 3F (16, 14) leads to 2F at (16, 14) (Verified Turn 39433).
- MECHANIC: Exiting the Mansion to Cinnabar Island completely resets all switches and shutters to State A.
- CONSTRAINT: 2F East is permanently blocked by a solid wall at y=8. You CANNOT reach 2F North by crossing 2F East from the 1F (23, 22) stairs.
- Statue at 1F (18, 24)/(18, 25) IS a switch. Verified Turn 41375.
- EMPIRICAL PROOF (Turn 41475): Confirmed the y=22 corridor connects the West and East wings without shutters. The dark grey shutters at x=13 only span y=17 to y=21. The main entrance hallway is blocked at y=17 by a solid wall (x=1..8). Access between North/South sections of West Wing is via the Yellow Shutters at y=6/y=7 or the Dark Grey Shutters at x=9.
- EMPIRICAL PROOF (Turn 41482): Confirmed Yellow Shutter at 1F (16, 16)/(17, 16) is OPEN in State B.
- WARNING (Turn 41743): The Layout B1F notes above are a hallucination of 1F South (e.g. Diary at 6,12, Burglar, etc. are actually on 1F). Do not trust them. B1F is yet to be fully explored.
PATH TO 2F STAIRS (1F):
1. Enter Mansion at (21, 27) (East Wing, State A default).
2. Walk North to y=25.
3. Walk West through open dark grey shutter at (20, 25) to reach switch at (18, 25).
4. Press switch to toggle to State B.
5. Walk North along x=18 to y=16.
6. Walk West through open yellow shutters at (17, 16) and (16, 16).
7. Walk North along x=16 to y=7.
8. Walk West through open yellow shutter at (16, 7).
9. Walk West and South to the main stairs at (5, 10).
- EMPIRICAL PROOF: The stairs at 1F (23, 22) lead to 2F East. However, 2F (23, 23) is an invisible drop hole that falls back to 1F (21, 23). This area is a trap.

<hr>

<h1><code>Scratchpad/Pokemon_Mansion</code></h1>

Pokemon Mansion Navigation & Discoveries:

MECHANICS:
- State A: Dark Grey Shutters OPEN, Yellow Shutters CLOSED.
- State B: Dark Grey Shutters CLOSED, Yellow Shutters OPEN.

NEW ROUTING GOAL TO SECRET KEY (B1F):
1. I am currently trapped in 1F East in State B. The dark grey shutters at x=20 are closed, blocking exit to the main entrance.
2. The stairs at 1F (23, 22) lead DOWN to B1F. This is my only path.
3. Take the stairs at 1F (23, 22) DOWN to B1F.
4. On B1F, the path North along x=24 is blocked by dark grey shutters in State B. The path West along x=11 is also blocked by dark grey shutters.
5. I must find a switch in the accessible area of B1F to toggle the mansion back to State A.
6. Methodically test all unchecked statues in the accessible area of B1F, especially the row at y=23.

Tested Statues on B1F:
- y=19 (x=14 to x=19): NONE are switches.
- Need to test statues at y=23.

<hr>