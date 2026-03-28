<h1><code>Main</code></h1>

Team:
- Squirtle (HYDRO) - Lv 8
- Pidgey (AERO) - Lv 3
- Rattata (FANG) - Lv 4
Rival Team (GARY):
- Bulbasaur

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

<hr>

<h1><code>Quests/Main_Story</code></h1>

Current Task: Train FANG (currently Lv 4, needs 17 EXP) to Lv 5 on Route 2 using switch-training with HYDRO. HYDRO is at 10/26 HP, which is risky but should be enough for one last battle.

<hr>

<h1><code>Locations/Route_2</code></h1>

Route 2 Layout:
- South exit to Viridian City: (8, 72) connects to Viridian City at (18, 0).
- Sign at (9, 73).
- Ledge at Y=61. Gap is at X=7 (walkable both North and South, verified Turn 428).
- Dense Bushes block movement East from the grass. The bushes start at X=5 (Y=54 to Y=56), and X=6 to X=12 at Y=56.
- Tall grass is found at X=4 (extending North from Y=57) and X=5 (Y=57).
- Item Ball spotted at (13, 54). Currently inaccessible from the main (West) path due to a wall of Dense Bushes.
- Small building/structure at (5, 65). Best path South is via X=8.
- Ledge at Y=47 blocking Northbound movement across the grass.

<hr>

<h1><code>Scratchpad/Route2_Exploration</code></h1>

[Turn 217] Re-entered Route 2 at (8, 71). Heading North to find tall grass for catching new team members. Avoid Y=72, as it triggers the warp back to Viridian.

<hr>

<h1><code>Scratchpad/Training_Plan</code></h1>

- Plan to train FANG (currently Lv 4 Rattata) to at least Lv 5 on Route 2 before taking on Viridian Forest.
- Method: Switch-training. FANG is in slot 1. When battle starts, switch to HYDRO to tank hits and secure the KO.
- Status: Switch-training in progress. Pacing along X=4 (Y=48 to Y=51) to trigger encounters.
- [Turn 458] FANG needs 17 EXP. Current enemy is Lv 3 Pidgey (yields 11 EXP shared). We will need exactly one more battle after this to reach Lv 5. HYDRO is at 10 HP, so we MUST return to the Pokémon Center to heal before the final battle.

<hr>

<h1><code>Mechanics/Menu_Behavior</code></h1>

Menu Cursor Memory: In many menus (like the Start menu and Party action menu), the cursor remembers its last selected position rather than resetting to the top. Always visually verify the cursor's starting position before executing blind button sequences (Verified Turn 449-451).

<hr>