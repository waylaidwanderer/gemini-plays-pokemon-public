<h1><code>Main</code></h1>

# Pokémon Blue - Journey Log

## Status
- Badges: 0 / 8
- Active Team: Squirtle (SHELDON) Lv 7
- Money: ¥125
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
- [x] Return to Viridian City, heal team & purchase Poké Ball [Turn 284]
- [ ] Traverse Route 2 & Viridian Forest to Pewter City

<hr>

<h1><code>Inventory</code></h1>

# Inventory Log

## Items
- POTION x1
- POKé BALL x1

## Key Items
- POKéDEX (received from Prof. Oak on Turn 214)
- TOWN MAP (received from Daisy on Turn 225)

## Money
- ¥125

## Party Pokémon
- SQUIRTLE (Nickname: SHELDON) [Lv 7, Water]
  - HP: 23 / 23
  - Stats: Attack 13, Defense 15, Speed 13, Special 13
  - Moves: Tackle (PP 35/35), Tail Whip (PP 30/30)

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
  - Row 4: Safe east-west open path corridor connecting x=10..17 north of row 5 ledge.
  - Rows 6..9: Tall grass patch spanning x=10..17 across route. Northbound path through corridor at x=14..17 crosses rows 9..6.
  - Row 26: Safe east-west path corridor (verified clear from x=12 to 17).
  - Western strip (x=0..2): Walled off by fence (x=3, y=16..27) and trees (x=3, y=28..30); inaccessible from main route.
- Northern Exit to Viridian City:
  - Row 1: Wall structure blocks columns 12..18.
  - Columns 10..11: Open 2-tile road corridor leading directly north into Viridian City.

<hr>

<h1><code>Mechanics/Combat</code></h1>

# Combat Mechanics & Observations

## Battle Engine & Turn Priority
- Move Order: Determined strictly by Speed stat. Sheldon (Lv 7, Speed 13) consistently outspeeds Route 1 wild Pokémon (Lv 2-4 Rattata/Pidgey).
- Item Priority: Bag item usage (e.g. Potion) executes at turn start before Pokémon moves.

## Strategy
- Route 1: Defeat wild Pidgey/Rattata with Tackle for EXP toward Lv 8 (Bubble).
- Conserve Potions unless HP <= 5.
## Stat Modifiers & Stage Divisors
- Tail Whip: Decreases target Defense by 1 stage per use (-1 stage = 2/3 Defense, -2 stages = 1/2 Defense).
  - Verified: Lv 4 Rattata Tackle dealt 6 damage to Sheldon at -2 Defense vs ~3-4 damage at neutral Defense.

## Damage Ranges (Squirtle Tackle)
- Against Lv 3-4 Route 1 wild targets (neutral): Tackle deals ~6-7 HP per hit (~35-50% max HP), yielding consistent 2-to-3-hit KOs.
- Critical Hits: Double effective level in damage calculation, dealing ~50% bonus damage.

## Verified Encounter Observations (Turns 196-200)
- Enemy: Wild Pidgey (Lv 3) on Route 1.
- Player: Squirtle (SHELDON) Lv 7 (Attack 13, Defense 15, Speed 13, Special 13).
- Tackle Damage: Dealt ~55% on hit 1; regular Tackle dealt ~45% on hit 2 (KO in 2 hits).
- Enemy Attack: Pidgey Gust Critical Hit dealt 3 damage, regular Gust dealt 3 damage (HP 17 -> 11).
- Experience: Awarded 23 EXP upon defeat.

## Verified Encounter Observations (Turns 248-253)
- Enemy: Wild Rattata (Lv 4) on Route 1.
- Player: Squirtle (SHELDON) Lv 7 (Attack 13, Defense 15 -> dropped to stage -2 via Tail Whip).
- Battle Flow:
  - Turn 249: Sheldon Tackle dealt ~40% HP; Rattata used Tail Whip (-1 Def).
  - Turn 250: Sheldon Tackle dealt ~35% HP; Rattata used Tail Whip (-2 Def).
  - Turn 251: Sheldon Tackle dealt ~20% HP (Rattata survived with ~1-2 HP); Rattata Tackle dealt 6 damage to -2 Def Sheldon (HP 11 -> 5).
  - Turn 252: Sheldon Tackle KO'd Rattata!

## Experience & Growth Mechanics
- Wild Rattata Lv 3: 24 EXP | Lv 4: 32 EXP
- Wild Pidgey Lv 3: 23 EXP
- Growth Curve: Medium-Slow (Lv 7 at 318 EXP, Lv 8 at 482 EXP).
- Movepool: Squirtle learns Bubble at Lv 8 (fills empty slot 3).

<hr>

<h1><code>Locations/Kanto_ViridianCity</code></h1>

# Viridian City Points of Interest & Geography

## Connections
- South: Route 1 entrance at (21, 36).
- North: Route 2 entrance at (18..19, 0).

## Geography & Layout
- Main Thoroughfare: Columns 20-21 form the primary north-south street connecting Route 1 (south) to Route 2 (north).
- Southern Cross Street: Row 30 runs east-west from column 4 to column 35, south of the pond and row 27 ledge.
- Row 27 Ledge: Pond occupies rows 26-27 (columns 9-13); passable gap at (19, 27) leads to row 26.
- Mid-City Street (Row 16): Striped road running east-west south of the house at (21..23, 14..15), connecting column 25 to the main avenue at columns 20-21. Row 13 fence blocks northward travel across columns 20-30.
- Row 13 Passage: Fence spans columns 20..30 (east) and column 16 (west); columns 17..19 form an open 3-tile north-south corridor connecting row 16 to row 12.

## Key Buildings
- Pokémon Center: Located at (22..25, 24..25) with entrance door at (23, 25) and sign at (24, 25).
- Poké Mart: Located at (28..31, 18..19) with entrance door at (29, 19) and "MART" sign at (30, 19).
  - Verified Stock & Prices (Turn 277):
    - POKé BALL: ¥200
    - ANTIDOTE: ¥100
    - PARLYZ HEAL: ¥200
    - BURN HEAL: ¥250
  - Verified Resale Values (Turn 280):
    - POTION: ¥150

<hr>

<h1><code>Locations/Kanto_Route2</code></h1>

# Route 2 Geography & Points of Interest

## Connections
- South: Viridian City northern gate at (8, 72). Player enters at (8, 71).
- North: Viridian Forest southern gatehouse.

## Layout & Features
- Southern Entrance: Columns 8-9 form the main open road heading north from y=71.
- Boundaries: Fences on west (column 6), dense trees on east (columns 10..13).
- Row 67: Paved striped road at columns 8-9; flower patch to the west (columns 4..7).
- Rows 64..65: Paved cross street connects west to column 4; signpost located at (5, 65).
- Row 61 Ledge & Northbound Ramp: South-facing ledge spans across columns 2..6 and 8..11. Tile (7, 61) is a verified passable tan ramp/gap providing direct northward passage from row 62 to the open highway at row 60+.
- Rows 58..59: Wide paved highway spanning columns 4..9 heading north toward Viridian Forest.

<hr>