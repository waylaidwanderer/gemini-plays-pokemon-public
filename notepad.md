<h1><code>Main</code></h1>

Badges: Boulderbadge
Team:
- Pidgey (AERO) - Lv 12
- Squirtle (HYDRO) - Lv 13
- Metapod (KEWLAR) - Lv 4
- Rattata (FANG) - Lv 11
- Caterpie (MOTHRA) - Lv 5
Rival Team (GARY):
- Bulbasaur
Inventory: 3 Potions, 4 Antidotes, 4 Poké Balls.
Survival Rule: Always verify inventory (Potions/Antidotes) before entering dungeons or long routes to prevent forced retreats.
Survival Rule 2: If a Pokémon is poisoned, use an Antidote IMMEDIATELY after battle. Overworld poison damage (1 HP per 4 steps) is lethal.

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

Current Task: Head East to Route 3 towards Mt. Moon and Cerulean City. (Boulderbadge obtained!)

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
- Battle Item Menu: The item menu in battle remembers the cursor's last position. Attempting to use a key item like the Town Map triggers Professor Oak's warning and wastes a turn. Always verify cursor position!
- Party Menu Cursor: The cursor wraps around. Pressing Up from the 1st slot moves the cursor to the last slot (e.g., 5th slot) (Verified Turn 1251-1252).
- Battle Item Menu: Pressing A on an item in battle uses it immediately; there is no USE/TOSS sub-menu like in the overworld.

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
- Pewter Gym: Located at (16, 17). Blocked from the East by fences. Access by routing West along Y=13 to bypass the house, then South, then East along Y=18 to reach the door.
- Poké Mart: Located at (23, 17).
- Crossing: To cross between the East side (Poké Mart) and West side (Gym/Center), use the clear horizontal path at Y=13. Do NOT use X=10 to go South, as it is blocked by trees at Y=21.
- Navigation from Gym to Center: The Gym area is boxed in by trees to the South (Y=21) and East (X=18). To leave, you MUST go North via X=10 to Y=13, then East to X=19, then South to Y=26, then West to reach the Center entrance at (13, 25).
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
- Southern Lane (Y=8 to Y=13): A return path West to Pewter City. Blocked to the East by trees at X=23. Plain ground, no encounters.
- Tall Grass: Located at X=24 to X=32, Y=10 to Y=13. Bounded by trees to the West (X=23) and ledges to the South. To enter, take the Northern Lane East to X=27, then head South through the gap.
Trainers:
- Lass at (23, 4) facing Down.
- Bug Catcher at (24, 6) facing Right.
- Youngster at (22, 9) facing Up.
- NPC (Blue sprite, likely a Lass) at (33, 10) facing Down.
- Lass at (15, 9) facing Left. Uses Pidgey.
- Gap in the Y=11 ledge at X=15 allows returning North to the Y=10 path.

<hr>

<h1><code>Scratchpad/Training_Plan</code></h1>

Training Plan (Route 3):
- AERO (Lv 12) has learned Quick Attack and is doing well.
- FANG (Lv 10) is currently battling to gain more EXP.
- Goal: Get AERO and FANG to at least Lv 12-14 before entering Mt. Moon.
- Strategy: We have 3 Potions. Use them carefully. Switch-train FANG against weaker/passive enemies like Metapod to conserve HP.

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

Route 3 Tall Grass:
- Located from X=24 to X=32, Y=10 to Y=13.
- Pacing here triggers encounters for training.
- Encounters seen: Pidgey (Lv 6), Spearow (Lv 7).
- Encountered Spearow (Lv 5). Attempting to catch.
- Encountered Lv 6 Pidgey, gave 47 EXP (Turn 1344).

<hr>