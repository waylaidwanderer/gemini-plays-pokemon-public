# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Investigation Status & Active Hypotheses (Updated Turn 12091)
- **Verified Game State**:
  - Metro Turnstile at (19, 21): Displays "I should find dad first!" (Repels South).
  - Route 2 Exit at (52, 19-22): Displays "I can't go yet... I have things to do!" (Repels West; verified Turn 12163).
  - Professor Ivo's Lab Stairs at (12, 7): Displays "I probably shouldn't head down here..."
  - Sovio Sewers Storage Room at (37, 14): Displays "Its a simple storage room..."
  - Active Quest: NONE (Machop's Toy cancelled on Turn 12142 to clear the single active quest slot; verified free for new side quests or event triggers).
  - *Deduction*: Jackson departed the Metro Station lobby following the seismic tremor (Turn 1437) to investigate the disturbance outside. Finding Jackson is the mandatory event flag to unlock Metro transit to Amor City.

- **Testable Hypotheses**:
  1. **Hypothesis A (Karate House & Machop's Toy - Formulated Turn 12068, FALSIFIED Turn 12132)**:
     - *Audited Results*:
       - Machop at (9, 34) (Turn 12123): Displays only "Machop: Chop Chop!" / "He seems a bit agressive...". Zero items, zero quest updates.
       - Karate Trainer at (3, 34) (Turn 12125): Ambient debate text ("kickbox is far better than karate").
       - Girlfriend at (3, 33) (Turn 12127): Counterpart debate text ("karate is far better than kickboxing").
       - 2F (Turn 12132): Empty room, generic bookshelf text ("It's crammed full of Pok�mon books.").
     - *Conclusion*: Conclusively FALSIFIED on Turn 12132. Karate House holds zero progression triggers or links to Jackson.
  2. **Hypothesis B (Sewers Storage Room - Formulated Turn 12068)**:
     - *Hypothesis*: The storage room at (37, 14) where Jackson was held captive may open via an overworld event trigger or switch.
     - *Constraint*: Inventory audit (Turn 11897) confirmed zero keys held. Falsification: If no observable trigger or switch is found on the surface or accessible sewer areas, Hypothesis B is FALSIFIED.
  3. **Hypothesis C (Surface NPCs with Unexamined Conditions - Formulated Turn 12068)**: Re-test key Sovio surface NPCs to verify if dialogue updates based on current story flags, avoiding premature "100% Falsified" assumptions.

  4. **Hypothesis F (Route 1 Northwest Clearing Western Expanse - FALSIFIED Turn 12350)**:
     - *Empirical Audit*: Audited columns 24-28 across rows 14-22. Traversed to westernmost clearing edge at (24, 18) and (24, 15).
     - *Verified Collision*: Columns 0 to 23 are an impenetrable, continuous wall of solid pine trees across rows 14-22. Row 14 is solid pine trees/trunks. Youngster Mike at (29, 20) provides ambient defeat dialogue ('My Pokémon was completely destroyed by yours...'). Lass Sonia at (27, 15) provides ambient defeat dialogue ('Hmm, more harmony maybe?').
     - *Conclusion*: Zero secret western paths, exits, or NPCs exist. Northwest Clearing is 100% audited; completely FALSIFIED with zero progression triggers.