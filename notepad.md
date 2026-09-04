<h1><code>Main</code></h1>

# Pokémon Blue - Journey Log

## Status
- Badges: 0 / 8
- Active Team: Squirtle (SHELDON) Lv 7
- Money: ¥175
- Pokédex: 1 Caught / 2 Seen (Bulbasaur seen)

## Milestones
- [x] Complete Intro & Name Character/Rival (Player: BLUE, Rival: RED) [Turn 14]
- [x] Withdraw starting Potion from bedroom PC [Turn 18]
- [x] Receive Starter Pokémon from Professor Oak (Squirtle) [Turn 40]
- [x] Defeat Rival RED in Oak's Lab [Turn 58]
- [x] Reach Viridian City via Route 1 [Turn 132]
- [x] Visit Viridian City Poké Mart [Turn 169]
- [x] Deliver parcel to Prof. Oak in Pallet Town [Turn 211]
- [x] Obtain Pokédex from Prof. Oak [Turn 214]
- [x] Obtain Town Map from Daisy in Pallet Town [Turn 225]
- [ ] Return to Viridian City & purchase Poké Balls

<hr>

<h1><code>Inventory</code></h1>

# Inventory Log

## Items
- POTION x2 (x1 from bedroom PC on Turn 18, x1 from Route 1 Mart clerk sample on Turn 76)

## Key Items
- POKéDEX (received from Prof. Oak on Turn 214)
- TOWN MAP (received from Daisy on Turn 225)
(Note: OAK'S PARCEL delivered to Prof. Oak on Turn 211)
## Money
- ¥175 (won from Rival RED in Oak's Lab on Turn 58)

## Party Pokémon
- SQUIRTLE (Nickname: SHELDON) [Lv 7, Water]
  - HP: 11 / 23
  - Stats: Attack 13, Defense 15, Speed 13, Special 13
  - Moves: Tackle (PP 30/35), Tail Whip (PP 30/30)

<hr>

<h1><code>Locations/Kanto_Route1</code></h1>

# Route 1 Geography & Mechanics

## Map Structure
- Connects Pallet Town (south, y=35) to Viridian City (north, y=0).
- Southbound Fast-Return Ledges (one-way South):
  - Row 5: Ledge on west segment (x=11..13), verified jump from (11, 4) to (11, 6). Open corridor on east (x=14..17).
  - Row 13: Ledge at x=8..9, tree hedge at x=10..13. Northbound passage is through the tall grass patch at x=14..17 (rows 12..15), where the Mart clerk wanders.
  - Row 19: Ledge split into two segments: west (x=4..8) and east (x=10..17), separated by an open gap at (9, 19). Jumps into row 20.
  - Row 23: Ledge spanning x=16 to 17. Jumps into row 24.
  - Row 27: Ledge spanning x=10 to 17. Jumps into row 28. Signpost at (9, 27). Open gap at x=6..8.
- Fixed Obstacles:
  - Vertical fence at x=3 (runs vertically).
  - Vertical fence at x=18 (runs vertically).
  - Tree hedge at row 23 (x=4 to 11).
- Open Pathways:
  - Rows 6..9: Tall grass patch spanning x=10..17 across route. Northbound path through corridor at x=14..17 crosses rows 9..6.
  - Row 26: Safe east-west path corridor (verified clear from x=12 to 17).
  - Western strip (x=0..2): Walled off by fence (x=3, y=16..27) and trees (x=3, y=28..30); inaccessible from main route.
- Open Gaps:
  - Row 19: Open path gap at (9, 19) through the row 19 ledge.
  - Row 27: Open path gap at (8, 27) next to signpost at (9, 27).

<hr>

<h1><code>Mechanics/Combat</code></h1>

# Combat Mechanics & Observations

## Active Pokémon: SQUIRTLE (SHELDON)
- Type: Water | Level: 6
- Moves:
  - Tackle: Normal physical attack (35 max PP). Deals ~4-5 damage to neutral Lv 5 targets.
  - Tail Whip: Lowers target Defense by 1 stage (30 max PP).

## Strategy
- Route 1: Defeat wild Pidgey/Rattata with Tackle for EXP toward Lv 8 (Bubble).
- Conserve Potions unless HP <= 5.
## Verified Encounter Observations (Turns 124-128)
- Enemy: Wild Rattata (Lv 3) on Route 1.
- Player: Squirtle (SHELDON) Lv 6 (Attack 12, Defense 14).
- Tackle Damage: Dealt ~6-7 HP (~50-55% of Rattata max HP); KO in 2 hits.
- Enemy Attack: Rattata Tackle Critical Hit dealt 3 damage to Sheldon (HP 21 -> 18).
- Enemy Status: Rattata used Tail Whip, reducing Sheldon Defense by 1 stage.
- Experience: Awarded 24 EXP upon defeat.

## Verified Encounter Observations (Turns 186-190)
- Enemy: Wild Pidgey (Lv 3) on Route 1.
- Player: Squirtle (SHELDON) Lv 6 -> grew to Lv 7!
- Tackle Damage: Critical Hit dealt ~50% damage on hit 1; regular Tackle dealt ~45% on hit 2 (KO in 2 hits).
- Enemy Attack: Pidgey Gust dealt 3 damage to Sheldon (HP 18 -> 15).
- Experience: Awarded 23 EXP upon defeat, triggering Level 7!
- Stat Growth at Lv 7: Attack 12->13, Defense 14->15, Speed 12->13, Special 12->13.

## Verified Encounter Observations (Turns 196-200)
- Enemy: Wild Pidgey (Lv 3) on Route 1.
- Player: Squirtle (SHELDON) Lv 7 (Attack 13, Defense 15, Speed 13, Special 13).
- Tackle Damage: Dealt ~55% on hit 1; regular Tackle dealt ~45% on hit 2 (KO in 2 hits).
- Enemy Attack: Pidgey Gust Critical Hit dealt 3 damage, regular Gust dealt 3 damage (HP 17 -> 11).
- Experience: Awarded 23 EXP upon defeat.

<hr>

<h1><code>Locations/Kanto_ViridianCity</code></h1>

# Viridian City Points of Interest & Geography

## Connections
- South: Route 1 entrance at (21, 36).

## Geography & Layout
- Main Southern Entrance: Street at columns 20-21 leads north from Route 1 to row 30 cross street.
- Southern Cross Street: Row 30 runs east-west from column 4 to column 35, south of the pond and row 27 ledge.
- Row 27 Ledge Observations:
  - Water pond occupies rows 26-27 between columns 9 and 13.
  - Open ledge gap discovered at (19, 27) allowing northward passage to row 26.
  - Collisions confirmed at (5, 27), (17, 27), and (20, 27).

## Key Buildings
- Pokémon Center: Located at (22..25, 24..25) with entrance door at (23, 25) and sign at (24, 25).
- Poké Mart: Located at (28..31, 18..19) with entrance door at (29, 19) and "MART" sign at (30, 19).

<hr>