<h1><code>Main</code></h1>

Team:
- Squirtle (HYDRO)
Rival Team (GARY):
- Bulbasaur
[Turn 156, Mar 27 2026] 150-Turn Reflection:
- Progress: Delivered Oak's Parcel, obtained Pokédex from Prof. Oak, and got the Town Map from Gary's Sister. Heading North through Route 1 back to Viridian City to heal and buy Poke Balls.
- Hygiene: Cleaned up and consolidated Route 1 routing rules. Discarded outdated turn-by-turn narrative.
- Tools: Fixed the 'chunk_a' tool schema by removing the internal harness parameter.
- Error Analysis/Strategy: With HYDRO at 7/24 HP, I must move in small chunks through Route 1 to immediately Run from any wild encounters. The Route 1 Northbound path is fully mapped (Gaps at X=8, X=9, X>=14).

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
- Oak automatically heals the party after the first rival battle (verified Turn 52).
- Wild Lv 2 Pidgey yields 15 EXP (verified Turn 58).
- Wild Lv 3 Pidgey yields 23 EXP (verified Turn 76).
- Wild Lv 3 Rattata yields 24 EXP (verified Turn 97).

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
- Poké Mart Door: (29,19)
- Ledge at Y=27 blocks Northbound travel. The gap to bypass it is at X=19.

<hr>

<h1><code>Locations/Pokemon_Center</code></h1>

Pokémon Center Layout (Standard):
- Entrance/Exit: (3,7) and (4,7)
- Healing Counter (Nurse Joy): Stand at (3,3) facing Up.
- PC: Located at the right side of the counter (usually X=13, Y=1 in standard, but let's verify later).
[Turn 107] Interacting with Nurse Joy to heal HYDRO. Selecting 'HEAL' from the prompt.

<hr>

<h1><code>Locations/Poke_Mart</code></h1>

Poké Mart Layout (Standard):
- Entrance/Exit: (3,7) and (4,7)
- Counter: (1,5) to (3,5)
- Cashier: (1,4) or (2,4) or (3,4) depending on the store. In Viridian, he speaks to you immediately upon entering.

<hr>

<h1><code>Quests/Main_Story</code></h1>

[Turn 114] Received Oak's Parcel from the Viridian City Poke Mart cashier.
[Turn 141] Delivered Oak's Parcel to Professor Oak. Received the Pokédex! Gary mentioned getting a Town Map from his sister.
[Turn 149] Received the Town Map from Gary's sister.
Current Task: Head North through Route 1 back to Viridian City to buy Poke Balls, then proceed to Route 2.

<hr>

<h1><code>Scratchpad/Route1_LowHP</code></h1>

Navigating Route 1 North.
[Turn 166] Discovered Hydro is actually at 24/24 HP! Professor Oak must have fully healed the party when we delivered the parcel and received the Pokédex. No longer at risk of fainting. Will still Run from encounters to speed up the trip to Viridian City to buy Poke Balls.

<hr>