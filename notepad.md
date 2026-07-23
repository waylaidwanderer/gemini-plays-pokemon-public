<h1><code>Main</code></h1>

# Pokémon Blue - Crystal Palette Swap Mod Playthrough

## Current Location
- Pallet Town (Tall Grass Entrance, Route 1 Event Triggered)

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
- **Map ID:** 1
- **PC Location:** (0, 1) - Keyboard is at (0, 1), Monitor at (0, 0).
  - Standing at (0, 2) facing Up or (1, 1) facing Left lets you access it.
  - Contains **1x Potion** (Withdrawn).
- **Staircase (to 1F):** (7, 1)
  - **Mechanic / Collision:** Walking Up from (7, 2) to (7, 1) is blocked. To warp downstairs, you must enter from the Left: (6, 1) -> (7, 1).

## Player's House - Living Room (1F)
- **Map ID:** 2
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
- **Map ID:** 3
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

## Daisy's House (Blue's House)
- **Map ID:** 1 (standard/implied but layout is verified inside)
- **Daisy's House Door (Pallet Town):** (13, 5). Exiting Daisy's house spawns the player at (13, 6) facing Down.
- **Inside Daisy's House Layout:**
  - **Daisy:** Sits at (2, 3) behind a table.
  - **Table with Book/Map:** Located at (3, 3).
  - **Player standing position to talk to Daisy:** Standing at (2, 4) facing Up.
  - **Exit Warp/Door Mats:** (2, 7) and (3, 7). Walking Down from (2, 7) or (3, 7) warps you back to Pallet Town.

<hr>

<h1><code>Locations/ViridianCity</code></h1>

# Viridian City - Locations & Landmarks

## Overworld (Map ID: 3? Or check standard ID)
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

<hr>