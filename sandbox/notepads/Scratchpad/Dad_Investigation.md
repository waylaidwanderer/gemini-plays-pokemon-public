# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Blockers & Status
- **Metro Turnstile**: Stepping onto (19, 21) triggers "I should find dad first!" and forces Asher 1 step down to (19, 22) (re-verified active Turn 14644).
- **Route 2 Gate**: Stepping onto (52, 19-22) triggers "I can't go yet... I have things to do!" (re-verified active Turn 14647).
- **Jackson Status**: Captured by Team Siara during tremor cutscene (Turn 1666). Marie broadcast radio retreat on Turn 2682. Jackson's whereabouts remain the central progression gate.

## Verified / Settled Locations
- **Sovio Metro Lobby**:
  - Timetable Board (columns 21-23): Verified Turns 7149, 14276-14278 as purely decorative flavor text ("It's a timetable showing various destinations!").
  - Platform Attendant at (22, 19): Inaccessible behind solid north brick wall at row 23; platform passage gated at turnstile (19, 21).
- **Global Storage Systems (Verified Turns 14291-14315)**: HuPhone Mailbox ('There's no Mail here.'), HuPhone Item Storage ('There are no items.'), and Someone's PC Box 1 (0 Pokémon) audited 100% empty. Party size/composition does not gate turnstile blocker.
- **Sovio Sewers Audited Features**:
  - Machop's Toy Quest: Completed Turn 13331 (Black Belt obtained).
  - Deep Subterranean Sector (2, 38): Audited Turn 14052; single-purpose quest room, all perimeter walls inert.

## Active Hypotheses & Strategic Focus
- **Hypothesis SS2 (Sovio Sewers Inner Sectors & Jackson Detention Cell)**:
  - **Rationale**: Progression analysis confirms the Metro blocker ('I should find dad first!') is hard-coded to Jackson's rescue event flag. Tile (37, 14) returning 'Its a simple storage room...' was an ambient prop, not Jackson's actual cutscene cell. Marie's broadcast (Turn 2682) cleared the grunts, but Jackson's sprite remains waiting in an accessible room, alcove, or platform in the sewer complex.
  - **Primary Objective**:
    1. Sewer Western Terrace & Grunt 2 Platform Audit (Cols 14-19, Rows 11-23): Systematically probe terrace perimeter and Grunt 2's platform for Jackson or detention room entrance.

## Settled Hypotheses
- **Hypothesis SC2 (Sovio City Commercial Building & Surface Audits - 100% SETTLED)**: Verified decorative exterior with zero doors or triggers (documented in Locations/Sovio_City.md).
- **Hypothesis SC1 (Sovio City Exterior Map Boundaries - 100% AUDITED)**:
  - Status: Settled Turn 14727. Map edge perimeters (Southern Avenue tree lines, southwest lawn at 12, 30, rear Biker lane at col 12, western office boundary at col 11, northern alcove at 39, 7, and elevated terrace edge at col 52) are 100% verified solid dead-ends with no map exits. Note: Internal urban building facades and interactions within city limits remain subject to specific auditing under SC2.

## Archived Hypotheses (Exhausted / Evaluated)
- **Hypothesis SS1 (Sovio Sewers Eastern Storage Room - EXHAUSTED)**:
  - Status: Concluded Turn 14836. Audited multiple times (Turns 8637, 11127, 11149; Turn 14829 attempt aborted into wild combat). Tile (37, 14) displays ambient text 'Its a simple storage room...'; south tile is void chasm collision. Flanking tiles (36, 14) and (38, 14) are bare stone floor. 
