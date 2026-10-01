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
  4. **Hypothesis D (Route 1 Northwest Clearing Western Expanse - FALSIFIED Turn 12350)**: Fully audited rows 14-22; western boundary solid pine trees at col 24, row 14 solid pine trees north; Mike and Sonia ambient.
  5. **Hypothesis E (Alternative Event Flag Mechanisms - FALSIFIED Turn 12410)**: HuPhone Item Storage, Mailbox, Quest Status, and World Map verified empty/static; passive checks do not trigger story flags.
  6. **Hypothesis F (Cottage East Corridor Northbound - FALSIFIED Turns 12444, 12455)**:
     - Tile (40, 20) is confirmed impassable elevation ledge; 3 Up presses from (40, 21) yielded 0 tiles moved. The south-facing row 20 ledge strictly prevents northbound traversal from the Cottage yard.
  7. **Hypothesis G (Southern Route 1 Northbound Connection to Sovio City - ACTIVE Turn 12455)**:
     - *Premise*: Since players repeatedly travel from Lancio Town to Sovio City (verified Turns 818-1165, 10811-11002, 11792-11909) without HMs, a valid northbound traversal path must exist in the southern sector.
     - *Investigation Scope*: Trace the connection from Sand Highway (columns 35-37, rows 26-38) and Northwest corridor to locate the true northbound bypass around the row 20 ledge.