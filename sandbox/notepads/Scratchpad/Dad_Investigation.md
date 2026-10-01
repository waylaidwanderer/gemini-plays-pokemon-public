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

## Active Hypotheses & Strategic Focus
- **Hypothesis SC2 (Sovio City Unexamined Spaces & System Triggers)**:
  - **Rationale**: Sovio Sewers are completely exhausted across all sectors (Machop's toy returned, Siara grunts retreated, storage room verified ambient). Metro turnstile blocker explicitly checks Jackson's rescue flag ('I should find dad first!'). We must exit the sewers to Sovio City and systematically audit unexamined spaces, structures, and interaction mechanics.
  - **Primary Targets**:
    1. Two-Story Commercial/Residential Building (columns 47-51, rows 20-29) south of Central Plaza. Verify whether any entrance exists or if lower story wooden siding has interaction triggers.
    2. Review HuPhone Quest Log pages 2-5 for potential side-quest dependencies or flags.
    3. Re-audit key Sovio City locations and dialogue triggers with fresh eyes.
  - **Status**: Formulated. Currently exiting Sovio Sewers to commence investigation in Sovio City.

## Settled Hypotheses
- **Hypothesis SC1 (Sovio City Exterior Physical Boundaries - 100% AUDITED)**:
  - Status: Settled Turn 14727. Southern Avenue tree lines, southwest lawn (12, 30), southwest building perimeter, rear Biker lane (col 12, rows 20-30), western office facade (col 11, rows 16-20), Karate house corner (12, 15), Gumball/tan building gap (31, 13), northern alcove (39, 7), and elevated terrace (cols 50-52, rows 15-17) are 100% verified solid boundaries. No external event triggers exist.

## Archived Hypotheses (Exhausted / Evaluated)
- **Hypothesis SS1 (Sovio Sewers Eastern Storage Room - EXHAUSTED)**:
  - Status: Concluded Turn 14836. Audited multiple times (Turns 8637, 11127, 11149; Turn 14829 attempt aborted into wild combat). Tile (37, 14) displays ambient text 'Its a simple storage room...'; south tile is void chasm collision. Flanking tiles (36, 14) and (38, 14) are bare stone floor. Grunts retreated Turn 2682; sewers contain zero remaining progression triggers.
- **Hypothesis LA1 (Lancio Town Southern Coastline to Azluf - Cartographic Deduction)**:
  - Status: Evaluated Turn 14674/14731. World Map shows Lancio Town as a coastal terminus connecting exclusively northeast to Route 1. Traversing east to Azluf Town is water-gated by regional topology and impossible on foot without Surf or water transport.
- **Hypothesis SE1 (Sustained Exploration of Sovio Sewers Loop - RECONCILED)**:
  - Status: Concluded Turn 14428. The open loop (Western stairs -> Terrace -> Gangway -> Bridge -> Dark Sector) contains no roaming NPCs or triggers.