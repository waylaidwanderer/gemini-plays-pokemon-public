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

- **Hypothesis GT1 (Global Trigger & Party / Inventory Mechanics Investigation)**:
  - **Context**: Having confirmed that all Sovio residences, surface quadrants, Route 1, Lancio Town, and sewer sectors are settled/ambient, shuttling between surface and sewers without new variables is circular stagnation. The blocker flags ('I should find dad first!' and 'I have things to do!') may be gated by a non-spatial game mechanic.
  - **Targets**: Party composition (Sirius Lv14 solo; Zephyr in PC?), PC Boxes / Mailbox in Pokémon Center, HuPhone app configurations, or unexamined overworld mechanics.
  - **Method**: Check PC Box / Party system, verify if Zephyr (Pidgey) or an item/message is waiting in PC storage, test turnstile interaction from (19, 22) facing Up with 'A'.
  - **Falsification Criteria**: If inspecting Someone's PC Box storage shows no progression items/flags, and withdrawing Zephyr (or manipulating party composition) does not alter the turnstile trigger at (19, 21), declare party size/composition strictly independent of the Jackson blocker and immediately falsify GT1.
