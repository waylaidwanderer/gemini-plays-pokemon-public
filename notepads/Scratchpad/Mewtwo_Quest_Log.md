# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Status: At (1, 8) on Map 0_228 (1F).

## Verified Topological Proof of B1F Access:
- **Direct 2F West Loop (Disproven on Turn 133794)**: We verified that 2F West is 100% split and impassable on foot at (2, 3) due to a solid rock wall, so ascending via Southwest Ladder 6 does not connect to the Northwest Ladder on 2F West.

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

## Direct 1F Surfing Route to B1F Verification (Turn 133853)
- **Status**: Formulated the direct 1F surfing descent path to reach the B1F stairs. Since 2F West is confirmed to be split into isolated, impassable sections, we must use the western water canal on 1F (Map 0_228) to bypass all 2F West obstacles.
- **Hypothesis**: The player can stand on the southwest platform at (1, 11) or (2, 11) on foot, Surf into the western water canal, Surf north to (1, 4) or (2, 4), and dismount directly Up onto the B1F stairs/staircase at (1, 3).
- **Execution Plan**:
  1. From our current position on Water Ramp 2 at (11, 13) on foot, walk across the central platform to (17, 15).
  2. Descend the stairs at (17, 15) to reach (17, 16) on the ground.
  3. Walk west along Row 17 to (1, 13) and climb the wooden stairs up to the southwest platform.
  4. Stand at (1, 11) or (2, 11) on the southwest platform, face the water, and select SURF to board the western water canal.
  5. Surf north along the western water canal to (1, 4).
  6. Dismount Up onto (1, 3) to enter B1F directly!