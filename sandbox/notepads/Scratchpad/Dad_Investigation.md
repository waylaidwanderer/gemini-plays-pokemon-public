# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Investigation Status & Active Hypotheses (Updated Turn 12242)
- **Verified Game State**:
  - Metro Turnstile at (19, 21): Displays "I should find dad first!" (Repels South).
  - Route 2 Exit at (52, 19-22): Displays "I can't go yet... I have things to do!" (Repels West; verified Turn 12163).
  - Professor Ivo's Lab Stairs at (12, 7): Displays "I probably shouldn't head down here..."
  - Sovio Sewers Storage Room at (37, 14): Displays "Its a simple storage room..." (Exhausted/Inert; zero keys held).
  - Active Quest: NONE (Machop's Toy cancelled on Turn 12142 to clear active quest slot).
  - *Deduction*: Jackson departed the Metro Station lobby following the seismic tremor (Turn 1437) to investigate the disturbance outside. Finding Jackson is the mandatory event flag to unlock Metro transit to Amor City.

- **Hypotheses & Status**:
  1. **Hypothesis A (Karate House & Machop's Toy - FALSIFIED Turn 12132)**: Fully audited on Turns 12123-12132; all occupants and 2F confirmed ambient with zero progression triggers.
  2. **Hypothesis B (Sewers Storage Room at 37, 14 - EXHAUSTED)**: Verified inert text ("Its a simple storage room..."). No keys held. Closed pending a new key item or explicit story event.
  3. **Hypothesis C (Sovio City Exterior Perimeters - FALSIFIED Turn 12239)**:
     - Commercial building covered passage (cols 47-51, row 22): row 23 north facade audited solid across cols 48, 49, 50 with zero door scripts.
     - West Avenue north boundary (cols 16-26, rows 15-16): commercial facade foundation audited solid at (26, 15) and (16, 15); no northern passage exists.
     - West Avenue NPCs: Rocky at (24, 17) verified ambient comic relief ("It's just a normal rock...").
     - *Falsification Result*: All external building perimeters and boundaries in Sovio City are confirmed continuous solid walls. No hidden outdoor entrances exist in Sovio City.
  4. **Hypothesis D (Alternative Event Flag / Metro Interior Investigation)**:
     - *Hypothesis*: The turnstile barrier "I should find dad first!" is governed by an event flag triggered either inside the Metro Station (unmapped western lobby/platform interactions) or through an unexamined dialogue/item trigger in Lancio Town (Professor Ivo's Lab).
     - *Falsification Criteria*: If the entire Metro Station lobby (including western tiles at columns 16-18) contains no triggers and Professor Ivo has no new dialogue/items, Hypothesis D is FALSIFIED.
