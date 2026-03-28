<h1><code>Main</code></h1>

Team:
- Squirtle (HYDRO)
Rival Team (GARY):
- Bulbasaur
[Turn 31, Mar 27 2026] Log updated.
[Turn 51, Mar 27 2026] 50-Turn Reflection:
- Progress: Starter acquired, rival defeated, heading to Route 1.
- Hygiene: Map markers for Pallet Town are clean. Notepads are organized.
- Custom Tools: Considered creating tools for battle logic or grass exploration, but manual control is safer for now.
- Error Analysis: Tracing exact tile steps prevents wall-bumping. Must continue this practice in Route 1.

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

<hr>

<h1><code>Routing/Route_1</code></h1>

Route 1 Optimal Path (South to North):
- The Western path (X=1, X=2) is the return path (North to South) containing one-way ledges. Do not attempt to use it to go North.
- The path North winds along the Eastern side of the route.
- Ledge 1 (Y=27): Gap is at X=6, X=7, X=8.
- Ledge 2 (Y=19): Gap is at X=9.
- Ledge 3 (Y=13): Gap is at X>=14. Dark green leaf tiles (e.g., at X=12, Y=13) are solid obstacles (Dense Bushes).
- Ledge 4 (Y=5): Gap is at X>=14. Moving straight North from (14,9) through the gap.

<hr>

<h1><code>Scratchpad/Battles</code></h1>

[Turn 94] Encountered a wild Rattata. HYDRO is at 10/24 HP. I have 1 Potion from the Poke Mart employee. Waiting to see the Rattata's level before deciding to fight or heal.
- [Turn 95] Rattata is only Lv 3. HYDRO (Lv 7) is at 10/24 HP. The level advantage means Rattata's attacks should do very little damage. Opting to save the Potion and use FIGHT -> TACKLE instead.

<hr>