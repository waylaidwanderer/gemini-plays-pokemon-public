# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Blockers & Status
- **Metro Turnstile**: Stepping onto (19, 21) triggers "I should find dad first!" and forces Asher 1 step down to (19, 22).
- **Route 2 Gate**: Stepping onto (52, 19-22) triggers "I can't go yet... I have things to do!".
- **Jackson Status**: Captured by Team Siara during tremor cutscene (Turn 1666). Marie broadcast radio retreat on Turn 2682. Jackson's whereabouts remain the central progression gate.

## Verified / Settled Locations
- **External Settlements & Residences**: Lancio Town, Route 1, Sovio surface quadrants, and all 6 domestic residences remain settled (detailed records in Locations/*.md).
- **Sovio Metro Lobby**:
  - Timetable Board (columns 21-23): Verified Turns 7149, 14276-14278 as purely decorative flavor text ("It's a timetable showing various destinations!").
  - Platform Attendant at (22, 19): Inaccessible behind solid north brick wall at row 23; platform passage gated at turnstile (19, 21).
- **Global Storage Systems (Verified Turns 14291-14315)**: HuPhone Mailbox ('There's no Mail here.'), HuPhone Item Storage ('There are no items.'), and Someone's PC Box 1 (0 Pokémon) audited 100% empty. Party size/composition does not gate turnstile blocker.
- **Sovio Sewers Audited Features**:
  - Machop's Toy Quest: Completed Turn 13331 (Black Belt obtained).
  - Deep Subterranean Sector (2, 38): Audited Turn 14052; single-purpose quest room, all perimeter walls inert.
  - Eastern Storage Room at (37, 14): Audited Turns 8637, 11127, 11149; ambient "Its a simple storage room..." with solid south void collision. Row 13 east of col 24 runs beneath solid north brick wall (rows 10-12).

## Active Hypotheses & Primary Focus
- **Hypothesis SE1 (Sustained Exploration of Sovio Sewers Unexhausted Frontier)**:
  - **Context**: Surface and global systems (PC, Bag, residences, timetable) are verified 100% ambient/settled. The sole storyline thread tied to Jackson and Team Siara is the Sovio Sewers. We are executing a continuous, methodical mapping of all sewer sectors without aborting mid-transit.
  - **Sector 1 Traversal (Verified Turns 14321-14337)**:
  - **Sector 2 Traversal (Verified Turns 14338-14341)**:
    - Row 5 east of column 23 verified: shallow puddle at (26-27, 5) terminates east at (27, 5) into impassable void chasm at column 28. Confirmed dead-end; does NOT connect directly to wooden staircase platform.
  - Vertical Bridge at column 23 (rows 6-12) traversed south from (23, 5) to (23, 13) (Verified Turn 14350). Confirmed complete connection from Northern Gangway (row 5) south across chasm to row 13 gangway.
  - **Sector 3 Traversal (Verified Turns 14356-14361)**:
    - Northern alcove at (23, 8) verified (Nugget already collected Turn 4576).
    - Rugged rock at (22, 10) confirmed intact (equipment-gated).
    - Western alcove at (14-16, 9-10) verified (warp to Deep Subterranean Sector 2, 38 where Machop's toy was retrieved).
    - Confirmed 100% devoid of NPCs, items, or story triggers.
  - **Result**: Continuous loop traversed (Lower walkway row 28 cols 34-18 -> Western stairs 14, 17 -> Upper terrace 14, 12 -> Wall ladder 15, 11 -> Northern Gangway row 5 cols 15-27, dead end at 27, 5 -> Vertical Bridge col 23 rows 6-12 -> Row 13 gangway cols 23-30 -> Column 30 causeway -> Dark Sector corridor row 9 cols 30-16). Zero NPCs, cutscenes, or progression triggers encountered along this loop.
