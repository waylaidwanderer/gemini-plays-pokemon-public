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
- Turn 1626: Currently at (18, 0) in Viridian City, facing Down.
  - Team status: GEMMY (SQUIRTLE) 10/24 HP, BIRBIE (PIDGEY) 13/18 HP. No healing items.
  - Objective: Reach the Pokémon Center door at (23, 25) to heal our team.
  - Let's plan our immediate navigation steps using the grid coordinates.
  - Looking at the current screen:
    - (18, 0) to (18, 4) is completely clear path (TYPE_3fe2).
    - If we walk Down 4 steps, we will land at (18, 4).
    - Let's execute this: Down 4 times to reach (18, 4).
- Turn 1627: We are at (18, 0) facing Down. SQUIRTLE (GEMMY) is at 10/24 HP. PIDGEY (BIRBIE) is at 13/18 HP.
  - Let's check our path south:
    - Row 0: Column 18 is (18, 0) TYPE_3fe2 (where we are).
    - Row 1: Column 18 is (18, 1) TYPE_3fe2.
    - Row 2: Column 18 is (18, 2) TYPE_3fe2.
    - Row 3: Column 18 is (18, 3) TYPE_3fe2.
    - Row 4: Column 18 is (18, 4) TYPE_3fe2.
  - So walking Down 4 steps is completely clear!
  - Let's press Down 4 times to reach (18, 4).
- Turn 1629: Successfully arrived at (18, 4) in Viridian City, facing Down.
  - An NPC (SPRITE_578e) moved to (18, 5), directly blocking our path south.
  - Since we want to navigate south-east to the Pokémon Center at (23, 25), we will step Right to (19, 4) to bypass the NPC and move closer to column 23.
  - Plan: Step Right to (19, 4).
- Turn 1631: Arrived at (18, 8) in Viridian City facing Down. SQUIRTLE (GEMMY) is at 10/24 HP, PIDGEY (BIRBIE) is at 13/18 HP.
  - Looking at the current screen:
    - We are standing at (18, 8) (TYPE_3fe2).
    - To our right is a building with a green roof, door at (21, 9) (Trainer School).
    - To our left at (17, 9) is an orange-haired girl NPC.
    - Columns 18 and 19 are completely open down to row 12.
  - Plan: Move south along column 18 by pressing 'Down' 4 times to reach (18, 12).
- Turn 1634: Successfully arrived at (18, 12) facing Down. SQUIRTLE (GEMMY) is at 10/24 HP. PIDGEY (BIRBIE) is at 13/18 HP.
  - Let's check our surroundings on the screen:
    - We are standing at (18, 12) (TYPE_3fe2).
    - Directly to our right, columns 20-23 has building roofs/fences/structures.
    - Directly below us is clear path (18, 13) (TYPE_3fe2).
    - Looking further down, at row 14 and 15:
      - (20, 14) to (23, 14) is a green roof.
      - (21, 15) has a door with yellow light (which is the Trainer School, door is at (21, 15)).
      - Wait! Our map marker at (21, 15) is indeed the Trainer School! This explains why row 9 had another building—it was a different house, and this one at row 14-15 is indeed the Trainer School!
    - Let's check our path south:
      - (18, 13) is TYPE_3fe2 (clear).
      - (18, 14) is TYPE_3fe2 (clear).
      - (18, 15) is TYPE_3fe2 (clear).
      - (18, 16) is TYPE_3fe2 (clear).
      - (17, 13) is TYPE_3fe2 (clear).
      - (19, 13) is TYPE_3fe2 (clear).
    - So column 18 is completely clear down to row 16!
    - Let's walk Down 4 steps from (18, 12) to (18, 16).
    - Let's execute this.
- Turn 1635: Standing at (18, 12) facing Down. Looking at the screen:
  - We are at (18, 12).
  - Directly south: (18, 13) is TYPE_3fe2 (clear path).
  - To our right, row 13 has fence posts (TYPE_2889) at (20, 13), (21, 13), (22, 13), (23, 13).
  - Row 14 below row 13: (20, 14) to (23, 14) is a green roof.
  - Row 15: (21, 15) is the Trainer School door (with yellow light).
  - So columns 18 and 19 are completely open all the way down to row 16!
  - Let's trace our path Down:
    - Down to (18, 13)
    - Down to (18, 14)
    - Down to (18, 15)
    - Down to (18, 16)
  - All of these are clear path (TYPE_3fe2) with 0% encounter rate.
  - Let's step Down 4 times to reach (18, 16).
- Turn 1636: SQUIRTLE (GEMMY) is at 10/24 HP. PIDGEY (BIRBIE) is at 13/18 HP. Currently standing at (18, 12) facing Down.
  - Let's check our path south:
    - (18, 13) is TYPE_3fe2.
    - (18, 14) is TYPE_3fe2.
    - (18, 15) is TYPE_3fe2.
    - (18, 16) is TYPE_3fe2.
    - (17, 13) is TYPE_3fe2.
    - (19, 13) is TYPE_3fe2.
  - No NPC blocks column 18.
  - Let's walk Down 4 steps to (18, 16).
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