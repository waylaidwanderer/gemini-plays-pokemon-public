# Scratchpad: Wild Captures and Leveling Goals

## High-Level Strategy:
- Active Grinding Phase (Started Turn 910)

## Live Status:
- Turn 1141: SQUIRTLE is at 21/24 HP (Level 7).
- Money: ¥1075.
- Inventory: 10 Poké Balls, 1 Antidote, 1 Town Map.
- Location: Route 2 (Map 0_13) at (8, 65) facing Up.
- Grinding Phase Started: Turn 910

## Active Team & Captures Checklist:
- [ ] Pidgey (Target Level 8-10) - Status: Not Captured
- [ ] Rattata (Target Level 8-10) - Status: Not Captured
- [ ] Caterpie (Target Level 10 Butterfree) - Status: Not Captured
- [x] GEMMY (SQUIRTLE) - Level: 7 (Goal: Level 10)

## Route 2 Wild Encounters Strategy:
- Active Patrol: Currently patrolling the tall grass patch on Columns 8 & 9 (Rows 61 to 67) to find wild Pokémon.
- Verified tall grass tile appearance: Grey vertical tufts (TYPE_3fe2).
- Verified decorative path flowers: Red flowers (TYPE_3fe2), which do not trigger wild encounters.

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

## Encounter Rate Tracking (Columns 8 & 9 Tall Grass)
- **Methodology**: Record the number of active steps taken on tall grass tiles (TYPE_3fe2, with vertical grey grass tufts) in Route 2, and log each encounter that is triggered, along with the turn number and wild Pokémon details.
- **Log**:
  - Turn 1052: GEM arrived at (8, 66) (Tall Grass tile, TYPE_3fe2).
  - Turn 1057: Step 1. Moved Up from (8, 66) to (8, 65). Result: No encounter.
  - Turn 1065: Step 2. Moved Up from (8, 65) to (8, 64). Result: No encounter.
  - Turn 1068: Step 3. Moved Up from (8, 64) to (8, 63). Result: No encounter.
  - Turn 1078: Step 4. Moved Up from (8, 63) to (8, 62). Result: No encounter.
  - Turn 1083: Step 5. Moved Right from (8, 62) to (9, 62). Result: No encounter.
  - Turn 1093: Step 6. Moved Down from (9, 62) to (9, 63). Result: No encounter.
  - Turn 1094: Step 7. Moved Down from (9, 63) to (9, 64). Result: No encounter.
  - Turn 1107: Step 8. Moved Down from (9, 64) to (9, 65). Result: No encounter.
  - Turn 1118: Step 9. Moved Down from (9, 65) to (9, 66). Result: No encounter.
  - Turn 1124: Step 10. Moved Down from (9, 66) to (9, 67). Result: No encounter.
  - Turn 1128: Step 11. Moved Left from (9, 67) to (8, 67). Result: No encounter.
  - Turn 1134: Step 12. Moved Up from (8, 67) to (8, 66). Result: No encounter.