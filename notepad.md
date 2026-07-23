<h1><code>Main</code></h1>

# Pokémon Blue - Crystal Palette Swap Mod Playthrough

## Current Location
- Route 1

## Verified Map Coordinates & Layouts
- Detailed coordinate files are organized in the `Locations/` directory.
- Refer to `Locations/PalletTown_And_Route1` for Pallet Town and Route 1 layouts.
- Refer to `Locations/ViridianCity` for Viridian City layouts.

## Rules & Learnings
- **mgba.get_coordinates() Warning:** Returns `{'x': 0, 'y': 0}` in some emulator/harness states. Do NOT trust it for spatial tracking in scripts. Use the injected `GameStateInformation` coordinate report in the system prompt instead.
- **Map Transition Verification:** Always verify map transitions visually (checking surrounding objects/NPCs) and by watching for the `SYSTEM NOTE: Map Transition Detected` injection, rather than assuming a movement was successful.

<hr>

<h1><code>Locations/PalletTown_And_Route1</code></h1>

# Pallet Town & Route 1 - Map Coordinates & Layouts

## Player's House - Bedroom (2F)
- **PC Location:** (0, 1) - Keyboard is at (0, 1), Monitor at (0, 0).
  - Standing at (0, 2) facing Up or (1, 1) facing Left lets you access it.
  - Contains **1x Potion** (Withdrawn).
- **Staircase (to 1F):** (7, 1)
  - **Mechanic / Collision:** Walking Up from (7, 2) to (7, 1) is blocked. To warp downstairs, you must enter from the Left: (6, 1) -> (7, 1).

## Player's House - Living Room (1F)
- **Staircase (to 2F):** (7, 1)
- **Front Door Exit:** (2, 7) (door mat).
  - Walking Down from (2, 7) exits to Pallet Town.
  - (3, 7) is a wall/blocked at the bottom (y=8 is wall).
- **Table / Chairs:** In the middle-right area.
- **Mom:** Sitting at the table.

## Pallet Town (Overworld)
- **Red's House Door:** (5, 5). Exiting Red's house spawns the player at (5, 6) facing Down.
- **Oak's Lab Door:** (12, 11). Exiting Oak's Lab spawns the player at (12, 12) facing Down.
- **Route 1 Entrance:** Tall Grass starts at (10, 1) and (11, 1).
  - Attempting to step onto (10, 1) or (11, 1) triggers Professor Oak's event.
  - Fences line the north boundary from x=4 to x=9 at y=1, blocking direct passage north except through the tall grass gap at x=10-11.

## Route 1
- **Bottom Entrance (from Pallet Town):** (10, 35) and (11, 35).
- **Northern Entrance (from Viridian City):** (10, 0) and (11, 0).
- **Tree Line at y=13:** Blocks x=10-13.
  - *Bypass/Gap:* Walk through x=8 (left corridor, clear ground) or x=14 (right corridor).
- **Ledge at y=19:** One-way ledge (jumpable going south).
- **Tree Line at y=23:** Blocks x=5-11.
  - *Bypass/Gap:* Walk through tall grass corridor at x=12 and x=13.
- **Ledge at y=27:** One-way ledge (jumpable going south).
- **Grey Fence Stones at y=32:** Blocks x=5-9 and x=12-17.
  - *Bypass/Gap:* Walk through tall grass corridor at x=10 and x=11 (this is the only entrance/exit to/from Pallet Town).
- **Northern Segment Layout (near Viridian City exit):**
  - **Fences:** Row 1 has solid gray fence stones from x=3 to x=9, and x=12 to x=18 (blocking direct passage north except through the gap).
  - **Clear Path:** Columns 10 and 11 are clear ground (gray with vertical dots) from row 0 to row 4, forming the main north-south road to/from Viridian City.
  - **Decorative Lawn:** Columns 5 to 9 and 12 to 15 on rows 2 and 3 contain checkered green decorative lawn, which has a 0% encounter rate. The actual tall grass (leafy texture) only starts at row 6.

## Daisy's House (Blue's House)
- **Daisy's House Door (Pallet Town):** (13, 5). Exiting Daisy's house spawns the player at (13, 6) facing Down.
- **Inside Daisy's House Layout:**
  - **Daisy:** Sits at (2, 3) behind a table.
  - **Table with Book/Map:** Located at (3, 3).
  - **Player standing position to talk to Daisy:** Standing at (2, 4) facing Up.
  - **Exit Warp/Door Mats:** (2, 7) and (3, 7). Walking Down from (2, 7) or (3, 7) warps you back to Pallet Town.

<hr>

<h1><code>Locations/ViridianCity</code></h1>

# Viridian City - Locations & Landmarks

## Overworld
- **Southern Entrance (from Route 1):** (20, 35) and (21, 35).
- **Ledge at y=27:** Blocks upward passage across the main entrance road.
  - **Walkable Gap:** (19, 27) is a grassy/dirt opening. Walking through (19, 28) -> (19, 27) -> (19, 26) lets the player bypass the ledge and head north.
- **Pokémon Center Entrance:** (23, 25).
  - Exiting spawns the player at (23, 26) facing Down.
- **Poké Mart Entrance:** (29, 19).
  - Exiting spawns the player at (29, 20) facing Down.
  - Triggers OAK's PARCEL quest upon entry.

## Pokémon Center (Inside)
- **Nurse Joy:** Behind the counter at (3, 2).
  - Counter is at (3, 3).
  - Talking to her from (3, 4) facing Up heals the party to full health.
- **NPC Girl:** Sits on the left side of the room.
  - Sits at (0, 4) behind a desk.
  - Standing at (1, 4) facing Left and talking to her gives dialogue about Pokémon Centers.
- **Exit Door:** at (3, 7) and (4, 7). Walking Down from (3, 7) exits back to Viridian City at (23, 26).

## Poké Mart (Inside)
- **Clerk:** Sits at (0, 5) behind the counter.
- **Counter:** Located at (1, 5).
- **Player standing position to buy/sell:** Standing at (2, 5) facing Left.
- **Exit Door:** at (3, 7) and (4, 7). Walking Down from (3, 7) exits back to Viridian City at (29, 20).

## Western Boundary & Cliff Barrier
- **Cliff Barrier:** A solid, vertical checkered brown cliff barrier runs at column 3, blocking access to the west (columns 0, 1, 2) from the main city.
  - **Checkered Cliff Tiles (Blocked):** (3, 19), (3, 20), (3, 21), (3, 22), (3, 23), (3, 24).
  - **Diagonal Cliff Transition (Blocked):** (3, 18).
- **Walkable Gap / Route 22 Path:**
  - **Clear Ground Opening:** (3, 16) and (3, 17) are clear ground (unblocked), allowing the player to walk Left from column 4 to columns 0, 1, 2 (the path to Route 22).
  - **Coordinates:** Walking Left through (4, 16) -> (3, 16) -> (2, 16) -> (1, 16) -> (0, 16) leads directly to Route 22.

<hr>

<h1><code>Progression_And_Party_Stats</code></h1>

# Progression & Party Stats

## Key Progression Milestones
- **Pokédex:** Obtained from Professor Oak in Oak's Pokémon Lab on Turn 128.
- **Town Map:** Obtained from Daisy in Daisy's House on Turn 137.
- **Caught First Companion:** Caught NIBBLES (Rattata, Level 3) on Route 1 on Turn 318.
- **Caught Second Companion:** Caught GUSTY (Pidgey, Level 3) on Route 1 on Turn 350.

## Party Statistics
- **SHELLBY (Squirtle):**
  - **Level:** 8
  - **Moveset:** Tackle, Tail Whip, Bubble
  - **HP:** 8 / 25
  - **Status:** Healthy
- **NIBBLES (Rattata):**
  - **Level:** 3
  - **Moveset:** Tackle, Tail Whip
  - **Status:** Healthy
- **GUSTY (Pidgey):**
  - **Level:** 3
  - **Moveset:** Tackle, Sand-Attack
  - **Status:** Healthy

## Inventory
- **Poké Balls:** 2 (3 used to catch NIBBLES, 5 used to catch GUSTY)
- **Potion:** 0 (1 used during the battle with NIBBLES)

<hr>

<h1><code>Mechanics/Search_Scripting_Pitfalls</code></h1>

# Search Scripting Pitfalls

## Turn 79 Baseline Drift Pitfall
- **Description:** When running navigation scripts, if you execute a sequence of movements and then a reset sequence without first verifying that the initial movements were successful (e.g. they weren't blocked by a wall, NPC, or wild battle), the actual position of the player will drift from the expected position.
- **Prevention:** Always verify that each step or sequence of steps succeeded (checking GameState coordinates and screen visual) before continuing or executing corrective/reset steps.

<hr>

<h1><code>Locations/Route22</code></h1>

# Route 22 - Locations & Landmarks

## Layout & Landmarks
- **Eastern Entrance (from Viridian City):** (39, 8) (warp/transition spawn point).
- **Tall Grass Area:** Row 6 and Row 7 have tall grass starting from x=36 to x=44 (and possibly more).

## Wild Encounter Investigations (Turn 303)
- **Empirical Test:** Paced for 68 steps inside Route 22's tall grass (x=36 to 44, y=6 to 7) on Turn 221-230.
- **Result:** 0 wild encounters triggered.
- **Conclusion/Hypothesis:** Wild encounters on Route 22 appear to be disabled or extremely rare at this stage of the game (before delivering Oak's Parcel / getting Pokédex, or perhaps until we defeat Brock). To prevent repeating this exhausted path, we will avoid hunting for wild Pokémon on Route 22 until a later progression milestone is met.

<hr>