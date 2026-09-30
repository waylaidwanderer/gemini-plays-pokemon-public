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
  1. **Hypothesis A (Karate House & Machop's Toy - Formulated Turn 12068, Testing Turn 12091+)**:
     - *Hypothesis*: The reactive dialogue on Machop at (8, 35) indicates the Karate House has an active script condition when Machop's Toy is active.
     - *Test Plan*: Interact with Machop, Karate trainer (3, 34), girlfriend (3, 33), and search 2F.
     - *Falsification Criteria*: If Machop only displays flavor/ambient aggression text ('He seems a bit agressive...') and no resident/object provides an item, quest update, or story flag related to Jackson, Hypothesis A is conclusively FALSIFIED. (Stopping condition: single pass of 1F/2F).
  2. **Hypothesis B (Sewers Storage Room - Formulated Turn 12068)**:
     - *Hypothesis*: The storage room at (37, 14) where Jackson was held captive may open via an overworld event trigger or switch.
     - *Constraint*: Inventory audit (Turn 11897) confirmed zero keys held. Falsification: If no observable trigger or switch is found on the surface or accessible sewer areas, Hypothesis B is FALSIFIED.
  3. **Hypothesis C (Surface NPCs with Unexamined Conditions - Formulated Turn 12068)**: Re-test key Sovio surface NPCs to verify if dialogue updates based on current story flags, avoiding premature "100% Falsified" assumptions.
