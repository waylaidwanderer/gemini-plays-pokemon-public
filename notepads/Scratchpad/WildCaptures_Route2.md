# Scratchpad: Wild Captures and Leveling Goals

## High-Level Strategy:
- Active Grinding Phase (Started Turn 910)
- Pivot Strategy (Turn 1411): After 42 cumulative steps on Route 2 Columns 8 & 9 (Rows 61-67) with 0 encounters, we hypothesize that encounters on this specific grass patch might be disabled or extremely rare. We are pivoting to explore north towards Viridian Forest to find active wild encounters.

## Live Status:
- Turn 1670: GEMMY (SQUIRTLE) is at 10/24 HP (Level 7). BIRBIE (PIDGEY) is at 13/18 HP (Level 4). Currently at (4, 4) inside Viridian City Pokémon Center, standing directly in front of Nurse Joy.
- Money: ¥1075.
- Inventory: 8 Poké Balls, 1 Antidote, 1 Town Map.
- Location: Viridian City Pokémon Center (Map 0_41) at (4, 4) facing Up.
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