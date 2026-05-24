# Scratchpad: Wild Captures and Leveling Goals

## High-Level Strategy:
- Active Grinding Phase (Started Turn 910)
- Pivot Strategy (Turn 1411): After 42 cumulative steps on Route 2 Columns 8 & 9 (Rows 61-67) with 0 encounters, we hypothesize that encounters on this specific grass patch might be disabled or extremely rare. We are pivoting to explore north towards Viridian Forest to find active wild encounters.

## Live Status:
- Turn 1562: GEMMY (SQUIRTLE) is at 15/24 HP (Level 7). Caught wild PIDGEY (Level 4). Currently on the nickname entry screen, typing 'BIRBIE'.
- Money: ¥1075.
- Inventory: 9 Poké Balls, 1 Antidote, 1 Town Map.
- Location: Route 2 (Map 0_13) at (5, 48) facing Left (In Nickname Screen).
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
    - Current Position: (5, 48) on Route 2.
    - Cumulative steps taken on tall grass: 13
    - Encounters triggered: 1 (Level 4 PIDGEY on Turn 1537)
    - Poké Balls thrown: 2 (Failed on Turn 1551, Succeeded on Turn 1554)
    - Status: Exploring TYPE_fed7 tall grass patch starting at row Y=51.

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
- Turn 1567: Caught Level 4 Pidgey ("BIRBIE"). SQUIRTLE (GEMMY) is Level 7 with 15/24 HP.
- Plan: We want to catch Rattata and Caterpie. Since the grass patch here is active, let's explore it more or head north towards Viridian Forest. Let's do some more encounters in this active grass patch first, to see if we can find Rattata/Caterpie or level Squirtle to Level 8 (learn Bubble).
- Let's check our current position: (5, 48).
- We have the custom tool `patrol_route2_grass2` to move in the 16-step loop: (4,51)->(9,51)->(9,48)->(4,48)->(4,51). Let's use it!
- Turn 1570: Moved from (5, 48) to (4, 48) in the tall grass patrol. No wild encounter was triggered on this step. SQUIRTLE (GEMMY) is Level 7, PIDGEY (BIRBIE) is Level 4. We will continue the patrol loop down to (4, 51).
- Turn 1572: Moved to (4, 49) in the tall grass patrol. Currently facing down. We are at (4, 49) and will continue patrolling the active tall grass patch of Route 2. SQUIRTLE (GEMMY) is Level 7, PIDGEY (BIRBIE) is Level 4.
- Turn 1574: Moved to (4, 50) in the tall grass patrol. Facing down. Currently in TYPE_fed7 tall grass. SQUIRTLE (GEMMY) is Level 7, PIDGEY (BIRBIE) is Level 4. We will step down to (4, 51) next.
- Turn 1576: Arrived at (4, 51) in the tall grass patrol. Currently facing down. SQUIRTLE (GEMMY) is Level 7, PIDGEY (BIRBIE) is Level 4. No encounter on this step. Next we will step right to (5, 51).
- Turn 1578: Triggered a wild Level 5 PIDGEY encounter at (5, 51) while trying to step right in the patrol. GEMMY (SQUIRTLE) is Level 7, HP 15/24. BIRBIE (PIDGEY) is Level 4. We already have a Pidgey, so we will defeat this one to gain EXP and work towards Level 8 (Bubble).
- Strategy: Use Tackle to defeat the Pidgey.
- Turn 1580: GEMMY's first Tackle missed, and Pidgey used Sand-Attack, reducing GEMMY's accuracy. SQUIRTLE (GEMMY) HP is 15/24. We will use Tackle again.
- Turn 1582: SQUIRTLE (GEMMY) HP is 15/24. Enemy PIDGEY Level 5 is at 100% HP. Enemy Sand-Attack failed. We will use Tackle again.