# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Turn: 132551
- Current Position: standing on foot at (11, 13) on Map 0_228 (1F)

## Active Progress & Discoveries:
- **Empirical Proof of Water Separation (Verified Turn 131004)**:
  - Stood at (10, 6) surfing and visually verified that Rows 4 and 5 are completely blocked by solid rock walls (TYPE_2889) across Columns 6 to 13.
  - This conclusively disproves any direct horizontal water connection between the eastern and western water canals on 1F on those rows.

## Active Hypotheses (Scratchpad Category)
- **Surfing Crossover to Northwest Ladder (Active Hypothesis)**:
  - *Hypothesis*: Can we surf directly to the B1F entrance area on Map 0_228 (1F) from Water Ramp 2 at (11, 13) without needing to navigate any other floors?
  - *Methodology*: From Water Ramp 2 at (11, 13), initiate SURF, and navigate through the water canals on Rows 4-5 towards Column 1.
  - *Status*: ACTIVE. We have reached Water Ramp 2 and are currently opening the menu to initiate Surf.

## Disproven Theories Archive
- **1F Ladder at (21, 11) Functionality Test (Disproven)**:
  - *Hypothesis*: Is the vertical ladder at (21, 11) on 1F actually inactive, or did we prematurely assume it is a one-way dropdown ladder? If we can climb it, where does it land on 2F? Could it provide the missing link to B1F?
  - *Test & Results*: Tested on foot (Turn 132271-132282). Result was completely inactive; walking onto it or pressing A has no effect.
  - *Conclusion*: The ladder at (21, 11) is inactive and cannot be climbed from 1F.

- **2F West Column 2 Passability Test (Disproven)**:
  - *Hypothesis*: Is Column 2 on 2F West (specifically at (2, 9), (2, 12), and (2, 7)) actually open and passable, allowing us to walk directly from the Southwest Ladder (3, 11) to the Northwest Ladder (1, 3)?
  - *Test & Results*: Systematic physical collision tests under active overworld:
    - Turn 132442: Step Down to (2, 12). Result: BUMP.
    - Turn 132449: Step Left to (1, 11). Result: BUMP.
    - Turn 132464: Step Left to (1, 10). Result: BUMP.
    - Turn 132482: Step Up to (2, 9). Result: BUMP.
  - *Conclusion*: Koga's southwest pocket is 100% isolated on foot on 2F West. Backtracking to 1F is mandatory.

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