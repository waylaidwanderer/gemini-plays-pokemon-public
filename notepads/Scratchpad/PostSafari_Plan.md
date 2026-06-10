# Post-Safari Zone Route & Progression Plan

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 78160)
- **Active Exploration Mission**: Locate and retrieve the Secret Key on B1F.
- **Switch Matrix (State A vs. State B)**:
  - We have toggled Statue 2 (2F, (2, 11)) back to **State A** (Default) on Turn 77818.
  - State A: Gate 1 on 1F (25, 13) is CLOSED, blocking foot access to the Southeast room.
  - State A: Gate 3 on 2F (18, 8)-(19, 8) is OPEN.
  - State A: Gate 4 on 1F East (21, 17) is OPEN.
  - State A: Gate 6 on 2F (9, 4)-(9, 5) is CLOSED.

## Cinnabar Gym Blaine Matchup Preparation Strategy
- **The Balcony Drop Paradox & On-Foot Basement Path (Turn 78267)**:
  - Systematically tested all five columns (1 to 5) of the 3F West southwest balcony on Row 17 under State A (Turns 77945-77965, and re-tested on Turn 78264). Every single column resulted in a bump, proving they are solid, impassable railings under State A.
  - Socratic Question 1 analysis: In vanilla Pokémon Red/Blue, the balcony drop on 3F is a scripted map transition (warp) that lands the player on 2F East in the isolated Southeast room, containing the stairs at (25, 14) down to 1F East South. Once on 1F East, they are inside the south-central pocket (Columns 21-23, Rows 18-27). Gate 4 at (21, 17) is OPEN under State A and CLOSED under State B.
  - If they dropped under State B, Gate 4 on 1F East would be closed, trapping them on 1F. Therefore, dropping under State A is mathematically mandatory.
  - But why are the railings solid on 3F under both states? Our new hypothesis: The landing tile on 2F East is blocked. In Generation 1, a ledge jump or balcony drop is completely blocked in the overworld if its landing tile is occupied.
  - On 2F East, there might be a gate at (25, 13) on 2F East that is closed under State A and open under State B, blocking the landing under State A, while under State B we are trapped anyway.

## Cinnabar Mansion B1F Progression Investigation
- **Disproven SW Balcony Drop**: All reachable columns (1 to 5) on Row 17 of 3F West southwest balcony are solid, impassable railings under State A and State B (Turns 77945-77965 and Turn 78264). We cannot drop down from the southwest balcony under State A or State B.
- **Active Hypotheses**:
  - We must determine how to reach 3F East to drop through Pit A at (11, 12).
  - Let's check Gate 2 (Column 11 on 3F) under both states to see if it can be opened, or if we can find a different balcony drop.
  - Wait, why is Column 12 Row 14 and 15 marked as TYPE_21ec (balcony drop/ledge) on 3F West? Let's check if there is an active balcony drop on the southeast of 3F West.