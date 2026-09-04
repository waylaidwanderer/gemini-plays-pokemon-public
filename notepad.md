<h1><code>Main</code></h1>

# Pokémon Blue - Journey Log

## Status
- Badges: 1 / 8 (Boulderbadge)
- Active Team: Wartortle (SHELDON) Lv 18, Spearow (FALCO) Lv 5
- Money: ¥2421
- Pokédex: 2 Caught / 11 Seen

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
- [ ] Explore Mt. Moon and retrieve Fossil

<hr>

<h1><code>Inventory</code></h1>

# Inventory Log

## Items
- TOWN MAP
- POKé BALL x3
- POTION x3
- ESCAPE ROPE x1
- ANTIDOTE x0 (Depleted)
- TM12 (WATER GUN)
- TM34 (BIDE)

## Key Items
- POKéDEX

## Money
- ¥2421

## Party Pokémon
- WARTORTLE (Nickname: SHELDON) [Lv 18, Water]
  - Status: Healthy
  - HP: 20 / 51
  - Stats: Attack 32, Defense 39, Speed 33, Special 33
  - Moves: Tackle (PP 35/35), Tail Whip (PP 30/30), Bubble (PP 14/30), Water Gun (PP 1/25)
- SPEAROW (Nickname: FALCO) [Lv 5, Normal/Flying]
  - Status: Healthy

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

# Combat Mechanics & Tactical Guidelines

## Turn Priority & Item Mechanics
- Move Execution Order: Strictly determined by Speed stat under neutral conditions. Higher Speed acts first. When Speed stats are identical (Speed tie), turn priority is resolved randomly (50/50) each turn.
- In-Battle Item Priority: Bag item usage (e.g. Potion) possesses top execution priority (+1 priority), resolving at the beginning of the turn before any Pokémon moves, irrespective of Speed.
- Item Effects: Potion restores exactly 20 HP to the designated Pokémon.
- Potion Tactical Doctrine: Conserve Potions unless active Pokémon HP <= 5 and opponent possesses lethal KO potential on the current turn. When HP <= 5 and enemy attack cannot be prevented by outspeeding and knocking out the target, item priority ensures 100% survival.

## Battle Menu & Cursor Memory
- Move Selection Cursor Memory: During consecutive attack turns within a single battle, the move menu cursor retains its position from the previously confirmed attack (e.g. executing Bubble from Slot 3 leaves the cursor at Slot 3 on the following turn). It does NOT automatically reset to Slot 1.
- Testing Boundary: Empirically verified across consecutive attack turns with Bubble, Tail Whip, and Tackle, AND verified to persist after navigating through the ITEM submenu to use a Potion. Behavior after PKMN submenu or aborting actions remains unverified.
- Battle Initialization Reset: At the start of a new battle, the move selection cursor resets to Slot 1 (Tackle), regardless of what move was used in previous encounters.
- Main Battle Menu Cursor Memory: The primary 4-choice battle menu (FIGHT, PKMN, ITEM, RUN) retains its position from the previously confirmed action. Specifically, using an Item leaves the cursor on ITEM on subsequent turns, rather than resetting to FIGHT.
- Battle Bag Menu Cursor Memory: Opening the ITEM menu during battle retains the cursor position from the previously confirmed item (empirically verified on Turn 1195: cursor was on POKé BALL at Slot 2 after using a Poké Ball on Turn 1192).
- Battle Move Menu Layout: The 4 moves are arranged in a single vertical 4-line list (Slot 1 at top, Slot 2 second, Slot 3 third, Slot 4 fourth), NOT a 2x2 grid. Pressing "Down" from Slot 1 moves to Slot 2, not Slot 3. To reach Slot 3 from Slot 1 requires pressing "Down" twice.

## Stat Stage Modifiers
- Tail Whip: Decreases target Defense by 1 stage per application (Stage -1 = approx. 2/3 Defense, Stage -2 = approx. 1/2 Defense). Verified: Lv 6 Weedle took 11-12 damage from Tackle at -1 Defense vs ~6-8 at neutral Defense.
- Bubble Secondary Effect: Has a chance to lower target Speed by 1 stage.
- String Shot: Lowers target Speed by 1 stage.

## Verified Damage Ranges & Combat Bounds
- Sheldon (Squirtle Lv 7-8, Attack 13-14, Defense 15-17, Special 13-15):
  - Tackle (Normal, Physical, Power 35, Acc 95%):
    - Against neutral Lv 3-4 wild targets (Pidgey, Rattata): 6-8 HP damage (~35-50% max HP).
    - Against -1 Defense Lv 6 targets: 11-12 HP damage (~60% max HP).
  - Bubble (Water, Special, Power 20 + STAB = 30, Acc 100%):
    - Against neutral Lv 6 Bug/Poison (Weedle): ~8-9 HP damage (~45% max HP).
    - Against neutral Lv 6 Bug (Caterpie): ~15-16 HP damage (~75-80% max HP).
  - Critical Hits: Deal approximately double regular damage, ignoring positive defense stages.
- Sheldon Lv 10-11 Combat Bounds (Attack 17-18, Defense 20-22, Special 17-19):
  - Bubble vs Lv 11 Diglett (Ground, Special ~16): Deals 20-22 damage.
  - Bubble vs Lv 11 Sandshrew (Ground, Special ~15): Deals 16-18 damage (~50% max HP).
  - Enemy Diglett Lv 11 Scratch vs Defense 20: 5 damage on normal hit, 8 damage on critical hit.
  - Enemy Sandshrew Lv 11 Scratch vs Defense 22: 9 damage on critical hit.
  - Enemy Sandshrew Lv 11 Scratch vs Sheldon (Defense 37): 3 HP damage.
  - Bubble (Sheldon Lv 17, Special 32) vs Trainer Sandshrew Lv 11: deals 22 damage on turn 1, KO on turn 2.
  - Enemy Zubat Lv 11 Leech Life vs Sheldon (Defense 39): 1 HP damage.
  - Bubble (Sheldon Lv 18, Special 33) vs Trainer Zubat Lv 11: deals ~14-16 damage (~55% max HP).
- Enemy Offensive Damage Bounds against Sheldon (Defense 25-27):
  - Trainer Pidgey Lv 9 Gust: 5 HP damage on normal hit, 9-10 HP damage on critical hit.
  - Sand-Attack: lowers accuracy by 1 stage per hit (caps at stage -6).

- Enemy Offensive Damage Bounds against Sheldon (Defense 17):
  - Wild Route 1-2 targets (Lv 3-4 Pidgey Gust / Rattata Tackle): 3-4 HP damage.
  - Forest Bug Pokémon (Lv 6 Weedle Poison Sting / Caterpie Tackle): 2-3 HP damage (Critical hit deals ~4 HP).
  - Status Affliction Risk: Poison Sting inflicts Poison on hit (~20-30% chance). Poison deals periodic 1/16 max HP damage in battle and 4 HP every 4 overworld steps.

## Experience & Growth Curves
- Level Milestones:
  - Level 7: 318 EXP
  - Level 8: 482 EXP (Learns Bubble, fills Slot 3)
  - Level 9: 703 EXP
  - Level 10: Max HP 29, Attack 17, Defense 20, Speed 17, Special 17
  - Level 11: Max HP 31, Attack 18, Defense 22, Speed 18, Special 19
  - Level 12: Stats unverified
  - Level 13: Max HP 35, Attack 20, Defense 25, Speed 20, Special 21
  - Level 14: Max HP 37, Attack 22, Defense 27, Speed 22, Special 23
  - Level 15: Max HP 39, Attack 23, Defense 29, Speed 23, Special 24 (Learns Water Gun, fills Slot 4)
  - Level 16 (Squirtle): Max HP 41, Attack 24, Defense 30, Speed 24, Special 25
  - Level 16 (Wartortle): Max HP 46 (Current HP scaled to 34 / 46)
  - Level 17: Max HP 49, Attack 31, Defense 37, Speed 31, Special 32
  - Level 18: Max HP 51, Attack 32, Defense 39, Speed 33, Special 33

## Defeat Yields
- Wild Rattata Lv 3: 24 EXP | Lv 4: 32 EXP
- Wild Pidgey Lv 3: 23 EXP | Lv 4: ~23-28 EXP
- Trainer Weedle Lv 6: 66 EXP
- Trainer Caterpie Lv 6: ~66 EXP
- Trainer Pidgey Lv 9: 105 EXP
- Trainer Weedle Lv 9: 99 EXP
- Trainer Kakuna Lv 9: 136 EXP
- Trainer Caterpie Lv 9: 102 EXP
- Trainer Metapod Lv 9: 138 EXP
- Trainer Metapod Lv 11: 169 EXP
- Trainer Caterpie Lv 10: 112 EXP
- Trainer Caterpie Lv 11: 124 EXP
- Trainer Rattata Lv 10: 121 EXP
- Trainer Nidoran♂ Lv 10: 127 EXP
- Trainer Rattata Lv 11: 133 EXP
- Trainer Weedle Lv 10: 111 EXP
- Trainer Diglett Lv 11: 190 EXP
- Trainer Sandshrew Lv 11: 219 EXP
- Trainer Zubat Lv 11: 126 EXP
- Trainer Ekans Lv 11: 145 EXP
- Leader Geodude Lv 12: 220 EXP
- Trainer Jigglypuff Lv 14: 228 EXP
- Leader Onix Lv 14: 324 EXP

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
- Eastern Ledge & Ramp at (27, 7): Empirically verified walkable tile. Stepping South from (27, 6) landed directly onto (27, 7) without jumping, confirming it is an open pathway connecting the upper terrace to the lower tier.
- Eastern Road (Cols 28..37, Rows 8..9): Wide 2-tile tall open clear-ground road running East past column 37 toward Mt. Moon.
- Eastern Ledge & Ramp (37, 7): Empirically verified passable ramp. Stepping North from (37, 8) stepped through (37, 7) onto the upper terrace at (37, 6), connecting the lower road to the upper highway.
- Far Eastern Highway (Cols 38..47, Rows 4..6): Wide continuous open green highway running east past column 47 toward the Mt. Moon entrance courtyard.
- Far Eastern Mountain Spur (Col 50): Solid mountain cliff blocks eastward passage on rows 3..7.
- Far Eastern Ramp (49, 7): Empirically verified 2-way passable ramp (ascended North from (49, 10) through (49, 7) to (49, 6)). Connects lower bypass road to the upper highway.
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
- Couch NPC (0, 4): Resident who advises: "If you have too many POKéMON, you should store them via PC!".
## Cave & Landmarks
- Mt. Moon Cave Entrance: Located at (18, 5). Cave mouth set into the north cliff face, entered from (18, 6) facing North.
- Route 4 Signpost: Located at (17, 7).


<hr>

<h1><code>Locations/Kanto_MtMoon_1F</code></h1>

# Mt. Moon 1F Geography & Exploration

## Connections
- South Exit: Warp at (14, 35) leading outside to Route 4.
- Ladder (13, 27): Ladder descending to basement chamber (empirically verified warp).
- Ladder (17, 11): Ladder in north-central corridor.

## Layout & Corridors
- Entrance Corridor (Cols 14..15, Rows 31..35): 2-tile wide north-south cave passage bounded by rock walls at cols 10..13 (west) and cols 16..19 (east).
- Main Cavern Junction (Rows 27..29, Cols 10..15): Entrance corridor opens into a wide open cavern extending west toward columns 0..9 and north toward row 20+.
- Signpost (15, 23): Reads "Beware! ZUBAT is a blood sucker!".
- Bug Catcher Kent (16, 23): Stationed at (16, 23) facing South down column 16.
- Northern Boundary Wall (Rows 20..21): Solid rock wall blocking northward travel above junction (cols 10..19).
- Western Cavern Corridor (Cols 0..13, Rows 22..29): Wide open cavern passage leading west toward items and northwest ladder.
- Ground Item (5, 32): TM12 (WATER GUN) collected.
- Ground Item (2, 20): POTION collected.
- East-West Cross Corridor (Row 22, Cols 10..21): Clear passage running east above Bug Catcher Kent (16, 23) connecting the central junction to the eastern avenue.
- Eastern North-South Avenue (Cols 20..21, Rows 18..25+): 2-tile wide vertical corridor bounded by eastern rock wall (Col 22) and central pillar (Cols 18..19). Runs north past row 18 toward the northeast caverns and ladders.
- Central Rock Pillar (Cols 18..19, Rows 8..21): Massive rock pillar separating Eastern Avenue (cols 20..21) from Western Avenue (col 17). Bypassed to the south via East-West Cross Corridor (Row 22) or to the north via Row 7 corridor.
- Ladder (17, 11): Located in Western Avenue along column 17, accessed from the south via row 22 cross-corridor.
- Eastern Avenue (Cols 24..27, Rows 11..27): Wide 4-tile north-south thoroughfare connecting southern bypass (rows 26..27) directly north to row 11 corridor. Note: (25, 15) is regular floor (empirically verified on Turn 1184).
- Northern Corridor (Row 11, Cols 17..30+): East-west corridor connecting Eastern Avenue, Ladder (21, 17) via column 21, and Ladder (17, 11).


<hr>

<h1><code>Locations/Kanto_MtMoon_Basement1</code></h1>

# Mt. Moon Basement (Entrance Ladder 13, 27 Chamber)

## Connections
- Ladder (15, 27): Ascending ladder leading back to Mt. Moon 1F at (13, 27) (empirically verified warp on Turn 1173).

## Layout & Geography
- Arrival Warp: Warped from 1F (13, 27) onto basement (13, 27) and automatically scripted 2 steps east to (15, 27).
- Southern Ridge/Plateau: Elevated cliff ridge spanning rows 28..30, cols 12..20. Lower speckled floor path runs along row 31.
- Western Corridor: North-south corridor along column 11 (rows 23..31).
- Main Northern Cavern (Cols 14..20, Rows 23..27): Wide open speckled cave floor extending north toward unexplored basement depths.
- Ground Item (25, 21): Item ball visible on elevated northern platform above row 23 ledge.
- Row 23 Ledge (Cols 24..25, Row 23): South-facing one-way ledge separating northern platform (rows 21..22) from southern floor (rows 24..27).
- Eastern Cavern (Cols 20..28+, Rows 24..27): Wide speckled cave floor extending east past column 28.
- Eastern Ridge (Cols 30..31, Rows 21..28): 2-tile wide impassable elevated cliff ridge separating central terrace from eastern corridor. Empirically verified impassable.
- Eastern Corridor (Cols 32..34, Rows 22..29+): Open cave floor running north-south east of the ridge.

## NPCs & Trainers
- Team Rocket Grunt: Stationed at (15, 24) facing South. Line of sight triggers when walking north on column 15 at (15, 25).
  - Team: 3 Pokémon (Sandshrew Lv 11, Rattata Lv 11, Zubat Lv 11).
  - Status: Defeated.

- Western Ledge (Cols 12..13, Rows 21..28): 2-tile wide elevated ridge with east-facing jump ledge at column 13. Empirically verified impassable from east (bumped at (13, 25) from (14, 25)).
- Room Connectivity: Ladder at (15, 27) is a visible candidate exit to Mt. Moon 1F.


<hr>