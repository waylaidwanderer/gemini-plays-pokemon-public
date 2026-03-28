<h1><code>Main</code></h1>

Team:
- Squirtle (HYDRO) - Lv 9
- Pidgey (AERO) - Lv 7
- Rattata (FANG) - Lv 6
- Metapod (KEVLAR) - Lv 4
- Caterpie (MOTHRA) - Lv 5
Rival Team (GARY):
- Bulbasaur
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
- Wild Lv 2 Pidgey yields 15 EXP (verified Turn 58).
- Wild Lv 3 Pidgey yields 23 EXP (verified Turn 76).
- Wild Lv 3 Rattata yields 24 EXP (verified Turn 97).
- Professor Oak automatically heals the party after major story events (verified after first rival battle on Turn 52, and delivering parcel/receiving Pokédex on Turn 166).
- Catching Mechanics: Poké Balls can fail even on full HP, very low-level Pokémon (e.g., Lv 3 Pidgey broke out at full HP, verified Turn 235). Weaken them first if possible, or expect to use multiple balls.
- Weakening: Tackle from a Lv 7 Squirtle deals ~50-60% damage to a Lv 3 Pidgey, safely putting it into the yellow HP zone without OHKOing it (verified Turn 243).
- Catching Mechanics: Full HP catches fail frequently even on Lv 2s (Rattata broke out twice, Turns 298/303). Weakening to red HP using weak moves (Lv 3 Gust) allowed an immediate catch (Turn 311).
- Switch-Training: Swapping a Pokémon out shares the EXP among all participants. Odd EXP values are truncated (e.g., Lv 3 Pidgey yields 23 EXP total, but gave 11 EXP each to FANG and HYDRO, verified Turn 437).
- Damage Scaling: A Lv 4 Pidgey's Gust deals ~3 damage to a Lv 8 Squirtle, and ~5 damage on a critical hit (verified Turn 496).
- Free Switch-In: When an enemy Pokémon faints and the game asks "Will [Player] change POKEMON?", selecting YES allows sending out a new Pokémon without taking a hit that turn. This is ideal for sharing EXP with weak Pokémon like a Lv 3 Pidgey, who can be sent out freely and then immediately switched out on the first turn of the next battle round.
- Stat Stages: Stat-boosting moves like Harden will display 'Nothing happened!' once the stat has reached its maximum level (verified Turn 648 against a Kakuna spamming Harden).
- Catching Mechanics: A Poké Ball failed to catch a Lv 4 Metapod in the yellow HP zone (verified Turn 770). Multiple balls are often required even when weakened.
- Wild Encounter: Encountered a Lv 5 Caterpie in Viridian Forest tall grass at (25, 36) on Turn 792. Using it to switch-train KEVLAR.
- Weakening: Tackle from a Lv 6 Rattata deals ~40-50% damage to a Lv 5 Caterpie (verified Turn 796).
- Damage Scaling: A Lv 6 Pidgey's Gust (Critical Hit) deals ~80% damage to a Lv 3 Caterpie (verified Turn 810).

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

Current Task: Reached Pewter City. Healing party at the Pokémon Center, then planning to explore the city, visit the Poké Mart, and challenge the Pewter Gym.

<hr>

<h1><code>Locations/Route_2</code></h1>

Route 2 Layout:
- South exit to Viridian City: (8, 72) connects to Viridian City at (18, 0).
- Sign at (9, 73).
- Ledge at Y=61. Gap is at X=7 (walkable both North and South, verified Turn 428).
- Dense Bushes block movement South on the East side. The bushes start at X=5 (Y=54 to Y=56), and X=6 to X=13 at Y=53. To travel South, use the tall grass at X=3 or X=4.
- Tall grass is found at X=4 (extending North from Y=57) and X=5 (Y=57).
- Item Ball spotted at (13, 54). Currently inaccessible from the main (West) path due to a wall of Dense Bushes.
- Item Ball spotted at (13, 45). Currently inaccessible from the main (West) path due to a solid wall of trees at X=11.
- Small building/structure at (5, 65). Best path South is via X=8.
- Ledge at Y=47 blocks Northbound movement from X=0 to X=7. Bypass by walking East through tall grass at Y=48 to reach the clear path at X=8.
- Gatehouse to Viridian Forest: Located at the north end of Route 2. Entrance door is at (3, 43).
- Viridian Forest Gatehouse Interior: South exits are at (4,7) and (5,7). Connects Route 2 to Viridian Forest.
- Viridian Forest Gatehouse Interior Layout: A counter divides the room vertically at X=6, but there is a walkable gap at (6,4). The North exit to Viridian Forest is at (5,0) only. The tile at (4,0) is a wall.
- Southbound travel along the West path (X=3) requires exactly one step through tall grass at (3, 63) before reaching a clear horizontal path at Y=64 that connects back to the main South exit at X=8.
[Turn 876] Exited the Viridian Forest Gatehouse and arrived at the Northern section of Route 2 at (3, 11). Heading North towards Pewter City.
[Turn 877] The path North at X=3 is a dead end nook at (3, 7). The clear path continues North along the East side at X=8. Routing South to Y=8, then East to X=8, then North.
[Turn 880] Proceeding North from (8, 0) on Route 2 to enter Pewter City.

<hr>

<h1><code>Scratchpad/Route2_Exploration</code></h1>

[Turn 217] Re-entered Route 2 at (8, 71). Heading North to find tall grass for catching new team members. Avoid Y=72, as it triggers the warp back to Viridian.

<hr>

<h1><code>Mechanics/Menu_Behavior</code></h1>

Menu Cursor Memory: In many menus (like the Start menu and Party action menu), the cursor remembers its last selected position rather than resetting to the top. Always visually verify the cursor's starting position before executing blind button sequences (Verified Turn 449-451).
- Battle Item Menu: The item menu in battle remembers the cursor's last position. Attempting to use a key item like the Town Map triggers Professor Oak's warning and wastes a turn. Always verify cursor position!

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
- Sign spotted at (19, 29).
[Turn 884] Read a sign at (19, 29) which confirmed the switch-training mechanic: "Any POKéMON that takes part in battle, however short, earns EXP!". Proceeding North along the X=18 path to explore the city.
- Pokémon Center: Located on the West side of the main path. The building's sign says "POKé" and is visible at (14, 25).
- Pewter Gym: Located at (16, 17).
- Poké Mart: Located at (23, 17).
[Turn 885] The main path at X=18 is blocked by trees at Y=21. Routing East to X=19 to bypass them and continue North.
[Turn 894] Fully healed party at the Pewter City Pokémon Center. Exiting the center now to head to the Poké Mart.

<hr>