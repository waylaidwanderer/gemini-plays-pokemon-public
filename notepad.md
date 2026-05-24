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
- Turn 1711: SQUIRTLE (GEMMY) is at 24/24 HP (Level 7). BIRBIE (PIDGEY) is at 18/18 HP (Level 4). Team is completely healed!
- Money: ¥1075.
- Inventory: 8 Poké Balls, 1 Antidote, 1 Town Map.
- Location: Viridian City at (18, 8) facing Up.
- Grinding Phase 2 Started: Turn 1690 (May 23, 2026, 6:38 PM)
  - Goal: Train GEMMY to Level 8 to learn Bubble, and find Rattata and Caterpie in Route 2's active grass patch at (5, 51).
  - Plan: Walk Up 8 steps to transition to Route 2, then walk to active grass patch.

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
- Turn 1653: Standing at (23, 18) in Viridian City, facing Down. SQUIRTLE (GEMMY) is at 10/24 HP, PIDGEY (BIRBIE) is at 13/18 HP.
  - Verification from `<CurrentScreen turn="1653">`:
    - We are at (23, 18), standing on the red flowers/grass (TYPE_3fe2).
    - Below us: (23, 19) is TYPE_3fe2 (clear), (23, 20) is TYPE_3fe2 (clear), (23, 21) is TYPE_3fe2 (clear).
    - At row 22: (22, 22) to (25, 22) is TYPE_2889 (green fence).
    - Column 21 has the gap: (21, 22) is TYPE_3fe2 (clear).
  - This perfectly confirms Route A (Left-side bypass):
    - Walk Down 3 steps: (23, 18) -> (23, 19) -> (23, 20) -> (23, 21).
    - Walk Left 2 steps: (23, 21) -> (22, 21) -> (21, 21).
    - Walk Down 2 steps: (21, 21) -> (21, 22) -> (21, 23).
  - Let's execute this movement sequence now!
- Viridian City Routing & Pokémon Center Entry Summary (Turns 1650-1678):
  - On Turn 1654, we stood at (23, 18) and analyzed the layout of southern Viridian City.
  - Obstacle Detection: A green hedge (TYPE_2889) blocks column 23 at row 22.
  - Obstacle Detection: The Pokémon Center's brick building wall (TYPE_2889) blocks row 23 and row 24 from column 22 to column 25.
  - Obstacle Detection: At row 25, the brick wall at (22, 25) blocks direct horizontal entry to the door mat from the west.
  - Route A (Left-side bypass) Execution:
    - We walked Down 3 steps to (23, 21) on Turn 1654.
    - We walked Left 2 steps to (21, 21) on Turn 1656.
    - We walked Down 4 steps along column 21 to row 25 on Turn 1659.
    - Because (22, 25) was impassable, we adjusted our path and walked Down 1 step to row 26, Right 2 steps, and Up 1 step to the door mat at (23, 25) on Turn 1663.
    - This successfully bypassed all obstacles and let us enter the Pokémon Center.

- Pokémon Center Interior Analysis:
  - We entered the Pokémon Center (Map 0_41) on Turn 1664 at the door mat (3, 7).
  - Nurse Joy's counter is located on row 2, and the tiles directly in front of the counter are row 3.
  - On Turn 1668, we stood at (4, 4) facing Up to talk to Nurse Joy at (4, 3) (or behind the counter).
  - Obstacle: A wandering spiky-haired trainer NPC stood at (4, 3) directly in front of the center of the counter.
  - When we pressed A, we spoke to this NPC instead of Nurse Joy, receiving his dialogue.
  - We pivoted and stepped Left to (3, 4) on Turn 1676, and then Up to (3, 3) on Turn 1678, to stand directly in front of the left counter spot.
  - We are currently standing at (3, 3) facing Up, preparing to test if we can interact with Nurse Joy from the left counter spot.

## Test 4: Left Counter Tile Interaction Check
- **Hypothesis**: The player can interact with Nurse Joy from (3, 3) facing Up (the left counter tile) to heal their Pokémon, bypassing the blocking NPC at (4, 3).
- **Methodology**:
  - Turn 1679: Standing at (3, 3) facing Up.
  - Action: Press 'A' to interact with the counter directly above us at (3, 2).
  - Verification: Check if Turn 1687 state shows the Pokémon Center healing dialogue on screen.
- **Results**:
  - Turn 1687: Successfully verified! The screen shows "Shall we heal your POKéMON?" and the interactive menu `▶HEAL / CANCEL` is open, with the cursor pointing at `▶HEAL`.
  - **Conclusion**: Confirmed! In Generation 1, you can talk to Nurse Joy and heal your Pokémon from the left counter tile (3, 3) facing Up. You do not need to stand in the center (4, 3). This is an incredibly useful mechanic to bypass any NPC blocking the center counter spot.

- Turn 1687: Healing menu is open with the cursor pointing at `▶HEAL`. We will press A to confirm healing our team.
- Turn 1692: Standing at (3, 3) facing Up inside the Pokémon Center. Our team is fully healed (GEMMY at 24/24 HP, BIRBIE at 18/18 HP).
  - Since our healing is complete, we will now exit the Pokémon Center.
  - Path to exit: Press 'Down' 5 times to walk from (3, 3) down column 3 to (3, 7) and transition outside to Viridian City at (23, 26).
  - From there, we will navigate back to Route 2's active grass patch at (5, 51) to continue our training.
## Grinding Phase 2 Navigation Log (Turn 1696):
- Status: Fully healed at Viridian City Pokémon Center. Ready to return to Route 2's active grass patch at (5, 51).
- Exact Route Plan from (23, 26) to Route 2 (18, 0):
  1. Walk Left 2 steps to (21, 26).
  2. Walk Up 8 steps to (21, 18) (passing through the fence gap at (21, 22)).
  3. Walk Left 3 steps to (18, 18).
  4. Walk Up 18 steps along column 18 to (18, 0) to transition back to Route 2.
- Let's execute the first part of this route: Left 2, Up 8.
- Turn 1700: Arrived at (18, 18) facing Down. Verified that column 18 is open northwards.
- Plan: Walk Up 10 steps to (18, 8). Then walk Up 8 steps to (18, 0) to transition to Route 2.
- Turn 1702: Standing at (18, 8) facing Up. The path north along column 18 is clear as far as the screen can see (up to row 4).
- Plan: Walk Up 8 steps to (18, 0) to transition to Route 2.
- Turn 1705: Observed NPC (SPRITE_578e) moved to (17, 5).
- Turn 1709: Verified NPC (SPRITE_578e) moved to (18, 5), blocking column 18.
- Plan: Execute Left-side bypass of (18, 5) to reach Route 2 (18, 0):
  1. Left to (17, 8).
  2. Up 4 steps to (17, 4).
  3. Right to (18, 4).
  4. Up 4 steps to (18, 0) to transition.
- Method of Verification: Tile coordinates checked on Turn 1709 screen overlay. (17, 8), (17, 7), (17, 6), (17, 5), (17, 4) are all TYPE_3fe2.

<hr>