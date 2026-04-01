<h1><code>Main</code></h1>

Badges: Boulderbadge
Team (5/6):
- Wartortle (HYDRO) - Lv 26 (74/74 HP)
- Rattata (FANG) - Lv 15 (39/39 HP)
- Pidgey (AERO) - Lv 26 (80/80 HP)
- Spearow (TALON) - Lv 10 (29/29 HP)
- Zubat (ECHO) - Lv 10 (29/29 HP)
Inventory: 4 Potions, 2 Antidotes, 5 Poké Balls, 1 Moon Stone, 1 HP UP, 1 Rare Candy, TM28, TM34, Town Map, S.S. Ticket.

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

Current Task: Investigate Cerulean City.
- Current Objective: Find the South exit to Vermilion City.
- Status: Defeated the Team Rocket Grunt, recovered TM28 (Dig), and fully healed the party at the Pokémon Center.
- Next Steps: Explore the southern edge of Cerulean City to find a path leading to Vermilion City so I can use the S.S. Ticket.

<hr>

<h1><code>Locations/Route_2</code></h1>

Route 2 Layout:
- Connects Viridian City (South) to Pewter City (North).
- Southern Section: Exits Viridian City at (8, 71).
- The main path is along X=8, X=9.
- A secondary path exists to the West, accessible by cutting a tree (currently blocked).
- Gatehouse to Viridian Forest: Entrance door is at (3, 43).
- Viridian Forest Gatehouse Interior: South exits at (4,7) and (5,7). Connects Route 2 to Viridian Forest. Layout: Counter divides room vertically at X=6 (walkable gap at (6,4)). North exit to Viridian Forest is at (5,0) only.
- Southbound travel along West path (X=3) requires one step through tall grass at (3, 63) before reaching a clear path at Y=64 that connects back to the main South exit at X=8.
- Northern Section (post-Forest): Gatehouse North exit is at (3, 11). Path North at X=3 is a dead end nook at (3, 7). The clear path continues North along the East side at X=8. Exit to Pewter City is at (8, 0).

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
- Following the tall grass South at X=16..18, the path turns West at Y=16..19, leading to clear ground. There is a decorative dirt patch at (13, 19) (verified nothing happens when interacted with). The path is blocked West at X=10 by trees, and South at Y=21 by trees. The path continues North through tall grass starting at X=11..13, Y=17, but this North path is a dead end at Y=1.

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
- Far East Section: The Northern Lane is blocked by a solid mountain wall spanning from X=50 to X=55. You MUST jump South into the eastern grass pit, navigate East past X=50, and use the ramp at (59, 7) to return to the Northern Lane leading to Route 4.
- Bypassing the Mountain Wall: To reach Route 4, you must bypass the X=50 mountain wall from the NORTHERN LANE (West of X=50). Find a path North of Y=4. Currently tracking a one-way ledge at Y=3 blocking Northward movement from X=38 onwards. Must find a gap in this ledge before X=50.
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
- Keep sharing EXP with FANG (Lv 15) to level him up.
- HYDRO (Lv 26) and AERO (Lv 26) are my strongest, but both are very low on HP.
- Need to return to Cerulean City to heal at the Pokémon Center soon.
- Executing EXP share: Sent FANG in against Lv 17 Drowzee (Turn 6428), switching to AERO on turn 1 to take the hit.

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
- Safe Route to Cerulean: To protect low HP, avoid the tall grass (X=30 to X=60) by jumping South over the Y=9 ledge to the plain ground at Y=10. Follow Y=10 East until X=61. Walk West along Y=8 to the ramp at (57, 7), go UP the ledge, then jump back South at (59, 7) to completely bypass the Lass at (63, 3) and tall grass on the upper plateau. Continue East on Y=8 until X=79 (blocked by white fence). Jump South over the Y=9 ledge to land on the paved path at Y=10.
- Cerulean City Entrance: The paved path at Y=10 and Y=11 continues directly East into Cerulean City, safely bounded by white fences at Y=9 and Y=12.

<hr>

<h1><code>Locations/Mt_Moon</code></h1>

Mt. Moon Layout (1F):
- Entrance: South exit to Route 4 at (14, 35). Starts on Brown Speckled Floor.
- Main Path (Brown Floor):
  - From (14, 35), goes North to Y=24.
  - Path East is partially blocked by a solid sign at (15, 23), but there is an open corridor Eastward at Y=22.
  - The Y=22 corridor goes East to X=21, then turns NORTH into a 2-tile wide path at X=20/X=21. The north branch of this path terminates at a blue rock wall at Y=8/9.
  - Path North at X=14 is blocked by a solid blue rock wall at Y=21. The true path forward to the Northern Area (and the 1F (17, 11) ladder) branches off the X=20/21 corridor: Go East to X=20, North to Y=15, East to X=30, North to Y=7, West to X=17, and South to the ladder at (17, 11).
  - Path goes West at Y=24, crossing to X=8, leading to the South-West area.
- South-West Area (Brown Floor):
  - Spans X=2 to X=12. Bounded North by wall at Y=19, West by wall at X=1.
  - Bounded South by a horizontal cliff (Purple floor) at Y=34. This is a solid impassable boundary, NOT a jumpable ledge (Tested Turn 4356).
  - This entire area is a completely empty dead end.
- Purple Floor Areas:
  - Access from the Brown Floor is currently unknown; searching for stairs or a gap in the cliffs.
- 1F Northern Area (West of X=18 wall):
  - Reached via the path North of the (17, 11) ladder area.
  - Bounded West by a solid blue rock wall at X=13 from Y=2 down to Y=15. At Y=16, the area opens to the West. The Youngster at (12, 16) blocks the Y=16 path; bypass him via Y=17. The clear path North through the Y=15 cliff is specifically at the X=14 gap.
  - Bounded North by a cliff at Y=1 (Purple floor at Y=1 drops down to Brown floor at Y=2). This cliff is impassable from the South (Verified Turn 4427).
  - The path along Y=2 extends East to a solid blue rock wall at X=38 (Verified Turn 4443).
  - Bounded South by a solid blue rock wall at Y=20 (from at least X=14 to X=18), separating it from the main entrance path. Further West, the southern boundary is a cliff edge dropping to Purple floor at Y=18 (from X=2 to X=9).
  - Middle-Western Section (X=2 to X=12, North of Y=18): Contains a Youngster at (5, 6) facing Left, and a ladder DOWN at (5, 5) (Discovered Turn 4481).

Mt. Moon Layout (B1F):
- Took ladder at 1F (17, 11) down to B1F (25, 9). This B1F platform is a wide purple room.
- The B1F platform contains a ladder back up at (25, 9) and a new ladder down at (17, 11).
- The platform is bounded by a blue rock wall on the North at Y=7, void West at X=13, and void South at Y=12. It is a linear path between the two ladders with no other exits.
- Ladder at (21, 17) is reached via a narrow path East along Y=17 from the B1F platform accessed via 1F (5, 5).
- B1F Central Area: From the ladder at (25, 15), the platform extends East to X=27 (black void). North is blocked by a blue wall at Y=13.
- B1F Central Area: From the ladder at (25, 15), a path goes West to X=24, then South to a wide room at Y=26.
- The Y=26 room spans from X=10 (West dead end, exhaustively verified Turn 3926) to X=27 (East dead end). The entire western edge is bounded by rocks and contains nothing of interest. It contains a ladder down to B2F at (13, 27).

Mt. Moon Layout (B2F):
- Reached via ladder at B1F (13, 27). Arrived at (15, 27).
- Stairs at (24, 23) lead to a small 2x2 dead-end platform (Item: HP UP).
- Ladder at B2F (21, 17) is on the lower (purple) floor, bounded West by a chasm. The path goes North to Y=14, East to X=26, then South to stairs UP at (26, 15) leading to a raised platform.
- The stairs at (26, 15) and (32, 15)/(33, 15) both lead UP to the same Southern Raised Platform (Y=16 to Y=18).
- This Raised Platform spans from X=25 to X=34. It contains a Rocket Grunt at (29, 17) but NO items (previous item ball sighting was a visual error). West is blocked by a wall at X=24.
- The entire B2F area accessed via 1F (5,5) is a self-contained dead end. We must check the item ball to verify if it is a fossil.
- Lower floor path wraps around the HP UP platform and goes West along Y=20.
- B2F South-West Section: Reached via ladder at B1F (13, 27) to B2F (15, 27). Previous notes claim this is a dead end, but only mention the North path being blocked at Y=21. The South path remains unverified.
- Battled Team Rocket Grunt at (15, 22) on Turn 2282.
- B2F North-East Section: Reached via ladder at B1F (17, 11). Arrived at B2F Raised Platform at (25, 9).
- The Raised Platform has a Rocket Grunt at (29, 11) and a bluish shell at (33, 9).
- The platform has a dead-end alcove North along X=32-35, blocked at Y=5 and West at X=31 by blue rocks.
- The Raised Platform is bounded South by a solid cliff at Y=11. The area West of the B2F (25, 9) ladder is blocked by a blue rock wall at X=23. The entire B2F area accessed via 1F (17, 11) is a confirmed dead end.
- 1F East/West Raised Platform Boundary: Area North of Y=10 (from X=17 to X=29) is blocked by a solid light blue rock wall at Y=8/9. The ladder at (17, 11) is south of this wall, bounded East by a blue wall at X=18/19.
- However, at X=30 to X=32, there is a gap in the horizontal wall, allowing movement NORTH past Y=10 (Discovered Turn 4401).
- 1F East Elevated Platform details: The eastern edge (X=34, 35) is separated from the main area (X=20-25) by a vertical blue rock wall at X=33 that spans from at least Y=11 to Y=27. To move between the X=34 strip and the X=25 area, you must go around this wall to the North at Y=7.
- 1F East Elevated Platform (South-East Dead End): The area spanning from X=30 to X=37, and Y=16 down to Y=33, is a complete dead end bounded by rock walls. It contains no ladders or items. Verified turn 3863.
- At B2F (33, 9), there is a bluish shell-like object. It acts as an impassable solid obstacle. I have rigorously tested pressing 'A' on it from all accessible sides (Left, Top, Bottom, Right) and it produces no text or item. It is completely un-interactable background scenery, NOT a fossil.
- The path wrapping East around the HP UP platform is blocked at (27, 22) and (28, 21) by blue rock walls.
- B2F South-West Section: The area south of the (15, 27) ladder is a solid wall at Y=29. The area West is a solid blue wall at X=13.
- The path East from (15, 27) goes along Y=26/27 to X=28, connecting with the Y=20 corridor. The path North from (15, 27) goes up to Y=22, where it is blocked North by a blue rock wall at Y=21. It continues East along Y=22.
- The entire South-West B2F section is a continuous loop around a central rock structure, bounded by Y=21 (North), Y=29 (South), X=13 (West), and X=29 (East). Exhaustively verified on turn 4662. There are no other stairs or ladders here.
- 1F East Elevated Platform (Southern Area): The area from X=20 to X=29, south of Y=26, contains the Super Nerd at (24, 31). The item ball at (20, 33) was a visual artifact that disappeared when stepped on. This entire area is a dead end. Its connection to the 1F Main Path is currently unverified and requires further exploration.
- B1F North-West Section: Reached via ladder at 1F (5, 5). Arrived at B1F (5, 5) on Raised Floor. Item ball at (2, 2) contained a Moon Stone. Team Rocket Grunt at (5, 6). Path extends East along Y=17 past X=18 to X=21, where there is a ladder DOWN at (21, 17) to B2F.
- B2F North-West Expansion: Reached via ladder at B1F (21, 17). Contains the stairs at (26, 15) and (32, 15) leading to the Southern Raised Platform. The massive lower floor area East of X=32 is bounded East by a solid wall at X=39 and South by a solid wall at Y=25. A 3-tile wide corridor (X=32 to X=34) continues South to Y=32. A 2-tile wide path turns West at Y=31/32. The path continues West of X=13 along Y=31/32, bounded by a rock wall at Y=30 and a dark wall at Y=34. At X=7, there is an opening North into a new corridor. This corridor goes North to Y=17, turns East to X=12, and goes North to stairs UP at (12, 9) and (13, 9).
- B2F Lower Floor Pocket (X=31 to X=36, Y=12 to Y=15): Accessed via stairs at (32, 15). Completely bounded by Y=11 (cliff), X=30 (wall), X=36 (wall), and Y=16 (wall/chasm). Confirmed dead end. The true path is NOT here.
- B2F Fossil Area: Reached via stairs UP at (12, 9) and (13, 9). The true fossils were located at (12, 6) and (13, 6). The Super Nerd is now at (12, 7). The exit is a ladder at (5, 7). To reach it from the fossil area, walk East to X=13, North to Y=4, West to X=3, South down the stairs at (3, 5), East to X=5, and South to the ladder.
- B1F Exit Corridor: Reached via ladder UP from B2F (5, 7). Arrives at B1F (23, 3). A short linear path leads East to a ladder UP at (27, 3).

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

<hr>

<h1><code>Locations/Cerulean_City</code></h1>

Cerulean City Layout:
- Boundaries & Connections: West entrance (X=0, Y=18/19) from Route 4. Path North to Nugget Bridge is located at X=20/21, starting above Y=10.
- West Area: Trade House (Jynx for Poliwhirl) at (13, 15). Ruined House at (9, 11) with a backyard that dead-ends at X=18.
- Central Area: Pokémon Center at (19, 17). Signpost at (23, 19). Robbed House at (27, 11) - Inside, follow the footprints around the right side of the room to reach the hole in the back wall leading to the backyard.
- East Area: Cerulean Gym entrance at (30, 19). Poké Mart at (25, 25).
- Dead Ends & Blockages: Path East of the Blocked House (X=28-31, Y=12-15) is a dead end. Ledges block direct Northward movement above the Gym.
- Cerulean Gym: Entrance at (30, 19). Gym Guide at (7, 10) inside. Leader is North at X=4/X=5. Awards Cascadebadge (up to L30 obey, CUT outside battle).
- Nugget Bridge: Connected to Cerulean City North exit. Starts at (11, 39).
- Southern Boundary: The southern edge of the city (Y=28) is mostly blocked by dense bushes and a Cut tree (19, 28). There is a gap at X=16 with a "house roof edge" that needs to be tested as a potential exit.
- Navigation Note: The gap at (32, 19) is a solid Ledge_Inner_Corner and cannot be passed. The path North must be elsewhere.

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

<hr>

<h1><code>Scratchpad/Route25_Mechanics</code></h1>

Hypothesis: The item ball at (22, 2) on Route 25 might still be accessible. After a map reset, the defeated Jr. Trainer M at (24, 4) returns to his original position. It needs to be empirically tested whether stepping into his sightline at (24, 7) will cause him to move towards the player even if he is already defeated.

<hr>

<h1><code>Tracking/Rival_Data</code></h1>

Rival Team (GARY):
- Bulbasaur (Confirmed in Cerulean City battle).

<hr>

<h1><code>Scratchpad/Vermilion_Route</code></h1>

- Goal: Reach Route 5 (Vermilion City route).
- Route 4 was proven to be a dead end. Cerulean City MUST have a path connecting the area near the Pokémon Center (Y=17) to the Northern area (Robbed House at Y=11).
- Hypothesis: The path North is the gap at X=10, 11, 12, between the Trade House (13, 15) and the Ruined House (9, 11).
- I MUST walk West to X=11 and walk North to test this gap!
- The southern boundary from X=2 to X=34 is completely solid. I cannot walk around the building at (16, 29).
- Therefore, the exit to Vermilion City MUST be a warp inside a building.
- Plan: Enter the house at (19, 25), which I have not checked yet. It may be the Underground Path.

<hr>