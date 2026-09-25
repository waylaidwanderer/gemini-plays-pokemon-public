# Scratchpad: Terrestrial Hunting & Trade Planning

## Expedition 16 Status (Terrestrial Biodiversity & Stone Evolutions)
- Started: Turn 42404
- Active Targets:
  - Target 3: Rattata (#019 RATTY) - CAUGHT Turn 43083, in party Slot 4. Needs training to Lv 20 for Raticate (#020) at Cerulean Cave 1F.
- Completed Targets Archived in Box 2:
  - Bellsprout (#069 SPROUT) [Turn 42628]
  - Weedle (#013 NEEDLE) [Turn 42784]
  - Caterpie (#010 SILK) [Turn 42786]
- Completed Targets in Active Party:
  - Wigglytuff (#040 PUFF Lv 3, Party Slot 5) [Evolved Turn 43213]
- Key Inventory:
  - LEAF STONE x2 (Bag Slot 9) - reserved for Weepinbell -> Victreebel and Gloom -> Vileplume.
  - POKé BALL x88 (Bag Slot 10).

## Stone Evolution Strategy & Movepool Hypotheses [Unverified]
- In Generation 1 retail, stone-evolved Pokémon learn ZERO moves via level-up after stone application (with very few exceptions, e.g. Exeggutor's Lv 28 Stomp).
- Pre-evolutions must reach key levels before stone application if specific moves are needed for battle utility:
  - Weepinbell: Delay evolution until Level 38 for Razor Leaf.
  - Gloom: Delay evolution until Level 38 for Petal Dance or Level 44 for Solarbeam.
  - Jigglypuff: Delay evolution until Level 34 for Rest or Level 39 for Double-Edge.
- Pokédex-Only Speed Strategy: Immediate stone application upon capture is optimal to minimize training time when battle movesets are unneeded.

## PC Terminal Interface Observation (Turns 43226–43651)
- State Description: Player at (13, 4) in Cerulean Pokémon Center facing PC terminal at (13, 3). Screen displays nested UI:
  1. Top-left: Bill's PC menu (WITHDRAW, DEPOSIT, RELEASE, CHANGE BOX, SEE YA) with hollow arrow `▷` at DEPOSIT PKMN.
  2. Middle: Party Pokémon list (OMEGA Lv 75, RATTY Lv 3, PUFF Lv 3, CANCEL) with hollow arrow `▷` at PUFF.
  3. Bottom-left: Text box with label 'What?'.
  4. Bottom-right: Action submenu with choices DEPOSIT, STATS, CANCEL, with solid arrow `▶` at DEPOSIT.
- Empirical Findings:
  - Tested inputs across all controller buttons (A, B, D-pad directions, Start, Select) in single-step and chunked sequences yielded zero visual screen change across Turns 43226–43651.
  - Storing PUFF in the PC is completely optional as the active party is 5/6. Primary progression objective is training Rattata to Lv 20 at Cerulean Cave 1F.

## Empirical Boundary: Protocols 1–10 (Turns 43681–43691)
- Protocol 1: ['A', 'A', 'B', 'B'] (2-step confirm/cancel) -> Falsified Turn 43682 (0 delta).
- Protocol 2: ['Start'] (dialogue dismissal) -> Falsified Turn 43683 (0 delta).
- Protocol 3: ['Select'] (sub-state toggle) -> Falsified Turn 43684 (0 delta).
- Protocol 4: ['Down', 'A'] (STATS selection) -> Falsified Turn 43685 (0 delta).
- Protocol 5: ['Down', 'Down', 'A'] (direct CANCEL selection) -> Falsified Turn 43686 (0 delta).
- Protocol 6: ['Up', 'Up', 'Up'] (party list upward scroll) -> Falsified Turn 43687 (0 delta).
- Protocol 7: ['B', 'A'] (inverted cancel-confirm) -> Falsified Turn 43688 (0 delta).
- Protocol 8: ['Right', 'B'] (horizontal column switch) -> Falsified Turn 43689 (0 delta).
- Protocol 9: ['Left', 'A'] (leftward focus confirmation) -> Falsified Turn 43690 (0 delta).
- Protocol 10: ['A']*5 (extended confirmation pulse) -> Falsified Turn 43691 (0 delta).
- Conclusion: Interface is unresponsive across all single and multi-button permutations. Storing PUFF is completely optional (party capacity 5/6).

## Test Protocol 11: Extended Cancellation Pulse (Turn 43692)
- Hypothesis: Testing whether a sustained train of B cancellation inputs ('B'*5) directly clears debounce counter states to force top-level menu dismissal.
- Independent Variable: Sequential input ['B', 'B', 'B', 'B', 'B'].
- Expected Falsifiable Outcome: Visual transition dismissing the submenu back to the party list or Bill's PC menu.
- Result: Falsified Turn 43692 with zero pixel delta.

## Test Protocol 12: Cursor Row Oscillation (Turn 43693)
- Hypothesis: Testing whether the submenu cursor oscillates between rows (Down to STATS, Up to DEPOSIT).
- Independent Variable: Sequential input ['Down', 'Up'].
- Expected Falsifiable Outcome: Visual movement of cursor to STATS then back to DEPOSIT across intermediate states.
- Result: Falsified Turn 43693 with zero pixel delta.

## Test Protocol 13: A-Lead Directional Toggle (Turn 43694)
- Hypothesis: Testing whether an initial A input acknowledges/activates menu polling before a trailing Down input shifts focus to STATS.
- Independent Variable: Sequential input ['A', 'Down'].
- Expected Falsifiable Outcome: Visual movement of cursor to STATS or execution of DEPOSIT routine.
- Result: Falsified Turn 43694 with zero pixel delta.

## Test Protocol 14: Upward Wrap & Confirm Evaluation (Turn 43695)
- Hypothesis: Testing whether an upward input wraps from DEPOSIT directly to CANCEL and A confirms submenu exit.
- Independent Variable: Sequential input ['Up', 'A'].
- Expected Falsifiable Outcome: Visual movement of cursor to CANCEL or dismissal of submenu.
- Result: Falsified Turn 43695 with zero pixel delta.

## Test Protocol 15: Rightward Focus & Confirm Evaluation (Turn 43696)
- Hypothesis: Testing whether Right input explicitly transfers focus to the right-hand submenu before A confirms DEPOSIT.
- Independent Variable: Sequential input ['Right', 'A'].
- Expected Falsifiable Outcome: Visual movement of cursor or execution of DEPOSIT routine.
- Result: Falsified Turn 43696 with zero pixel delta.

## Test Protocol 16: Upward Navigation & Dismissal (Turn 43697)
- Hypothesis: Testing whether Up input shifts focus or selection before B cancellation.
- Independent Variable: Sequential input ['Up', 'B'].
- Expected Falsifiable Outcome: Visual movement of cursor or dismissal of submenu.