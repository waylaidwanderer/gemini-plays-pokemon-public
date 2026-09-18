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
## 2F East-West Separation (Empirical Proof Turns 53520-53525)
- Row 10 is a solid horizontal rock barrier across cols 10-19.
- 2F map boundary ends at Y=15; no southern passage exists around (14, 15).
- East sector of 2F is isolated from West sector; traversing to SW Ladder (3, 11) requires 1F water network.
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
## Verified 1F Water Network & Shoreline Access (Turn 53541)
- Upper terrace (Row 6) is an elevated cliff above Row 5 water.
- Ground level shoreline is at (24..25, 11) facing water basin at (24..25, 10).
- Access to ground level: from upper terrace, walk south to (21, 11) and hop down ledge to (21, 12) -> (24, 12) -> (24, 11).
- From (24, 10), water canal spans east to cols 28-29, which run north to Row 5 northern lake.
- Row 5 northern lake extends west across the entire cave to cols 2-3, connecting south to SW Ladder at (3, 11).
- SW Ladder (3, 11) leads directly to 2F SW Sector -> Ladder A (1, 3) -> B1F Mewtwo!