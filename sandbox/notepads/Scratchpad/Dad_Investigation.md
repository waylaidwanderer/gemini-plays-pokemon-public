# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Blockers & Status
- **Metro Turnstile**: Stepping onto (19, 21) triggers "I should find dad first!" and forces Asher 1 step down to (19, 22).
- **Route 2 Gate**: Stepping onto (52, 19-22) triggers "I can't go yet... I have things to do!".
- **Jackson Status**: Captured by Team Siara during tremor cutscene (Turn 1666). Marie broadcast radio retreat on Turn 2682. Jackson's whereabouts remain the central progression gate.

## Verified / Settled Locations
- **Lancio Town**: Professor Ivo static ambient dialogue ("Hey, Ashi, how's your new Pokémon?"), lab basement stairs blocked ("I probably shouldn't head down here..."), harbor boat empty/discontinued.
- **Route 1**: All trainers defeated; roadside cottage boy gifts Max Repel; open hedge passage connected; tall grass wild encounters catalogued.
- **Sovio Surface**: Plaza confrontation tiles (43-44, 13-15), Central Park pond walkway, and south sidewalk return baseline ambient interactions.
- **Sovio Domestic Interiors (SC1-SC5, Name Rater)**: All 6 residences fully audited and verified 100% ambient/settled (detailed records in Locations/Sovio_City.md).
- **Sovio Metro Lobby**:
  - Timetable Board (columns 21-23): Verified Turns 7149, 14276-14278 as purely decorative flavor text ("It's a timetable showing various destinations!").
  - Platform Attendant at (22, 19): Inaccessible behind solid north brick wall at row 23; platform passage gated at turnstile (19, 21).
- **Sovio Sewers**:
  - Eastern Storage Room at (37, 14): Audited Turns 8637, 11127, 11149; displays ambient "Its a simple storage room..." with solid south void collision. Row 13 east of col 24 runs beneath solid north brick wall (rows 10-12). Confirmed decorative storage dead-end; not the holding cell from Turn 1666 cutscene.
  - Machop's Toy Quest: Completed Turn 13331 (Black Belt obtained).
  - Deep Subterranean Sector (2, 38): Audited Turn 14052; single-purpose quest room, all perimeter walls inert.

## Active Hypotheses & Primary Focus
- **Hypothesis TB1 (Metro Timetable Columns 21-22 - FALSIFIED / SETTLED)**:
  - Verified Turns 14276-14278: Columns 21 and 22 repeat identical baseline text. Entire board is confirmed purely decorative.

- **Hypothesis GT1 (Global Trigger & Party / Inventory Mechanics - FALSIFIED / SETTLED)**:
  - **Empirical Audit (Verified Turns 14291-14315)**:
    - HuPhone Mailbox audited empty ('There's no Mail here.', Turn 14291).
    - HuPhone Item Storage audited empty ('There are no items.', Turn 14292).
    - Someone's PC Box 1 audited visually (Turn 14315): completely empty across all 30 slots; zero Pokémon stored in PC. Active party holds only Sirius (Lv14 Riolu).
  - **Result**: Hypothesis GT1 is 100% FALSIFIED. Party size and PC storage do not gate the turnstile blocker ('I should find dad first!').

- **Hypothesis SE1 (Sustained Exploration of Sovio Sewers Unexhausted Frontier)**:
  - **Context**: All surface locations (SC1-SC5, Name Rater, Central Plaza/Park, West Avenue, Route 1, Lancio Town) and Metro timetable/systems are verified 100% ambient/settled. The sole storyline location tied to Jackson and Team Siara is the Sovio Sewers. Past attempts suffered cognitive thrashing by aborting after <10 tiles. We commit to a sustained, methodical exploration of the unexhausted sewer pathways.
  - **Target Sectors**:
    1. Lower Level Walkway & Western Wing (rows 24-28, columns 8-22).
    2. Elevated Northern Gangway & Vertical Bridge (row 5, columns 15-23; rows 6-12, column 23).
    3. Column 30 Causeway & Dark Sector Basement (ladder at col 30, staircase 30, 4).
  - **Method**: Enter sewers via Metro lobby mat (18-19, 25), maintain steady forward progression through wild encounters, systematically trace every walkable branch to its true boundary.
  - **Falsification Criteria**: A sewer branch is only settled when its boundary tiles and connections are visually confirmed on-screen and verified in intermediate states.
