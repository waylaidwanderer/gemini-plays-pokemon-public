# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Investigation Status & Active Hypotheses (Updated Turn 12365)
- **Verified Game State**:
  - Metro Turnstile at (19, 21): Displays "I should find dad first!" (Repels South).
  - Route 2 Exit at (52, 19-22): Displays "I can't go yet... I have things to do!" (Repels West; verified Turn 12163).
  - Professor Ivo's Lab Stairs at (12, 7): Displays "I probably shouldn't head down here..."
  - Sovio Sewers Storage Room at (37, 14): Displays "Its a simple storage room..."
  - Active Quest: NONE (Machop's Toy cancelled on Turn 12142 to clear the single active quest slot; verified free for new side quests or event triggers).
  - *Deduction*: Jackson departed the Metro Station lobby following the seismic tremor (Turn 1437) to investigate the disturbance outside. Finding Jackson is the mandatory event flag to unlock Metro transit to Amor City.

- **Testable Hypotheses**:
  1. **Hypothesis A (Karate House & Machop's Toy - FALSIFIED Turn 12132)**: Audited all residents and 2F; 100% ambient flavor with zero progression triggers.
  2. **Hypothesis B (Sewers Storage Room - On Hold)**: Storage room at (37, 14) is currently inert ("Its a simple storage room...").
  3. **Hypothesis C (Surface NPCs with Unexamined Conditions - On Hold)**: Re-testing key NPCs if story flags change.
  4. **Hypothesis D (Route 1 Northwest Clearing Western Expanse - FALSIFIED Turn 12350)**:
     - Audited columns 24-28 across rows 14-22. Traversed to westernmost edge at (24, 18) and (24, 15).
     - Columns 0 to 23 are an impenetrable wall of solid pine trees across rows 14-22. Row 14 is solid pine trees/trunks.
     - Mike at (29, 20) and Sonia at (27, 15) confirmed ambient defeat flavor dialogue. 100% FALSIFIED.
  5. **Hypothesis E (Alternative Event Flag Mechanisms - FALSIFIED Turn 12410)**:
     - *HuPhone App Audit*:
       - Item Storage (Turn 12381): Verified empty ('There are no items.'). Zero stored items.
       - Mailbox (Turn 12388): Verified empty ('There\'s no Mail here.'). Zero incoming transmissions or stored mail.
       - Quest Status (Turn 12402): Verified empty ('You aren\'t doing any Quest'). Zero active side quests or story tracking.
       - World Map (Turn 12410): Static regional map viewer. Zero objective markers, flashing nodes, or pins.
     - *Conclusion*: Passive device browsing / storage checks do not trigger story progression. Progression is strictly event-flag / overworld triggered. Hypothesis E is FALSIFIED.
