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

## PC Terminal Interface Observation & Testing Summary (Turns 43226–43772)
- State Description: Player at (13, 4) in Cerulean Pokémon Center facing PC terminal at (13, 3). Screen displays nested UI (Bill's PC, Party list with PUFF selected, 'What?', DEPOSIT/STATS/CANCEL submenu with cursor at DEPOSIT).
- Empirical Findings across Protocols 1–38:
  - All standard controller inputs ('A', 'B', 'Start', 'Select', 'Up', 'Down', 'Left', 'Right') and multi-button permutations tested across Turns 43226–43750 yielded zero visual screen delta.
  - Storing PUFF in the PC is completely optional as the active party is 5/6 (or 3 active trainees/sweepers). Primary progression objective is training Rattata to Lv 20 at Cerulean Cave 1F.

## Test Protocol 39: Isolated Submenu Dismissal (Turn 43805)
- Hypothesis: Single B input dismisses the DEPOSIT/STATS/CANCEL submenu to return focus to the party list.
- Independent Variable: Isolated controller input ['B'].
- Result: Falsified Turn 43806 with zero pixel delta across intermediate and final states.

## Test Protocol 40: Isolated Storage Confirmation (Turn 43806)
- Hypothesis: Single A input confirms DEPOSIT on PUFF to initiate the storage routine or display a box capacity notice.
- Independent Variable: Isolated controller input ['A'].
- Expected Falsifiable Outcome: Screen transition displaying storage dialogue ('PUFF was stored in BOX 2.') or capacity notice ('The BOX is full.').
- Result: Falsified Turn 43808 with zero pixel delta across intermediate and final states.

## Test Protocol 41: Isolated Down Navigation (Turn 43808)
- Hypothesis: Single Down directional input shifts the selection cursor from DEPOSIT to STATS.
- Independent Variable: Isolated controller input ['Down'].
- Expected Falsifiable Outcome: Visual movement of solid cursor arrow from DEPOSIT (row 11) to STATS (row 13).
- Result: Falsified Turn 43810 with zero pixel delta across intermediate and final states.
## Test Protocol 42: Sequential Double B Submenu Dismissal (Turn 43811)
- Hypothesis: Two consecutive B inputs provide both the cancel trigger and the edge transition needed to clear the active submenu and restore party list focus.
- Independent Variable: Sequential input ['B', 'B'].
- Expected Falsifiable Outcome: Visual dismissal of the lower-right DEPOSIT/STATS/CANCEL window.
- Result: Falsified Turn 43813 with zero pixel delta across intermediate and final states.

## Test Protocol 43: Sequential Down-A to Stats Screen (Turn 43813)
- Hypothesis: Down shifts cursor from DEPOSIT to STATS, and A confirms selection to open the full-screen Pokémon STATS interface.
- Independent Variable: Sequential input ['Down', 'A'].
- Expected Falsifiable Outcome: Transition from nested PC windows to the full-screen STATS display for PUFF.
- Result: Falsified Turn 43815 with zero pixel delta across intermediate and final states.

## Test Protocol 44: Sequential Down-Down-A to Confirm Cancel (Turn 43815)
- Hypothesis: Two Down directional inputs navigate cursor to CANCEL, and A confirms selection to dismiss the submenu.
- Independent Variable: Sequential input ['Down', 'Down', 'A'].
- Expected Falsifiable Outcome: Visual movement of cursor to CANCEL and dismissal of the lower-right submenu.