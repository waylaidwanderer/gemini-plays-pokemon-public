# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Status: Standing at (3, 11) on foot on Map 0_226 (2F West). Southwest Ladder 6 successfully ascended! We are mapping out the route on 2F West to reach Northwest Ladder 5 at (1, 3). No Surfing needed!

## Verified Topological Proof of B1F Access:
- **1F Northwest Isolation Proof (Turn 133595)**:
  - Row 3 on 1F (Map 0_228) is a continuous, solid rock wall of TYPE_2889 from Column 1 to Column 12, blocking vertical on-foot or surfing transitions from Row 4.
  - Column 4 on 1F is completely blocked on Rows 0-2 on foot by solid rock walls at (4, 1) and (4, 2), blocking horizontal on-foot access from the eastern side.
  - Therefore, the northwest landmass (Rows 0-2, Columns 1-3) on 1F is 100% isolated on foot and from water on 1F.
  - **Socratic Solution**: To reach the B1F stairs, we MUST use Southwest Ladder 6 at (3, 11) on 1F to ascend to 2F West, navigate the open 34-step path on 2F West to the Northwest Ladder at (1, 3), and descend it. This lands us directly on the isolated northwest landmass of 1F where the B1F stairs are located. Dismounting directly onto (2, 3) from water is impossible because (2, 3) is solid rock wall.

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