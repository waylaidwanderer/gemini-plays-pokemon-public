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

<h1><code>Scratchpad/Route_1</code></h1>

Routing through Route 1:
- Objective: Head north from Pallet Town through Route 1 to reach Viridian City.
- Hypothesis: Route 1 is a mostly linear path north with patches of tall grass. Expect wild encounters like Pidgey and Rattata.
- Strategy: We have no Poké Balls yet, so we cannot catch anything. We should battle a few wild Pokémon to level up HYDRO, using our Potion if HP gets too low. If HP gets dangerously low, we should run from battles or return to Mom in Pallet Town to heal.
[Turn 47] Routing to Route 1: Navigating around Oak's Lab. Bumping into the building at (10,11), so shifting left to X=8 before proceeding north.
[Turn 48] Routing from (8,8) to Route 1. Traced path: Up 3 to (8,5), Right 2 to (10,5), then Up towards (10,1).
[Turn 49-52] Reached the edge of Route 1 at (10,2). Attempted to use a Potion, but discovered HYDRO is actually at 22/22 HP. Professor Oak automatically heals the player's Pokémon after the first rival battle. Potion use failed ("It won't have any effect."). Proceeding north into the tall grass.
[Turn 53] Successfully entered Route 1. The map transitions at Y=35. Proceeding North through the grass.
[Turn 54] Encountered a wild Pidgey at (10, 34). Initiating battle to gain EXP for HYDRO.
[Turn 55] Battle with Lv 2 Pidgey. HYDRO is at 22/22 HP. Selecting FIGHT -> TACKLE.
[Turn 56] Pidgey used Gust (HYDRO HP: 20/22). HYDRO used Tackle. Pidgey is around 50% HP. Selecting FIGHT -> TACKLE again.
[Turn 57] Pidgey HP is in the red. HYDRO used Tackle again.
[Turn 58] HYDRO's Tackle missed on turn 57. Pidgey used Gust (HYDRO HP: 16/22). Selecting FIGHT -> TACKLE again to finish it.
[Turn 58-59] Defeated Lv 2 Pidgey. HYDRO gained 15 EXP. Current HP is 16/22. Resuming journey north.

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

<hr>