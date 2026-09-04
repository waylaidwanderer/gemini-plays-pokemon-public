<h1><code>Main</code></h1>

# Pokémon Blue - Journey Log

## Status
- Badges: 1 / 8 (Boulderbadge)
- Active Team: Squirtle (SHELDON) Lv 13
- Money: ¥2331
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
- [x] Traverse Route 2 & Viridian Forest to Northern Gatehouse [Turn 485]
- [x] Reach Pewter City [Turn 495]
- [x] Defeat Pewter Gym Leader Brock [Turn 594]
- [ ] Traverse Route 3 and reach Mt. Moon

<hr>

<h1><code>Inventory</code></h1>

# Inventory Log

## Items
- TOWN MAP
- POKé BALL x6
- POTION x2
- ESCAPE ROPE x1
- ANTIDOTE x2
- TM34 (BIDE)

## Key Items
- POKéDEX

## Money
- ¥2331

## Party Pokémon
- SQUIRTLE (Nickname: SHELDON) [Lv 13, Water]
  - Status: Healthy
  - HP: 35 / 35
  - Stats: Attack 20, Defense 25, Speed 20, Special 21
  - Moves: Tackle (PP 35/35), Tail Whip (PP 30/30), Bubble (PP 30/30)


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
- Move Execution Order: Strictly determined by Speed stat under neutral conditions. Higher Speed acts first. When Speed stats are identical (Speed tie), turn priority is resolved randomly (50/50) each turn (empirically confirmed Turns 456 & 458: Sheldon at Speed 15 and Trainer Weedle Lv 9 alternated move priority under neutral conditions, demonstrating an empirical Speed tie).
- In-Battle Item Priority: Bag item usage (e.g. Potion) possesses top execution priority (+1 priority), resolving at the beginning of the turn before any Pokémon moves, irrespective of Speed.
- Item Effects: Potion restores exactly 20 HP to the designated Pokémon.
- Potion Tactical Doctrine: Conserve Potions unless active Pokémon HP <= 5 and opponent possesses lethal KO potential on the current turn. When HP <= 5 and enemy attack cannot be prevented by outspeeding and knocking out the target, item priority ensures 100% survival.

## Battle Menu & Cursor Memory
- Move Selection Cursor Memory: During consecutive attack turns within a single battle, the move menu cursor retains its position from the previously confirmed attack (e.g. executing Bubble from Slot 3 leaves the cursor at Slot 3 on the following turn). It does NOT automatically reset to Slot 1.
- Testing Boundary: Empirically verified across consecutive attack turns with Bubble, Tail Whip, and Tackle, AND verified to persist after navigating through the ITEM submenu to use a Potion (Turn 399). Behavior after PKMN submenu or aborting actions remains unverified.
- Battle Initialization Reset: At the start of a new battle, the move selection cursor resets to Slot 1 (Tackle), regardless of what move was used in previous encounters. Verified on Turn 437.
- Main Battle Menu Cursor Memory: The primary 4-choice battle menu (FIGHT, PKMN, ITEM, RUN) retains its position from the previously confirmed action. Specifically, using an Item leaves the cursor on ITEM on subsequent turns, rather than resetting to FIGHT. Verified on Turn 566.
- Battle Move Menu Layout: The 4 moves are arranged in a single vertical 4-line list (Slot 1 at top, Slot 2 second, Slot 3 third, Slot 4 fourth), NOT a 2x2 grid. Pressing "Down" from Slot 1 moves to Slot 2, not Slot 3. To reach Slot 3 from Slot 1 requires pressing "Down" twice.

## Stat Stage Modifiers
- Tail Whip: Decreases target Defense by 1 stage per application (Stage -1 = approx. 2/3 Defense, Stage -2 = approx. 1/2 Defense). Verified: Lv 6 Weedle took 11-12 damage from Tackle at -1 Defense vs ~6-8 at neutral Defense.
- Bubble Secondary Effect: Has a chance to lower target Speed by 1 stage (observed to drop enemy Weedle's Speed on Turns 381, 385, and 462).
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
  - Bubble vs Lv 11 Diglett (Ground, Special ~16): Deals 20-22 damage (observed Turns 557-558: took Diglett from 100% to ~2 HP).
  - Bubble vs Lv 11 Sandshrew (Ground, Special ~15): Deals 16-18 damage (~50% max HP, observed Turn 569).
  - Enemy Diglett Lv 11 Scratch vs Defense 20: 5 damage on normal hit (Turn 551), 8 damage on critical hit (Turn 556).
  - Enemy Sandshrew Lv 11 Scratch vs Defense 22: 9 damage on critical hit (Turn 566).
- Enemy Offensive Damage Bounds against Sheldon (Defense 17):
  - Wild Route 1-2 targets (Lv 3-4 Pidgey Gust / Rattata Tackle): 3-4 HP damage.
  - Forest Bug Pokémon (Lv 6 Weedle Poison Sting / Caterpie Tackle): 2-3 HP damage (Critical hit deals ~4 HP).
  - Status Affliction Risk: Poison Sting inflicts Poison on hit (~20-30% chance). Poison deals periodic 1/16 max HP damage in battle and 4 HP every 4 overworld steps.

## Experience & Growth Curves
- Level Milestones:
  - Level 7: 318 EXP
  - Level 8: 482 EXP (Learns Bubble, fills Slot 3)
  - Level 9: 703 EXP
  - Level 10: Max HP 29, Attack 17, Defense 20, Speed 17, Special 17 (reached on Turn 466)
  - Level 11: Max HP 31, Attack 18, Defense 22, Speed 18, Special 19 (reached on Turn 561)
  - Level 13: Max HP 35, Attack 20, Defense 25, Speed 20, Special 21 (reached on Turn 594)

## Defeat Yields
- Wild Rattata Lv 3: 24 EXP | Lv 4: 32 EXP
- Wild Pidgey Lv 3: 23 EXP | Lv 4: ~23-28 EXP
- Trainer Weedle Lv 6: 66 EXP
- Trainer Caterpie Lv 6: ~66 EXP
- Trainer Weedle Lv 9: 99 EXP
- Trainer Diglett Lv 11: 190 EXP
- Trainer Sandshrew Lv 11: 219 EXP
- Leader Geodude Lv 12: 220 EXP
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
- South: Southern gatehouse from Route 2; player enters at (17, 47) [Turn 335].

## Verified Geography & Landmarks
- Southern Entry Corridor (Rows 44..47): Open path across columns 15..18, bounded by stone posts at columns 14 and 19.
- Signpost (18, 45): Trainer Tips - "Weaken POKéMON before attempting capture! When healthy, they may escape!" [Turn 337]
- Resident/NPC (16, 43): Youngster warns "I came here with some friends! They're out for POKéMON fights!" [Turn 338]
- Main South-Central Avenue (Rows 36..40): 2-tile wide clear path along columns 16..17 flanked by tall grass (col 15 and 18) and stone posts (col 14 and 19). Completely avoids grass encounters.
- Signpost (16, 32): Trainer Tips - "For poison, use ANTIDOTE! Get it at POKéMON MARTs!" [Turn 345]
- Western Maze Passage (Rows 32..33): Avenue terminates at row 31 tree wall; path branches west through tall grass opening at rows 32..33 into the western forest maze.
- Ground Item (12, 29): Visually confirmed item ball in an enclosed clearing north of row 30 trees [Turn 346]. Traversal of northern corridors (columns 11-13, 16-18, 25-26) confirmed no northern breach into this clearing; it remains isolated from the main paths (likely requires Cut or alternative access).
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
- Eastern Notice Signpost: Located at (33, 19) at the eastern exit road to Route 3. Reads: "NOTICE! Thieves have been stealing POK�MON fossils at MT. MOON! Please call PEWTER POLICE with any info!".

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
- Western Entrance (Rows 8..11, Cols 0..1): 4-tile wide open ground passage connecting to Pewter City, bounded by solid mountain cliff walls to the north (rows 6..7) and south (rows 12..14).
- First Tall Grass Field (Rows 8..11, Cols 2..5+): Tall grass spans across columns 2 to 5+. Stone boundary posts located at (4, 8) and (4, 11). Rows 9 and 10 provide continuous east-west passage through the grass field.

- Shrub Obstacles (Col 9): Small trees at (9, 10) and (9, 11) block row 10..11; bypass via tall grass at (9, 8..9).
- Terraces & Ledges:
  - Upper tier: Row 6..7 bounded by south ledge at row 7 (cols 10..13).
  - Middle tier: Rows 8..10 tall grass (cols 10..13).
  - Lower tier: Rows 12..13 tall grass, south of row 11 ledge.
- Trainer (10, 6): Stationed on upper tier at (10, 6) facing South behind row 7 ledge (cannot engage from below).
- Lass (16, 9): Stationed at (16, 9) facing West across row 9 middle corridor. Line of sight triggers at (14, 9).
- Shrub Barrier (Col 17): Vertical column of small trees at column 17 (rows 7..11) separating middle grass field from eastern Route 3.
- Upper East Trainer: Stationed at (18, 5..6) in blue outfit.

<hr>