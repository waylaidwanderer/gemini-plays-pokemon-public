# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Investigation Status & Active Hypotheses (Updated Turn 12091)
- **Verified Game State**:
  - Metro Turnstile at (19, 21): Displays "I should find dad first!" (Repels South).
  - Route 2 Exit at (52, 19-21): Displays "I can't go yet... I have things to do!" (Repels West).
  - Professor Ivo's Lab Stairs at (12, 7): Displays "I probably shouldn't head down here..."
  - Sovio Sewers Storage Room at (37, 14): Displays "Its a simple storage room..."
  - Active Quest: "Machop's Toy" (given by Old Man at 51, 15; family Machop in Karate house at 14, 15 reacts: "He seems a bit agressive...").
  - *Deduction*: Jackson departed the Metro Station lobby following the seismic tremor (Turn 1437) to investigate the disturbance outside. Finding Jackson is the mandatory event flag to unlock Metro transit to Amor City.

- **Testable Hypotheses**:
  1. **Hypothesis A (Karate House & Machop's Toy - Formulated Turn 12068, Testing Turn 12091+)**: The reactive dialogue on Machop at (6-7, 33-35) indicates the Karate House has an active script condition when Machop's Toy is active. Test if interacting with Karate trainer, girlfriend, Machop, or searching Karate house 1F/2F progresses the quest or unlocks an event.
  2. **Hypothesis B (Sewers Storage Room / Hidden Key - Formulated Turn 12068)**: In Turn 1666-1707 cutscene, grunts held Jackson captive in sewer storage room. When grunts retreated (Turn 2682), storage room remained locked/inert. Test if an item or trigger unlocks storage room at (37, 14).
  3. **Hypothesis C (Surface NPCs with Unexamined Conditions - Formulated Turn 12068)**: Re-test key Sovio surface NPCs to verify if dialogue updates based on current story flags, avoiding premature "100% Falsified" assumptions.
