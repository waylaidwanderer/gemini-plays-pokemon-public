# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City (re-verified Turn 17681).
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher 1 step south to (19, 22) (re-verified Turn 17675). Attendant at (22, 18-19) is unreachable behind solid wall/turnstile structure.
- **Rugged Rocks (Sewers)**: (22, 10) and (10, 18) display "It's a rugged rock, but with some equipment, I could smash it." Field obstacle clearance requires specialized player equipment rather than traditional HM moves. Zero equipment currently in possession.

## Settled Inquiries
- **Route 1, Lancio Town & Inizio Isle (H24)**: 100% audited; verified devoid of active triggers for Jackson.
- **Sovio Surface Residences & Facilities (H26)**: All civilian homes (Karate, Gumball, Wii, Nana, Name Rater), Pokémon Center (1F & 2F), and Metro lobby alcoves 100% physically audited; zero story triggers or NPCs present.
- **Sovio Outdoor Perimeters (H27)**: Southern sidewalk (rows 27-31), Central Park, and Route 2 barrier (52, 19-22) audited; barrier active, NPCs ambient.
- **Sewer Subterranean Audit (H28)**: 100% physically mapped; upper landing, lower corridor (row 28), western terrace, catwalks, and Dark Sector contain zero interactive triggers, items, or NPCs post-retreat. Rugged rocks require specialized equipment.
- **Inventory & System Audit (H32)**: Items Pocket (Potion x1, Poison Barb x1, Antidote x1), Key Items (HuPhone registered to SELECT, TM Case), Poké Balls (Timer Ball x1, Poké Ball x10). Zero equipment or keys in possession.
- **Sewer Storage Room & Platform Audit (H33)**: Fully audited platform (36-38, 12-14); doorway at (37, 14) is an inactive warp that bumps and displays "Its a simple storage room...". Platform tiles (37, 12 alcove; 38, 13-14 floor; 36, 14 void) contain zero items or switches. Doorway is currently inactive/locked from the outside.

- **PC Terminal & Storage Audit (H37, Turns 17713-17734)**: Someone's PC Box 1 empty (0 Pokémon, 0 eggs); Asher's PC Item Storage contains only Nugget x 1; Mailbox displays "There's no Mail here.". Zero items, messages, or progression flags present in PC.

## Active Hypotheses for Progression
### Hypothesis H38: Sewer Storage Room Unlock & Patrol Position Audit
- **Premise**: Cutscene explicitly showed Jackson held captive by Team Siara in a sewer storage room. The platform door at (37, 14) displays "Its a simple storage room..." and has solid collision, indicating it cannot be opened without a specific key, event flag, or prerequisite trigger. We audit the former grunt battle locations in Sovio Sewers (such as Grunt 2's platform at 18, 21-22 and the lower walkway) to check for dropped keys, hidden switches, or overlooked triggers.
- **Audit Findings**:
  - Grunt 2's platform (17-18, 21-22): 100% audited. Zero dropped keys, items, or hidden mechanisms present.
  - Western Terrace (12-17, 11-12): 100% audited. Zero dropped keys, items, or hidden switches present.
- **Plan**:
  1. Exit Pokémon Center to Sovio City (Complete).
  2. Enter Sovio Sewers via Metro Station mat at (18-19, 25) (Complete).
  3. Inspect Grunt 2's platform (18, 21-22) (Complete, 0 items).
  4. Inspect rugged rock (10, 18) and Western Terrace (Complete, 0 items).
  5. Audit Northern Gangway (row 5) and bridge (In progress).