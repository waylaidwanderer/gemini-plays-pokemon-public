# Scratchpad: Wild Captures and Leveling Goals

## High-Level Strategy:
- Active Grinding Phase (Started Turn 910)
- Pivot Strategy (Turn 1411): After 42 cumulative steps on Route 2 Columns 8 & 9 (Rows 61-67) with 0 encounters, we hypothesize that encounters on this specific grass patch might be disabled or extremely rare. We are pivoting to explore north towards Viridian Forest to find active wild encounters.

## Live Status:
- Turn 1592: GEMMY (SQUIRTLE) is at 10/24 HP (Level 7). BIRBIE (PIDGEY) is at 13/18 HP (Level 4). Currently at (5, 51) after escaping a wild Level 5 Pidgey.
- Money: ¥1075.
- Inventory: 8 Poké Balls, 1 Antidote, 1 Town Map.
- Location: Route 2 (Map 0_13) at (5, 51) facing Down.
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
- Turn 1594: Successfully ran from the wild Level 5 Pidgey. SQUIRTLE (GEMMY) is at 10/24 HP. PIDGEY (BIRBIE) is at 13/18 HP. Current position is (5, 51) on Route 2. We will now head south to Viridian City's Pokémon Center to heal.
- Route back to Viridian City:
  - From (5, 51), walk Right to (8, 51) or (9, 51) to get out of the grass columns, or walk south through the grass to (5, 52) first.
  - Wait, row 53 has trees (TYPE_2889) blocking (6, 53) to (10, 53). (5, 53) is a clear path (TYPE_3fe2).
  - Let's check Row 52: (4, 52) is TYPE_3fe2, (5, 52) is TYPE_3fe2.
  - Row 53: (4, 53) is TYPE_3fe2, (5, 53) is TYPE_3fe2, but (6, 53) is TYPE_2889 (tree).
  - So from (5, 51), we can walk down to (5, 52), then to (5, 53), then we need to check further south.
  - Let's step Down to (5, 52) first.
- Turn 1595: Visual Check on Screen.
  - We are at (5, 51) on Route 2.
  - Our goal is to go south to Viridian City's Pokémon Center to heal.
  - Looking at row 52 on the screen: (4, 52), (5, 52), (6, 52), (7, 52), (8, 52), (9, 52) are all TYPE_3fe2 (clear path).
  - Row 53: (4, 53) and (5, 53) are TYPE_3fe2 (clear path). But (6, 53) to (10, 53) are TYPE_2889 (trees, impassable!).
  - So if we go down to (5, 52) then (5, 53), can we proceed further south?
  - Row 54: (4, 54) is TYPE_3fe2. But (5, 54) to (10, 54) are TYPE_2889 (trees, impassable!).
  - Row 55: (4, 55) is TYPE_3fe2. But (5, 55) to (10, 55) are TYPE_2889 (trees, impassable!).
  - So there is a clear path on column 4! (4, 51), (4, 52), (4, 53), (4, 54), (4, 55).
  - If we walk Left to (4, 51) then walk Down, we can easily bypass all the trees!
  - Let's trace this path:
    1. Walk Left to (4, 51).
    2. Walk Down to (4, 52).
    3. Walk Down to (4, 53).
    4. Walk Down to (4, 54).
    5. Walk Down to (4, 55).
  - Let's execute this step-by-step.
  - First step: Walk Left to (4, 51).
- Turn 1596: Refined safe route to avoid wild encounters while returning south:
  - We are at (5, 51).
  - Row 52 is completely clear path (TYPE_3fe2).
  - So, instead of stepping Left to (4, 51) (which is tall grass and could trigger an encounter), we will:
    1. Step Down to (5, 52) (clear path, 0% encounter rate).
    2. Step Left to (4, 52) (clear path, 0% encounter rate).
    3. Step Left to (3, 52) (clear path, 0% encounter rate).
    4. Proceed Down along column 3 (clear path, 0% encounter rate).
  - Let's execute step 1: Step Down to (5, 52).
- Turn 1598: Arrived at (5, 52) on Route 2. We are facing Down. Let's check the current screen:
  - (5, 52) is TYPE_3fe2 (clear path).
  - Next step in our plan is to step Left to (4, 52).
  - (4, 52) is TYPE_3fe2 (clear path).
  - Let's execute this step.
- Turn 1601: Currently at (3, 52) on Route 2 facing Left. Our team is weak: GEMMY (SQUIRTLE) at 10/24 HP, BIRBIE (PIDGEY) at 13/18 HP. We will walk south along column 3, which is a clear path (TYPE_3fe2) with 0% encounter rate, to safely make our way back to Viridian City.
  - Plan: Press 'Down' 4 times to move from (3, 52) to (3, 56).
- Turn 1603: Successfully arrived at (3, 56) facing Down. Looking at the screen, we can trace our next steps south.
  - Rows 57, 58, 59, 60:
    - Row 57: Column 3 is (3, 57) TYPE_3fe2 (clear path).
    - Row 58: Column 3 is (3, 58) TYPE_3fe2 (clear path).
    - Row 59: Column 3 is (3, 59) TYPE_3fe2 (clear path).
    - Row 60: Column 3 is (3, 60) TYPE_3fe2 (clear path).
  - So we can walk directly Down 4 more steps to (3, 60).
  - Let's execute this: Down 4 times to reach (3, 60). All of these tiles are TYPE_3fe2, ensuring 0% encounter rate.