# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher 1 step south to (19, 22). Attendant at (22, 18-19) is unreachable behind solid wall/turnstile structure.
- **Rugged Rocks (Sewers)**: (22, 10) and (10, 18) display "It's a rugged rock, but with some equipment, I could smash it." Zero equipment currently in possession.
- **Storage Room Mat (Sewers 37, 14)**: Displays "Its a simple storage room..." and has solid void collision to south with zero warp. Closed inquiry.

## Settled Hypotheses
- **H1 (South Commercial Roof Passage, cols 47-51, rows 20-22)**: FALSIFIED (Turn 16147). Plain traversable corridor with solid walls; zero doors, items, or triggers.
- **H2 (Tan Building Facade along row 12 across cols 32-37)**: FALSIFIED (Turn 16148). Solid foundation wall collision across all columns; 100% decorative exterior.
- **H3 (Lower Eastern Sewer Basin Rim, rows 28-32, cols 34-37)**: AUDITED & SETTLED (Turn 16136). Enclosed dead-end basin rim; zero warps, items, or NPCs.
- **H4 (Elevated Metro Terrace & House 49, 14)**: FALSIFIED (Turn 16177). Terrace deck empty; Nana and Granddaughter repeat static ambient cooking dialogue; zero leads.

## Active Hypotheses


### Hypothesis H5: Metro Station Lobby & Platform Boundary Probing
- **Premise**: In the Metro lobby, turnstile at (19, 21) triggers "I should find dad first!". Station attendant is at (22, 18-19). Can the attendant, counter at cols 21-22, scanner pillars, or western blue chairs (cols 15-17) be interacted with to provide information or advance the story?
- **Test Coordinates**:
  1. Metro lobby (21-22, row 22): probe facing North toward platform attendant and counter.
  2. Metro lobby (15-17, rows 22-25): probe blue chairs and west wall.
- **Pass Criteria**: Dialogue from attendant or discovery of an interactable object/trigger advancing the search for Dad.
- **Fail Criteria**: Attendant is unreachable behind barrier; chairs/counters are inert; turnstile continues to block with "I should find dad first!".