# Pokémon Mansion Gate State Matrix (Turn 75980)
Active State: **State B (Statue 1 Toggled)** (Toggled on Turn 78020)

## State Table
| Gate ID & Location | State A (Statue 2 Default) | State B (Statue 2 Toggled) | Verification & Proof of Work |
| :--- | :--- | :--- | :--- |
| **Gate 1** (1F, (25, 13)) | **CLOSED** (Impassable) | **OPEN** (Passable) | State A: Verified CLOSED on Turn 75301 and Turn 75361. State B: Verified OPEN on Turn 75550 by walking through it to (25, 14). |
| **Gate 4** (1F, (21, 17)) | **UNREACHABLE on foot** (Hypothesized OPEN) | **CLOSED** (Impassable) | State A: Unreachable because Column 11 partition wall is solid (TYPE_2889) from Row 13 to Row 27, completely isolating 1F East from 1F West (Verified Turns 76184-76193). State B: Verified CLOSED (has orange/yellow horizontal bars) on Turn 75551. |
- **Gate 2** (3F, Col 11) | **CLOSED** (Impassable) | **OPEN** (Passable) | State A: Verified CLOSED (solid wall of TYPE_2889) on Turn 75091. Physical testing on Turns 76608 and 76610 proved that Column 9 is solid (TYPE_2889) on Rows 12 and 13 under State A. State B: In unmodded Pokémon, this gate is open under State B. It corresponds to Row 8 Column 10-11. We bumped at (10, 9) on Turn 82559 under State B, which is a solid rubble tile. Let's systematically test Column 10's vertical passability under State B by testing (10, 11) next. Oh wait! On Turn 85112, we completed a direct physical test of Column 10 Row 9 (10, 9) under State A, resulting in a solid bump. We also tested Column 7 Row 7 (7, 7) under State A, resulting in a solid bump. Row 7 and Column 10 are completely impassable on foot under both states, meaning 3F West is completely isolated from 3F East. Therefore, the ONLY way to reach 3F East is by climbing the second staircase on 2F East at (21, 10), which is accessible under State B!
| **Gate 3** (2F, (18, 8)-(19, 8)) | **OPEN** (Passable) | **CLOSED** (Impassable) | State A: Verified OPEN on Turn 78836 by walking through it to 2F East South. State B: Verified CLOSED (has orange/yellow horizontal bars) on Turn 84976. |
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

## 1F West Mewtwo Statue Test (Turn 80082)
- **Coordinates**: Mewtwo Statue is located at (10, 8) on 1F West (Map 0_165).
- **Methodology**: Stood at (10, 9) facing Up, and pressed 'A' to interact with the statue at (10, 8) under State A.
- **Results**: No textbox appeared and no interaction took place.
- **Conclusion**: The Mewtwo Statue at (10, 8) on 1F West is purely decorative. There is no active switch at this location.
| **Gate 26** (2F, (12, 26)-(13, 26)) | **CLOSED** (Impassable) | **CLOSED** (Impassable) | State A: Verified CLOSED on Turn 80627 by standing at (12, 25) facing Down and pressing Down, resulting in a bump. State B: Verified CLOSED on Turn 78980. This gate is 100% closed under both states, blocking foot access to Row 27. |
| **Gate 13** (2F, (12, 13)-(13, 13)) | **CLOSED** (Impassable) | **CLOSED** (Impassable) | State A: Verified CLOSED on Turn 78855. State B: Verified CLOSED on Turn 79849 by bumping into (12, 13) from (12, 12). This gate is 100% closed under both states, meaning 2F East South cannot be accessed via Column 12-13 on Row 13. |
- Turn 80849: Stood at (21, 16) facing Down and pressed Down. Resulted in a direct BUMP against (21, 17) (Gate 4), physically proving that Gate 4 at (21, 17) is CLOSED and impassable under Gate State B. This confirms that the 1F south-central pocket is completely unreachable on foot from the north.