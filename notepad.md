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

<h1><code>Scratchpad/ViridianForest_Grinding</code></h1>

# Scratchpad: Viridian Forest Grinding and Caterpie Capture
- Started: Turn 2110, Timestamp: Saturday, May 23, 2026 at 8:57 PM PDT

## Current Status:
- Turn 3093: Successfully healed our team at the Viridian City Pokémon Center (Turn 2925). All Pokémon are at 100% HP with fully restored PP. Currently grinding at the southernmost grass patch of Viridian Forest.
- SQUIRTLE (GEMMY): Level 10, HP: 25/30. (Goal: Level 10+ for gym sweep - ACHIEVED!)
- PIDGEY (BIRBIE): Level 4, HP: 18/18.
- RATTATA (REMY): Level 4, HP: 16/16.
- METAPOD (BUGGY): Level 7, HP: 26/26. (Goal: Level 7 Metapod - ACHIEVED! -> Level 10 Butterfree -> Level 12 Confusion)
- Poké Balls: 6. Antidotes: 1.

## Grinding & Encounters Log:
- Target: Caterpie (highly wanted for Butterfree evolution!).
- Location: Southernmost grass patch (rows 40-41, columns 12-15 and 18-21).
- Cumulative steps taken on grass: 69
- Encounters:
  - Encounter 1: Level 3 CATERPIE (Turn 2114/2115). Decision: Throw Poké Ball directly at full health. (Captured, Nicknamed BUGGY)
  - Encounter 2: Level 5 METAPOD (Turn 2189). Decision: Switch-trained successfully. BUGGY gained 25 EXP.
  - Encounter 3: Level 4 METAPOD (Turn 2801). Decision: Switch-trained to GEMMY. Tested BUBBLE damage: BUBBLE on Turn 2807 dealt ~25-30% damage to METAPOD, completely ignoring its physical Defense boost from Harden. This empirical test confirms special moves are highly effective at bypass-clearing physical walls.

## Switch-Training Strategy:
- Lead: BUGGY (CATERPIE) in slot 1.
- Step 1: When a wild battle starts, select POKéMON.
- Step 2: Switch BUGGY out for GEMMY (SQUIRTLE).
- Step 3: Defeat the wild Pokémon with GEMMY's Tackle or Bubble.
- Step 4: BUGGY shares 50% EXP safely to reach Level 10 and evolve into Butterfree!

- Turn 2269: BUGGY has successfully reached Level 4! GEMMY's HP is down to 7/26. We will pause grinding and head back to the Viridian City Pokémon Center to heal.
- Turn 2279-2293 (Summary): Safely exited Viridian Forest, passed through Route 2 Gatehouse, and walked south along Route 2, successfully bypassing the northern grass patch and avoiding wild encounters with GEMMY at 7 HP.
- Turn 2294-2300 (Summary): Reached the southern ledge gap of Route 2 at (7, 61), successfully bypassed the ledge, walked down column 7 to (8, 71), and entered Viridian City on Turn 2301.
- Turn 2301-2310 (Summary): Arrived in Viridian City at (18, 0). Navigated down column 18 to row 4, and walked East to (18, 4). SQUIRTLE (GEMMY) remains at 7/26 HP. We are heading directly to the Pokémon Center to heal.
- Turn 2314-2337 (Summary): Navigated from (23, 4) down the west side of column 25, bypassed the Trainer School and row 13 fence via the column 19 fence gap, walked down column 19 to row 26, then headed east and entered the Pokémon Center door at (23, 25) on Turn 2336. Walked straight Up column 3 to standing on the left counter tile (3, 3) facing Up on Turn 2339.

## Brock Gym Battle Preparation & Strategy Checklist
- **Primary Goal**: Defeat Leader Brock at Pewter Gym.
- **Gym Team Composition & Roles**:
  1. **GEMMY (SQUIRTLE - Water)**: Level 10 (aiming for Level 10-12). Primary sweeper. Bubble deals 4x special damage to Brock's Rock/Ground types (Geodude and Onix), completely bypassing their massive physical Defense.
  2. **BUGGY (CATERPIE -> BUTTERFREE - Bug/Flying)**: Level 6 (aiming for Level 10+). Needs to reach Level 7 to evolve into Metapod, and Level 10 to evolve into Butterfree. At Level 12, Butterfree learns CONFUSION (Psychic), which deals high special damage and acts as an excellent backup against Brock.
  3. **BIRBIE (PIDGEY - Normal/Flying)**: Level 4. Gust deals wind-based special damage, used for clearing trainers or backup.
  4. **REMY (REMY - Normal)**: Level 4. Physical damage dealer with Tackle. Ineffective against Rock, but useful for chip damage or sacrifice if needed.

- **Leveling Targets before Gym**:
  - [x] GEMMY: Level 10+ (for sufficient HP/Special stats)
  - [ ] BUGGY: Level 10 (Evolve to Butterfree)
  - [ ] BUGGY: Level 12 (Learn Confusion)

## Switch-Training Optimization & Empirical Test Log
- **Purpose**: Safely train low-level BUGGY (CATERPIE) using high-level GEMMY (SQUIRTLE) as the active combatant.
- **Methodology (Verified on Turn 2252)**:
  - Lead with BUGGY (first slot).
  - Turn 1: On battle start, select PKMN, select GEMMY (slot 4), select SWITCH.
  - Turn 2: GEMMY enters the field. Use BUBBLE or TACKLE to defeat the opponent.
  - Result: Experience is divided 50/50 between BUGGY and GEMMY. BUGGY receives 18-25 EXP safely without taking any damage.
- **PP Management**: BUBBLE has 30 PP, TACKLE has 35 PP. Ensure GEMMY heals at the Pokémon Center when PP is low.

## Pewter Gym Intelligence & Battle Mechanics Guide
- **Gym Location**: Pewter City.
- **Gym Leader**: Brock (Rock/Ground Type Specialist).
- **Gym Leader Brock's Pokémon & Move Pools**:
  1. **GEODUDE (Level 12)**:
     - Type: Rock/Ground
     - Stats: High Defense, Low Special.
     - Known Moves: Tackle (Normal physical), Defense Curl (Raises Defense).
     - Strategy: GEMMY's Bubble deals 4x super-effective special damage, completely ignoring Geodude's high physical Defense. One or two Bubbles will easily knock it out.
  2. **ONIX (Level 14)**:
     - Type: Rock/Ground
     - Stats: Very High Defense, Low Special, Decent Speed.
     - Known Moves: Tackle (Normal physical), Screech (Sharply lowers Defense), Bide (Stores damage for 2-3 turns and returns double), Bind (Multi-turn physical trap).
     - Strategy: Bubble deals 4x super-effective special damage. Beware of Bide! If Onix uses Bide, DO NOT attack. Use Tail Whip, switch, or heal. Firing a Bubble while Bide is active is extremely dangerous as the double-damage counter will easily OHKO GEMMY.
- **Gym Junior Trainer♂**:
  - Pokémon: Diglett (Level 9), Sandshrew (Level 9).
  - Diglett is Ground type and Sandshrew is Ground type. Both are weak to Water (Bubble deals 2x special damage).

## Shopping List & Economy Planner
- **Current Balance**: ¥1075.
- **Inventory Check**: 6 Poké Balls, 1 Antidote.
- **Shopping Strategy**:
  - We do not need more Poké Balls immediately since we already have 6 and have captured our key targets (Pidgey, Rattata, Caterpie).
  - Potions are not sold at the Viridian Poké Mart, but we can buy Antidotes (¥100) if we expect more poison encounters in Viridian Forest. We currently have 1 Antidote.
  - Save money to buy Potions in Pewter City or preserve capital for other essential items.

## Grinding Safety Thresholds & Retreat Plan:
- **RETREAT THRESHOLDS**:
  1. **HP Threshold**: GEMMY's HP drops below 8 HP. Weedle's Poison Sting can poison us, which deals damage every overworld step. If GEMMY gets poisoned or drops below 8 HP, we must retreat immediately.
  2. **PP Threshold**: BUBBLE PP drops to 0, or total offensive PP (Tackle + Bubble) is below 5. SQUIRTLE cannot defeat opponents effectively without PP.
- **RETREAT ROUTE TO VIRIDIAN CITY**:
  - Head South from southernmost grass patch: (14, 41) -> (15, 41) -> (15, 43) -> (15, 44) -> (16, 44) -> (16, 47) -> (17, 47) (Warp to Route 2 Gatehouse).
  - Walk South through Route 2 Gatehouse to Route 2, then walk South along Route 2, bypass the northern grass, hop over the ledge gap at (7, 61), and enter Viridian City Pokémon Center to heal with Nurse Joy using custom tool `heal_pokemon_center`.

### Grinding Session 2 Telemetry & Analysis (Canonical Record):
- **Session Started**: Turn 2480, Timestamp: Saturday, May 23, 2026 at 9:51 PM PDT
- **Active Status**: Currently returning to the southern tall grass patch of Viridian Forest (Rows 40-41, Columns 12-15) to complete training.
- **Gym Readiness**: 90% (successfully analyzed on Turn 2758 by early_game_benchmarks_agent). The agent recommended getting SQUIRTLE (GEMMY) to Level 10+ and evolving CATERPIE (BUGGY) to BUTTERFREE (Level 10) to secure backup Confusion coverage (at Level 12) for Pewter Gym sweep readiness.
- **Telemetry Records**:
  - Total Grass Steps in Session 2: 191 steps.
  - Active Battles Cleared in Session 2: 15 battles.
  - METAPOD (BUGGY) is Level 7, HP 26/26.

## Grinding Milestones & Summaries:
- **Battle 6 (Turn 2617)**: Defeated wild Level 5 Metapod. BUGGY reached Level 6! HP increased to 23/23. SQUIRTLE (GEMMY) is Level 9.
- **Battle 7 (Turns 2656-2678)**: Defeated wild Level 4 Kakuna. Initiated switch-training: BUGGY started, immediately switched to GEMMY. GEMMY used super-effective BUBBLE, defeating Kakuna. BUGGY and GEMMY shared experience, gaining 20 EXP each.
- **Battle 8 (Turn 2795)**: Defeated wild Level 3 CATERPIE. Switch-trained BUGGY to GEMMY. BUGGY gained 11 EXP, GEMMY gained 11 EXP.
- **Battle 9 (Turn 2810)**: Defeated wild Level 4 METAPOD. Switch-trained BUGGY to GEMMY. BUGGY and GEMMY shared EXP.
- **Battle 10 (Turn 2880)**: Defeated wild Level 3 CATERPIE. Switch-trained BUGGY to GEMMY. BUGGY and GEMMY shared EXP.
- **Battle 11 (Turns 3007-3011)**: Defeated wild Level 3 CATERPIE. Switch-trained BUGGY to GEMMY. BUGGY and GEMMY shared EXP.
- **Battle 12 (Turns 3026-3033)**: Defeated wild Level 4 CATERPIE. Switch-trained BUGGY to GEMMY. BUGGY and GEMMY shared EXP. SQUIRTLE's TACKLE PP is at 31/35.
- **Battle 13 (Turns 3039-3047)**: Defeated wild Level 4 CATERPIE. Switch-trained BUGGY to GEMMY. BUGGY grew to Level 7 and began evolving! SQUIRTLE's TACKLE PP is at 28/35.
- **Battle 14 (Turns 3064-3069)**: Defeated wild Level 3 CATERPIE. Switch-trained BUGGY to GEMMY. BUGGY and GEMMY shared EXP (gained 11 EXP each). SQUIRTLE's TACKLE PP is at 26/35.
- **Battle 15 (Turns 3083-3089)**: Defeated wild Level 4 CATERPIE. Switch-trained BUGGY to GEMMY. BUGGY and GEMMY shared EXP (gained 14 EXP each). SQUIRTLE's TACKLE PP is at 24/35.
- **Grinding Pathing Summary (Turns 2618-2880)**: Moved systematically across the southernmost tall grass patch (Rows 40-41, Columns 8-15) to trigger encounters.

### Detailed Viridian Forest Encounter & Switch-Training Mechanics Guide:
1. **Wild Encounter Distribution**:
   - Caterpie (Level 3-5): 50% encounter rate. Great target for quick leveling.
   - Metapod (Level 4-6): 10% encounter rate. High physical Defense due to Harden, making Bubble the optimal choice.
   - Weedle (Level 3-5): 30% encounter rate. Warning: Poison Sting can poison our team. If poisoned, we must immediately use our single Antidote or retreat.
   - Kakuna (Level 4-6): 10% encounter rate. High physical Defense, similar to Metapod. Easily fainted with GEMMY's special moves.
2. **Squirtle (GEMMY) Progression & Scaling**:
   - Level 10 Stats: HP 30, Attack 17, Defense 18, Speed 15, Special 15.
   - Move Pool Utility: Bubble deals super-effective special damage to Ground/Rock and normal special damage to Bug types, which completely ignores physical Defense boosts. Tackle is a reliable physical option but scales poorly against high-Defense enemies.
3. **Caterpie (BUGGY) Progression & Evolution Path**:
   - Level 6 Stats: HP 23, Attack 10, Defense 10, Speed 11, Special 8.
   - Level 7: Evolves into Metapod. Base HP increases, physical Defense rises dramatically, but its offensive capabilities are temporarily limited.
   - Level 10: Evolves into Butterfree. HP, Speed, and Special stats scale significantly, turning BUGGY into a viable backup sweeper.
   - Level 12: Learns Confusion, a high-accuracy Psychic-type move. Confusion deals high Special damage and provides complete type coverage for Pewter Gym backup.

### Benchmark Checkpoint (Turn 2731):
- Gym Readiness: 90% (successfully analyzed on Turn 2758 by early_game_benchmarks_agent).
- Next Evolution Milestones: Evolve CATERPIE (BUGGY) into Metapod at Level 7, then Butterfree at Level 10.
- Leveling Goal: Train SQUIRTLE (GEMMY) to Level 10+ to maximize Bubble's power for Brock's Rock/Ground types.
- Current Party Status on Turn 2731: GEMMY (Level 9, 10/28 HP, 6/30 Bubble PP), BUGGY (Level 6, 23/23 HP). We were continuing our systematic grass patrol to trigger encounters.

- **Wild Encounter Probability Weights in Viridian Forest (Gen 1 Blue)**:
  - Caterpie: 50% encounter rate (Level 3, 4, 5). Yields 22-37 EXP. Extremely favorable for BUGGY's switch-training due to low physical threat and high yield.
  - Weedle: 30% encounter rate (Level 3, 4, 5). Yields 22-37 EXP. Warning: Weedle has Poison Sting. Poisoning in the overworld is a critical retreat trigger.
  - Metapod: 10% encounter rate (Level 4, 5, 6). Yields 50-70 EXP. High physical defense (Harden) makes it tedious to fight with Tackle, but GEMMY's Bubble bypasses physical Defense entirely to defeat it quickly.
  - Kakuna: 10% encounter rate (Level 4, 5, 6). Yields 50-70 EXP. High physical defense (Harden). Defeated easily using GEMMY's Bubble.
- **Switch-Training Experience Yields (Shared 50/50)**:
  - Against Level 4 Caterpie: ~22 EXP total -> BUGGY receives 11 EXP, GEMMY receives 11 EXP.
  - Against Level 5 Metapod: ~56 EXP total -> BUGGY receives 28 EXP, GEMMY receives 28 EXP.
  - Against Level 6 Kakuna: ~71 EXP total -> BUGGY receives 35 EXP, GEMMY receives 36 EXP.
- **Brock AI Behavior and Counters**:
  - Brock's Geodude and Onix are Rock/Ground type, which makes them take 4x damage from GEMMY's Bubble.
  - Brock's AI is programmed to favor moves like Tackle and Screech (Onix) or Defense Curl (Geodude). However, Onix's Bide is a massive risk. If Bide is used, any Bubble damage will be doubled and returned, easily fainting GEMMY. Therefore, our strategy is to immediately stop attacking if Bide is declared.
  - Having BUGGY evolved into Butterfree (Level 10) and then Level 12 (Confusion) provides an incredibly powerful backup plan. Confusion deals high special damage, completely bypassing Geodude's and Onix's physical Defense.
- **Retreat Decision Metrics**:
  - We must retreat immediately if:
    - SQUIRTLE (GEMMY) falls below 8 HP.
    - SQUIRTLE (GEMMY) BUBBLE PP falls to 0 (cannot bypass Metapod/Kakuna Harden or clear Brock easily).
    - Any party member is poisoned and we have no Antidotes (currently we have 1 Antidote).
- **Overwatch Compliance**: In-place edits of status variables and milestone tracking will be utilized moving forward to satisfy the 3-turn note-taking pace, preventing redundant, verbose play-by-play logs.

### Custom Battle Tool Performance & EXP Analysis (Turn 2796):
- **Tool Assessment**:
  - `battle_switch_buggy_to_gemmy`: Executed perfectly on Turn 2788. The sequence (Right -> A -> sleep -> Down x3 -> A -> sleep -> A) is robust and handles the menu load times seamlessly.
  - `battle_use_tackle`: Executed on Turn 2791 and Turn 2794. Safely selected Fight and Tackle, and handled the auto-advance. Highly reliable.
- **Battle Outcome**: Defeated a wild Level 3 CATERPIE.
  - Experience shared: BUGGY gained 11 EXP, GEMMY gained 11 EXP.
  - SQUIRTLE (GEMMY) HP is now 10/28.
- **Caterpie EXP Progression Modeling**:
  - Growth Group: Medium Fast (EXP = L^3).
  - Level 6 Threshold: 216 cumulative EXP.
  - Level 7 (Metapod Evolution) Threshold: 343 cumulative EXP.
  - Net EXP required from Level 6 to 7: 127 EXP.
  - At 11 EXP per shared Level 3 Caterpie battle, BUGGY needs approximately 12 shared battles total at this level to evolve. Higher level encounters (like Level 5 Metapod or Kakuna) will dramatically speed this up, yielding up to 35 EXP per shared battle.
- **Tactical Strategy**: SQUIRTLE (GEMMY) is down to 10/28 HP. We can safely handle at least one more Caterpie/Metapod battle. If GEMMY's HP falls below 8, or PP falls to critical levels, we will execute our retreat path to the Viridian City Pokémon Center to heal.

### Tactical XP Analysis & Grinding Projections (Turn 2861):
- **Caterpie (BUGGY) Experience Scaling Table**:
  - Growth Group: Medium Fast (Formula: EXP = L^3).
  - **Level 6**: 216 cumulative EXP (Current state).
  - **Level 7 (Metapod Evolution)**: 343 cumulative EXP. Net EXP needed: 127 EXP.
  - **Level 10 (Butterfree Evolution)**: 1000 cumulative EXP. Net EXP needed: 784 EXP.
  - **Level 12 (Confusion Move learned)**: 1728 cumulative EXP. Net EXP needed: 1512 EXP.
- **Grinding Battle Estimation (Switch-Training Model)**:
  - SQUIRTLE (GEMMY) is the active battler, meaning experience is shared 50/50.
  - Against Level 3 Caterpie/Weedle: ~22 EXP total -> BUGGY receives 11 EXP.
  - Against Level 4 Caterpie/Weedle/Metapod/Kakuna: ~40 EXP total -> BUGGY receives 20 EXP.
  - Against Level 5 Metapod/Kakuna: ~56 EXP total -> BUGGY receives 28 EXP.
  - **Projected Battles to Milestones**:
    - To Metapod (Level 7): ~6 additional shared battles of average Level 4 encounters.
    - To Butterfree (Level 10): ~39 additional shared battles of average Level 4 encounters.
    - To Confusion (Level 12): ~76 additional shared battles of average Level 4 encounters.
- **Resource depletion monitoring**:
  - GEMMY has 10/30 HP, and 6 BUBBLE PP. This is extremely close to our retreat thresholds. We can safely handle 1-2 more battles at most before executing our tactical retreat to Viridian City Pokémon Center. We will monitor these resources on every overworld step.

## Tactical Retreat & Return Milestone (Turns 2884-2929):
- **Retreat Phase**: Successfully navigated from Viridian Forest southern grass patch down Route 2, bypassing tall grass via column 3 and the ledge gap at (7,61) to minimize wild encounter risks with GEMMY at 8 HP. Entered Viridian City Pokémon Center and healed all Pokémon to 100% HP/PP on Turn 2925.
- **Return Phase**: Initiated return journey to Viridian Forest. Column 19 is a verified north-south clear path bypassing the Trainer School fence at row 17.

### Grinding & Training Efficiency Analysis (Turn 2971):
- **Special Attack Dominance**: GEMMY's BUBBLE deals special damage. This is extremely efficient against high-Defense wild bug types (METAPOD, KAKUNA) as it completely ignores their Harden defense boosts.
- **Butterfree Pivot**: Switch-training BUGGY (CATERPIE) to BUTTERFREE (Level 10) will secure our team's backup coverage. Once BUGGY reaches Level 12 and learns CONFUSION (special Psychic move), we have two highly potent special attackers to completely bypass Brock's physical walls.
- **Onix Bide Countermeasure**: Brock's Onix has BIDE. Bide accumulates damage over 2-3 turns and returns double. To prevent an instant OHKO on GEMMY, we must immediately switch or use status/non-damaging moves (like Tail Whip) if Bide is active.
- **Viridian Forest Southern Re-entry Plan (Turn 2979)**: With GEMMY's HP (30/30) and Bubble PP (30/30) fully restored, our training efficiency is maximized. We will proceed straight to the southernmost grass patch at (15,41) and initiate our switch-grinding loop to target high-yield wild Metapod and Kakuna encounters, utilizing BUBBLE to bypass Harden and split EXP 50/50. Our safety thresholds (GEMMY < 8 HP or Bubble PP = 0) remain active.
- **Target Optimization Strategy (Turn 2982)**: To maximize training efficiency, we will prioritize wild Metapod (Level 4-6) and Kakuna (Level 4-6) encounters which yield up to 35 shared EXP per battle, compared to Caterpie/Weedle which yield ~11-20 EXP. This target focus will optimize our progression to BUTTERFREE.

- **BUGGY (CATERPIE) EXP Projection Modeling (Turn 2992)**:
  - Growth Group: Medium Fast (EXP = L^3).
  - Current State: Level 6 (216 cumulative EXP).
  - Target 1: Level 7 Metapod (343 EXP, 127 EXP remaining).
    - ~11.5 battles against L3 Caterpie (11 EXP/battle)
    - ~5.1 battles against L4 Metapod (25 EXP/battle)
    - ~3.4 battles against L6 Metapod (37 EXP/battle)
  - Target 2: Level 10 Butterfree (1000 EXP, 784 EXP remaining).
    - ~71.3 battles against L3 Caterpie (11 EXP/battle)
    - ~31.4 battles against L4 Metapod (25 EXP/battle)
    - ~21.2 battles against L6 Metapod (37 EXP/battle)
  - Target 3: Level 12 Confusion (1728 EXP, 1512 EXP remaining).

- **Wild Move Pool & Hazard Analysis (Turn 2995)**:
  - **Weedle**: Uses *Poison Sting* (20% poison chance in Gen 1). Poisoning is a critical threat that triggers our immediate retreat protocol (or using our single Antidote).
  - **Metapod / Kakuna**: Use *Harden* (raises Defense). Non-threatening, but physical Tackle scales poorly against them. SQUIRTLE's special BUBBLE bypasses Harden completely, making it our primary offensive option. SQUIRTLE's *Tackle* is reserved for low-Defense Caterpie to preserve Bubble PP.
  - **Caterpie**: Uses *Tackle* and *String Shot* (lowers Speed). Zero status threat, making it the safest training partner for BUGGY.
- **Session 2 Re-entry & Current Status (Turn 3012)**: Re-entered Viridian Forest and arrived at the southernmost grass patch (14, 41). BUGGY is Level 6 (23/23 HP), GEMMY is Level 10 (30/30 HP, 30 Bubble PP). Ready to resume grass patrol and switch-training.

<hr>