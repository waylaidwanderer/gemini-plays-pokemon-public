# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Turn: 132339
- Current Position: at (11, 14) on Map 0_228 (1F)

## Active Progress & Discoveries:
- **Empirical Proof of Water Separation (Verified Turn 131004)**:
  - Stood at (10, 6) surfing and visually verified that Rows 4 and 5 are completely blocked by solid rock walls (TYPE_2889) across Columns 6 to 13.
  - This conclusively disproves any direct horizontal water connection between the eastern and western water canals on 1F on those rows.

## Active Hypotheses (Scratchpad Category)
- **1F Ladder at (21, 11) Functionality Test (Active Hypothesis)**:
  - *Hypothesis*: Is the vertical ladder at (21, 11) on 1F actually inactive, or did we prematurely assume it is a one-way dropdown ladder? If we can climb it, where does it land on 2F? Could it provide the missing link to B1F?
  - *Methodology*: Head to (21, 11) on foot and attempt to interact with/climb it.
  - *Status*: COMPLETE. Empirically disproved: the ladder at (21, 11) is inactive and cannot be climbed from 1F. Systematic testing (Turn 132271-132282) confirmed that walking onto it from any direction (north/south) does not trigger a warp, and interacting with 'A' has no effect.

- **2F West Column 2 Passability Test (Active Hypothesis)**:
  - *Hypothesis*: Is Column 2 on 2F West (specifically at (2, 9), (2, 12), and (2, 7)) actually open and passable, allowing us to walk directly from the Southwest Ladder (3, 11) to the Northwest Ladder (1, 3)? If Column 2 is open, we can reach the B1F stairs on foot without any complex backtracking loops!
  - *Methodology*: Head to Southwest Ladder 6, climb to 2F West, stand at (3, 9) and (3, 12) and systematically attempt to walk Left into Column 2, logging the result of every physical test.
  - *Status*: ACTIVE. Currently surfing on water at (11, 7) on Map 0_228 (1F), backtracking to Water Ramp 2 at (11, 13) to land on foot and proceed to Southwest Ladder 6.

- **1F Row 6/7 Column 7 Water Canal Crossover (Disproven)**:
  - *Hypothesis*: Is it possible that Column 7 on Row 6 or Row 7 is actually open and passable on water, despite the rock texture (TYPE_2889), allowing us to Surf Left from Column 8 directly into the western water canal (Column 1-5)?
  - *Methodology*: Surf from current position to (8, 6) or (8, 7) on water, face Left, and attempt to Surf Left into Column 7 to verify passability.
  - *Test & Results*: 
    - Turn 131968: Stood at (8, 6) surfing, faced Left, and pressed Left. Result: BUMP (visited 0 tiles).
    - Turn 131971 & 131972: Stood at (8, 7) surfing, faced Left, and pressed Left. Result: BUMP (visited 0 tiles).
  - *Conclusion*: Both (7, 6) and (7, 7) are solid, impassable rock wall tiles of TYPE_2889. There is absolutely no horizontal water canal crossover on Row 6 or Row 7 from Column 8 to Column 5. Both canals are completely separated.

- **1F Row 3 Passability (Northern Landmass to Water)**:
  - *Hypothesis*: Row 3 on 1F contains an open vertical passage on some column (e.g. Column 12, 11, 10, 9, 8, 7, 6, 5) allowing us to step Down from the northern landmass directly into the water canal and Surf to (1, 3) on foot.
  - *Methodology*: Walk Left along Row 2 or Row 1, and systematically attempt to step Down (South) on each column to test passability. We will log the results.
  - *Status*: Columns 13 down to 6 have been physically tested (Turn 131644-131649) and are confirmed BLOCKED. Row 3 is solid rock across all these columns.

## Disproven Theories Archive
- **1F Row 2 Column 4 Northwest Crossover (Disproven)**:
  - *Hypothesis*: Is it possible that Column 4 on Row 2 (4, 2) on Map 0_228 (1F Northwest) is actually open and passable on foot, despite the visual rock graphics?
  - *Test & Results*: Standing on foot at (5, 2), pressed Left to step onto (4, 2) on Turn 132029. Result was a BUMP (visited 0 tiles).
  - *Conclusion*: (4, 2) is a solid rock blockage. Both (4, 1) and (4, 2) are completely impassable. There is no direct horizontal land crossover on Row 1 or 2.
- **Row 4 Passability on 2F West (Direct Path)**:
  - *Hypothesis*: Row 4 (specifically (4, 4)) is open on 2F West to reach (1, 3) directly from (9, 1).
  - *Test*: Stood at (4, 3) on 2F West facing Left and pressed Down on Turn 131464.
  - *Result*: BUMP (visited 0 tiles). Disproven. Row 4 is completely impassable. Moving from Ladder 5 on 2F West to Northwest Ladder (1, 3) directly on foot is impossible.
- **Row 4 Detour on 2F West**:
  - *Hypothesis*: Columns 6, 7, or 8 on Row 4 on 2F West are open, allowing a detour from (9, 1) -> Row 3 -> Row 4 -> Row 5 -> (1, 3).
  - *Test*: Stood at (8, 3) and pressed Down on Turn 131775. Stood at (7, 3) and pressed Down on Turn 131780. Stood at (6, 3) and pressed Down on Turn 131784.
  - *Result*: Consistent BUMPs on all three columns. Disproven. Row 4 is completely impassable across all Columns 3 to 8 on 2F West.
- Turn 131589: Discovered (3, 7) on 1F is a solid rock wall blockage (TYPE_2889).
- Turn 131591: Confirmed via screen overlay that (3, 7) is indeed TYPE_2889.
- Turn 131838: Verified on-screen that Row 5 Columns 8-13 is completely blocked by TYPE_2889 solid rock walls. Columns 10, 11, and 12 are definitively blocked. There is absolutely no horizontal water canal crossover on Row 5 between Column 8 and Column 13 on 1F.