## Mansion B1F Access Model & Route Analysis

- **State A (Statue 2 Default)**:
  - Gate 4 on 1F East (21, 17) is OPEN.
  - The stairs to B1F are located at (21, 23) on 1F East.
  - To reach these stairs under State A on foot, we must find an open vertical pathway from 1F West through 1F East that bypasses the Row 13 wall barrier.
  - *Proposed Pathway to Test*: We can cross from 1F West to 1F East along Row 11 on foot. Let's systematically test Row 13 Column 26, 27, and 28 in the Northeast room of 1F East under State A to see if any of these columns are open and passable, allowing us to walk south to the southern half of 1F East, then walk west to Gate 4, and south to the B1F stairs.

## Disproven Path Models:
- **Disproven Model (State B Pit Drop Route)**:
  - We previously hypothesized falling through 3F West Pit A, traversing 2F East South, and taking the southeast stairs down to 1F.
  - However, physical testing has proved that Column 24 is a solid wall on Rows 19-24 and Gate 4 is closed under State B, meaning the 1F Southeast room is completely isolated from the B1F stairs.
  - Thus, the State B Pit Drop Route is DEFINITIVELY DISPROVEN.

- **Turn 84175 Column 26 Row 13 Passability Test (State A)**:
  - Methodology: Stood at (26, 12) facing Down under State A, and pressed Down to attempt to step onto (26, 13) (`TYPE_2889`).
  - Result: **Bump** (0 tiles visited), remaining at (26, 12) facing Down.
  - Conclusion: Column 26 Row 13 is 100% solid and impassable under State A.

- **Turn 84178 Column 27 Row 13 Passability Test (State A)**:
  - Methodology: Stood at (27, 12) facing Down under State A, and pressed Down to attempt to step onto (27, 13) (`TYPE_2889`).
  - Result: **Bump** (0 tiles visited), remaining at (27, 12) facing Down.
  - Conclusion: Column 27 Row 13 is 100% solid and impassable under State A.

- **Turn 84182-84186 Column 28 Row 13 Passability Test (State A)**:
  - Methodology: Stood at (28, 12) facing Down under State A, and pressed Down to attempt to step onto (28, 13) (`TYPE_2889`).
  - Result: **Bump** (0 tiles visited), remaining at (28, 12) facing Down. Repeated 4 times to ensure complete empirical verification.
  - Conclusion: Column 28 Row 13 is 100% solid and impassable under State A.

## Final Row 13 Passability Conclusion under State A
- Every column of Row 13 on 1F East (Columns 21, 23, 24, 25, 26, 27, 28) has now been physically and systematically tested on foot under State A and proven 100% solid and impassable.
- This definitively disproves the hypothesis of an on-foot corridor bypass under State A. The northern half of 1F East is completely separated from the southern half under State A.
- Therefore, there is NO on-foot path to the B1F stairs on 1F under State A. We must find another way.

## Breakthrough Discovery: State A 2F East South Balcony Drop Route (Turn 84261)
- **The Core Overlook**: We previously concluded that the southern balcony of 2F East South on Columns 11-17 was "100% physically and mathematically unreachable on foot under State A." This proof of unreachability was FLAWED because it completely overlooked the Column 11 Row 22 crossover!
- **The Proof**: On Turn 80595, we physically crossed Column 11 Row 22 on foot under State A and successfully entered the Column 12 corridor on 2F East South at (12, 22). 
- **The Path**: From (12, 22) under State A, we can simply walk north along Column 12 to Y=15/16. This grants us 100% foot access to the southern balcony of 2F East South on Columns 11-17 under State A!
- **The Balcony Drop**: In vanilla Pokémon, the southern balcony of 2F East South contains a jumpable gap in the railing on Columns 11-17 (around Y=15/16). Walking Down (South) off the correct column will trigger a vertical drop, landing us directly in the south-central pocket of 1F East.
- **B1F Access**: Since we are in State A, Gate 4 at (21, 17) on 1F East is OPEN, allowing us to walk directly to the B1F stairs at (21, 23) and descend to B1F!
- **Action Plan**:
  1. Return to 2F West.
  2. Toggle Mewtwo Statue 2 at (2, 11) to State A.
  3. Walk East along Row 11 of 2F West, crossing Column 11 Row 22 on foot under State A to reach (12, 22).
  4. Walk North along Column 12 to Row 15/16.
  5. Systematically test walking Down (South) off Columns 11-17 on Rows 15/16 to find the active balcony drop!