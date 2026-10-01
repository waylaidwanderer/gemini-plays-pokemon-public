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
- **Hypothesis SS2 (Sovio Sewers Inner Perimeter & Jackson Rescue Flag)**:
  - **Rationale**: Marie's retreat broadcast (Turn 2682) despawned hostile grunts, but Jackson's captive state was never cleared, leaving the Metro turnstile blocked ('I should find dad first!'). In Pokémon Sors / CFRU scripting, grunts guard the path leading directly to the captive NPC. We must advance to the terminus of the grunt corridor (upper gangway, storage room, and adjacent sectors) to locate Jackson's holding area and trigger his dialogue/rescue.
  - **Primary Objectives**:
    1. Ascend western stairs at (14, 17) to Western Terrace and take the wall ladder at (15, 6-10) to the northern gangway.
    2. Cross the vertical bridge at column 23 to row 13 platform.
    3. Systematically audit the eastern gangway (row 13) leading to the storage room at (37, 14), probing all wall segments, corridor thresholds, and the command post area where the Turn 2682 retreat fired.

## Settled Hypotheses
- **Hypothesis SC2 (Sovio City Commercial Building & Surface Audits - 100% SETTLED)**:
  - Status: Settled Turn 14969. Commercial building southern facade (47-51, 28-31) verified decorative wooden shutters with trash can / hedge barriers and zero enterable doors. Surface structures contain zero entry points or progression triggers. Validates that Jackson's progression gate must be resolved within Sovio Sewers.
- **Hypothesis SC1 (Sovio City Exterior Map Boundaries - 100% AUDITED)**:
  - Status: Settled Turn 14727. Map edge perimeters (Southern Avenue tree lines, southwest lawn at 12, 30, rear Biker lane at col 12, western office boundary at col 11, northern alcove at 39, 7, and elevated terrace edge at col 52) are 100% verified solid dead-ends with no map exits. Note: Internal urban building facades and interactions within city limits remain subject to specific auditing under SC2.

## Archived Hypotheses (Exhausted / Evaluated)
- **Hypothesis SS1 (Sovio Sewers Eastern Storage Room - EXHAUSTED)**:
  - Status: Concluded Turn 14836. Audited multiple times (Turns 8637, 11127, 11149; Turn 14829 attempt aborted into wild combat). Tile (37, 14) displays ambient text 'Its a simple storage room...'; south tile is void chasm collision. Flanking tiles (36, 14) and (38, 14) are bare stone floor. Grunts retreated Turn 2682; sewers contain zero remaining progression triggers.
- **Hypothesis LA1 (Lancio Town Southern Coastline to Azluf - Cartographic Deduction)**:
  - Status: Evaluated Turn 14674/14731. World Map shows Lancio Town as a coastal terminus connecting exclusively northeast to Route 1. Traversing east to Azluf Town is water-gated by regional topology and impossible on foot without Surf or water transport.
- **Hypothesis SE1 (Sustained Exploration of Sovio Sewers Loop - RECONCILED)**:
  - Status: Concluded Turn 14428. The open loop (Western stairs -> Terrace -> Gangway -> Bridge -> Dark Sector) contains no roaming NPCs or triggers.