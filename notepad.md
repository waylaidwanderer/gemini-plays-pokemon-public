<h1><code>Main</code></h1>



<hr>

<h1><code>Locations/PalletTown_And_Route1</code></h1>



<hr>

<h1><code>Locations/ViridianCity</code></h1>



<hr>

<h1><code>Progression_And_Party_Stats</code></h1>

# Progression and Party Stats

## Gym Badge Milestones
- **Boulder Badge:** Earned by defeating Gym Leader Brock in Pewter City Gym on Turn 1025.
- **Cascade Badge:** Earned by defeating Gym Leader Misty in Cerulean City Gym on Turn 5262.
- **Thunder Badge:** Earned by defeating Gym Leader Lt. Surge in Vermilion City Gym on Turn 7025.

## Current Party Stats (as of Turn 11040)
1. **TESLA** (Pikachu)
   - Level: 18
   - HP: 10/44
   - Status: Healthy (Low HP)
2. **TRUFFLE** (Paras)
   - Level: 14
   - HP: 37/37
   - Status: Healthy
3. **GUSTY** (Pidgey)
   - Level: 5
   - HP: 19/19
   - Status: Healthy
4. **NIBBLES** (Rattata)
   - Level: 7
   - HP: 22/22
   - Status: Healthy
5. **SHELLBY** (Blastoise)
   - Level: 36
   - HP: 67/112 (Damaged by Selfdestruct on Turn 11032)
   - Status: Healthy

## Major Milestones and Items
- **Cut:** Taught to Pokémon on Turn 6787.
- **Bill's House:** Visited on Route 25 on Turn 4765. Restored Bill's human form.
- **Burgled House:** Explored in Cerulean City.
- **S.S. Anne:** Boarded and cleared, obtained Cut from the Captain.


<hr>

<h1><code>Mechanics/Search_Scripting_Pitfalls</code></h1>



<hr>

<h1><code>Locations/Route22</code></h1>



<hr>

<h1><code>Mechanics/Naming_Screen_Offset</code></h1>



<hr>

<h1><code>Locations/Route2</code></h1>



<hr>

<h1><code>Locations/ViridianForest</code></h1>



<hr>

<h1><code>Locations/PewterCity</code></h1>



<hr>

<h1><code>Locations/Route3</code></h1>



<hr>

<h1><code>Mechanics/UI_And_Border_Rendering</code></h1>



<hr>

<h1><code>Locations/Route4</code></h1>



<hr>

<h1><code>Locations/CeruleanCity</code></h1>



<hr>

<h1><code>Locations/Route24</code></h1>



<hr>

<h1><code>Locations/Route25</code></h1>



<hr>

<h1><code>Locations/Route5</code></h1>



<hr>

<h1><code>Locations/Route6</code></h1>



<hr>

<h1><code>Locations/VermilionCity</code></h1>



<hr>

<h1><code>Locations/SSAnne</code></h1>



<hr>

<h1><code>Locations/Route9</code></h1>



<hr>

<h1><code>Locations/Route10</code></h1>



<hr>

<h1><code>Locations/RockTunnel1F</code></h1>

# Rock Tunnel 1F - Overworld Mapping & Navigation

## Map Dimensions
- Dimensions: Width = 40, Height = 18.

## Mapped Coordinates & Layout
- **Entry Warp:** Route 10 East connects to Rock Tunnel 1F at (15, 3). Walking SOUTH from (15, 3) enters the main corridor.
- **Ladder to B1F (Top-Left Section):** Located at `(5, 3)`. Connects to Rock Tunnel B1F at `(27, 3)`.
- **Ladder to B1F (Top-Right Section):** Located at `(37, 3)`. Connects to Rock Tunnel B1F at `(33, 25)`.
- **Ladder to B1F (Central Section):** Located at `(17, 11)`. Connects to Rock Tunnel B1F at `(23, 11)`.

### Verified Walkable Coordinates:
- (15, 3)
- (15, 4), (15, 5), (15, 6)
- (5, 3)
- (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (5, 16), (5, 17), (5, 18)
- (7, 6)
- (7, 7), (7, 8), (7, 9)
- (8, 9), (9, 9), (10, 9), (11, 9)
- (11, 10), (11, 11), (11, 12), (11, 13)
- (11, 14), (11, 15)
- (12, 15), (13, 15), (14, 15)
- (14, 14), (14, 13), (14, 12), (14, 11)
- (15, 11), (16, 11), (17, 11)


### Defeated Trainers:
- **Hiker Dudley:** Engaged at (14, 15) on Turn 11009. Defeated on Turn 11037.
  - Roster: Geodude Lv 21, Graveler Lv 21.

## Verified Collisions

## Map Transitions
- **Unreachable Ladder to B1F (Hypothesis):** Located at `(37, 17)` on Rock Tunnel 1F. It is isolated by walls on Row 14-15 and Column 31, and is hypothesized to connect to B1F but has not been empirically verified in-game.


<hr>

<h1><code>Locations/RockTunnelB1F</code></h1>

# Rock Tunnel B1F - Overworld Mapping & Navigation

## Map Dimensions
- Dimensions: Width = 40, Height = 36.

## Mapped Coordinates & Layout
- **Ladder to 1F (Central Section):** Located at `(23, 11)`. Connects to Rock Tunnel 1F at `(17, 11)`.

### Verified Walkable Coordinates (Physically stepped on in this session):
- (23, 11), (22, 11), (21, 11), (20, 11), (19, 11), (18, 11)
- (17, 11), (17, 12), (17, 13), (17, 14), (17, 15), (17, 16), (17, 17), (17, 18), (17, 19)
- (16, 19), (15, 19), (14, 19)
- (14, 18), (14, 17), (13, 17), (12, 17), (11, 17), (10, 17)
- (10, 18), (10, 19), (10, 20), (10, 21), (10, 22), (10, 23), (10, 24)

## Verified Collisions
- (13, 19): Rock Wall (Turn 11056)


<hr>

<h1><code>Scratchpad/RockTunnel1F_Routing</code></h1>

# Rock Tunnel 1F - Routing Hypotheses & Unvisited Path Predictions

## Unverified Observations from (14, 15)
- All previously listed coordinates leading to the central ladder at (17, 11) have been physically verified on Turn 11046.


<hr>

<h1><code>Scratchpad/RockTunnelB1F_Routing</code></h1>

# Rock Tunnel B1F - Routing Hypotheses & Unverified Map Restorations

## Unverified Hypotheses & Landmarks (Need physical verification in this session):
- **Ladder to 1F (Top-Left Section):** Hypothesized at `(27, 3)` (connects to 1F at `(5, 3)`).
- **Ladder to 1F (Top-Right Section):** Hypothesized at `(33, 25)` (connects to 1F at `(37, 3)`).

### Hypothesized Walkable Coordinates (from restored memory):
- **Top-Left Path to Ladder (34, 5) -> (27, 3):**
  - (27, 3), (28, 3), (29, 3), (30, 3), (31, 3), (32, 3), (33, 3), (34, 3)
  - (34, 4), (34, 5)
- **Vertical Channel (Columns 33-34):**
  - Walkable coordinates on columns 33 and 34 going down to (33, 25).
- **Horizontal Corridor (Row 16):**
  - Walkable corridor on row 16 spanning from column 17 to column 34.
  - (17, 16), (18, 16), (19, 16), (20, 16), (21, 16), (22, 16), (23, 16), (24, 16), (25, 16), (26, 16), (27, 16), (28, 16), (29, 16), (30, 16), (31, 16), (32, 16), (33, 16), (34, 16)
- **Vertical Channel (Column 22):**
  - Walkable column 22 connecting down to other sections.
- **Key Trainer Locations (Hypothesized):**
  - (26, 31) (Pokémaniac)
  - (17, 28) (Jr. Trainer♀)
  - (21, 21) (Pokémaniac Winston)
  - (34, 5) (Hiker Erik)


<hr>