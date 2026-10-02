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
- **Central Park Dating Couple (H29)**: Speaking to blonde girl (44, 24) and pink-shirt boy (33, 22) sequentially produces static reciprocal dialogue ("Was I catfished?"); verified zero quest triggers, items, or progression changes.
- **Gumball House 2F Audit (H30)**: Bed/sleeping resident at (27, 15-16) and blue PC terminal at (20, 12) verified 100% inert decorative scenery; green bookshelf at (22, 12) displays generic "It's crammed full of Pokémon books.". Zero progression triggers or clues.
- **Metro Station Lobby Audit (H31)**: Lobby 100% audited; west wall chairs (16, 24-25) confirmed inert decorative scenery. Platform visually audited: 4 blue chairs, yellow vending machine, station attendant at (22, 19). Turnstile passage at (19, 21) actively triggers 'I should find dad first!' and forces step back to (19, 22).
- **Inventory & System Audit (H32)**: Items Pocket (Potion x1, Poison Barb x1, Antidote x1), Key Items (HuPhone registered to SELECT, TM Case), Poké Balls (Timer Ball x1, Poké Ball x10). Zero equipment or keys in possession.
- **Sewer Storage Room & Platform Audit (H33)**: Fully audited platform (36-38, 12-14); doorway at (37, 14) is an inactive warp that bumps and displays "Its a simple storage room...". Platform tiles (37, 12 alcove; 38, 13-14 floor; 36, 14 void) contain zero items or switches. Doorway is currently inactive/locked from the outside.
- **West Avenue Exterior Landmarks (H34)**: Boy Rocky at (23, 17) and partner rock at (24, 17) re-verified static flavor text ("Rocky: ...", "It's just a normal rock..."). Southwest lawn (12-13, 30) verified dead-end pine boundary with zero items or hidden triggers.

- **Central Park Pond Feature (H35)**: Tested Turn 17705-17708. North curb/bank at (39, 17) has solid collision from row 16; interacting South into (39, 18) yields zero text. Confirmed non-interactive on foot.

## Active Hypotheses for Progression
### Hypothesis H36: Storage Room Access & Quest Triggers ("Medic!")
- **Premise**: Main story progression (finding Dad) is blocked at the turnstile ("I should find dad first!") and Route 2 ("I can't go yet... I have things to do!"). In the HuPhone Quest Log, Quest 4 is named "Medic!", and inside Sovio Pokémon Center a camper specifically complains his Weedle is poisoned. We test whether the camper triggers Quest 4 "Medic!" or provides a story clue.
- **Plan**:
  1. Enter Sovio Pokémon Center at (44, 12).
  2. Talk directly to the straw-hat Camper at (5, 7).
  3. Check if dialogue initiates "Medic!" or requests an Antidote.