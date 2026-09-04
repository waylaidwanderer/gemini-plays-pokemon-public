<h1><code>Main</code></h1>

# Pokémon Blue - Journey Log

## Status
- Badges: 0 / 8
- Active Team: Squirtle (SHELDON) Lv 6
- Money: ¥175
- Pokédex: 1 Caught / 2 Seen (Bulbasaur seen)

## Milestones
- [x] Complete Intro & Name Character/Rival (Player: BLUE, Rival: RED) [Turn 14]
- [x] Withdraw starting Potion from bedroom PC [Turn 18]
- [x] Receive Starter Pokémon from Professor Oak (Squirtle) [Turn 40]
- [x] Defeat Rival RED in Oak's Lab [Turn 58]
- [x] Reach Viridian City via Route 1 [Turn 132]
- [x] Visit Viridian City Poké Mart [Turn 169]
- [ ] Deliver parcel to Prof. Oak in Pallet Town [Started Turn 171]

<hr>

<h1><code>Inventory</code></h1>

# Inventory Log

## Items
- POTION x2 (x1 from bedroom PC on Turn 18, x1 from Route 1 Mart clerk sample on Turn 76)

## Key Items
- OAK'S PARCEL (received from Viridian City Poké Mart clerk on Turn 171)
## Money
- ¥175 (won from Rival RED in Oak's Lab on Turn 58)

## Party Pokémon
- SQUIRTLE (Nickname: SHELDON) [Lv 6, Water]
  - HP: 21 / 21
  - Stats: Attack 12, Defense 14, Speed 12, Special 12
  - Moves: Tackle (PP 35/35), Tail Whip (PP 30/30)

<hr>

<h1><code>Locations/Kanto_Route1</code></h1>

# Route 1 Geography & Mechanics

## Map Structure
- Connects Pallet Town (south, y=35) to Viridian City (north, y=0).
- Southbound Fast-Return Ledges (one-way South):
  - Row 5: Ledge on west segment (x=11..13), verified jump from (11, 4) to (11, 6). Open corridor on east (x=14..17).
  - Row 19: Ledge split into two segments: west (x=4..8) and east (x=10..17), separated by an open gap at (9, 19). Jumps into row 20.
  - Row 23: Ledge spanning x=16 to 17. Jumps into row 24.
  - Row 27: Ledge spanning x=12 to 17. Jumps into row 28 tall grass.
- Fixed Obstacles:
  - Vertical fence at x=3 (runs vertically).
  - Vertical fence at x=18 (runs vertically).
  - Tree hedge at row 23 (x=4 to 11).
- Open Pathways:
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