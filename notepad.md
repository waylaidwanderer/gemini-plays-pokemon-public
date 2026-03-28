<h1><code>Main</code></h1>

Team:
- Squirtle (HYDRO)
Rival Team (GARY):
- Bulbasaur
[Turn 103, Mar 27 2026] 100-Turn Reflection:
- Progress: Successfully navigated Route 1 and arrived in Viridian City. HYDRO is at 7/24 HP and urgently needs healing.
- Hygiene: Cleaned up Route 1 routing notes and consolidated Battle Data. Added Map Marker for the Route 1 South exit.
- Tools: Deleted the unsafe 'spam_a' tool as it lacked HP-awareness. Considering writing a Pokémon Center healing macro in the future once the interaction sequence is verified.
- Error Analysis: Confused tall grass with solid trees on Route 1. Learned to visually distinguish light green walkable grass from dark green solid 'Obstacle/Dense_Bush' tiles.

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

Route 1 Optimal Path (South to North):
- The Western path (X=1, X=2) is the return path (North to South) containing one-way ledges. Do not attempt to use it to go North.
- The path North winds along the Eastern side of the route.
- Ledge 1 (Y=27): Gap is at X=6, X=7, X=8.
- Ledge 2 (Y=19): Gap is at X=9.
- Ledge 3 (Y=13): Gap is at X>=14. Dark green leaf tiles (e.g., at X=12, Y=13) are solid obstacles (Dense Bushes).
- Ledge 4 (Y=5): Gap is at X>=14. Moving straight North from (14,9) through the gap.
- Southbound Strategy: The western path is blocked from the top by a white fence at X=3. However, since ledges are one-way DOWN (South), I can simply walk straight South through the central/eastern paths and jump the ledges without needing to find gaps. Currently at (4,2), heading South.
- [Turn 123] Encountered Dense Bushes at (4,13) and (5,13). Must shift East to X=6 to jump over the ledge at (6,13).
- [Turn 126] At (6,22). Path South is blocked by trees at Y=23. Moving East to X=16 to use the ledge at (16,23) to continue South.
- [Turn 126] Jumped ledge at (16,23). Currently at (16,25). Jumping ledge at Y=27, then moving West to X=11 and South to exit to Pallet Town.

<hr>

<h1><code>Locations/Viridian_City</code></h1>

Viridian City Points of Interest:
- South Exit to Route 1: (21,35)
- Sign at (21,29)
- Pokémon Center Door: (23,25)
- Poké Mart Door: (29,19)

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
Current Task: Return to Pallet Town and deliver the parcel to Professor Oak in his lab.

<hr>