# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Blockers & Status
- **Metro Turnstile**: Stepping onto (19, 21) triggers "I should find dad first!" and forces Asher 1 step down to (19, 22) (re-verified active Turn 14644).
- **Route 2 Gate**: Stepping onto (52, 19-22) triggers "I can't go yet... I have things to do!" (re-verified active Turn 14647).
- **Jackson Status**: Captured by Team Siara during tremor cutscene (Turn 1666). Marie broadcast radio retreat on Turn 2682. Jackson's whereabouts remain the central progression gate.

## Verified / Settled Locations
- **Lancio Town Audit (Settled Turn 14528)**: Laboratory and Harbor verified static (details in Locations/Lancio_Town.md).
- **Sovio Metro Lobby**:
  - Timetable Board (columns 21-23): Verified Turns 7149, 14276-14278 as purely decorative flavor text ("It's a timetable showing various destinations!").
  - Platform Attendant at (22, 19): Inaccessible behind solid north brick wall at row 23; platform passage gated at turnstile (19, 21).
- **Global Storage Systems (Verified Turns 14291-14315)**: HuPhone Mailbox ('There's no Mail here.'), HuPhone Item Storage ('There are no items.'), and Someone's PC Box 1 (0 Pokémon) audited 100% empty. Party size/composition does not gate turnstile blocker.
- **Sovio Sewers Audited Features**:
  - Machop's Toy Quest: Completed Turn 13331 (Black Belt obtained).
  - Deep Subterranean Sector (2, 38): Audited Turn 14052; single-purpose quest room, all perimeter walls inert.
  - Eastern Storage Room at (37, 14): Audited Turns 8637, 11127, 11149; ambient "Its a simple storage room..." with solid south void collision. Row 13 east of col 24 runs beneath solid north brick wall (rows 10-12).

## Active Hypotheses & Strategic Focus
- **Hypothesis SC1 (Systematic Audit of Sovio City Exterior Perimeters & Structures)**:
  - **Rationale**: The Metro turnstile blocker ('I should find dad first!') and Route 2 gate ('I can't go yet...') are both in Sovio City. Lancio Town is verified on-foot isolated (connecting exclusively northeast to Route 1 and ocean elsewhere; on-foot passage to Azluf is physically impossible without Surf). Looping back and forth across Route 1 without state changes is unproductive. Asher must systematically search Sovio City perimeters, alleyways, tree lines, and building facades to find Dad or trigger the next story event.
  - **Plan**: Perform systematic, tile-by-tile boundary checks in Sovio City:
    1. Southern Avenue tree lines: (12, 30) lawn tested Turn 14686 (11, 30 solid pine tree collision; dead end); east row 30 dead-ends at col 18. [AUDITED]
    2. Southwest building perimeter: (18, 27) solid wall, (17, 25) solid wall, sidewalk at (16-17, 26-27) open. [AUDITED]
    3. West Avenue western facade & corridor behind Bikers: Col 12 fully open rows 20-30 behind Bikers to southwest lawn. Column 11 rows 16-20 solid office wall with 0 doors/scripts; (12, 15) solid Karate house wall. [AUDITED]
    4. North Central alleyways: Probe columns 30-31 between Gumball house (29, 14) and tan building (32-37), and alleyway (39-40) north to house (39, 7).
    5. Plaza eastern boundaries and elevated terrace edges: (51-52, 15-17) terrace floor open, east wall solid at col 52, south terminated by signpost at (51, 18). [AUDITED]

## Archived Hypotheses (Exhausted / Debunked)
- **Hypothesis LA1 (Lancio Town Southern Coastline to Azluf - DEBUNKED)**:
  - Status: Debunked Turn 14674. Lancio Town has no on-foot coastal exit to Azluf Town; regional geography confirms Lancio connects exclusively northeast to Route 1 and is otherwise surrounded by ocean. Requires water traversal/Surf not currently accessible.
- **Hypothesis SE1 (Sustained Exploration of Sovio Sewers Loop - EXHAUSTED)**:
  - Status: Concluded Turn 14428. Continuous loop traversed (Lower walkway -> Western stairs -> Upper terrace -> Wall ladder -> Northern Gangway -> Bridge -> Row 13 -> Dark Sector). Zero NPCs, cutscenes, or progression triggers encountered along this loop. 100% settled.
