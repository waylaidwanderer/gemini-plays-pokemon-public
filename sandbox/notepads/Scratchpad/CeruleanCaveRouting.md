# Scratchpad: Cerulean Cave Routing & Frontier Ledger

## 2F Sector Isolation Proofs
1. **2F East Sector (cols 19-29)**: Contains Ladder D (29, 1), Ladder B (22, 6), Ladder C (19, 7).
   - Blocked to the west by solid vertical rock wall along Column 19 (rows 0-8) and Column 13/14 (rows 10-14).
   - Blocked to south on row 9 at (22, 9) rock wall (Turn 52217 collision proof).
   - No direct 2F path from Ladder B or Ladder C to Ladder A (1, 3).
2. **2F Northwest Sector (cols 3-9, rows 0-3)**: Contains Ladder E (7, 1).
   - Blocked to west by solid rock wall along Column 2 (rows 1-4) and Row 4 (cols 3-7).
3. **2F Southwest Sector (cols 0-7, rows 0-11)**: Contains SW Ladder at (3, 11) and Ladder A at (1, 3) (descends to B1F Mewtwo). Isolated from Northwest Sector (Ladder E) by solid rock wall along Column 2. Must be reached via SW Ladder (3, 11) from 1F.

## 2F Northwest Sector Isolation (Empirical Proof Turns 52941-52980)
- The sector containing Ladder E (9, 1) spanning (3..9, 1..5) is completely enclosed and isolated from the rest of 2F by solid rock barriers at (2, 1..3), (6, 4), (7, 4), (8, 4), (8, 5), and (9, 6).
- Ladder E does NOT lead to Ladder A (1, 3).

## Verified True Route to B1F (Mewtwo)
- Ladder A (1, 3) on 2F is located in the Southwest Sector, which is accessible ONLY via the SW Ladder at (3, 11) from 1F.
- Plan:
  1. Take Ladder C at (19, 7) or Ladder B at (22, 6) down to 1F.
  2. Surf across 1F waterways to the Southwest Sector (cols 1-6, rows 8-15).
  3. Locate the landing/passage into SW Ladder at (3, 11).
  4. Climb SW Ladder (3, 11) to 2F SW Sector.
  5. On 2F, walk north along Column 0/1 to Ladder A (1, 3).
  6. Descend Ladder A into B1F Mewtwo's Chamber!
## Row 9 Bypass Route Verified (Turn 53520)
- The rock at (14, 9) blocking Row 9 is bypassed via: (18, 11) -> Up to (18, 9) -> West to (15, 9) -> Up to (15, 8) -> West to (13, 8) -> Down to (13, 9).
- From (13, 9), Row 9 continues straight west across cols 13..3 into the Southwest Sector towards Ladder A at (1, 3) leading to B1F Mewtwo!
## Verified Southern Corridor Bypass (Turn 53521)
- Row 10 is a solid horizontal rock barrier across cols 10-19.
- Southern Bypass Route: From (14, 13) -> Right to (15, 13) -> Down col 15 to (15, 17) -> West row 17 to (11, 17) -> Up to (11, 16) -> Left to (10, 16) -> Up to (10, 14).
- From (10, 14), path leads west into the Southwest Sector towards SW Ladder (3, 11) and Ladder A (1, 3) to B1F Mewtwo!
## Verified 1F Surf Route to SW Ladder & Mewtwo (Turn 53525)
- 2F East Sector is completely isolated from West Sector (Y=15 is bottom map boundary, Row 10 is solid rock).
- The true canonical route to Mewtwo:
  1. Take Ladder B at (22, 6) down to 1F (23, 7).
  2. Walk north to 1F lake at Row 5.
  3. Use Surf to travel west across 1F lake to cols 1-3.
  4. Surf south along the western channel to SW landing at (3, 11).
  5. Climb SW Ladder (3, 11) to 2F SW Sector.
  6. Walk north along Col 1 to Ladder A at (1, 3).
  7. Descend Ladder A into B1F Mewtwo's Chamber!