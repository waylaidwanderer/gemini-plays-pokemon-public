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

## Active Hypotheses for Progression
### Hypothesis H37: Pokémon Center PC Terminal & Storage Audit (Start: Turn 17713)
- **Premise**: Physical NPCs and surface landmarks in Sovio City have yielded zero progression triggers. We audit the physical PC terminal at (12, 1) in the Pokémon Center, specifically checking Someone's PC (Pokémon storage / gift Pokémon) and Mailbox for any unread messages or story items.
- **Audit Findings**:
  - Someone's PC (Box 1): Completely empty (0 Pokémon, 0 eggs).
  - Asher's PC (Item Storage): Contains Nugget x 1 (retrieved from Dark Sector). Zero keys or equipment stored.
- **Plan**:
  1. Boot up PC terminal at (12, 1) (Complete).
  2. Inspect Someone's PC -> Withdraw Pokémon (Complete, 0 stored Pokémon).
  3. Inspect Asher's PC -> Item Storage (Complete, Nugget x 1).
  4. Inspect Asher's PC -> Mailbox (In progress).

### Hypothesis H38: Sewer Storage Room Unlock & Capture Investigation
- **Premise**: Cutscene explicitly showed Jackson held captive by Team Siara in a sewer storage room. The platform door at (37, 14) displays "Its a simple storage room..." and has solid collision, indicating it cannot be opened without a specific key, event flag, or prerequisite trigger.
- **Plan**:
  1. Complete Mailbox audit (H37).
  2. Investigate potential unlock mechanisms: re-audit sewer layout for dropped keys, investigate Siara broadcast origin, or identify missing prerequisite triggers in Sovio City.