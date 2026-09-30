# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Deductions & Blocker Mechanics
- **Blocker Distinction**:
  - Route 2 exit at (52, 19-21): Displays "I can't go yet... I have things to do!" (Repels West).
  - Sovio Metro turnstile at (19, 21): Displays "I should find dad first!" (Repels South).
  - *Deduction*: Jackson departed the Metro Station lobby following the seismic tremor (Turn 1437) to investigate the disturbance outside. Finding Jackson is the mandatory event flag to unlock Metro transit to Amor City.

## Investigation Status & Active Hypotheses
- **Verified Game State**:
  - Metro Turnstile at (19, 21): Displays "I should find dad first!" (Repels South).
  - Route 2 Exit at (52, 19-21): Displays "I can't go yet... I have things to do!" (Repels West).
  - Professor Ivo's Lab Stairs at (12, 7): Displays "I probably shouldn't head down here..."
  - Sovio Sewers Storage Room at (37, 14): Displays "Its a simple storage room..."
  - Active Quest: "Machop's Toy" (given by Old Man at 51, 15; family Machop in Karate house at 14, 15 reacts: "He seems a bit agressive...").

- **Testable Hypotheses**:
  1. **Hypothesis A (Karate House & Machop's Toy)**: The reactive dialogue on Machop at (6-7, 33-35) indicates the Karate House or Old Man questline has active event script flags. Test if interacting with the Karate trainer, girlfriend, Machop, or searching the Karate house 1F/2F while the quest is active progresses the quest or reveals a key/item.
  2. **Hypothesis B (Sewers Storage Room / Hidden Key)**: In Turn 1666-1707 cutscene, grunts held Jackson captive in the sewer storage room. When grunts retreated (Turn 2682), the storage room remained locked/inert. Test if an item (Key) or specific trigger unlocks the storage room at (37, 14), or if an item/switch exists in the Dark Sector or sewers.
  3. **Hypothesis C (Surface NPCs with Unexamined Conditions)**: Re-test key Sovio surface NPCs to verify if dialogue updates based on current story flags, avoiding premature "100% Falsified" assumptions.
