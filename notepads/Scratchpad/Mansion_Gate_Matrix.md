# Pokémon Mansion Gate State Matrix (Turn 75980)

## State Table
| Gate ID & Location | State A (Statue 2 Default) | State B (Statue 2 Toggled) | Verification & Proof of Work |
| :--- | :--- | :--- | :--- |
| **Gate 1** (1F, (25, 13)) | **CLOSED** (Impassable) | **OPEN** (Passable) | State A: Verified CLOSED on Turn 75301 and Turn 75361. State B: Verified OPEN on Turn 75550 by walking through it to (25, 14). |
| **Gate 4** (1F, (21, 17)) | **UNREACHABLE on foot** (Hypothesized OPEN) | **CLOSED** (Impassable) | State A: Unreachable because Column 11 partition wall is solid (TYPE_2889) from Row 13 to Row 27, completely isolating 1F East from 1F West (Verified Turns 76184-76193). State B: Verified CLOSED (has orange/yellow horizontal bars) on Turn 75551. |
| **Gate 2** (3F, Col 11) | **CLOSED** (Impassable) | **CLOSED** (Impassable) | State A: Verified CLOSED (solid wall of TYPE_2889) on Turn 75091. Physical testing on Turns 76608 and 76610 proved that Column 9 is solid (TYPE_2889) on Rows 12 and 13 under State A, meaning Column 11 is completely unreachable from the West on foot. State B: Verified CLOSED (solid wall of TYPE_2889) on Turn 75612. Comprehensive empirical testing on Turns 76460-76492 proved that Column 10 is solid on Rows 8-15 and Column 9 is solid on Rows 12-13 under State B, meaning 3F East is completely impassable from the West under both State A and State B on foot on Rows 8-15. |
| **Gate 3** (2F, (18, 8)-(19, 8)) | **OPEN** (Passable) | **CLOSED** (Impassable) | State A: Verified OPEN (has open floor of TYPE_3fe2, visually clear) on Turn 75880. State B: Verified CLOSED (has orange/yellow horizontal bars) on Turn 75760. |
| **Gate 6** (2F, (9, 4)-(9, 5)) | **CLOSED** (Impassable) | **OPEN** (Passable) | State A: Verified CLOSED (has orange/yellow vertical bars of TYPE_a83b) on Turn 75868. State B: Verified OPEN (passable floor) when walking to West wing. |

## B1F Basement Gate Matrix (Added Turn 75980)
- This table tracks the circuitry state of the Basement (B1F) of Pokémon Mansion once we enter and locate statues/gates there.

| Gate ID & Location | State A (Statue 2 Default) | State B (Statue 2 Toggled) | Verification & Proof of Work |
| :--- | :--- | :--- | :--- |
| *TBD* | *TBD* | *TBD* | *TBD* |