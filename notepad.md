<h1><code>Main</code></h1>

# Pokémon Blue Playthrough Dashboard

## Main Objectives
- [x] Choose first Pokémon (Turn 81 - Squirtle!)
- [x] Reach Viridian City Poké Mart to get Oak's Parcel (Turn 247)
- [x] Deliver Oak's Parcel to Professor Oak (Turn 461)
- [x] Get Pokédex from Professor Oak (Turn 464)
- [x] Get Town Map from Daisy in Pallet Town (Turn 507)
- [x] Return to Viridian City to buy Poké Balls (Turn 825)
- [x] Capture additional wild Pokémon (Pidgey, Rattata, etc.) to build our team
- [x] Navigate north through Route 2 and enter Viridian Forest Gatehouse (Turn 2082)
- [x] Explore Viridian Forest to find and capture Caterpie (Turn 2125)

## Directory
- `Locations/PalletTown` - Permanently verified Pallet Town location records.
- `Locations/Route1` - Permanently verified Route 1 connections and layout features.
- `Locations/ViridianCity` - Permanently verified Viridian City connections and buildings.
- `Mechanics/General` - Verified game mechanics and controls.
- `Scratchpad/ViridianForest_Grinding` - Active grinding, switch-training, and leveling preparation in Viridian Forest.

<hr>

<h1><code>Archive/GameStartIntro</code></h1>

# Game Start Intro Archive
- Turn 0 (11:43 AM): Title screen of Pokémon Blue Version visible. Gengar and Red are on the screen.
- Plan:
  1. Press Start to access the main menu.
  2. Select "NEW GAME".
  3. Name the Player.
  4. Name the Rival.
- Turn 1: Screen shows main menu with cursor on 'NEW GAME'. Pressing A to start.
- Turn 3: Professor Oak's intro has begun. Naming plan: Player = GEM, Rival = BLUE. Pressing A to advance dialogue.
- Turn 5: Screen shows 'Welcome to the world of POKéMON!'. No down arrow visible. Pressing A to advance to the next screen.
- Turn 6: Screen shows 'My name is OAK! People call me' with a down arrow (▼). Pressing A to advance.
- Turn 7: Dialogue is at 'People call me the POKéMON PROF!' with no down arrow. Pressing A to advance.
- Turn 8: Dialogue says 'This world is inhabited by' with Nidorino on screen. There is no down arrow. Pressing A to advance.
- Turn 9: Screen shows 'inhabited by creatures called'. The harness is in dialogue mode. Wait, there is no down arrow on the current screenshot, but there was a down arrow after 'called' in standard dialogue. Let's see what the next text is. Pressing A to advance the dialogue.
- Turn 10: Screen is white (fade transition). Intermediate state shows 'creatures called POKéMON!' text was advanced. Now fading to the next dialogue. Pressing A.
- Turn 11: Screen shows 'For some people, POKéMON are' with a down arrow (▼). Nidorino is still on screen. Pressing A to advance.
- Turn 12: Screen shows 'For some people, POKéMON are' with a down arrow (▼). Nidorino is on screen. Pressing A to advance the dialogue.
- Turn 13: Screen shows 'pets. Others use' with a down arrow (▼) and Nidorino on screen. Pressing A to advance the dialogue.
- Turn 14: Screen shows 'pets. Others use them for fights.' with down arrow (▼). Pressing A to advance dialogue.
- Turn 15: Screen shows 'Myself...' with no down arrow. This is the transition to naming ourselves. Pressing A to proceed.
- Turn 16: Dialogue shows 'I study POKéMON as a profession.' with no down arrow, and Nidorino is still on screen. Pressing A to advance the dialogue.
- Turn 17: Screen shows 'I study POKéMON as a profession.' with no down arrow, and Nidorino is still on screen. Pressing A to advance the dialogue.
- Turn 18: Screen shows 'First, what is your name?' with down arrow (▼). Pressing A to go to the naming menu.
- Turn 19: Character name selection screen is displayed. Options:
  - ▶NEW NAME
  - BLUE
  - GARY
  - JOHN
  Preparing to select 'NEW NAME' to input our custom name 'GEM'. Cursor is currently at 'NEW NAME'. Pressing A.
- Turn 22: Keyboard screen for character name entry is loaded. The cursor is currently pointing to 'A' at (0, 4).
  Plan to spell 'GEM' and select 'END' (ED):
  1. To 'G' (6, 4): Press Right 6 times, then A.
  2. To 'E' (4, 4): Press Left 2 times, then A.
  3. To 'M' (3, 5): Press Left 1, Down 1, then A.
  4. To 'ED' (8, 8): Press Right 5, Down 3, then A.
  Sequence to execute: ['Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'A', 'Left', 'Left', 'A', 'Left', 'Down', 'A', 'Right', 'Right', 'Right', 'Right', 'Right', 'Down', 'Down', 'Down', 'A']
- Turn 28: Player name 'GEM' is confirmed by Oak! Screen says 'Right! So your name is GEM!'. Pressing A to continue.

<hr>

<h1><code>Mechanics/General</code></h1>

# General Mechanics & Controls
- Verified basic game mechanics, controls, and UI behaviors.

## Battle Mechanics:
- Turn-based combat. First starter battle triggers immediately after selecting starter and rival picking theirs.
- Lead Pokémon (first slot) is automatically sent out first.
- HP (Hit Points) represents health. Our starter SQUIRTLE (GEMMY) starts with 20 max HP.
- Moves have PP (Power Points) representing usage limits. SQUIRTLE's Tackle has 35 PP, Tail Whip has 30 PP.

## Overworld Navigation:
- PC in player's room can store items. Potion withdrawn on Turn 62 successfully.
- Warps (stairs, doors) transition between maps and are activated by walking onto them.

## Ledge Mechanics:
- Ledges (TYPE_44f6) are one-way drop-offs.
- Verified on Turn 262: Moving South (Down) from (10, 4) to (10, 6) over a ledge at (10, 5) successfully jumps over the ledge.
- Moving North (Up) against a ledge is impassable.

## Pokémon Center Counter Mechanics:
- Test 4: Left Counter Tile Interaction Check
  - **Hypothesis**: The player can interact with Nurse Joy from (3, 3) facing Up (the left counter tile) to heal their Pokémon, bypassing the blocking NPC at (4, 3).
  - **Methodology**:
    - Turn 1679: Standing at (3, 3) facing Up.
    - Action: Press 'A' to interact with the counter directly above us at (3, 2).
    - Verification: Check if Turn 1687 state shows the Pokémon Center healing dialogue on screen.
  - **Results**:
    - Turn 1687: Successfully verified! The screen shows "Shall we heal your POKéMON?" and the interactive menu `▶HEAL / CANCEL` is open, with the cursor pointing at `▶HEAL`.
    - **Conclusion**: Confirmed! In Generation 1, you can talk to Nurse Joy and heal your Pokémon from the left counter tile (3, 3) facing Up. You do not need to stand in the center (4, 3). This is an incredibly useful mechanic to bypass any NPC blocking the center counter spot.

## Verified Route 2 Mechanics:
### Test 1: Red Flower Tile Collision Check
- **Hypothesis**: Red flower tiles (visually red flowers, system tile type `TYPE_3fe2`) are passable and do not block player movement.
- **Results**: Verified on Turn 1042. Player successfully moved from (4, 66) to (5, 66) (a red flower tile). Red flower tiles are passable.

### Test 2: Route 2 Southern Tall Grass Patch Wild Encounters Check
- **Hypothesis**: Tall grass tiles (TYPE_3fe2) in the southern portion of Route 2 (Columns 8 & 9, Rows 61-67) contain wild Pokémon encounters.
- **Results**: Completed on Turn 1411. Player took 42 cumulative steps on these tiles between Turn 1052 and Turn 1411 without triggering a single wild encounter. Consistently negative. Encounters on this specific grass patch are either disabled or extremely rare.

### Test 3: Route 2 Northern Tall Grass Patch Wild Encounters Check
- **Hypothesis**: The TYPE_fed7 tall grass patch (starting at Y=51, Columns X=4 to X=9) contains active wild encounters.
- **Results**: Completed on Turn 1554. On Turn 1537, at 13 cumulative steps, we triggered a wild Level 4 PIDGEY encounter (captured as BIRBIE). The northern tall grass patch contains active wild encounters.

<hr>

<h1><code>Locations/PalletTown</code></h1>

# Pallet Town Location Records
- Permanently verified map connections, buildings, and POIs in Pallet Town.

## GEM's House:
- Upstairs (GEM's Bedroom - Map 0_38):
  - Starting position: (3,6) facing Up.
  - TV/SNES at (3,5) (TYPE_2889). Bed at (3,4) (TYPE_2889).
  - GEM's PC at (0,1) (adjacent (0,2)), containing 1 POTION. Potion withdrawn on Turn 63.
  - Dresser at (0,6) (TYPE_2889).
  - Stairs down at (7,1) (TYPE_fed7).
- Downstairs (GEM's Living Room - Map 0_37):
  - Stairs up at (7,1) (TYPE_fed7).
  - GEM's Mom is seated at (5,4) (TYPE_3fe2).
  - Table with tea at (3,4) and (4,4) (TYPE_2889).
  - TV/cabinet at (3,5) and (4,5) (TYPE_2889).
  - Front door exit at (2,7) and (3,7) (TYPE_3fe2 warp mat).

## Overworld (Pallet Town - Map 0_0):
- GEM's House Front Door: (5,5) (exits to (5,6)).
- Northwestern boundary: Impassable fence at Row Y=1 (from X=0 to X=7).
- Route 1 Entrance (North exit): Located at Column X=10 and X=11, Row Y=0 (tall grass trigger).
- Blue's House Front Door: (13,5) (exits to (13,6)).
- Oak's Lab Entrance Door: (12,11) (exits to (12,12)).

<hr>

<h1><code>Locations/Route1</code></h1>

# Route 1 Location Records
- Permanently verified map connections, layout features, and key points of interest on Route 1.

## Connections:
- South exit connects to Pallet Town (Map 0_0) at Route 1 Column X=10 and X=11 (Row Y=35).
- North exit connects to Viridian City (Map 0_1) at Route 1 Column X=10 and X=11 (Row Y=0).

## Layout & Spatial Features:
- Between Y=35 and Y=32: A narrow corridor of tall grass (TYPE_fed7) flanked by impassable fences (TYPE_2889) at X=9 and X=12.
- At Y=31: A clear path (TYPE_3fe2) begins.
- At Y=27: A one-way southward ledge (TYPE_44f6) blocks straight north movement on Columns X=10 to X=15.
- Row Y=27 Ledge:
  - Northbound Bypass: Walk Left to Column X=8 (clear path at (8,31) and (8,30)), then proceed north through Columns X=6, X=7, or X=8.
  - Southbound Bypass: Jump directly south over the ledge from Column X=4 (Turn 341).
- Row Y=5 Ledge:
  - Northbound Bypass: The Row 5 ledge (TYPE_44f6) blocks Columns X=6 to X=13. Columns X=14 and X=15 are completely open clear path (TYPE_3fe2) at (14,5) and (15,5). To bypass, walk Right to Column X=14 or X=15, and head north to Viridian City.
  - Southbound Bypass: Jump directly south over the ledge from (10,4) to (10,6) (Turn 262).

## Key Interactions & POIs:
- Poké Mart Clerk NPC: Located at (5, 24). Talked to him on Turn 182 and received a free POTION.
- Wild Pokémon: Tall grass contains wild Pidgey and Rattata (verified Turn 194). SQUIRTLE leveled up to Level 7 here.

<hr>

<h1><code>Locations/ViridianCity</code></h1>

# Viridian City Location Records
- Permanently verified map connections, buildings, and POIs in Viridian City.

## Connections:
- South exit connects to Route 1 (Map 0_12) at Viridian City Column X=20 and X=21 (Row Y=35).
- North exit leads towards Route 2 / Viridian Forest.
- West exit leads to Route 22.

## Key Buildings & POIs:
- Pokémon Center: Located on Columns X=22 to X=24, with its entrance door at (23, 25).
- Trainer School: Located on Columns X=20 to X=23, rows Y=14 to Y=15, with its entrance door at (21, 15). Inside (Map 0_43), there is a student at (3, 5) and teacher at (4, 1).
- Poké Mart: Located on Columns X=29 to X=32, rows Y=17 to Y=19, with its entrance door at (29, 19) and "MART" sign at (30, 19).
  - Inside (Map 0_42), the clerk at (1, 4) hands over OAK's PARCEL (delivered on Turn 461) and subsequently sells standard items.
  - Verified Shop Inventory (Turn 832):
    1. POKE BALL (¥200)
    2. ANTIDOTE (¥100)
    3. PARLYZ HEAL (¥200)
    4. BURN HEAL (¥250)
    5. CANCEL
  - Note: Potions are NOT sold at the Viridian City Poké Mart.
- Map Layout & Points of Interest:
  - Viridian Gym: Located in the northeastern section of the city. Doors are locked, and the gym leader is currently away.
  - Old Man: Located in the northern part of the city. He initially blocks the path to Route 2, complaining about not having his coffee. After delivering Professor Oak's Parcel, he is no longer blocking the road and can teach the player how to catch Pokémon.
  - Center Pond: A large water pond is located in the center of the city.
  - Cut Tree: A small cuttable tree is located near the southern entrance, which can be cut down once HM01 (Cut) is obtained.
  - Route Connections:
    - Route 1 Exit/Entrance: (20, 35) and (21, 35).
    - Route 2 Exit/Entrance: (18, 0).
    - Route 22 Exit/Entrance: (0, 18) and (0, 19).

<hr>

<h1><code>Archive/RouteToViridian_Turns521_557</code></h1>

# Route to Viridian Archive (Turns 521-557)
This archive preserves the turn-by-turn log of Gem's journey from Pallet Town back to Route 1 (up to column 8 positioning) with Squirtle at 12/24 HP.

- Pallet Town Phase (Turns 521-529): Successfully navigated from Blue's House at (13, 6) through Pallet Town northwards to the Route 1 transition at (10, 0) with Squirtle at 12/24 HP. We prepared the route, bypassed obstacles, and entered the tall grass of Route 1.
- Turn 536: Arrived on Route 1 at (10, 35). Verified screen layout matches our records. Fences block Left (9, 35) and Right (12, 35). Straight north is tall grass (TYPE_fed7) from Y=35 to Y=32. Y=31 is a clear path (TYPE_3fe2).
  Plan: Move Up to (10, 31). Steps:
  1. Up to (10, 34)
  2. Up to (10, 33)
  3. Up to (10, 32)
  4. Up to (10, 31)
- Turn 538: Successfully stepped north to Route 1 (10, 34). No wild encounter. Facing north. SQUIRTLE's health remains 12/24 HP. Moving north to (10, 33).
- Turn 541: Arrived at Route 1 (10, 33). No wild encounter. SQUIRTLE health at 12/24 HP. Preparing to move north to (10, 32).
- Turn 543: Successfully moved Up to (10, 32). No wild encounter. Facing north. Ready to step onto the clear row at (10, 31). SQUIRTLE's health is 12/24 HP.
- Turn 545: Position (10, 32), facing north. SQUIRTLE's HP is 12/24. Verified Row 31-28 layout.
  Plan to bypass the Row 27 ledge (which blocks columns 10-15):
  1. Move Up to (10, 31).
  2. Move Left to (9, 31) and then (8, 31).
  3. Move Up to (8, 30), then (8, 29), and (8, 28).
  This will put us at (8, 28) facing north, clear of the ledge on columns 10-15.
- Turn 548: Position (10, 32), facing north. SQUIRTLE HP is 12/24. Ready to move Up to (10, 31) to reach the clear path.
- Turn 553: Successfully reached (10, 31) on Route 1. Facing north. SQUIRTLE is at 12/24 HP. Bypassing the ledge at Row 27 requires moving Left to (8, 31). Ready to execute.
- Turn 557: Arrived at Route 1 (8, 31) successfully. Facing left. SQUIRTLE's health is 12/24 HP. Moving Up to (8, 30), which is clear path.
- Turn 567: Arrived at Route 1 (8, 30) successfully. No wild encounter. SQUIRTLE's health is 12/24 HP. Moving Up to (8, 29), which is tall grass (TYPE_fed7).
- Turn 572: Performing active steps to break execution stagnation. SQUIRTLE at 12/24 HP. Preparing to step north to (8, 29).
- Turn 580: Arrived at Route 1 (8, 28) facing North. SQUIRTLE's health is 12/24 HP. Bypassed the tall grass corridor! Ready to move Up to (8, 27), which is a clear path.
- Turn 586: Position (8, 27), facing north. SQUIRTLE's health is 12/24 HP. Bypassed the row 27 ledge. Looking ahead to row 23, column 8 is blocked by TYPE_2889 (stone block/fence). We must walk Right to column 12 to pass row 23 through tall grass.
  Plan:
  1. Move Up 3 steps to (8, 24).
  2. Move Right 4 steps to (12, 24).
  3. Move Up 2 steps to (12, 22).
- Turn 601: Position (12, 24), facing north. SQUIRTLE's health is 12/24 HP. Successfully walked Right 4 steps to reach Column 12 on Turn 595, positioning us in front of the Row 23 grass passage. Now moving Up 3 steps to reach the clear path at (12, 21).
- Turn 608: Position (12, 21), facing north. SQUIRTLE's health is 12/24 HP. No wild encounters. Preparing to execute the Row 19 ledge bypass by moving Left 3 steps to Column 9, then Up 4 steps to (9, 17).
- Turn 612: Position (9, 17) facing north. SQUIRTLE's health is 12/24 HP. Analyzed layout for Row 13 barrier: columns 5 to 9 are blocked by ledges (TYPE_44f6) or obstacles, and columns 10 to 13 are blocked by stone blocks (TYPE_2889). Column 14 has tall grass (TYPE_fed7) which is open and passable at Row 13.
  Plan to proceed north:
  1. Move Right 5 steps to (14, 17) [TYPE_3fe2].
  2. Move Up 1 step to (14, 16) [TYPE_3fe2].
  3. Move Up 3 steps to (14, 13) [TYPE_fed7 - tall grass] and step beyond Row 13 to (14, 12).
- Turn 627: Standing at (14, 17) facing Left. SQUIRTLE is at 12/24 HP. No wild encounters. Clerk NPC (SPRITE_853c) has wandered to (15, 13) which leaves Column 14 at Row 13 completely open!
  Immediate action: Move Up to (14, 16) [TYPE_3fe2 - clear path, no encounter risk] to turn north and establish our position on Column 14.

<hr>

<h1><code>Scratchpad/WildCaptures_Route2</code></h1>



<hr>

<h1><code>Locations/Route2_Gatehouse</code></h1>

# Route 2 Gatehouse (Map 0_50) Location Records
- Permanently verified map connections, layout, and NPCs in the Route 2 Gatehouse.

## Connections:
- Southern warp connects to Route 2 (Map 0_13) at (3, 43).
- Northern warp connects to Viridian Forest.

## Layout & Spatial Features:
- Standing at (4, 2) facing Up.
- Column X=4 is a completely open, clear checkered path running north-south from the southern door at (4, 7) straight through to the northern side.
- Counter desks are located on the east side around Row Y=3.
- Exit to Viridian Forest is located at (5, 0) of TYPE_3fe2.

## NPCs:
- Scientist/Aide NPC located around (2, 4) on the west side.
- Blue-haired female trainer NPC located at (8, 4) facing Down.

## Route 2 Northern Gatehouse Map Transition (Turn 3675):
- **Warp Connection**: Successfully stepped UP from (1, 0) on Map 0_51 (Viridian Forest) to transition north into the Route 2 Gatehouse (Map 0_47).
- **Current Position**: Standing at (4, 7) facing UP inside the Gatehouse.
- **Physical Layout**:
  - The Gatehouse is a 10x8 grid (X from 0 to 9, Y from 0 to 7).
  - Row Y=7 is the southern entrance/exit leading back to Viridian Forest at (4, 7) / (5, 7).
  - An NPC (likely a Scientist) is standing at (2, 5).
  - The northern exit leading to Route 2 (Pewter City side) is at the top of the room.
- **Immediate Plan**: Walk north through the gatehouse, talk to the NPC at (2, 5) to see if they offer any helpful items or dialogue, and then exit north onto Route 2.

<hr>

<h1><code>Locations/ViridianForest</code></h1>

# Viridian Forest (Map 0_51) Location Records

## Connections:
- Southern entrance connects to Route 2 Gatehouse (Map 0_50) via warp at (17, 47) / (18, 47) area.

## Layout & Spatial Features:
- Entrance area:
  - Gatehouse exit is situated around (17, 47).
  - (17, 46) is blocked by a signpost/tree (TYPE_2889).
  - There is a clear path leading Left to (16, 47) then Up along column 16.
  - An NPC is standing at (16, 43) facing Down.

## NPCs & Interactions:
- NPC at (16, 43): Wearing a blue cap. Facing Down near the entrance. (Status: Interacted on Turn 2104. Dialogue: "I came here with some friends! They're out for POKéMON fights!")
- Friendly Bug Catcher NPC at (27, 40): Standing near the southern grass patch. (Status: Interacted on Turn 3377. Dialogue: "Ssh! You'll scare the bugs away!")
- Bug Catcher Trainer at (27, 33): Challenged player on Turn 3385. (Status: Defeated on Turn 3415. Money reward received, player's cash now ¥1135.)
- Bug Catcher Trainer at (30, 19): Spotted player and walked to (27, 19) on Turn 3437. (Status: Defeated on Turn 3487. Money reward received, player's cash now ¥1205.)

<hr>

<h1><code>Archive/Route2_GrindingHistory</code></h1>

# Scratchpad: Wild Captures and Leveling Goals (Archived from Route 2)

## High-Level Strategy:
- Active Grinding Phase (Started Turn 910)
- Pivot Strategy (Turn 1411): After 42 cumulative steps on Route 2 Columns 8 & 9 (Rows 61-67) with 0 encounters, we hypothesized that encounters on this specific grass patch might be disabled or extremely rare. We pivoted to the northern grass patch.
- Pivot Strategy (Turn 2072): After 60 cumulative steps on Route 2's northern tall grass patch with 6 encounters and 0 Caterpie, we conclude that Caterpie's encounter rate on Route 2 is too low to justify further time investment here. We are pivoting our primary search space north to Viridian Forest, where Caterpie has a significantly higher spawn rate in Pokémon Blue.

## Live Status:
- Turn 2077: SQUIRTLE (GEMMY) is at 14/26 HP (Level 8). BIRBIE (PIDGEY) is at 18/18 HP (Level 4). REMY (RATTATA) is at 16/16 HP (Level 4).
- Money: ¥1075.
- Inventory: 7 Poké Balls, 1 Antidote, 1 Town Map.
- Location: Route 2 (Map 0_13) at (9, 45) - Facing Up (Gatehouse in view).
- Grinding Phase 2: Pivoted.
  - Goal: Explore north to reach Viridian Forest to capture Caterpie.
  - Plan: Move Left 4 times to (5, 45), then Up once to (5, 44) to enter the Viridian Forest gatehouse warp.

## Active Team & Captures Checklist:
- [x] Pidgey (Level 4, Nickname: BIRBIE) - Status: Captured!
- [x] Rattata (Level 4, Nickname: REMY) - Status: Captured! (Turn 1940)
- [ ] Caterpie (Target Level 10 Butterfree) - Status: Not Captured (Pivoted search to Viridian Forest)
- [ ] GEMMY (SQUIRTLE) - Level 8 (Goal: Level 10)

## Route 2 Wild Encounters Strategy:
- Active Patrol: Completed. Tested southern patch (Columns 8 & 9, Rows 61-67, 42 steps, 0 encounters) and northern patch (Columns 4-9, Rows 48-51, 60 steps, 6 encounters: 4 Pidgey, 2 Rattata).

## Target Captures and Leveling Benchmarks:
1. Caterpie (Bug) -> Metapod (Bug) -> Butterfree (Bug/Flying):
   - Level range: 3-5
   - Strategy: Direct Poké Ball or minimal damage.
   - Purpose: Early evolution to Butterfree (Level 10) is extremely valuable because Butterfree learns CONFUSION at Level 12. Confusion deals super-effective damage to Rock/Ground types (like Geodude/Onix) in Pewter Gym, providing a massive tactical advantage!
   - Gamer Girl Nickname Ideas: FLUFFY, BUGGY, SILKY, BUTTERFLY.

## Pewter City Gym Preparation (Gym 1):
- Leader Brock uses Rock/Ground Pokémon (Geodude Level 12, Onix Level 14).
- Squirtle's Bubble/Water Gun (Water-type) is 4x super-effective against Geodude and Onix, making GEMMY our primary sweeper!
- Level 8 SQUIRTLE learns Bubble. Level 15 SQUIRTLE learns Water Gun.
- Goal: Train GEMMY to Level 10+ and secure a Butterfree/Pidgey support team before challenging the Gym.

## Summary of Journey:
- Turns 809-848: Entered Viridian Mart; purchased 10 Poké Balls and 1 Antidote.
- Turns 849-871: Bypassed Trainer School and moved Up Column 19 to (19, 12).
- Turns 872-895: Navigated past old man and transitioned to Route 2 (Map 0_13) at (8, 71).
- Turns 910-934: Patrolled Route 2 Columns 8 & 9. Verified tall grass tile graphics and prepared for wild captures.

## Grinding Cumulative Tally Tracking (Northern Tall Grass):
- **Grinding Run 2 (Completed Turn 2072)**:
  - Current Position: (9, 48) on Route 2.
  - Cumulative steps taken on tall grass: 60 (Turn 2072)
  - Encounters triggered: 6 (Level 3 PIDGEY on Turn 1829, Level 3 PIDGEY on Turn 1861, Level 5 PIDGEY on Turn 1878, Level 5 PIDGEY on Turn 1894, Level 4 RATTATA on Turn 1932, Level 2 RATTATA on Turn 2046)
  - Result 1: Defeated Level 3 Pidgey. GEMMY gained 23 XP, grew to Level 8, and learned BUBBLE! (Turn 1837)
  - Result 2: Successfully ran away to conserve HP. (Turn 1865)
  - Result 3: Successfully ran away to conserve HP. (Turn 1880)
  - Result 4: Successfully ran away to conserve HP. (Turn 1896)
  - Result 5: Successfully captured wild Level 4 RATTATA on Turn 1937! (Nicknamed REMY on Turn 1940)
  - Result 6: Encountered Level 2 RATTATA on Turn 2046. Successfully ran away on Turn 2049.
- Turn 2091: Arrived at Route 2 Gatehouse (4,2) facing Up. Preparing to exit north through (5,0) to enter Viridian Forest.

<hr>

<h1><code>Locations/Route2_Gatehouse_North</code></h1>

# Route 2 Northern Gatehouse (Map 0_47) Location Records
- Permanently verified map connections, layout, and NPCs in the Route 2 Northern Gatehouse.

## Connections:
- Southern warp connects to Viridian Forest (Map 0_51) at (4, 7) / (5, 7) area.
- Northern warp connects to Route 2 (Pewter City side) at the top of the room.

## Layout & Spatial Features:
- Standing at (4, 7) facing UP.
- Column X=4 is a clear path.
- An NPC is standing at (2, 5).

## NPC Investigations:
- NPC at (3, 2) (Youngster): "Many POKéMON live in forests" (Verified on Turn 3682).

<hr>

<h1><code>Locations/Route2_North</code></h1>

# Route 2 Northern Side (Map 0_13) Location Records
- Track connections, layout, and safety routes between the Northern Gatehouse and Pewter City.

## Connections:
- Southern entrance: Route 2 Gatehouse (North) door at (3, 15).
- Northern entrance: Leads directly into Pewter City (Map 0_03).

## Spatial Layout:
- Player exits gatehouse at (3, 11) facing UP.
- There is a patch of tall grass (TYPE_fed7) from X=0 to X=7 around Row Y=7.
- Safety Bypass: A clear path of TYPE_3fe2 exists at Column X=8, allowing us to walk around the tall grass to avoid wild encounters.
- Cuttable tree is located at (5, 10) (TYPE_5519).

<hr>

<h1><code>Archive/ViridianForest_Grinding</code></h1>

# Archived Scratchpad: Viridian Forest Grinding and Caterpie/Pikachu Capture
- Started: Turn 2110, Timestamp: Saturday, May 23, 2026 at 8:57 PM PDT
- Finished/Archived: Turn 3724

## Final Status at Archive:
- Turn 3724: Exited Viridian Forest and Route 2, entered Pewter City (Map 0_2) at (18, 35).
- SQUIRTLE (GEMMY): Level 11, HP: 4/32
- METAPOD (BUGGY): Level 8, HP: 3/28
- PIKACHU (SPARKY): Level 6, HP: 5/21
- PIDGEY (BIRBIE): Level 5, HP: 12/20
- RATTATA (REMY): Level 4, HP: 0/16 (Fainted)

## Grinding & Encounters Log:
- Target: Caterpie/Metapod/Kakuna.
- Location: Southernmost grass patch.
- Cumulative steps on grass: 92
- Encounters:
  - Encounter 1: Level 3 CATERPIE (Turn 2114). Decision: Throw Poké Ball. Captured, Nicknamed BUGGY.
  - Encounter 2: Level 5 METAPOD (Turn 2189). Switch-trained.
  - Encounter 3: Level 4 METAPOD (Turn 2801). Switch-trained to GEMMY. Bubble dealt ~25-30% damage, ignoring Defense boost.

## Switch-Training Strategy:
- Lead BUGGY, switch to GEMMY, defeat wild Pokemon. Safely shared EXP.

## Grinding Milestones & Summaries:
- Battle 6 (Turn 2617): Defeated wild Level 5 Metapod. BUGGY reached Level 6.
- Battle 7 (Turns 2656-2678): Defeated wild Kakuna. Shared EXP.
- Battle 8 (Turn 2795): Defeated wild Level 3 Caterpie. Shared EXP.
- Battle 9 (Turn 2810): Defeated wild Level 4 Metapod. Shared EXP.
- Battle 10 (Turn 2880): Defeated wild Level 3 Caterpie. Shared EXP.
- Battle 11 (Turns 3007-3011): Defeated wild Level 3 Caterpie. Shared EXP.
- Battle 12 (Turns 3026-3033): Defeated wild Level 4 Caterpie. Shared EXP.
- Battle 13 (Turns 3039-3047): Defeated wild Level 4 Caterpie. BUGGY reached Level 7 and evolved into METAPOD!
- Battle 14 (Turns 3064-3069): Defeated wild Level 3 Caterpie. Shared EXP.
- Battle 15 (Turns 3083-3089): Defeated wild Level 4 Caterpie. Shared EXP.
- Battle 16 (Turns 3110-3122): Defeated wild Level 4 Caterpie. Shared EXP.
- Battle 17 (Turns 3144-3153): Defeated wild Level 4 Kakuna. Shared EXP.
- Battle 18 (Turns 3161-3175): Captured Level 5 Pikachu (Sparky).
- Battle 19 (Turns 3220-3227): Defeated wild Level 4 Metapod. Shared EXP.
- Battle 20 (Turns 3438-3487): Defeated Bug Catcher trainer at (30, 19). Shared EXP. BUGGY reached Level 8, SPARKY Level 6.

## Viridian Forest North-South Corridor Spatial Layout (Turn 3599):
- Parallel vertical corridors mapped.
1. Westernmost Corridor (Column 2): Leads to exit gatehouse at (2, 1).
2. Middle-Left Corridor (Columns 6-8): Connected to Middle-Right at top (Row 1).
3. Middle-Right Corridor (Columns 11-13).
4. Eastern Corridor (Column 16): Runs south to entrance.

<hr>

<h1><code>Locations/PewterCity_Gym</code></h1>

# Pewter City Gym (Map 0_54) Location Records

## Connections:
- Southern exit door is at (4, 13) / (5, 13) which warps back to Pewter City (Map 0_2) at (16, 17).

## Layout & Spatial Features:
- Entrance area:
  - Player spawns at (4, 13) facing UP.
  - Pillars/statues are located on the left and right:
    - Left pillar: (3, 9) and (3, 10) of TYPE_2889.
    - Right pillar: (6, 9) and (6, 10) of TYPE_2889.
  - Central pathway: Columns 4 and 5 are open, clear paths of TYPE_3fe2 going north.

## NPCs & Interactions:
- Gym Guide: Standing at (7, 10). (Status: Not yet interacted).
- Gym Trainer: Standing at (3, 6) facing RIGHT. (Status: Defeated on Turn 3928. Reward: ¥220. GEMMY reached Level 12).
- Gym Leader Brock: Standing at (4, 1) (Status: Defeated on Turn 4083. Reward: Boulder Badge and TM34 Bide).

<hr>

<h1><code>Locations/PewterCity</code></h1>

# Pewter City (Map 0_3) Location Records

## Connections:
- South exit connects to Route 2 (Northern side) via map boundary transition.
- East exit connects to Route 3 (initially blocked by a Brock fan NPC, open after defeating Brock).

## Key Buildings & POIs:
- Pokémon Center: Located at (13, 25), inside Map 0_58. Healed team on Turn 3999. Left counter at (3, 3) facing UP. (🏥 marked)
- Pewter Gym: Located at (16, 17), inside Map 0_54. Exit at (4, 13). (🏋️ marked)
- Pewter Poké Mart: Located at (23, 17) (entrance door). (🏪 marked)
- Museum of Science: Located in the northern part of Pewter City. (Status: Not yet explored).

## Gym Leader Brock Defeated:
- Defeated on Turn 4083.
- Team:
  - GEODUDE (Level 12) - KO'd in 1 hit by GEMMY's Bubble (Critical hit!).
  - ONIX (Level 14) - KO'd in 2 hits by GEMMY's Bubble (used Bide, did nothing).
- Reward: Boulder Badge and TM34 (Bide).
- SQUIRTLE (GEMMY) reached Level 14. We took 0 damage in the gym!

## Verified Route around Pewter Gym:
- Bypassed the gym from the north side via Row 13 (columns 10 to 19) to reach the eastern corridor, then walked down column 19 to Row 26 (street level) and left to the Pokémon Center entrance at (13, 25).
- Note: A blocking NPC stands at (17, 25), and a fence covers (18, 18) to (18, 21), making the north-east direct route impassable, so the Row 13 bypass is the primary path.

<hr>

<h1><code>Scratchpad/Route3_MtMoon_Cerulean</code></h1>

# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 4171: Standing at (18, 26) in Pewter City. Grounding check on current screen overlay: verified the bypass path around the trees at column 21. Row 22 is completely passable (TYPE_3fe2). Walking Right 2, Up 4, and Right 3 steps to reach column 23 at (23, 22).

## Progression Roadmap & Checklist:
- [x] Defeat Pewter Gym Leader Brock (Boulder Badge & TM34 secured!).
- [x] Heal team at Pewter City Pokémon Center at (13, 25).
- [ ] Stock up on useful items at Pewter Poké Mart at (23, 17).
- [ ] Explore the Museum of Science (optional, northern part of town).
- [ ] Navigate east through Route 3 to Mt. Moon entrance.
- [ ] Traverse Mt. Moon to reach Route 4.
- [ ] Reach Cerulean City.

## Poké Mart Shopping Budget (¥2901 Cash):
- Goal: Stock up on crucial recovery items (especially Potions and Antidotes) and some Poké Balls for new captures on Route 3/Mt. Moon.
- Allocated Budget:
  - Potions (¥300 each): Buy 4 (¥1200) - highly needed for Mt. Moon.
  - Poké Balls (¥200 each): Buy 3 (¥600) - we have 4 currently, bringing us to 7.
  - Antidotes (¥100 each): Buy 3 (¥300) - critical for curing poison in Mt. Moon.
  - Paralyze Heal (¥200 each): Buy 1 (¥200) - optional utility.
  - Estimated Total Spend: ¥2300, leaving ~¥600 safety margin.
- Shopping Method:
  - Enter Mart at (23, 17), talk to clerk at (1, 4) or similar.
  - Buy listed items carefully and verify quantities before confirming.

<hr>