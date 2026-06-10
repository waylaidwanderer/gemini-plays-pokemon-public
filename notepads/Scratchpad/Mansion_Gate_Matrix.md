# Pokémon Mansion Gate State Matrix (Turn 75980)
Active State: **State B (Statue 1 Toggled)** (Toggled on Turn 78020)

## State Table
| Gate ID & Location | State A (Statue 2 Default) | State B (Statue 2 Toggled) | Verification & Proof of Work |
| :--- | :--- | :--- | :--- |
| **Gate 1** (1F, (25, 13)) | **CLOSED** (Impassable) | **OPEN** (Passable) | State A: Verified CLOSED on Turn 75301 and Turn 75361. State B: Verified OPEN on Turn 75550 by walking through it to (25, 14). |
| **Gate 4** (1F, (21, 17)) | **UNREACHABLE on foot** (Hypothesized OPEN) | **CLOSED** (Impassable) | State A: Unreachable because Column 11 partition wall is solid (TYPE_2889) from Row 13 to Row 27, completely isolating 1F East from 1F West (Verified Turns 76184-76193). State B: Verified CLOSED (has orange/yellow horizontal bars) on Turn 75551. |
| **Gate 2** (3F, Col 11) | **CLOSED** (Impassable) | **CLOSED** (Impassable) | State A: Verified CLOSED (solid wall of TYPE_2889) on Turn 75091. Physical testing on Turns 76608 and 76610 proved that Column 9 is solid (TYPE_2889) on Rows 12 and 13 under State A. State B: Verified CLOSED (solid wall of TYPE_2889) on Turn 75612. Comprehensive empirical testing on Turns 76460-76492 proved that Column 10 is solid on Rows 8-15 and Column 9 is solid on Rows 12-13 under State B. Note: Under State B on 2F East, Row 8 is permanently solid across Columns 22-28, verified on Turn 76760 by attempting to step South from (28, 7) and colliding (0 tiles visited). This isolates the 2F East Southeast room on foot in both states. |
| **Gate 3** (2F, (18, 8)-(19, 8)) | **OPEN** (Passable) | **OPEN** (Passable) | State A: Verified OPEN (has open floor of TYPE_3fe2, visually clear) on Turn 75880 and physically walked through on Turn 79932 from (18, 7) to (18, 11). State B: Verified OPEN on Turn 78435 by physically walking through (18, 8) from (17, 6) to (18, 10). |
| **Gate 6** (2F, (9, 4)-(9, 5)) | **CLOSED** (Impassable) | **OPEN** (Passable) | State A: Verified CLOSED (has orange/yellow vertical bars of TYPE_a83b) on Turn 75868. State B: Verified OPEN on Turn 78038 by walking through it to 2F East North. |

## B1F Basement Gate Matrix (Added Turn 75980)
- This table tracks the circuitry state of the Basement (B1F) of Pokémon Mansion once we enter and locate statues/gates there.

| Gate ID & Location | State A (Statue 2 Default) | State B (Statue 2 Toggled) | Verification & Proof of Work |
| :--- | :--- | :--- | :--- |

## 2F East Mewtwo Statue 3 Discovery (Turn 78407)
- **Coordinates**: Mewtwo Statue 3 is located at (13, 9) on 2F East (Map 0_214).
- **Accessibility**: Reached on foot from the west by walking across the Column 9 wall on Row 10 at (9, 10). (9, 10) is a standard open floor tile (TYPE_3fe2) and is completely passable under State B.
- **Circuit Matrix Hypotheses to Test**:
  - We stood adjacent to Statue 3 at (12, 9) on Turn 78425. We faced Right (towards (13, 9)) and pressed A to toggle the switch.
  - **Result**: No textbox appeared and no toggle occurred. This empirically proves that (13, 9) is a purely decorative statue of TYPE_2889 and has NO active switch in unmodded Gen 1.
  - **Conclusion**: There is no third Mewtwo Statue on 2F East. Our matrix model is simplified back to Statue 1 (1F West) and Statue 2 (2F West). We can safely navigate 2F East without worrying about a third state.