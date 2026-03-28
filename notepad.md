<h1><code>Main</code></h1>

Team:
- Squirtle (HYDRO)
- Pidgey (AERO)
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
[Turn 107] Interacting with Nurse Joy to heal HYDRO. Selecting 'HEAL' from the prompt.
[Turn 260] Initiated dialogue with Nurse Joy to document the exact text and button sequence required for a reliable healing macro.
- Healing Sequence Step 1: Stand at (3,3) facing Up. Press A.
- Text: "Welcome to our POKéMON CENTER!"
- Healing Sequence Step 2: Text "We heal your POKéMON back to perfect health!" appears alongside a HEAL/CANCEL prompt. Cursor defaults to HEAL. Press A to select HEAL.
- Healing Sequence Step 3: Text "OK. We'll need your POKéMON." followed by a healing jingle.
- Healing Sequence Step 4: Text "Thank you! Your POKéMON are fighting fit!"
- Healing Sequence Step 5: Text "We hope to see you again!" Interaction ends.
[Turn 273] Turned on PC at (13,4) facing Up. Menu options:
- SOMEONE'S PC
- ASH's PC
- PROF. OAK's PC
- LOG OFF

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

Current Task: Catching a Rattata on Route 2.

<hr>

<h1><code>Locations/Route_2</code></h1>

Route 2 Layout:
- South exit to Viridian City: (8, 72) connects to Viridian City at (18, 0).
- Sign at (9, 73).
- Ledge at Y=61. Gap is at X=7.
- Dense Bushes block movement East from the grass. The bushes start at X=5 (Y=54, Y=55), and X=6 to X=12 at Y=56.
- Tall grass is found at X=4 (extending North from Y=57) and X=5 (Y=56 to Y=57).
- Item Ball spotted at (13, 54). Currently inaccessible from the main (West) path due to a wall of Dense Bushes.
- Small building/structure at (5, 65). Best path South is via X=8.

<hr>

<h1><code>Scratchpad/Route2_Exploration</code></h1>

[Turn 217] Re-entered Route 2 at (8, 71). Heading North to find tall grass for catching new team members. Avoid Y=72, as it triggers the warp back to Viridian.

<hr>

<h1><code>Scratchpad/Route2_Encounters</code></h1>

[Turns 282-294] Pacing in Route 2 tall grass (X=4) to find a Rattata. No encounters yet.
[Turn 295] Encountered a wild Rattata on Route 2!
- [Turn 296] The wild Rattata is Lv 2. Attempting to catch it by throwing a Poké Ball at full HP to test the catch rate on Lv 2s.
- [Turn 298] First Poké Ball failed to catch the full HP Lv 2 Rattata. It broke free. This confirms that even at Level 2, full HP catches are not guaranteed. Throwing a second Poké Ball.
- [Turn 303] Second Poké Ball failed to catch the full HP Lv 2 Rattata. It broke free again. I will try switching to my Lv 3 Pidgey (AERO) to safely weaken it with Gust.
- [Turn 304] Opening the PKMN menu to switch to AERO.
- [Turn 305] Switching out HYDRO for AERO to weaken the Rattata safely.
- [Turn 306] AERO is out. Waiting for the Rattata's attack text to finish so I can select Gust.
- [Turn 307] Selecting FIGHT -> GUST with AERO to weaken the Lv 2 Rattata.
- [Turn 308] Gust dealt ~40% damage to the Lv 2 Rattata. Rattata used Tail Whip. Using Gust again to safely lower its HP further.
- [Turn 309] Second Gust brought the Lv 2 Rattata down to the red HP zone. Opening the ITEM menu to throw a Poké Ball.
- [Turn 310] Threw a third Poké Ball at the weakened (red HP) Lv 2 Rattata.
- [Turn 311] Catch successful! The weakened Lv 2 Rattata (red HP) was caught on the first ball thrown at that HP range. This confirms weakening is highly effective/necessary even at the lowest levels.

<hr>