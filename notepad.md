<h1><code>Main</code></h1>

# Pokémon Blue Playthrough Dashboard

## Main Objectives
- [x] Choose first Pokémon (Turn 81 - Squirtle!)
- [x] Reach Viridian City Poké Mart to get Oak's Parcel (Turn 247)
- [x] Deliver Oak's Parcel to Professor Oak (Turn 461)
- [x] Get Pokédex from Professor Oak (Turn 464)
- [x] Get Town Map from Daisy in Pallet Town (Turn 507)
- [x] Return to Viridian City to buy Poké Balls (Turn 825)
- [ ] Capture additional wild Pokémon (Pidgey, Rattata, etc.) to build our team
- [ ] Navigate north through Route 2 and enter Viridian Forest

## Directory
- `Locations/PalletTown` - Permanently verified Pallet Town location records.
- `Locations/Route1` - Permanently verified Route 1 connections and layout features.
- `Locations/ViridianCity` - Permanently verified Viridian City connections and buildings.
- `Mechanics/General` - Verified game mechanics and controls.
- `Scratchpad/WildCaptures_Route2` - Active grinding, capture checklist, and leveling preparation on Route 2.

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

# Scratchpad: Wild Captures and Leveling Goals

## High-Level Strategy:
- Active Grinding Phase (Started Turn 910)
- Pivot Strategy (Turn 1411): After 42 cumulative steps on Route 2 Columns 8 & 9 (Rows 61-67) with 0 encounters, we hypothesize that encounters on this specific grass patch might be disabled or extremely rare. We are pivoting to explore north towards Viridian Forest to find active wild encounters.

## Live Status:
- Turn 1623: GEMMY (SQUIRTLE) is at 10/24 HP (Level 7). BIRBIE (PIDGEY) is at 13/18 HP (Level 4). Currently at (18, 0) in Viridian City.
- Money: ¥1075.
- Inventory: 8 Poké Balls, 1 Antidote, 1 Town Map.
- Location: Viridian City (Map 0_1) at (18, 0) facing Down.
- Grinding Phase Started: Turn 910

## Active Team & Captures Checklist:
- [x] Pidgey (Level 4, Nickname: BIRBIE) - Status: Captured!
- [ ] Rattata (Target Level 8-10) - Status: Not Captured
- [ ] Caterpie (Target Level 10 Butterfree) - Status: Not Captured
- [x] GEMMY (SQUIRTLE) - Level: 7 (Goal: Level 10)

## Route 2 Wild Encounters Strategy:
- Active Patrol: Explored southern patch (Columns 8 & 9, Rows 61-67), suspended on Turn 1411 due to 0 encounters over 42 steps.
- Currently patrolling northern patch (Columns 4-9, Rows 48-51, TYPE_fed7 grass).

## Target Captures and Leveling Benchmarks:
1. Pidgey (Normal/Flying):
   - Level range: 3-5
   - Strategy: Weaken with Tackle, then use Poké Ball from inventory. Do not KO.
   - Purpose: Team member for Flying coverage and early-game leveling backup.
   - Gamer Girl Nickname Ideas: BIRBIE, AERO, CHIRPY, FLUTTER.

2. Rattata (Normal):
   - Level range: 2-4
   - Strategy: Weaken with Tackle/Tail Whip, then capture.
   - Purpose: Quick Normal-type attacker with Quick Attack/Bite later.
   - Gamer Girl Nickname Ideas: REMY, SQUEAKY, NIBBLES, WHISKERS.

3. Caterpie (Bug) -> Metapod (Bug) -> Butterfree (Bug/Flying):
   - Level range: 3-5
   - Strategy: Direct Poké Ball or minimal damage.
   - Purpose: Early evolution to Butterfree (Level 10) is extremely valuable because Butterfree learns CONFUSION at Level 12. Confusion deals super-effective damage to Rock/Ground types (like Geodude/Onix) in Pewter Gym, providing a massive tactical advantage!
   - Gamer Girl Nickname Ideas: FLUFFY, BUGGY, SILKY, BUTTERFLY.

## Early-Game Battle & Capture Mechanics:
- Pokémon must be weakened (HP in yellow or red range) to increase capture probability.
- Status conditions (sleep, paralysis) greatly improve catch rate, but we do not have status moves yet.
- Throwing a Poké Ball is accessed via the BAG (Item Menu) during battle.

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

## Empirical Testing & Hypotheses
### Test 1: Red Flower Tile Collision Check
- **Hypothesis**: Red flower tiles (visually red flowers, system tile type `TYPE_3fe2`) are passable and do not block player movement.
- **Methodology**:
  - Turn 1040: GEM is at (4, 66). The tile to the east (Right) is (5, 66), which is a red flower tile.
  - Action: Press 'Right' to move from (4, 66) to (5, 66).
  - Verification: Check if Turn 1041 state shows player coordinates as (5, 66).
- **Status**: Executed on Turn 1042. Result: Verified. Player successfully moved to (5, 66). Hypothesis confirmed: Red flower tiles do not block player movement.

### Test 2: Route 2 Southern Tall Grass Patch Wild Encounters Check
- **Hypothesis**: Tall grass tiles (TYPE_3fe2) in the southern portion of Route 2 (Columns 8 & 9, Rows 61-67) contain wild Pokémon encounters.
- **Methodology**:
  - Track active steps taken on these tiles and record any encounters triggered.
- **Results**:
  - Turned on Turn 1052. Player took 42 cumulative steps on these tiles between Turn 1052 and Turn 1411.
  - Number of wild encounters triggered: 0.
- **Status**: Completed on Turn 1411. Result: Unverified/Negative. Due to taking 42 steps without a single encounter, we conclude that encounters on this specific grass patch are either disabled or have an extremely low encounter rate. We are pivoting north to find a better training ground in Viridian Forest.

## Encounter Rate Tracking (Columns 8 & 9 Tall Grass)
- **Methodology**: Track the cumulative number of active steps taken on tall grass tiles (TYPE_3fe2) in Route 2 before each encounter is triggered.
- **Cumulative Tally**:
  - **Grinding Run 1 (Started Turn 1052)**:
    - Current Position: (5, 51) on Route 2.
    - Cumulative steps taken on tall grass: 18
    - Encounters triggered: 2 (Level 4 PIDGEY on Turn 1537, Level 5 PIDGEY on Turn 1578)
    - Poké Balls thrown: 2 (Failed on Turn 1551, Succeeded on Turn 1554)
    - Status: Escaped wild level 5 Pidgey.

## Navigation North on Route 2 (Started Turn 1417)
- Plan: Move north along column 4 (or columns 2-4) to explore further north.

## Discovered Encounter Grass on Route 2 (Turn 1434)
- Observation: At row Y=51, columns X=4 to X=9, the tile type is TYPE_fed7, which matches the encounter grass from Route 1.
- In contrast, the southern grass patch (Rows 61-67, Columns 8-9) had type TYPE_3fe2 and did not trigger encounters.
- Hypothesis: The TYPE_fed7 tall grass patch starting at row Y=51 will contain active wild encounters.
- Plan: Step up into (4, 51) to test this hypothesis.

## Test 3: Route 2 TYPE_fed7 Tall Grass Patch Wild Encounters Check
- **Hypothesis**: The TYPE_fed7 tall grass patch (starting at Y=51, Columns X=4 to X=9) contains active wild encounters.
- **Methodology**:
  - We are starting at (4, 51).
  - We will execute a 16-step loop on tall grass: (4,51)->(9,51) -> (9,48) -> (4,48) -> (4,51).
  - We will count each step taken on these tiles and record any encounters.
  - Starting Turn: 1438.
  - SQUIRTLE (GEMMY) HP: 21/24. Poké Balls: 10.
- **Results**:
  - On Turn 1537, at 13 cumulative steps on the tall grass patch, we triggered a wild Level 4 PIDGEY encounter!
  - We used SQUIRTLE's Tackle once to weaken it, then threw a second Poké Ball on Turn 1554 to successfully capture it.
- **Status**: Completed (Turn 1554). Result: Verified. The TYPE_fed7 tall grass patch contains active wild encounters.
- Turn 1624: Successfully entered Viridian City (Map 0_1) from Route 2. We are currently standing at (18, 0) facing Down.
  - Team: GEMMY (SQUIRTLE) Level 7, 10/24 HP. BIRBIE (PIDGEY) Level 4, 13/18 HP.
  - Money: ¥1075.
  - Goal: Walk to the Pokémon Center to heal our team.
  - Pokémon Center location: Door is at (23, 25).
  - Let's check our path to the Pokémon Center. We need to navigate from (18, 0) to (23, 25).
  - First, let's look at the current screen around (18, 0):
    - Rows 0 to 4:
      - Column 18: (18, 0) TYPE_3fe2, (18, 1) TYPE_3fe2, (18, 2) TYPE_3fe2, (18, 3) TYPE_3fe2, (18, 4) TYPE_3fe2.
      - Column 17: (17, 0) TYPE_3fe2, (17, 1) TYPE_3fe2, (17, 2) TYPE_3fe2, (17, 3) TYPE_3fe2, (17, 4) TYPE_3fe2.
      - Column 19: (19, 0) TYPE_3fe2, (19, 1) is TYPE_2889 (signpost), (19, 2) TYPE_3fe2, (19, 3) TYPE_3fe2, (19, 4) TYPE_3fe2.
    - So we can walk Down along column 18.
    - Let's step Down to (18, 4). This is 4 steps Down.
    - Let's execute this.
- Navigation Summary (Turns 1624-1636):
  - After fleeing from a wild Level 5 Pidgey on Route 2 on Turn 1589, we navigated south to return to Viridian City.
  - To avoid further encounters while our team was weakened, we selected a safe route along columns 3 and 4, which consist entirely of clear path tiles (TYPE_3fe2) with 0% wild encounter rate.
  - On row 61, we jumped south over the ledge at (3, 61), landing at (3, 62).
  - On row 70, column 3 was blocked by trees, so we detoured right to column 8 and exited Route 2 south at (8, 71), transitioning to Viridian City at (18, 0) on Turn 1618.
  - In Viridian City, we walked south along column 18 from (18, 0) to (18, 12).
  - This horizontal and vertical navigation bypasses any tall grass completely.
- Turn 1638: Successfully arrived at (18, 16) facing Down. SQUIRTLE (GEMMY) is at 10/24 HP, PIDGEY (BIRBIE) is at 13/18 HP.
  - Let's check our surroundings on the screen:
    - (18, 16) is clear path (TYPE_3fe2).
    - Directly to our right, row 17 has fences at (20, 17) to (23, 17) blocking east movement.
    - However, row 18 is completely clear (TYPE_3fe2) from column 18 to column 23.
    - Row 19 and row 20 are also completely clear.
  - Plan:
    1. Walk Down 2 steps to (18, 18).
    2. Walk Right 5 steps to (23, 18).
    3. From there, walk south along column 23 to the Pokémon Center door at (23, 25).
  - Let's execute step 1: Down 2 steps to (18, 18).
- Turn 1639: Standing at (18, 16) facing Down. SQUIRTLE (GEMMY) is at 10/24 HP. PIDGEY (BIRBIE) is at 13/18 HP.
  - Let's check our path south and east:
    - Row 17: (18, 17) is TYPE_3fe2 (clear), (19, 17) is TYPE_3fe2 (clear). (17, 17) is TYPE_2889 (signpost/structure). (20, 17) to (23, 17) are TYPE_2889 (wooden fence).
    - Row 18: (18, 18) is TYPE_3fe2 (clear). (19, 18) is TYPE_3fe2 (clear). (20, 18) to (23, 18) are TYPE_3fe2 (clear path with grass/flowers background).
    - So we can walk Down 2 steps to (18, 18).
    - Then walk Right 5 steps to (23, 18).
  - Let's execute this.
- Turn 1640: Currently at (18, 16) facing Down. SQUIRTLE (GEMMY) is at 10/24 HP. PIDGEY (BIRBIE) is at 13/18 HP.
  - Verification of surroundings on `<CurrentScreen turn="1640">`:
    - We are indeed at (18, 16) facing Down.
    - Below us: (18, 17) is TYPE_3fe2 (clear).
    - Below that: (18, 18) is TYPE_3fe2 (clear).
    - To our right: (19, 16) is TYPE_3fe2, (20, 16) is TYPE_3fe2.
    - Fences are at row 17 starting at column 20: (20, 17) to (23, 17) are TYPE_2889 (impassable wooden fence).
    - (17, 17) is TYPE_2889 (impassable mailbox/structure).
    - Row 18 is completely clear: (16, 18) to (19, 18) are TYPE_3fe2, and (20, 18) to (23, 18) are TYPE_3fe2.
  - Perfect routing plan:
    - Step Down 2 times:
      - (18, 16) -> (18, 17) -> (18, 18).
    - Step Right 5 times:
      - (18, 18) -> (19, 18) -> (20, 18) -> (21, 18) -> (22, 18) -> (23, 18).
    - This path is 100% on clear path (TYPE_3fe2) and avoids all obstacles.
  - Let's execute the first step of our movement plan: Down 2 times.
- Turn 1643: Successfully arrived at (18, 18) facing Down. SQUIRTLE (GEMMY) is at 10/24 HP. PIDGEY (BIRBIE) is at 13/18 HP.
  - Verified on `<CurrentScreen turn="1643">`:
    - Row 18 is completely clear from column 18 to column 23 (all tiles labeled TYPE_3fe2).
    - No NPCs are blocking our path.
  - Plan: Press 'Right' 5 times to move from (18, 18) to (23, 18).
- Turn 1646: Successfully arrived at (23, 18) in Viridian City facing Right. SQUIRTLE (GEMMY) is at 10/24 HP. PIDGEY (BIRBIE) is at 13/18 HP.
  - Let's check our surroundings on `<CurrentScreen turn="1646">`:
    - We are at (23, 18).
    - Directly south of us on column 23:
      - (23, 19) is clear path (TYPE_3fe2).
      - (23, 20) is clear path (TYPE_3fe2).
      - (23, 21) is clear path (TYPE_3fe2).
    - Wait! At row 22, there is a green fence structure!
      - (22, 22), (23, 22), (24, 22), (25, 22) are labeled TYPE_2889 (green hedge/fence structure, impassable!).
      - Let's check where the gap in the green fence is:
        - (19, 22) is TYPE_3fe2 (clear).
        - (20, 22) is TYPE_3fe2 (clear).
        - (21, 22) is TYPE_3fe2 (clear).
        - (26, 22) is TYPE_3fe2 (clear).
        - (27, 22) is TYPE_3fe2 (clear).
      - So the green hedge at row 22 blocks column 22, 23, 24, and 25!
      - We CANNOT walk south along column 23 past row 21!
      - To get past the row 22 hedge, we can:
        - Route A (Left side bypass): Walk Left to column 21 on row 20 or 21, and then walk south past row 22 through (21, 22).
        - Route B (Right side bypass): Walk Right to column 26 on row 20 or 21, and then walk south past row 22 through (26, 22).
      - Let's check which route is better to reach the Pokémon Center door at (23, 25):
        - If we use Route A (Left side):
          - Walk Down to (23, 21).
          - Walk Left to (21, 21) (2 steps Left).
          - Walk Down to (21, 22) (1 step Down).
          - Walk Down to (21, 23) (1 step Down).
          - Then we can walk Right back to column 23 and walk Down to the door at (23, 25).
        - If we use Route B (Right side):
          - Walk Down to (23, 21).
          - Walk Right to (26, 21) (3 steps Right).
          - Walk Down to (26, 22) (1 step Down).
          - Then walk south and west towards (23, 25).
        - Since column 21 is closer to column 23 than column 26, Route A (Left side bypass) is slightly shorter!
        - Let's trace Route A:
          - (23, 18) -> Down to (23, 21) (3 steps Down).
          - (23, 21) -> Left to (21, 21) (2 steps Left).
          - (21, 21) -> Down to (21, 22) (1 step Down).
          - (21, 22) -> Down to (21, 23) (1 step Down).
        - Let's execute the first part of this: Down 3 steps to (23, 21).
- Turn 1647: Let's do a strict visual validation of `<CurrentScreen turn="1647">`.
  - We are standing at (23, 18).
  - Directly south: (23, 19) is TYPE_3fe2, (23, 20) is TYPE_3fe2, (23, 21) is TYPE_3fe2.
  - At row 22, the green hedge (TYPE_2889) blocks columns 22, 23, 24, and 25.
  - The gap in the green hedge is at column 21: (21, 22) is TYPE_3fe2 (clear path).
  - Also, (20, 22) and (19, 22) are clear path.
  - On column 26: (26, 22) is TYPE_3fe2 (clear path).
  - So Route A (Left side bypass) is indeed completely open:
    - Step Down 3 times: from (23, 18) -> (23, 19) -> (23, 20) -> (23, 21).
    - Step Left 2 times: from (23, 21) -> (22, 21) -> (21, 21).
    - Step Down 2 times: from (21, 21) -> (21, 22) -> (21, 23).
  - Let's execute the first part of this: Down 3 steps to (23, 21).
- Turn 1648: Standing at (23, 18) facing Down (or right, wait, we are at (23, 18) facing Right). SQUIRTLE (GEMMY) is at 10/24 HP. PIDGEY (BIRBIE) is at 13/18 HP.
  - Verification from `<CurrentScreen turn="1648">`:
    - Yes, we are standing at (23, 18).
    - Directly south: (23, 19) is TYPE_3fe2, (23, 20) is TYPE_3fe2, (23, 21) is TYPE_3fe2.
    - At row 22: (22, 22), (23, 22), (24, 22), (25, 22) are TYPE_2889 (impassable green fence).
    - On column 21: (21, 22) is indeed TYPE_3fe2 (clear path).
    - Let's execute our Route A movement plan:
      - Step Down 3 times:
        1. Down -> (23, 19)
        2. Down -> (23, 20)
        3. Down -> (23, 21)
      - Step Left 2 times:
        4. Left -> (22, 21)
        5. Left -> (21, 21)
      - Step Down 2 times:
        6. Down -> (21, 22) (bypassing the green fence!)
        7. Down -> (21, 23)
      - Let's begin by stepping Down 3 times to (23, 21).
- Turn 1649: Currently at (23, 18) facing Down. Verified on `<CurrentScreen turn="1649">`:
  - Directly south: (23, 19), (23, 20), (23, 21) are clear path (TYPE_3fe2).
  - Row 22 has a green hedge at (22, 22) to (25, 22) of TYPE_2889 (impassable).
  - Column 21 has a gap: (21, 22) is TYPE_3fe2 (clear path).
  - This perfectly confirms Route A (Left side bypass):
    - Walk Down 3 steps to (23, 21)
    - Walk Left 2 steps to (21, 21)
    - Walk Down 2 steps to (21, 23) (bypassing the green hedge)
    - Then we can head back east to column 23 and down to the Pokémon Center door at (23, 25).
  - Let's execute the first 3 steps Down.

<hr>