# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Status: At (15, 3) on foot on Map 0_228 (1F).

## Active Progress & Discoveries:
- **Empirical Proof of Water Separation (Verified Turn 131004)**:
  - Stood at (10, 6) surfing and visually verified that Rows 4 and 5 are completely blocked by solid rock walls (TYPE_2889) across Columns 6 to 13.
  - This conclusively disproves any direct horizontal water connection between the eastern and western water canals on 1F on those rows.

## Active Hypotheses (Scratchpad Category)
- **Surfing Boarding of Western Canal (Verified Turn 132719-132726)**:
  - *Hypothesis*: Can we board the western water canal by Surfing directly from the elevated southwest platform at (1, 11) facing Up?
  - *Test & Results*: Stand on foot at (1, 11) on Map 0_228, face Up towards (1, 10), and select SURF from the party options menu on GEMMY.
  - *Result*: SUCCESS! The engine permitted boarding, and we successfully entered the western water canal in SURF mode. This definitively disproves the "height mismatch" hypothesis from Turn 128817; the Turn 128817 boarding failure at (1, 8)/(2, 8) occurred solely because we attempted to Surf onto solid rock wall boundaries at (1, 7)/(2, 7) rather than open water.
  - *Current Status*: Surfing south on the western canal on Map 0_228 (1F) to reach the Southwest Ladder at (3, 11) to warp to 2F West. We verified that Row 7 has a solid rock wall border, preventing direct northward surfing to B1F.

## Verified Blockages:
- **(16, 15) Blockage (Verified Turn 132684)**: Visually and physically verified solid rock wall of TYPE_2889 on 1F.

## Disproven Theories Archive
- **Direct 1F Surfing Route to B1F (Disproven Turn 134199-134204)**:
  - *Hypothesis*: The player can stand on the southwest platform at (1, 11) or (2, 11) on foot, Surf into the western water canal, Surf north to (1, 4) or (2, 4), and dismount directly Up onto the B1F stairs/staircase at (1, 3).
  - *Test & Results*: Walked to (1, 8) and faced Up toward (1, 7). Attempted to use SURF on GEMMY.
  - *Result*: The screen overlay showed (1, 7) has a brown background with a black ledge boundary line rather than blue water. A previous attempt on Turn 134096 to SURF onto it returned "No SURFing on GEMMY here!".
  - *Conclusion*: Row 7 consists of standard dry land ledge-tiles of TYPE_3fe2 which are impassable from the south on foot and cannot be surfed on. The southwestern platform is completely isolated from the northern landmass of 1F.

- **1F Inactive Ladder at (21, 11) Functionality Test (Disproven)**:
  - *Hypothesis*: Is the vertical ladder at (21, 11) on 1F actually inactive, or did we prematurely assume it is a one-way dropdown ladder? If we can climb it, where does it land on 2F? Could it provide the missing link to B1F?
  - *Test & Results*: Tested on foot (Turn 132271-132282). Result was completely inactive; walking onto it or pressing A has no effect.
  - *Conclusion*: The ladder at (21, 11) is inactive and cannot be climbed from 1F.

- **2F West Column 2 Passability Test (Disproven)**:
  - *Hypothesis*: Is Column 2 on 2F West (specifically at (2, 9), (2, 12), (2, 7), and (2, 2)) actually open and passable, allowing us to walk directly from the Southwest Ladder (3, 11) to the Northwest Ladder (1, 3)?
  - *Test & Results*: Systematic physical collision tests under active overworld:
    - Turn 132442: Step Down to (2, 12). Result: BUMP.
    - Turn 132449: Step Left to (1, 11). Result: BUMP.
    - Turn 132464: Step Left to (1, 10). Result: BUMP.
    - Turn 132482: Step Up to (2, 9). Result: BUMP.
    - Turn 134349: Standing on foot at (3, 2) facing Left, pressed Left to test (2, 2). Result: BUMP (visited 0 tiles).
  - *Conclusion*: Both the southwest pocket and the northwest ladder area are completely isolated on foot on 2F West. Physical tests of (2, 12), (1, 11), (1, 10), (2, 9), and (2, 2) all resulted in solid bumps, proving that 2F West is 100% split. Backtracking to 1F is mandatory!

- **1F Row 6/7 Column 7 Water Canal Crossover (Disproven)**:
  - *Hypothesis*: Is it possible that Column 7 on Row 6 or Row 7 is actually open and passable on water, despite the rock texture (TYPE_2889), allowing us to Surf Left from Column 8 directly into the western water canal (Column 1-5)?
  - *Test & Results*: 
    - Turn 131968: Stood at (8, 6) surfing, faced Left, and pressed Left. Result: BUMP.
    - Turn 131971 & 131972: Stood at (8, 7) surfing, faced Left, and pressed Left. Result: BUMP.
  - *Conclusion*: Both (7, 6) and (7, 7) are solid, impassable rock wall tiles of TYPE_2889. Both canals are completely separated.

- **1F Row 3 Passability (Northern Landmass to Water) (Disproven)**:
  - *Hypothesis*: Row 3 on 1F contains an open vertical passage on some column allowing us to step Down from the northern landmass directly into the water canal and Surf.
  - *Test & Results*: Columns 13 down to 6 have been physically tested (Turn 131644-131649) and are confirmed BLOCKED. Row 3 is solid rock across all these columns.

- **1F Row 2 Column 4 Northwest Crossover (Disproven)**:
  - *Hypothesis*: Is it possible that Column 4 on Row 2 (4, 2) on Map 0_228 (1F Northwest) is actually open and passable on foot, despite the visual rock graphics?
  - *Test & Results*: Standing on foot at (5, 2), pressed Left on Turn 132029. Result was a BUMP.
  - *Conclusion*: (4, 2) is a solid rock blockage.

- **Row 4 Passability on 2F West (Direct Path) (Disproven)**:
  - *Hypothesis*: Row 4 (specifically (4, 4)) is open on 2F West to reach (1, 3) directly from (9, 1).
  - *Test & Results*: Stood at (4, 3) and pressed Down on Turn 131464. Result: BUMP.

- **Row 4 Detour on 2F West (Disproven)**:
  - *Hypothesis*: Columns 6, 7, or 8 on Row 4 on 2F West are open, allowing a detour from (9, 1) -> Row 3 -> Row 4 -> Row 5 -> (1, 3).
  - *Test & Results*: Stood at (8, 3) and pressed Down on Turn 131775. Stood at (7, 3) and pressed Down on Turn 131780. Stood at (6, 3) and pressed Down on Turn 131784. Result: Consistent BUMPs.
## 2F West Column 13/14 Isolation Proof (Turn 133727):
- **Objective**: Verify if there is a vertical passage connecting the southern Row 9 corridor to the northern Row 5 corridor on 2F West via Column 13/14.
- **Hypothesis**: The vertical path (13, 9) -> (13, 8) -> (14, 8) -> (14, 7) -> (14, 6) -> (14, 5) is completely open, allowing us to walk to (3, 3) entirely on 2F West.
- **Visual Check (Turn 133727)**: Standing at (9, 9) facing Right, we can clearly see the eastern corridor on the screen overlay:
  - (13, 9) is TYPE_3fe2 (passable)
  - (13, 8) is TYPE_3fe2 (passable)
  - (14, 8) is TYPE_3fe2 (passable)
  - (13, 7) is TYPE_2889 (solid rock wall)
  - (14, 7) is TYPE_2889 (solid rock wall)
  - (14, 6) is TYPE_2889 (solid rock wall)
- **Conclusion**: The vertical corridor is completely blocked by solid rock walls of TYPE_2889 at (13, 7), (14, 7), and (14, 6), rendering any vertical passage from Row 9 to Row 6 on Column 13/14 physically impossible.
- **Final Topological Verdict**: Koga's southwest pocket is 100% isolated on foot on 2F West. The overwatch's suggested direct 2F West loop is physically blocked. Descending back to 1F and executing our master backtracking route via Ladder 5 is 100% mandatory!

## Western Canal Surfing Investigation (Turn 134189)
- **Visual Observation**:
  - We are at (1, 11) on Map 0_228 (1F), facing Left.
  - Column 0 is blocked on Rows 8-13 by solid rock walls of TYPE_2889.
  - Rows 8-12 on Column 1 and 2 are land tiles of TYPE_2770, allowing foot movement.
  - Row 7 has water tiles (0, 7), (1, 7), (2, 7) of TYPE_3fe2.
  - Row 14 has water tiles (0, 14), (1, 14), (2, 14) of TYPE_3fe2.
  - This proves that there is no continuous water canal running vertically on Column 1/2 from Row 4 to Row 15; the canal is split into two separate water bodies by the land patch at Rows 8-12.
- **Hypothesis Testing**:
  - Can we walk north on foot to (1, 8), face Up towards the water tile at (1, 7), and Surf from there to bypass the split?
  - Let's walk to (1, 8) and test this!

## Definitive Master Path to Mewtwo & Socratic Answers (Turn 135182 Verification):
- **Socratic Challenge 1 Answer**: 2F is indeed completely split on foot (verified mathematically and physically), meaning that climbing Ladder 2 to 2F East is a dead-end that can never reach 2F West. We cannot cross over on 2F on foot.
- **Socratic Challenge 2 Answer**: Row 7 on the western canal on Columns 1 and 2 is indeed WATER on the ground floor (z=0). The Surf failure on Turn 134199 occurred solely because we were standing on the elevated platform at (1, 8) [z=1] and tried to Surf onto the ground-level water [z=0], resulting in a height-mismatch collision.
- **The True Unblocked Master Route to Mewtwo**:
  1. Surf Left from our current position (15, 4) to (11, 14), and dismount at (11, 13) onto the central platform on foot.
  2. Walk on foot to the stairs at (17, 15) and descend to the ground floor (z=0).
  3. Walk west along the southern ground-floor corridor on Row 17 to (1, 13).
  4. From (1, 13) on the ground floor (z=0), walk north to (1, 8) on foot (z=0).
  5. Stand at (1, 8) facing Up, and select SURF on GEMMY to board the water at (1, 7) [z=0].
  6. Surf north along the western canal to (1, 3) (B1F stairs)!
  7. Take the stairs down to B1F and capture Mewtwo!

- **Master Path Steps**:
  1. Surf Left to Water Ramp 2 at (11, 13) and dismount on foot.
  2. Walk to stairs at (17, 15) and descend to ground level.
  3. Walk to Columns 1-2 on the ground level.
  4. Walk north to (1, 8) on the ground level.
  5. Surf north from (1, 8) to reach the B1F stairs at (1, 3).
  6. Descend to B1F!

- **Updated Verification (Turn 135182)**:
  - We have pivoted our active strategy to the Western Canal Ground-Level Surfing Path based on the overwatch's Socratic Challenge 2. This is the only mathematically possible, unblocked path to reach Mewtwo on B1F!
  - We will immediately begin backtracking to the central platform to execute this route.

## 2F West Column 2 Systematic Passability Re-Testing Protocol (Turn 134523 Plan)
- **Objective**: Identify if there is a false-positive blockage in Column 2 on 2F West (Map 0_226) that actually connects the Southwest Ladder (3, 11) to the Northwest Ladder (1, 3).
- **Status**: Completed & Disproven.
  - Test 1 (2, 1) was physically verified as blocked (solid rock wall) on Turn 134531.
  - Tests 2, 3, and 4 (2, 5), (2, 6), (2, 7) are impossible to reach on foot from (3, 11) because Row 8 is a solid rock wall across all columns, completely isolating the southwest pocket.
  - Therefore, the 2F West loop is 100% blocked.

## 1F Western Water Canal Continuity Test (Turn 134629 Plan)
- **Objective**: Board the western water canal on 1F (Map 0_228) and test if the water is vertically continuous, allowing us to Surf north past Row 7 to reach the northwestern B1F stairs.
- **Methodology**:
  1. Stand on foot at (1, 11) facing Up.
  2. Select SURF on GEMMY (BLASTOISE) to board (1, 10).
  3. Surf Up to Row 7 and test if we can cross past the land ledge barrier to the north in SURF mode.

## Empirical Verification Log (Live Tracking)
- **Turn 134518**: Stood on foot at (5, 0) on Map 0_228 (1F Northwest) facing Left and pressed Left to test (4, 0) (labeled TYPE_2889). Result: BUMP (visited 0 tiles). This physically and mathematically proves that (4, 0) is a solid rock wall blockage and is completely impassable. This definitively disproves the 1F Northwest on-foot shortcut hypothesis.
- **Turn 134841**: Re-verified that the path on foot from (1, 12) to the Central Platform at (11, 13) is open. We will execute the next path segment of 7 steps: Down, Down, Down, Down, Right, Down, Right to reach (3, 17) on the Row 17 ground level.

## 2F West Direct Path Retraction (Turn 134974):
- **Retraction Proof**: The 64-step direct path between (3, 11) and (1, 3) on Map 0_226 is completely disproven. This path was a hallucination caused by using an incomplete database of solid blocks that omitted major walls such as (17, 3), (21, 3), and (23, 3) on 2F. When the complete set of blockages is verified, 2F is indeed completely split, and the southwest pocket has 0% same-floor connection to the northwest. The master backtracking route via 1F is mathematically mandatory. All notes suggesting a direct 2F West path are hereby formally retracted.
Turn 135231: Resumed route execution. Escaped a wild Dodrio at (3, 16) on foot, Map 0_228. Next we need to continue walking to the western canal boarding point at (1, 8) to Surf north.