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
- **Hypothesis SS1 (Sovio Sewers Jackson Rescue Operation)**:
  - **Rationale**: The 5-point exterior audit of Sovio City (Turns 14682-14727) confirmed 100% solid boundaries with zero outdoor event triggers. The Metro turnstile blocker specifically checks Jackson's rescue flag ('I should find dad first!'). Turn 1666 cutscene showed grunts holding Jackson captive in a sewer storage room. Marie's radio retreat (Turn 2682) cleared the grunts from the corridors, but Jackson himself has not been located or spoken to in the detention room. The rescue trigger must be executed inside Sovio Sewers before the Metro turnstile will clear.
  - **Plan**: Enter Sovio Metro Station, descend into Sovio Sewers via the red capsule mat at (18-19, 25), and systematically search every branch and room (including the eastern dead-end storage room at 37, 14 and all side corridors) to locate Jackson and trigger his rescue dialogue.

## Settled Hypotheses
- **Hypothesis SC1 (Sovio City Exterior Perimeters - 100% AUDITED)**:
  - Status: Settled Turn 14727. Southern Avenue tree lines, southwest lawn (12, 30), southwest building perimeter, rear Biker lane (col 12, rows 20-30), western office facade (col 11, rows 16-20), Karate house corner (12, 15), Gumball/tan building gap (31, 13), northern alcove (39, 7), and elevated terrace (cols 50-52, rows 15-17) are 100% verified solid boundaries. No external event triggers exist.

## Archived Hypotheses (Exhausted / Debunked)
- **Hypothesis LA1 (Lancio Town Southern Coastline to Azluf - DEBUNKED)**:
  - Status: Debunked Turn 14674. Lancio Town has no on-foot coastal exit to Azluf Town; regional geography confirms Lancio connects exclusively northeast to Route 1 and is otherwise surrounded by ocean. Requires water traversal/Surf not currently accessible.
- **Hypothesis SE1 (Sustained Exploration of Sovio Sewers Loop - EXHAUSTED)**:
  - Status: Concluded Turn 14428. Continuous loop traversed (Lower walkway -> Western stairs -> Upper terrace -> Wall ladder -> Northern Gangway -> Bridge -> Row 13 -> Dark Sector). Zero NPCs, cutscenes, or progression triggers encountered along this loop. 100% settled.
