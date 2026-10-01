# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Investigation Status & Active Hypotheses (Updated Turn 12810)
- **Verified Game State**:
  - Metro Turnstile at (19, 21): Re-tested Turn 12777 (post-quest-cancellation & threshold sweep); strictly displays "I should find dad first!" and repels South to (19, 22).
  - Route 2 Exit at (52, 19-22): Displays "I can't go yet... I have things to do!" (Repels West).
  - Professor Ivo's Lab Stairs at (12, 7): Displays "I probably shouldn't head down here..."
  - Sovio Sewers Storage Room at (37, 14): Displays "Its a simple storage room..."
  - Active Quest: None (Machop's Toy officially cancelled on Turn 12771 with Old Man at 51, 15; quest slot free).
  - *Core Fact*: Jackson remains MISSING following the seismic tremor (Turn 1437). Every primary progression gate confirms finding Jackson is mandatory to advance.

## Settled / Falsified Hypotheses (Condensed)
- **Hypothesis H (Central Plaza Exterior Threshold Sweep)**: Tested Turn 12774. Traversed (45, 14) -> (45, 19) -> (49, 19) -> (49, 18) -> (48, 18); confirmed zero automated script triggers or cutscenes outside Metro portal.
- **Hypothesis I (Pre-Turnstile Metro Lobby NPCs/Trigger)**: Tested Turn 12775-12777. Lobby contains zero NPCs (Dad and Valora absent); turnstile at (19, 21) strictly blocks passage with 'I should find dad first!'.
- **Cognitive Correction on Jackson Status**: Context summary statements claiming Asher reunited with Jackson and Valora on Turn 2279-2716 are confirmed context summarization hallucinations. Verifiable ground truth: Jackson was held by grunts (Turn 1666), sewer storage room at (37, 14) is empty, and Jackson has NOT been found. Finding Jackson remains the active primary blocker.
- **Hypothesis A (Karate House Direct Story Gate)**: Falsified Turn 12132. Karate House residents and 2F audited ambient flavor; cancelling quest did not unlock Metro.
- **Hypothesis B (Sewers Storage Room)**: On hold. Room at (37, 14) currently inert ("Its a simple storage room...").
- **Hypothesis E (HuPhone Menu Inspection)**: Falsified Turn 12410. Item Storage, Mailbox, Quest Log, and World Map verified empty/static; passive digital checks do not trigger story progression.
- **Hypothesis F (Cottage East Ledge Northbound)**: Falsified Turns 12444, 12455. Row 20 ledge strictly prevents northward traversal from Cottage yard (0 tiles visited on 3 Up inputs).
- **Hypothesis G (Route 1 Two-Way Connection)**: Verified Turn 12564. Confirmed two-way foot route between Lancio Town and Sovio City via row 10 meadow and Eastern Highway; documented in Locations/Route_1.md.
- **Sub-Hypothesis 1 (Machop's Toy Ground Search in Sewers)**: CLOSED Turn 12724. Tested northern and western corridors (Western Terrace 14, 12; Northern Gangway 15-27, 5; puddles at 33-35, 22; 36-38, 27-28; 28, 19; 14-15, 11; 26-27, 5) with zero visible item balls or prompts found. Quest strategically deprioritized to refocus on primary story progression and locating Jackson on the surface.

## Active Investigation: Jackson's Whereabouts & Sovio City Surface Facilities

### Hypothesis J: Uninspected Sovio City Public Facilities & NPC States
- **Status**: ACTIVE.
- **Rationale**: Subterranean loops are exhausted (storage room 37, 14 inert, grunts vacated). Jackson disappeared onto the surface after the tremor (Turn 1437). Systematic check of civic/commercial facilities in Sovio City in the post-retreat state.
- **Target 1: Sovio City Pokémon Center & Mezzanine PokéMart**
  - Nurse Joy counter: Tested Turns 12788-12790; standard healing sequence, sets respawn checkpoint, zero story dialogue.
  - Boy in blue shirt: Tested Turns 12806-12808; confirmed unchanged ambient advice regarding corner PC ("Please feel free to use that PC in the corner. The receptionist told me so.").
  - Straw-hat Camper (5, 7): Tested Turn 12813; confirmed unchanged ambient dialogue regarding poisoned Weedle ("My weedle got poisoned so I will need t...").
  - Mezzanine PokéMart clerk (5, 3): Pending upstairs audit.
  - Protocol: Speak to all occupants to verify if dialogue updated or new clues are provided.
- **Target 2: Northern Commercial/Residential Row & Central Park Flanks**
  - Check non-enterable building facades and Central Park pond perimeter for post-sewer updates.
