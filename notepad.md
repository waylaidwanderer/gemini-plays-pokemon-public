<h1><code>Main</code></h1>

# Pokémon Blue - Journey Log

## Status
- Badges: 2 / 8 (Boulderbadge, Cascadebadge)
- Active Team: Wartortle (SHELDON) Lv 28, Spearow (FALCO) Lv 5, Geodude (ROCKY) Lv 8, Paras Lv 10
- Money: ¥8960
- Pokédex: 4 Caught / 13 Seen

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
- [x] Traverse Route 2 & Viridian Forest to Northern Gatehouse [Turn 485]
- [x] Reach Pewter City [Turn 495]
- [x] Defeat Pewter Gym Leader Brock [Turn 594]
- [x] Traverse Route 3 and reach Mt. Moon [Turn 1017]
- [x] Catch wild Geodude in Mt. Moon [Turn 1197]
- [x] Explore Mt. Moon and retrieve Fossil (Helix Fossil) [Turn 1853]
- [x] Exit Mt. Moon to Route 4 [Turn 1865]
- [x] Traverse Route 4 and reach Cerulean City [Turn 1938]
- [x] Defeat Cerulean Gym Leader Misty & earn Cascadebadge [Turn 2077]
- [x] Defeat Rival RED at Route 24 entrance [Turn 2296]
- [x] Clear Nugget Bridge & defeat Team Rocket Recruiter [Turn 2367]

<hr>

<h1><code>Inventory</code></h1>

# Inventory Log

## Items
- TOWN MAP
- POKé BALL x11
- ESCAPE ROPE x1
- TM34 (BIDE) x1
- TM12 (WATER GUN) x1
- POTION x1
- ANTIDOTE x2
- RARE CANDY x1
- HELIX FOSSIL x1
- NUGGET x1

## Key Items
- POKéDEX

## Money
- ¥8960

## Party Pokémon
- WARTORTLE (Nickname: SHELDON) [Lv 28, Water]
  - Status: Healthy
  - HP: 46 / 76
  - Stats: Attack 50, Defense 61, Speed 50, Special 52
  - Moves: Bite (PP 4/25), Tail Whip (PP 30/30), Bubblebeam (PP 10/20), Water Gun (PP 13/25)
- SPEAROW (Nickname: FALCO) [Lv 5, Normal/Flying]
  - Status: Healthy
  - HP: 19 / 19
- GEODUDE (Nickname: ROCKY) [Lv 8, Rock/Ground]
  - Status: Healthy
  - HP: 26 / 26
  - Stats: Attack 19, Defense 22, Speed 9, Special 11
  - Moves: Tackle (PP 35/35)
  - EXP: 314 (105 to Lv 9)
- PARAS (Nickname: FUNGI) [Lv 10, Bug/Grass]
  - Status: Healthy
  - HP: 29 / 29
  - Stats: Attack 21, Defense 16, Speed 11, Special 18
  - Moves: Scratch (PP 35/35)
  - EXP: 1000 (331 to Lv 11)

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

# Combat Mechanics & Reference

## Move & Damage Mechanics
- Same Type Attack Bonus (STAB): 1.5x damage multiplier.
- Type Effectiveness:
  - Super Effective: 2.0x damage.
  - Not Very Effective: 0.5x damage.
  - Immune: 0.0x damage.
- Critical Hits:
  - Based on base Speed stat: (BaseSpeed / 2) / 256 for non-high-crit moves.
  - In Gen 1, critical hits ignore all stat modifications (positive and negative) of both the attacker and defender.
- Stat Stages:
  - Tail Whip / Screech: Lowers defender's Defense stat stages.
  - 1 stage drop = 2/3 (66.7%), 2 stage drop = 2/4 (50%).

## Party Member Reference: Sheldon (Wartortle)
- Starter Squirtle Lv 5 -> Wartortle Lv 16 at Mt. Moon.
- Level 22 Stats: Max HP 61, Attack 39, Defense 48, Speed 39, Special 41
- Level 23 Stats: Max HP 63, Attack 41, Defense 50, Speed 41, Special 42
- Level 24 Stats: Max HP 66, Attack 43, Defense 52, Speed 43, Special 44
- Level 25 Stats: Max HP 68, Attack 43, Defense 52, Speed 43, Special 44
- Level 26 Stats: Max HP 71, Attack 46, Defense 56, Speed 47, Special 48
- Level 27 Stats: Max HP 73, Attack 48, Defense 59, Speed 48, Special 50
- Moves:
  - Bite (Normal, Physical, Power 60, Accuracy 100%, 10% flinch, PP 25/25)
  - Tail Whip (Normal, Status, Lowers Defense 1 stage, Accuracy 100%, PP 30/30)
  - Bubblebeam (Water, Special, Power 65, STAB, 33% chance to lower Speed, Accuracy 100%, PP 20/20)
  - Water Gun (Water, Special, Power 40, STAB, Accuracy 100%, PP 25/25)

## Party Member Reference: Rocky (Geodude)
- Level 8 Caught Stats: Max HP 26, Attack 19, Defense 22, Speed 9, Special 11
- Moves: Tackle (PP 35/35)
- EXP: 314 total, 105 to Lv 9 (Medium Slow experience curve: 419 EXP at Lv 9)

## Party Member Reference: Falco (Spearow)
- Level 5 Caught Stats: Max HP 19, Attack 12, Defense 9, Speed 14, Special 9
- Moves: Peck, Growl

## Party Member Reference: Fungi (Paras)
- Level 10 Caught Stats: Max HP 29, Attack 21, Defense 16, Speed 11, Special 18
- Moves: Scratch

## Cerulean Gym Combat Bounds
- Leader Misty Staryu Lv 18: Tackle deals 4 HP damage to Sheldon (neutral Defense 50). Uses X DEFEND when HP is critical. Sheldon Lv 23 Tackle deals ~30-35% max HP damage (Critical hit deals ~55% max HP damage). Defeat yield: 408 EXP.
- Leader Misty Starmie Lv 21: Tackle deals 6 HP damage (critical hit 10 HP damage) to Sheldon (neutral Defense 50). Uses X DEFEND. Sheldon Tail Whip lowers Starmie Def 1 stage. Defeat yield: 931 EXP. Prize: ¥2079, CASCADEBADGE, TM11 (BUBBLEBEAM).
- Swimmer Horsea Lv 16 Bubble vs Sheldon (Water type, Special 41): 2 HP damage.
- Sheldon Lv 22 Critical Tackle vs Horsea Lv 16: ~40% max HP damage. Defeat yield: 283 EXP.
- Swimmer Shellder Lv 16: Tackle deals 4 HP damage (critical hit 6 HP). Defeat yield: 331 EXP. Prize: ¥80.
- Sheldon Lv 22 Water Gun vs Shellder Lv 16: ~40% max HP damage.
- Jr. Trainer (Female) Goldeen Lv 19: Peck deals 5 HP damage (7 HP at -1 Def). Tail Whip lowers Def 1 stage. Defeat yield: 451 EXP. Prize: ¥380.
- Sheldon Lv 22 Tackle vs Goldeen Lv 19: ~25% max HP damage (~12-14 HP), critical hit deals ~35-40% max HP (~18-20 HP).

## Rival RED Battle (Route 24 Entrance - Turns 2284-2296)
- Opponent Team: Pidgeotto Lv 18, Abra Lv 15, Rattata Lv 15, Bulbasaur Lv 17.
- Pidgeotto Lv 18: Gust deals 8 HP damage to Sheldon (Defense 52). Bubblebeam deals ~80% HP on hit 1; hit 2 defeats. Yield: 435 EXP.
- Abra Lv 15: Low physical Defense (~12). Sheldon Bite deals 49+ damage (OHKO). Yield: 234 EXP.
- Rattata Lv 15: Sheldon Bubblebeam deals 69 damage (OHKO). Yield: 183 EXP.
- Bulbasaur Lv 17: Used Growl (-1 Attack). Sheldon Bite deals ~23 damage on hit 1, ~17 damage at -1 Attack on hit 2 (2HKO). Yield: 232 EXP.
- Total EXP Yield: 1,084 EXP. Prize: ¥595.

## Route 24 Nugget Bridge - Bug Catcher Cale (Turn 2304-2310)
- Position: (11, 31) facing West.
- Caterpie Lv 14: Defeated in 1 hit by Bubblebeam (Critical Hit). Yield: 159 EXP.
- Weedle Lv 14: Defeated in 1 hit by Bubblebeam. Yield: 156 EXP.
- Sheldon grew to Level 25! Max HP increased to 68 (Current HP: 60 / 68).
- Total EXP: 315 EXP. Prize: ¥140.

## Route 24 Nugget Bridge - Lass (Turn 2314-2319)
- Position: (10, 28) facing South.
- Pidgey Lv 14: Defeated in 1 hit by Bite. Yield: 165 EXP.
- Nidoran♀ Lv 14: Defeated in 1 hit by Bubblebeam. Yield: 177 EXP.
- Total EXP: 342 EXP. Prize: ¥210.

## Route 24 Nugget Bridge - Youngster (Turn 2321-2327)
- Position: (11, 25) facing West.
- Rattata Lv 14: Defeated in 1 hit by Bite. Yield: 171 EXP.
- Ekans Lv 14: Defeated in 1 hit by Bite. Yield: 186 EXP.
- Zubat Lv 14: Defeated in 1 hit by Bite. Yield: 162 EXP.
- Total EXP: 519 EXP. Prize: ¥210.

## Route 24 Nugget Bridge - Lass (Turn 2333-2341)
- Position: (10, 22) facing North. Dialogue: "I'm No. 4! Getting tired?".
- Pidgey Lv 16: Defeated in 2 hits by Bite (used Sand-Attack, -1 Sheldon accuracy). Yield: 187 EXP.
- Nidoran♀ Lv 16: Defeated in 1 hit by Bubblebeam. Yield: 201 EXP.
- Total EXP: 388 EXP. Prize: ¥240.

## Route 24 Nugget Bridge - Jr. Trainer ♂ (Turn 2346-2353)
- Position: (11, 19) facing West. Dialogue: "OK! I'm No. 5! I'll stomp you!".
- Mankey Lv 18: Defeated in 1 hit by Bubblebeam. Yield: 285 EXP.
- Total EXP: 285 EXP. Prize: ¥360.
## Route 24 Nugget Bridge - Team Rocket Recruiter (Turn 2356-2367)
- Position: (11, 15) facing West.
- Received NUGGET before battle.
- Ekans Lv 15: Used Wrap (2 damage/turn). Defeated by Water Gun (x2, critical hit). Yield: 198 EXP.
- Sheldon grew to Level 26! Max HP increased to 71 (HP: 59 / 71).
- Zubat Lv 15: Defeated in 1 hit by Bite (Critical Hit). Yield: 172 EXP.
- Total EXP: 370 EXP. Prize: ¥450.
## Route 25 - Hiker Franklin (Turn 2378-2385)
- Position: (8, 4) facing South. Sight range: 1 tile (engaged at (8, 5)).
- Dialogue: "I just got down from MT. MOON, but I'm ready!"
- Defeat Quote: "You worked hard!"
- Team:
  - Machop Lv 15: Used Karate Chop (5 damage). Defeated by Sheldon Water Gun (x2). Yield: 282 EXP.
  - Geodude Lv 15: Defeated in 1 hit by Water Gun (Super Effective). Yield: 276 EXP.
- Total EXP: 558 EXP. Prize: ¥525.

## Route 25 - Youngster (Turn 2392-2408)
- Position: (14, 2) facing South. Sight range: 2 tiles (engaged at (14, 4)).
- Pre-battle Dialogue: "Local trainers come here to practice!"
- Defeat Quote: "YOUNGSTER: You're decent."
- Team:
  - Rattata Lv 15: Defeated in 1 hit by Sheldon Bite. Yield: 183 EXP.
  - Spearow Lv 15: Defeated in 1 hit by Sheldon Bite. Yield: 186 EXP.
- Total EXP Yield: 369 EXP. Prize: ¥225.
- Sheldon HP: 54 / 71. Bite PP: 13 / 25.

## Route 25 - Hiker (Turn 2409-2416)
- Position: (13, 7) facing East. Sight range: 2 tiles (engaged at (15, 7)).
- Pre-battle Dialogue: "You're going to see BILL? First, let's fight!"
- Defeat Quote: "HIKER: You're something."
- Team:
  - Onix Lv 17: Defeated in 1 hit by Sheldon Water Gun (Super Effective 4x). Yield: 393 EXP.
- Total EXP Yield: 393 EXP. Prize: ¥595.
- Sheldon HP: 54 / 71. Water Gun PP: 19 / 25.

## Discovered Gen 1 Combat Mechanics
- **Confusion & PP Deduction (Verified Turn 2434)**: In Gen 1, if a Pokémon is confused and hurts itself in confusion, the chosen move's PP is NOT deducted. Move PP is only decremented if the move is successfully executed. Empirically verified on Turn 2434 when Sheldon's move menu showed Bite at 11/25 despite two prior turns of confusion self-damage.

## Route 25 - Youngster (Turn 2418-2442)
- Position: (18, 5) (engaged via direct interaction from (17, 5)).
- Pre-battle Dialogue: "Dad took me to a great party on S.S.ANNE at VERMILION CITY!"
- Defeat Quote: "YOUNGSTER: I'm not mad!"
- Team:
  - Slowpoke Lv 17: Used Confusion (deals 5-10 damage, inflicts confusion). Defeated by Sheldon Bite (x3). Yield: 360 EXP.
- Total EXP Yield: 360 EXP. Prize: ¥255.
- Sheldon grew to Level 27! Max HP increased to 73 (HP: 25 / 73).
- Sheldon Bite PP: 10 / 25.

## Route 25 - Lass Haley (Turn 2448-2458)
- Position: (18, 8) (engaged via manual interaction from (18, 7)).
- Pre-battle Dialogue: "Hi! My boy friend is cool!"
- Defeat Quote: "LASS: I was in bad condition!"
- Team:
  - Nidoran♂ Lv 15: Used Poison Sting (deals 2 damage, inflicts poison). Defeated by Sheldon Water Gun (x2). Yield: 192 EXP.
  - Nidoran♀ Lv 15: Defeated in 1 hit by Sheldon Bubblebeam (Critical Hit). Yield: 189 EXP.
- Total EXP Yield: 381 EXP. Prize: ¥225.
- Sheldon HP: 23 / 73 (Poisoned). Bubblebeam PP: 11 / 20, Water Gun PP: 17 / 25.
## Route 25 - Hiker Nob (Turn 2468-2485)
- Position: (23, 9) facing North. Engaged when player stepped to (23, 8).
- Pre-battle Dialogue: "I'm off to see a POKéMON collector at the cape!"
- Defeat Quote: "HIKER: You got me."
- Team:
  - Geodude Lv 13: Defeated in 1 hit by Sheldon Water Gun (Super Effective 4x). Yield: 238 EXP.
  - Geodude Lv 13: Defeated in 1 hit by Sheldon Water Gun (Super Effective 4x). Yield: 238 EXP.
  - Machop Lv 13: Defeated in 1 hit by Sheldon Bubblebeam. Yield: 244 EXP.
  - Geodude Lv 13: Defeated in 1 hit by Sheldon Water Gun (Super Effective 4x). Yield: 238 EXP.
- Total EXP Yield: 958 EXP. Prize: ¥455.
- Sheldon HP: 23 / 73 (Healthy). Bubblebeam PP: 10 / 20, Water Gun PP: 14 / 25.

## Route 25 - Jr. Trainer ♂ (Turn 2488-2498)
- Position: (24, 4) facing South. Sight range: 3 tiles (engaged at (24, 7)).
- Pre-battle Dialogue: "I'm a cool guy. I've got a girl friend!"
- Defeat Quote: "JR.TRAINER♂: Aww, darn..."
- Team:
  - Rattata Lv 14: Defeated in 1 hit by Sheldon Bite. Yield: 171 EXP.
  - Ekans Lv 14: Defeated in 1 hit by Sheldon Bite. Yield: 186 EXP.
- Total EXP Yield: 357 EXP. Prize: ¥280.
- Sheldon HP: 23 / 73 (Healthy). Bite PP: 8 / 25, Bubblebeam PP: 10 / 20, Water Gun PP: 14 / 25.
## Route 25 - Youngster (Turn 2509-2516)
- Position: (32, 3) facing West. Sight range: 3 tiles (engaged at (29, 3)).
- Pre-battle Dialogue: "I knew I had to fight you!"
- Defeat Quote: "YOUNGSTER: I knew I'd lose too!"
- Team:
  - Ekans Lv 14: Defeated in 1 hit by Sheldon Bite. Yield: 186 EXP.
  - Sandshrew Lv 14: Defeated in 1 hit by Sheldon Water Gun (Super Effective). Yield: 279 EXP.
- Total EXP Yield: 465 EXP. Prize: ¥210.
- Sheldon HP: 46 / 76 (Healthy). Level: 28. Bite PP: 7 / 25, Water Gun PP: 13 / 25, Bubblebeam PP: 10 / 20.
## Route 25 - Lass (Turn 2522-2531)
- Position: (37, 4) facing South. Sight range: 1 tile (engaged at (37, 5)).
- Pre-battle Dialogue: "My friend has a cute POKéMON. I'm so jealous!"
- Defeat Quote: "LASS: I'm not so jealous!"
- Team Size: 3 Pokémon.
- Team:
  - Oddish Lv 13: Defeated in 1 hit by Sheldon Bite. Yield: 216 EXP.
  - Pidgey Lv 13: Defeated in 1 hit by Sheldon Bite. Yield: 153 EXP.
  - Oddish Lv 13: Defeated in 1 hit by Sheldon Bite. Yield: 216 EXP.
- Total EXP Yield: 585 EXP. Prize: ¥195.
- Sheldon HP: 46 / 76 (Healthy). Level: 28. Bite PP: 4 / 25, Water Gun PP: 13 / 25, Bubblebeam PP: 10 / 20.

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
  - Verified Stock & Prices:
    - POKé BALL: ¥200
    - ANTIDOTE: ¥100
    - PARLYZ HEAL: ¥200
    - BURN HEAL: ¥250
  - Verified Resale Values:
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
- Rows 54..56: Central tree grove at columns 6..12; bypassed via western corridor at columns 3..5.
- Rows 48..51: Tall grass patch spanning columns 4..9.
- Row 47 Ledge & Passage: South-facing ledge spans columns 0..7; open passage at columns 8..9 leads north to the row 46 paved road.
- Viridian Forest Gatehouse: Located at (3..5, 42..43) with entrance door at (3, 43). Row 46 paved road connects column 8 to the gatehouse courtyard at columns 3..9.
## Northern Section (North of Viridian Forest)
- Gatehouse Exit: Player emerges from the north gatehouse at (3, 11) facing north. Gatehouse door at (3, 15).
- Paved Street (Rows 8..9): Wide east-west paved avenue connecting directly into Pewter City.

<hr>

<h1><code>Locations/Kanto_ViridianForest</code></h1>

# Viridian Forest Geography & Navigation

## Connections
- South: Southern gatehouse from Route 2; player enters at (17, 47).

## Verified Geography & Landmarks
- Southern Entry Corridor (Rows 44..47): Open path across columns 15..18, bounded by stone posts at columns 14 and 19.
- Signpost (18, 45): Trainer Tips - "Weaken POKéMON before attempting capture! When healthy, they may escape!"
- Resident/NPC (16, 43): Youngster warns "I came here with some friends! They're out for POKéMON fights!"
- Main South-Central Avenue (Rows 36..40): 2-tile wide clear path along columns 16..17 flanked by tall grass (col 15 and 18) and stone posts (col 14 and 19). Completely avoids grass encounters.
- Signpost (16, 32): Trainer Tips - "For poison, use ANTIDOTE! Get it at POKéMON MARTs!"
- Western Maze Passage (Rows 32..33): Avenue terminates at row 31 tree wall; path branches west through tall grass opening at rows 32..33 into the western forest maze.
- Ground Item (12, 29): Visually confirmed item ball in an enclosed clearing north of row 30 trees. Traversal of northern corridors (columns 11-13, 16-18, 25-26) confirmed no northern breach into this clearing; it remains isolated from the main paths (likely requires Cut or alternative access).
- Western Path Junction (Row 33, Col 7): Open grass path at (7, 33) connects the row 32..33 grass field to western and southern corridors.
- West-Central Corridor (Rows 33..37, Cols 6..7): 2-tile wide clear path bypassing the central tree clump (cols 3..5, rows 33..36) to the east; turns west along row 37.
- Southwest Grass Pocket (Rows 40..43, Cols 1..5): Dead-end 5x4 tall grass clearing bounded by western stone posts (col 0) and tree walls to north (row 38) and south (row 44). Exit is east to column 6.
- Southern Return Corridor (Rows 42..43, Cols 7..15): Open clear grass path connecting the west-central corridor at (7, 42) directly to the southern entrance avenue at (15, 42..43), bypassing the central-south tree clump. Completely clear of tall grass.
- Western Grass Pocket (Rows 30..31, Cols 1..5): Confirmed dead end. Bounded by western boundary posts at (0, 30..31), solid tree wall to the north (Rows 27..29, Cols 0..7), and solid tree wall to the south (Rows 32..35, Cols 1..5). No passage north along the western boundary.
- Eastern Cross-Corridor (Rows 42..43, Cols 18..21+): Column 19 fence ends at row 39. Rows 42 and 43 form an open clear-ground path extending east past column 21 into the unexplored eastern half of Viridian Forest.
- Signpost (24, 40): Located in tall grass north of row 42 cross-corridor.
- NPC / Trainer (27, 40): Located in the eastern corridor south of row 39 trees, facing south.
- Eastern Avenue Corridor (Cols 26..27, Rows 34..43): Verified 2-tile wide clear-ground highway running continuously north along the eastern edge, completely bypassing all tall grass.
- Bug Catcher (30, 33): Trainer stationed at (30, 33) facing west, guarding row 33 passage across the eastern avenue.
- Eastern Perimeter Corridor (Cols 31..32, Rows 4..33): Continuous 2-tile wide clear-ground highway running north along the eastern boundary fence (Col 33) from row 33 all the way to row 4, completely free of tall grass.
- Bug Catcher (30, 19): Stationary trainer facing west across row 19. Column 31 provides a clear bypass behind his back.
- Eastern Clearing (Row 18, Cols 27..32): 6-tile wide open clear-ground clearing connecting the eastern perimeter to westward passages.
- Signpost (26, 17): Trainer Tips - "Contact PROF. OAK via PC to get your POKéDEX evaluated!"
- Northern Avenue (Cols 25..26, Rows 14..19): 2-tile wide clear-ground corridor running north between column 24 stone posts and row 14-17 trees.
- Northern Perimeter Cross-Corridor (Rows 1..2, Cols 27..32+): 2-tile wide clear-ground corridor running west along the northern stone boundary wall (Row 0), connecting the eastern perimeter to the northern gatehouse route.
- West-Central Corridor (Cols 11..13, Rows 12..19): Northbound corridor bounded by column 9-10 stone posts on the west and column 14-15 trees on the east, connected to the north-central avenue via row 16-17 clear grass.
- Northern Exit Gatehouse (Cols 1..3, Rows 0..2): Visually confirmed gatehouse building structure at the northwest corner of the map. Accessible via the column 2 avenue.
- West Divider Wall (Cols 3..5, Rows 0..11+): Stone posts (Col 3) and trees (Cols 4..5) separating the exit avenue (Col 2) from the west-central corridor (Cols 6..8).
- Bug Catcher (2, 18): Stationed at (2, 18) facing West across the column 1-2 corridor, guarding the approach to the northern exit gatehouse.

<hr>

<h1><code>Locations/Kanto_PewterCity</code></h1>

# Pewter City Geography & Points of Interest

## Connections
- South: Route 2 northern entrance corridor at (18..19, 35).
- East: Route 3 (leading to Mt. Moon).

## Layout & Thoroughfares
- Southern Entrance (Rows 32..35, Cols 18..19): 2-tile wide paved corridor flanked by dense tree hedges.
- Main Avenue (Cols 18..19, Rows 22..27): 2-tile wide clear north-south thoroughfare connecting southern entrance to row 22 cross-street.
- Row 22 Cross-Street: Paved avenue running east from column 19 to column 23+. Dead-ends at column 15 to the west.
- Central Fence: Vertical fence posts at column 18 (rows 18..21) separating west and east avenues.
- Northbound Corridor: Columns 18..19 form an open clear ground avenue running north from row 22 past row 14 toward the Museum.
- Northern Boulevard (Rows 12..13, Cols 11..19): Wide east-west thoroughfare running above the Gym roof, connecting east and west sides of northern Pewter City.
- Western Corridor (Cols 10..11, Rows 13..18): North-south path along the western edge leading into the Gym courtyard.
- Gym Courtyard (Rows 18..20, Cols 10..17): Open plaza area in front of the Gym, bounded by row 20 trees to the south and column 18 fence to the east.
- Fenced Flower Garden: Located at rows 23..26 (cols 22..28), with wooden fence along row 23 and flower patches.

## Key Buildings
- Pokémon Center: Located at (12..15, 23..25). Entrance door at (13, 25) with "POKé" sign at (14, 25).
- Poké Mart: Located at (22..25, 16..17) with entrance door at (23, 17) and "MART" sign at (24, 17). Paved plaza in front at rows 18..19.
  - Verified Pewter Poké Mart Stock:
    - POKé BALL: ¥200
    - POTION: ¥300
    - ESCAPE ROPE: ¥550
    - ANTIDOTE: ¥100
    - BURN HEAL: ¥250
    - AWAKENING: ¥200
    - PARLYZ HEAL: ¥200
- Pewter Gym: Located at (12..17, 14..17) with entrance door at (16, 17) and "GYM" sign at (14..15, 16).

## Signposts & Points of Interest
- City Entrance Signpost: Located at (19, 29). Reads: "PEWTER CITY - A Stone Gray City".
- Garden Signpost: Located at (25, 23) along the north fence of the garden. Reads: "PEWTER CITY - A Stone Gray City".
- Western Signpost: Located at (11, 17) outside the western entrance to the Gym courtyard.
- Eastern Notice Signpost: Located at (33, 19) at the eastern exit road to Route 3. Reads: "NOTICE! Thieves have been stealing POKéMON fossils at MT. MOON! Please call PEWTER POLICE with any info!".

## NPCs
- Center Exterior NPC: Stationed at (17, 25) outside the Pokémon Center.
- Garden Resident: Wandering inside the fenced flower garden (rows 24..26).
- Mart Exterior Youngster: Standing at (27, 17) just east of the Mart.
- Western Pewter NPC: Stationed at (8, 15) in the western residential area.


## Pewter Gym Interior Layout & Landmarks
- Entrance Mat: Located at (4..5, 13) at the south edge; stepping Down onto row 14 triggers exit warp to Pewter City (16, 18).
- Central Highway: Columns 4 and 5 form a clear 2-tile wide grey floor corridor running north from row 12 to row 2.
- Entrance Statues: Left statue at (3, 10), right statue at (6, 10). Tops occupy row 9.
- Gym Guide: Stationed at (7, 10) east of the right statue. Talks from (7, 11).
- Boulder Barriers:
  - Row 9: Flanks central path at columns 0..2 (west) and 7..9 (east).
  - Row 7: Boulders at columns 5..7 and 9. Passage is through columns 3..4 and 8.
  - Row 5: Boulder at (5, 5).
  - Row 3: Boulders at columns 1..3 and 6..8 flanking the northern platform passage at columns 4..5.
  - Row 0: Solid northern boundary boulder wall across columns 0..9.
- Junior Trainer Liam: Stationed at (3, 6) facing East across column 4; line of sight triggers on tile (4, 6).
- Leader Brock Platform: Elevated platform at rows 1..2. Brock is stationed at (4, 1) facing South; player challenges Brock from (4, 2).

## Pewter Pokémon Center Interior
- Entrance Mat: (3..4, 7). Exits south to Pewter City at (13, 26).
- Counter: Extends across row 2 (cols 0..7). Poké Ball healing tray at (3, 2).
- Nurse Joy: Stationed behind counter at (3, 1). Talk from (3, 3) facing North to heal party.
- Green-haired Customer: Stationed at (4, 3) facing North. Dialogue: "I've 6 POKé BALLs set in my belt."
- Youngster: Stationed at (7, 3).
- PC: Located at (10, 0) in the northeast alcove.
- Couch NPC (0, 4): Jigglypuff trainer sitting at table. Dialogue: "When JIGGLYPUFF sings, POKéMON get drowsy...".
- Pokémon (1, 3): Jigglypuff standing next to trainer at (0, 4).
## Route 3 Border Connection
- Eastern Exit Corridor (Rows 16..19, Cols 32..39): 4-tile wide east-west thoroughfare connecting directly to Route 3. Passes the notice signpost at (33, 19). Fully passable at (32..33, 18).

<hr>

<h1><code>Locations/Kanto_Route3</code></h1>

# Route 3 Geography & Points of Interest

## Connections
- West: Pewter City eastern exit at (0, 8..11).
- East: Mt. Moon.

## Landmarks & Layout
- Lass Robin (33, 10): Stationed at (33, 10) facing North across row 8 road (walks to (33, 9) when triggered from (33, 8)).
- Western Entrance (Rows 8..11, Cols 0..1): 4-tile wide open ground passage connecting to Pewter City, bounded by solid mountain cliff walls to the north (rows 6..7) and south (rows 12..14).
- First Tall Grass Field (Rows 8..11, Cols 2..5+): Tall grass spans across columns 2 to 5+. Stone boundary posts located at (4, 8) and (4, 11). Rows 9 and 10 provide continuous east-west passage through the grass field.

- Shrub Obstacles (Col 9): Small trees at (9, 10) and (9, 11) block row 10..11; bypass via tall grass at (9, 8..9).
- Terraces & Ledges:
  - Upper tier: Row 6..7 bounded by south ledge at row 7 (cols 10..13).
  - Middle tier: Rows 8..10 tall grass (cols 10..13).
  - Lower tier: Rows 12..13 tall grass, south of row 11 ledge.
- Bug Catcher (10, 6): Stationed on upper tier at (10, 6) facing South/East.
- Youngster (14, 4): Stationed on upper tier at (14, 4) facing South across column 14.
- Lass (16, 9): Stationed at (16, 9) facing West across row 9 middle corridor. Line of sight triggers at (14, 9).
- Shrub Barrier (Col 17): Vertical column of small trees at column 17 from row 6 to row 10+ (row 6 is blocked at (17, 6); rows 4 and 5 are open passage).
- Bug Catcher (19, 5): Stationed at (19, 5) facing South across column 19.
- Lass (23, 4): Stationed at (23, 4) facing West across row 4. Vision range: 4 tiles (walks to (20, 4) when triggered from (19, 4)).
- Eastern Shrub (23, 6): Tree blocking row 6 at column 23.
- Bug Catcher James (24, 6): Stationed at (24, 6) facing West into tree at (23, 6).
- Upper East Bypass: Row 6 corridor (18..22, 6) is open; connects to row 5 at (22..24, 5) heading directly east toward Mt. Moon.
## Corridor Connectivity & Ramps
- Ledge Ramps (Passable 2-way):
  - Row 11 Ramp at (15, 11): Verified 2-way passable tan dirt ramp connecting lower tier (rows 12..13) and middle tier (rows 8..10). Can be walked North and South.
  - Row 7 Ramp at (11, 7): Matching tan dirt ramp connecting middle tier (rows 8..10) to upper tier (rows 4..6).
- Tier Structure:
  - Upper Tier (Rows 4..6): Main eastward thoroughfare.
  - Middle Tier (Rows 8..10): Guarded by Lass (16, 9); NPC stationed at (22, 9). Blocked by trees at col 17 (rows 6..11) and col 23.
  - Lower Tier (Rows 12..13): Southern tall grass trench. Accessible via jumping row 11 ledge or through (15, 11) ramp. Bounded by trees at (23, 12..13) and cliff at (9, 12).
- Eastern Ledge & Ramp at (27, 7): Empirically verified walkable tile.
- Eastern Road (Cols 28..37, Rows 8..9): Wide 2-tile tall open clear-ground road running East past column 37 toward Mt. Moon.
- Eastern Ledge & Ramp (37, 7): Empirically verified passable ramp.
- Far Eastern Highway (Cols 38..47, Rows 4..6): Wide continuous open green highway running east past column 47 toward the Mt. Moon entrance courtyard.
- Far Eastern Mountain Spur (Col 50): Solid mountain cliff blocks eastward passage on rows 3..7.
- Far Eastern Ramp (49, 7): Empirically verified 2-way passable ramp. Connects lower bypass road to the upper highway.
- Southern Bypass around Mountain (Rows 10..12, Cols 49..54+): Mountain cliff terminates at row 9. Rows 10 and 11 form a wide open clear-ground highway running east past column 54.
- Eastern Structure (58..59, 8..9): Impassable structure at western edge of eastern grass field. Tile (58, 9) is solid (collision confirmed from (58, 10) and (57, 9)). Sign located at (59, 9).
- Signpost (59, 9): Reads "ROUTE 3 - MT. MOON AHEAD".
- Resting NPC (57, 11): Youngster stationed at (57, 11). Dialogue: "Whew... I better take a rest... Groan... That tunnel from CERULEAN takes a lot out of you!". Friendly NPC who traversed Mt. Moon from Cerulean.
- Row 7 Ledge at (57, 7): South-facing ledge. Cannot be climbed North.
- Eastern Grass Pocket (Cols 58..65, Rows 8..13): Enclosed tall grass field at the southeastern boundary of Route 3. Bounded by solid rock cliff to the east (Col 66, Rows 8..13) and map boundary to the south (Row 14). Confirmed dead-end pocket for wild encounters (Spearow, etc.); does NOT lead to Mt. Moon.
- Out-of-Bounds Border: Repeating tan road metatiles visible south of row 13 and east of column 66 are the out-of-bounds border block.
- Mt. Moon Access Ramp (59, 7): Empirically verified 2-way passable tan dirt ramp located directly behind the Mt. Moon signpost at (59, 9). Ascends from row 8 up onto the elevated northern terrace at (59, 6).
- Northern Highway to Route 4 (Cols 56..57, Rows 0..6): 2-tile wide clear-ground corridor bounded by mountain cliff on the west (Col 55) and building structure on the east (Cols 58..63). Runs continuously North directly toward the Route 4 / Mt. Moon boundary.
- Northern Exit to Route 4: Located at (57, 0). Stepping North triggers the map transition directly into Route 4 outside Mt. Moon.

<hr>

<h1><code>Locations/Kanto_Route4</code></h1>

# Route 4 Geography & Points of Interest

## Connections
- South: Route 3 northern entrance at (7, 17).
- North/East: Mt. Moon entrance and Pokémon Center.
- East: Cerulean City border at column 80+ via row 10-11 bridge.

## Geography & Layout
- Southern Entry (7..11, 16..17): Open pale mint courtyard entering from Route 3.
- Row 15 Ledge: South-facing ledge spanning columns 6..9. Passable corridor around it is at columns 10..11.
- Northbound Avenue (Cols 10..11, Rows 13..17): Open unobstructed path heading north toward the Pokémon Center and Mt. Moon.
- Row 11 Ledge: South-facing ledge spanning columns 7..11. Passable corridor around it is through column 12+ to the east.
- Corridor (Cols 12..13, Rows 9..13): Open unobstructed passage bypassing the row 11 ledge to the north.
## Key Buildings
- Mt. Moon Pokémon Center: Located at columns 10..13, rows 4..5.
  - Entrance Door: Located at (11, 5).
  - "POKé" Sign: Located at (12, 5).
  - Courtyard: Clear open ground at rows 6..8, columns 11..13.
  - Exterior NPC: Cooltrainer F around (10, 7).
## Mt. Moon Pokémon Center Interior
- Entrance Mat: (3..4, 7). Exits south to Route 4.
- Counter: Extends across row 2 (cols 0..7). Poké Ball healing tray at (3, 2).
- Nurse Joy: Stationed behind counter at (3, 1). Talk from (3, 3) facing North.
- Green-haired Customer: Stationed at (4, 3) facing North. Dialogue: "I've 6 POKé BALLs set in my belt."
- Youngster: Stationed at (7, 3).
- PC: Located at (10, 0) in the northeast alcove.
- Couch NPC (0, 4): Jigglypuff trainer sitting at table. Dialogue: "When JIGGLYPUFF sings, POKéMON get drowsy...".
- Pokémon (1, 3): Jigglypuff standing next to trainer at (0, 4).
## Cave & Landmarks
- Mt. Moon Cave Entrance: Located at (18, 5). Cave mouth set into the north cliff face, entered from (18, 6) facing North.
- Route 4 Signpost: Located at (17, 7).

## Eastern Section (Mt. Moon Exit to Cerulean City)
- Mt. Moon Exit Cave: Located at (24, 5), player steps out to (24, 6) facing South.
- Route 4 Eastern Signpost: Located at (27, 7), read from (27, 6) facing South.
  - Text: "ROUTE 4 / MT. MOON - CERULEAN CITY"
### Eastern Section Geography & Elevation
- Northern Alcove / Passage (Cols 36..37, Rows 2..5): 2-tile wide dead-end alcove heading North between western mountain cliff (col 35) and eastern rock ridge (col 38), terminating at row 1 mountain wall.
- Middle Corridor (Rows 6..8, Cols 24..42+): Open east-west green corridor between Mt. Moon exit and Cerulean City.
- Upper Ledge (Row 5, Cols 39..42+): South-facing one-way jump ledge bounding the upper plateau from the middle corridor.
- Lower Ledge (Row 9, Cols 24..42+): South-facing one-way jump ledge bounding the middle corridor from the lower route.
- Column 45 Ledge: One-way jump ledge facing East at row 6. Stepping East from (44, 6) hops over (45, 6) to (46, 6).
- Central Corridor (Cols 46..49, Rows 2..10): Open green grass corridor between col 45 ledge and col 50 ridge. North boundary at row 1 is solid mountain cliff.
- Row 10 Corridor (Cols 42..61, Rows 10..12): Open grass corridor bordered to the north by row 9 ledge and south by row 13 ledge.
- Row 9 Ledge Gap: Located at (61, 9). Passable gap allows walking North from row 10 up onto row 8.
- Row 13 Ledge Gap: Located at (53, 13). Passable gap allows walking North from row 14 directly up into row 12.
- Eastern Row 13 Ramp/Gap: Located at (77, 13). Empirically verified walkable tile on Turn 2264 connecting row 12 and row 14.
- Lower Corridor (Cols 42..61, Rows 14..15): Bounded by row 13 south-facing ledge to the north. Walkable red flower bed at cols 42..47, open grass at cols 48..61.
- Row 8 Bypass: Open grass path at row 8 bypassing the col 62 tree line (which only blocks rows 9..15).
- Lower Corridor Boundaries: Solid rock wall at col 41 (verified at (41, 15)); solid water/shoreline at row 16 (verified at (44, 16) and (61, 16)); column 75 tree line extends rows 9..13 only (rows 14..15 are completely open grass connecting the bridge pocket to the western lower corridor).

<hr>

<h1><code>Locations/Kanto_MtMoon_1F</code></h1>

# Mt. Moon 1F Geography & Exploration

## Connections
- South Exit: Warp at (14, 35) leading outside to Route 4.
- Ladder (13, 27): Ladder descending to basement chamber.
- Ladder (17, 11): Ladder in north-central corridor.

## Layout & Corridors

- Entrance Corridor (Cols 14..15, Rows 31..35): 2-tile wide north-south cave passage bounded by rock walls at cols 10..13 (west) and cols 16..19 (east).

- Main Cavern Junction (Rows 27..29, Cols 10..15): Entrance corridor opens into a wide open cavern extending west toward columns 0..9 and north toward row 20+.

- Signpost (15, 23): Reads "Beware! ZUBAT is a blood sucker!".

- Bug Catcher (16, 23): Stationed at (16, 23) facing South down column 16.

- Northern Boundary Wall (Rows 20..21): Solid rock wall blocking northward travel above junction.

- Southwest Cavern Pocket (Cols 2..7, Rows 18..24): Enclosed pocket containing TM12 at (5, 32), Potion at (2, 20), and Bug Catcher at (7, 23). Bounded on north by solid rock wall at rows 18-19.

- Western Passage (Rows 24..26, Cols 8..10): Open passage connecting central junction west into Western Cavern Corridor. Columns 8..9 rock wall occupies rows 18..23.

- Bug Catcher (7, 22): Defeated (Weedle Lv 11, Kakuna Lv 11). Yielded ¥110.

- Ground Item (5, 32): TM12 (WATER GUN) collected.

- Ground Item (2, 20): POTION collected.
- Ground Item (35, 31): RARE CANDY collected in far southeast cavern pocket.
- Southeast Pocket (Cols 30..37, Rows 28..34): Open cavern ending at eastern rock wall at col 38.

- East-West Cross Corridor (Row 22, Cols 10..21): Clear passage running east-west south of the Northern Boundary Wall, passing behind Bug Catcher (16, 23) and connecting Eastern Avenue (col 21) west into Western Cavern Corridor.

- Eastern North-South Avenue (Cols 20..21, Rows 18..25+): 2-tile wide vertical corridor bounded by eastern rock wall (Col 22) and central pillar (Cols 18..19). Runs north past row 18 toward the northeast caverns and ladders.

- Central Rock Pillar (Cols 18..19, Rows 8..11): Rock wall at columns 18..19, rows 8..11 blocking westward movement along row 11.

- Eastern Avenue (Cols 24..27, Rows 11..27): Wide 4-tile north-south thoroughfare connecting southern bypass (rows 26..27) directly north to row 11 corridor.

- Northern Highway (Rows 6..7, Cols 16..25+): Wide open east-west corridor running along the northern section of 1F.

- Rock Wall Partition (Rows 8..9, Cols 18..29): Horizontal rock divider between northern highway and row 10.

- Eastern North-South Passage (Col 30, Rows 6..14): Open floor passage east of rock partition connecting row 10 directly north into Northern Highway.

- North-Central Alcove (Cols 16..17, Rows 8..17): North-south pocket descending from Northern Highway (rows 6-7) south to Ladder (17, 11).

- East-West Row 10 Corridor (Row 10, Cols 20..25+): Clear passage running east from column 20 past column 25 toward the eastern wall.

- Lass (30, 4): Stationed at (30, 4) facing South down column 30. Dialogue: "Wow! It's way bigger in here than I thought!". Team: Oddish Lv 11, Bellsprout Lv 11. Status: Defeated. Yielded ¥165.

- Vertical Wall Partition (Cols 12..13, Rows 3..11+): 2-tile wide vertical rock wall separating north-central corridor (cols 14-17) from northwest corridor (cols 10-11).

- Row 28 Boundary: Impassable southern rock boundary wall directly south of (14..19, 27) at row 28.

- Central Wall (Col 23, Row 22): Solid rock wall separating Eastern Avenue from central area.

- Super Nerd (24, 31): Defeated (Magnemite Lv 11, Voltorb Lv 11). Line of sight triggered at (24, 28). Dialogue: "What! Don't sneak up on me!". Loss: "My POKéMON won't do!". Prize: ¥275.

- Youngster (14, 16): Stationed at (12..14, 16) facing East. Dialogue: "Did you come to explore too?". Team: Rattata Lv 10, Rattata Lv 10, Zubat Lv 10. Status: Defeated. Prize: ¥150.

- Hiker (5, 6..7): Stationed at (5, 6) in front of Northwest Ladder, facing South. Dialogue: "WHOA! You shocked me! Oh, you're just a kid!". Team: Geodude Lv 10, Geodude Lv 10, Onix Lv 10. Status: Defeated. Prize: ¥350.
- Ladder (5, 5): Descending ladder in the northwest corner of 1F.


<hr>

<h1><code>Locations/Kanto_MtMoon_Basement1</code></h1>

# Mt. Moon Basement (B1F)

## Connections
### Southern Section (Entrance Ladder 13, 27 Area)
- Architectural Note: On Turn 1792, this section was empirically verified to connect seamlessly to B2F main cavern corridors without any map transitions. For unified geographic mapping of this floor, refer to Locations/Kanto_MtMoon_Basement2.md.
- Ladder (15, 27): Ascending ladder leading back to Mt. Moon 1F at (13, 27).

### Central Transit Corridor (1F Ladder 17, 11 Area)
- Ladder (25, 9): Ascending ladder leading back to Mt. Moon 1F at (17, 11).
- Ladder (17, 11): Descending ladder leading to Mt. Moon B2F at (25, 9).

## Layout & Geography
### Southern Section
- Arrival Warp: Warped from 1F (13, 27) onto basement (13, 27) and automatically scripted 2 steps east to (15, 27).
- Southern Ridge/Plateau: Elevated cliff ridge spanning rows 28..30, cols 12..20. Lower speckled floor path runs along row 31.
- Western Corridor: North-south corridor along column 11 (rows 23..31).
- Main Northern Cavern (Cols 14..20, Rows 23..27): Wide open speckled cave floor extending north toward unexplored basement depths.
- Ground Item (25, 21): Item ball visible on elevated northern platform above row 23 ledge.
- Row 23 Ledge (Cols 24..25, Row 23): South-facing one-way ledge separating northern platform (rows 21..22) from southern floor (rows 24..27).
- Eastern Cavern (Cols 20..28+, Rows 24..27): Wide speckled cave floor extending east past column 28.
- Eastern Ridge (Cols 30..31, Rows 21..28): 2-tile wide impassable elevated cliff ridge separating central terrace from eastern corridor.
- Eastern Corridor (Cols 32..34, Rows 22..29+): Open cave floor running north-south east of the ridge.
- Western Ledge (Cols 12..13, Rows 21..28): 2-tile wide elevated ridge with east-facing jump ledge at column 13. Empirically verified impassable from east.

### Central Transit Corridor
- Geography: 4-tile wide east-west corridor spanning rows 8..11, cols 14..25. Bounded by solid rock wall to the north at row 7. Connects Ladder (25, 9) and Ladder (17, 11).

### Northwest Transit Corridor (1F Ladder 5, 5 Area)
- Ladder (5, 5): Ascending ladder leading back to Mt. Moon 1F at (5, 5).
- Ladder (21, 17): Descending ladder leading to Mt. Moon B2F main cavern.
- Layout: Corridor runs south along cols 4..7 to row 16, turns east along rows 16..17 to col 21, connecting Ladder (5, 5) and Ladder (21, 17).

## NPCs & Trainers
- Team Rocket Grunt: Stationed at (15, 24) facing South in Southern Section.
  - Team: Sandshrew Lv 11, Rattata Lv 11, Zubat Lv 11.
  - Status: Defeated.

### Northeast Exit Transit Corridor
- Arrival from B2F Ladder (5, 7): Arrive at (23, 3).
- Ladder (27, 3): Ascending ladder leading up to Mt. Moon 1F Route 4 exit room.
- Corridor runs east-west along rows 2..3 between col 20 and col 27.

<hr>

<h1><code>Locations/Kanto_MtMoon_Basement2</code></h1>

# Mt. Moon B2F Geography & Exploration

## Connections
- Ladder (25, 9): Ascending ladder leading back to B1F transit corridor at (17, 11).

## Layout & Landmarks
- Entrance Plateau (Cols 24..35, Rows 6..11): Empirically verified isolated elevated terrace.
  - Northern Boundary (Rows 2..5): Solid rock wall across cols 28..35.
  - Southern Boundary (Row 11..12): Impassable elevation cliff across cols 24..37.
  - Eastern Boundary (Col 35..36): Impassable elevation cliff across rows 6..11.
  - Western Partition (Cols 30..31, Rows 5..7): Solid rock wall separating eastern plateau from (29, 5) item pocket.
- Ledge (Cols 28..29, Row 7): South-facing one-way jump ledge.
- Ground Item (29, 5): Item ball visible on elevated northern platform above row 7 ledge.
- Team Rocket Grunt (29, 11): Defeated (Zubat Lv 12, Ekans Lv 12). Prize: ¥360.
- Boulder: Isolated rock at (33, 9).
- Main Cavern Connectivity: Northern corridor at row 6 blocked to west by wall at (31, 6); southern edge bounded by cliff at row 11..12. 

### Main Cavern (Reached via Ladder 21, 17)
- Ladder (21, 17): Ascending ladder leading back to B1F Northwest corridor at (21, 17).
- Central Cross Corridor (Cols 18..28, Rows 12..14): Wide open cave floor running east-west below the entrance plateau cliff.
- Northern Highway (Cols 20..22, Rows 5..13): Corridor bounded on east by plateau cliff (Cols 23..24) and on north by solid rock wall at row 4. Checkered tiles at Cols 18..19 are impassable.
- Ledge (Cols 26..27, Row 15): South-facing one-way ledge.
- Team Rocket Grunt (29, 17): Defeated (Raticate Lv 16). Prize: ¥480. Dialogue: 'Little kids should leave grown-ups alone!' / 'I'm steamed!'.
- Southern Cavern Corridor (Cols 26..34, Rows 16..18): 3-tile high open cave corridor running east below the central rock formation and ledges. East boundary verified solid rock wall at Col 35 across rows 16, 17, and 18 (empirically tested blocked at 35, 16; 35, 17; 35, 18).

### Eastern Cavern Highway & Southern Cavern (Reached via Row 15 / Row 14)
- Breakthrough Passage (33, 15): Empirically verified fully passable northward from Row 16 to Row 14, connecting lower chamber directly back to northern corridors.
- Eastern Cavern Highway (Cols 36..38, Rows 14..24): 3-tile wide open north-south corridor running from row 14 south past row 24. Bounded on east by solid rock wall at Col 39.
- Southern Avenue (Cols 32..34, Rows 24..30): At row 24, the corridor turns west to cols 32..34, running south to row 30.
- Southern Corridor (Cols 11..33, Rows 31..32): 2-tile high corridor extending west from col 33 to col 11 along rows 31-32, bounded by rock walls to north (row 30) and south (row 33).
- Western Cavern Highway (Cols 7..11, Rows 23..32+): At column 11, the corridor opens into a wide 5-tile thoroughfare (cols 7..11) heading north past row 27 toward the western/northwestern quadrant.
- Unified Architecture Note: Southern Ladder (15, 27) and its surrounding plateau/corridors connect seamlessly with this main cavern without any map transition, confirming they are all part of this continuous B2F dungeon floor.

- Team Rocket Grunt (11, 16): Defeated (Rattata Lv 13, Zubat Lv 13). Prize: ¥390. Stationed at (11, 16) facing South down Western Cavern Highway. Line of sight triggered at (11, 19). Dialogue: 'TEAM ROCKET will find the fossils, revive them and sell them for cash!'.
- Fossil Approach Corridor (Cols 12..13, Rows 12..16+): 2-tile wide passage north of defeated Grunt (11, 16), running north along columns 12..13 toward the fossil chamber.

### Fossil Chamber (Rows 5..10, Cols 8..16)
- Super Nerd Miguel: Defeated (Grimer Lv 12, Voltorb Lv 12, Koffing Lv 12). Stationed at (12, 8) facing South down column 12.
- Ground Artifact (13, 6): HELIX FOSSIL (Claimed by player).
- Ground Artifact (12, 6): DOME FOSSIL (Claimed by Super Nerd Miguel).

### Northern Exit Corridor (Cols 9..16, Rows 2..4)
- 3-tile high horizontal corridor extending west from col 16 past col 9.
- North boundary: solid rock wall at rows 0..1.
- East boundary: rock wall at col 17.
- South boundary: rock wall at row 5, with opening at cols 12..13 connecting south into Fossil Chamber.
### Route 4 Exit Chamber (Cols 2..8, Rows 2..7)
- Northern Corridor: cols 3..10, rows 2..4.
- Jump Ledge: South-facing jump ledge at (3, 5).
- Southern Alcove: cols 2..7, rows 6..7.
- Ladder (5, 7): Ascending ladder leading to upper floors toward Route 4 exit.

<hr>

<h1><code>Locations/Kanto_CeruleanCity</code></h1>

# Cerulean City Geography & Points of Interest

## Connections
- West: Route 4 eastern bridge at (0, 18..19).
- North: Route 24 entrance at (20..21, 5..6).

## Geography & Layout
- Central Lawn Elevation (Cols 22..23, Row 17): Impassable northbound elevation boundary bounding the lawn between Pokémon Center and Gym, empirically verified impassable on Turns 2213-2214.
- Northwest House & Center Boundary: Northwest House spans cols 12..17, rows 14..15 (door at (13, 15), windows at (14..16, 15)). Connects flush to Pokémon Center (cols 18..21, rows 14..17) with no gap between buildings. Empirically verified on Turn 2195 that (17, 15) is solid collision.
- Bicycle Shop Citizen (9, 27): "I want a bright red bicycle!"
- Northern District Street (Cols 13..21+, Rows 12..13): Wide open east-west paved avenue revealed north of the Northwest House and Pokémon Center roofs.
- Western Elevation Boundary & (8, 15) Ramp: Row 15 features an impassable boundary across cols 9..11 (verified at (10, 15) on Turn 2183 and (9, 15) on Turn 2249), but tile (8, 15) is an open walkable ramp connecting Western Avenue directly north into Northern District Street (empirically verified on Turn 2276).
- Northern District House: Located at cols 8..12, rows 10..11 with front door at (9, 11) facing south onto the Northern District Street.
- Canal Northern Bank Landmark (4, 11): Northern cave/mouth structure at (4, 11) with green-haired NPC at (4, 12).
- Resident NPC (15, 16): "That bush in front of the shop is in the way. There might be a way around."
- Western Avenue (Cols 8..11, Rows 16..18): Open north-south street connecting to the main thoroughfare along row 18.
- Eastern Elevation Boundary (Row 19, Cols 32..37): Impassable northbound elevation boundary across cols 32..37.
- Eastern Bollard Line (Col 35, Rows 20..27): Vertical barrier of wooden bollards separating col 34 from cols 36..37. Empirically verified at (35, 27) on Turn 2236 that bollards are solid collision.
- Eastern Corridor (Col 34, Rows 20..25): Open north-south pale mint pathway running south between flower garden/building (cols 31..33) and bollards (col 35).
- Southeast Building: Located at cols 28..33, rows 24..25 with blue roof. Empirically verified on Turn 2191 that (33, 25) is solid wall (no functional entrance door).
- Gym Front Street NPC: Boy stationed at (31, 20) facing South. Passable to the south via row 21.
- Western Entrance (Cols 0..10, Rows 18..19): Wide paved street entering from the Route 4 bridge.
- Canal / River (Cols 0..6, Rows 14..16): Bounded by stone fence posts at row 17 (opening east at cols 8..9).
- Southern Green (Cols 5..10, Rows 20..25): Grassy lawn with south street branch at cols 6..7 and stone fence posts at col 4 (rows 20..27).
- Cerulean Bicycle Shop: Located at cols 10..15, rows 22..25. Front entrance door at (13, 25).
  - Interior: Entrance mat at (2..3, 7). Display bicycles at (0..1, 4..5) and (6..7, 6..7). Shop Clerk/Manager at (5, 4) with counter at (5..7, 3).
  - Pricing & Mechanics: Manager offers Bicycle for ¥1,000,000 (unaffordable without Bike Voucher).
  - Customer at (1, 3): Dialogue - bicycles are cool but way too expensive.
- Southern Barrier (Rows 28..29): Impassable barrier consisting of bushes, wooden bollards at (16, 29), Trainer Tips signpost at (17, 29), and a Cut tree at (19, 28) blocking direct southern access to Route 5 without HM01 Cut.
- Trainer Tips Signpost (17, 29): "TRAINER TIPS / Pressing B Button during evolution cancels the whole process."
- Resident NPC: Wandering citizen around (10, 21).

## Key Buildings & Facilities
- Northwest House: Located at cols 12..15, rows 14..15. Entrance door at (13, 15).
  - Interior: Entrance mat at (2..3, 7). Large table at (3..4, 3..4).
  - Resident 1 at (5, 4): Kid in blue overalls.
  - Resident 2 at (1, 2): Trader (offers JYNX for player's POLIWHIRL).
  - North wall: Solid wall with bookcases (0..1, 0..1), painting at (3, 0), window at (5, 0). No back door exit.
- Cerulean Pokémon Center: Located at cols 18..21, rows 14..17. Entrance door at (19, 17), "POKé" sign at (20, 17).
  - Interior: Entrance mat (3..4, 7). Nurse Joy behind counter at (3, 1), talk from (3, 3) facing North. Customer at (4, 3).
- Cerulean Gym: Located at cols 24..31, rows 16..19. Entrance door at (30, 19). Front street along row 20. Exterior signpost at (27, 21) verified on Turn 1955: "CERULEAN CITY POKéMON GYM / LEADER: MISTY".
  - Interior: Entrance mat at (4..5, 13). Central pool spanning rows 9..11 with central pier at cols 4..5. Left statue at (3, 10..11), right statue at (6, 10..11). Gym Guide stationed at (7, 10).
  - Gym Guide Advice (verified Turn 1979): Leader Misty specializes in Water-type Pokémon; recommends Grass (plant) and Electric types as counters.
  - Gym Trainers:
    - Swimmer (male) on central pier: Horsea Lv 16 (283 EXP), Shellder Lv 16 (331 EXP). Prize: ¥80. Defeated Turn 2005.
    - Jr. Trainer ♀ on northern platform at (4, 3): Goldeen Lv 19 (451 EXP). Prize: ¥380. Defeated Turn 2016.
    - Gym Leader Misty at (4, 2): Staryu Lv 18 (408 EXP), Starmie Lv 21 (931 EXP). Prize: ¥2079, CASCADEBADGE, TM11 (BUBBLEBEAM). Defeated Turn 2077.
- Cerulean Poké Mart: Located at cols 24..27, rows 22..25. Entrance door at (25, 25), "MART" sign at (26, 25). Front street at rows 26..27. NPC at (29, 26) with Pokémon at (28, 26).
  - Interior: Entrance mat (3..4, 7). Counter & register at (1, 4..5), Clerk at (0, 5) (talk from (2, 5) facing West). Customers at (3, 3) and (4, 2).
  - Catalog Items: POKé BALL (¥200), POTION (¥300), REPEL (¥350), ANTIDOTE (¥100).


<hr>

<h1><code>Locations/Kanto_Route24</code></h1>

# Route 24 Geography & Points of Interest

## Connections
- South: Cerulean City northern gateway at (10..11, 36) [connects to Cerulean (20..21, 0)].
- East: Route 25 border at northeast plateau.

## Geography & Layout
- Nugget Bridge: 2-tile wide golden bridge extending north across water along columns 10 and 11.
- Bridge Gauntlet: 5 trainers stationed consecutively along the bridge corridor.
  - Trainer 1: Bug Catcher Cale stationed at (11, 31) facing West. Team: Caterpie Lv 14 (159 EXP), Weedle Lv 14 (156 EXP). Defeated Turn 2310. Prize: ¥140.
  - Trainer 2: Lass stationed at (10, 28) facing South. Team: Pidgey Lv 14, Nidoran♀ Lv 14. Defeated Turn 2319. Prize: ¥210.
  - Trainer 3: Youngster stationed at (11, 25) facing West. Team: Rattata Lv 14, Ekans Lv 14, Zubat Lv 14. Defeated Turn 2327. Prize: ¥210.
  - Trainer 4: Lass stationed at (10, 22) facing North. Dialogue: "I'm No. 4! Getting tired?". Team: Pidgey Lv 16, Nidoran♀ Lv 16. Defeated Turn 2341. Prize: ¥240.
  - Trainer 5: Jr. Trainer ♂ stationed at (11, 19) facing West. Dialogue: "OK! I'm No. 5! I'll stomp you!". Team: Mankey Lv 18 (285 EXP). Defeated Turn 2353. Prize: ¥360.
  - Bridge Finish / Recruiter: Team Rocket Grunt stationed at (11, 15) facing West. Awards NUGGET for beating the 5 trainers, then battles player (Ekans Lv 15, Zubat Lv 15). Defeated Turn 2367. Prize: ¥450.
## Northern Section (North of Nugget Bridge)
- Northern Avenue (Cols 10..11, Rows 8..15): Open pale mint path connecting Nugget Bridge to row 8.
- Row 10 Bollard Barrier: Stone bollards spanning (12..18+, 10) enclosing southeast lawn.
- Row 7 Elevation Boundary: Brown elevation ridge spanning columns 7..12 at row 7 with corner post at (13, 7). Walkability/jump mechanics unverified.
- Row 8 Corridor: Open pale mint corridor spanning row 8 (cols 10..18+).
- Northern Corridor (Cols 14..15, Rows 4..8): Open 2-tile wide pale mint path heading north between column 13 cliff wall and column 16 rocky cliff.
- Eastern Avenue (Rows 8..9, Cols 14..18+): Open pale mint corridor extending east toward Route 25.
- Item Ball at (10, 5): Pok¥ Ball item visible on western elevated plateau north of row 7 ridge.

<hr>

<h1><code>Locations/Kanto_Route25</code></h1>

# Route 25 Geography & Points of Interest

## Connections
- West: Route 24 at (0, 8..9).
- East: Sea Cottage (Bill's House).

## Geography & Layout
- Western Gateway (Cols 0..9, Rows 8..9): 2-tile wide pale mint avenue from Route 24, terminating at column 9 (blocked by trees at (10, 8) and (10, 9)).
- Southern Barrier (Row 10): Line of stone bollards bounding the avenue from the southern lawn (cols 0..11+).
- Northern Elevation (Row 7): Brown elevation ridge spanning cols 0..7. Ends at col 7.
- Shrub Barrier (8, 7): Dense shrub at (8, 7) blocking sightline south from (8, 4).
- Corridor 1 (Col 9, Rows 4..8): Open grass connector linking row 8 avenue north to rows 4..7.
- Row 7 Tree Gap (Cols 10..11, Row 7): 1-tile wide east-west grass corridor between trees at (10..11, 6) and (10, 8..9).
- Trainer 1 - Hiker Franklin at (8, 4): Stationed facing South (sight range: 1 tile, covers (8, 5)). Defeated Turn 2385. Team: Machop Lv 15, Geodude Lv 15. Prize: ¥525.
- Northern Tree Canopy (Cols 2..7, Rows 4..5): Forest canopy north of row 6 grass corridor.
- Trainer 2 at (13, 7): Hiker stationed at (13, 7) facing East. Defeated Turn 2416. Team: Onix Lv 17. Prize: ¥595.
- Trainer 3 at (14, 2): Youngster stationed at (14, 2) facing South. Defeated Turn 2408. Team: Rattata Lv 15, Spearow Lv 15. Prize: ¥225.
- Trainer 4 at (18, 5): Youngster stationed at (18, 5). Defeated Turn 2442. Team: Slowpoke Lv 17. Prize: ¥255.
- Trainer 5 at (18, 8): Lass Haley stationed at (18, 8). Defeated Turn 2458. Team: Nidoran♂ Lv 15, Nidoran♀ Lv 15. Prize: ¥225.
- Item Ball at (22, 2): Poké Ball visible east of column 21 tree line.
- Trainer 6 at (23, 9): Hiker Nob stationed at (23, 9) facing North. Defeated Turn 2485. Team: Geodude Lv 13, Geodude Lv 13, Machop Lv 13, Geodude Lv 13. Prize: ¥455.
- Trainer 7 at (24, 4): Jr. Trainer ♂ stationed at (24, 4) facing South (sight range: 3 tiles). Defeated Turn 2498. Team: Rattata Lv 14, Ekans Lv 14. Prize: ¥280. Defeat Quote: "JR.TRAINER♂: Aww, darn...".
- Trainer 8 at (32, 3): Youngster stationed at (32, 3) facing West. Defeated Turn 2516. Team: Ekans Lv 14, Sandshrew Lv 14. Prize: ¥210. Defeat Quote: "YOUNGSTER: I knew I'd lose too!".
- Corridor Layout (Cols 28..32, Rows 2..6):
  - Row 2: Open grass cols 28..32. Blocked to west by tree at (27, 2).
  - Row 3: Open grass cols 28..31. Youngster at (32, 3) facing West.
  - Row 4-5: Trees at (31, 4..5) and (28..29, 7..9). Open grass at cols 28..30 (rows 4..5).
  - Row 6: Open grass corridor cols 27..32+ passing south of trees at (31, 4..5).
  - Alcove Access to (22, 2) Item Ball: Open path via (23, 7) -> (23, 5) -> (24, 5) -> (24, 3) -> (22, 2).
- Trainer 9 at (37, 4): Lass stationed at (37, 4) facing South (sight range: 1 tile). Defeated Turn 2531. Team: Oddish Lv 13, Pidgey Lv 13, Oddish Lv 13. Prize: ¥195. Defeat quote: "LASS: I'm not so jealous!".
- Sea Cottage / Northeast Building: Large house spanning cols 37..46+, rows 1..3 with blue gabled roof over east wing and front entrance door at (45, 3). Paved courtyard extends cols 42..46, rows 4..7.

<hr>

<h1><code>Locations/Kanto_SeaCottage</code></h1>

# Sea Cottage (Bill's House) Interior

## Layout & Features
- Entrance Mat: Located at (2..3, 7). Exits south to Route 25.
- Desk & PC: Located at (1..2, 4..5). PC at (1, 5).
- Resident: Bill (entered right teleporter at (6, 2)).
- North Area: Left Teleporter at (1..2, 1..2), Right Teleporter at (5..7, 1..2).
## Events & Quest
- Bill's Experiment: Spoke with Bill (transformed into a Pokémon) at (6, 5). Assisting with Cell Separation System.

<hr>