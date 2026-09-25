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

## Active Hypothesis & Test Protocol (Turn 43681)
- Hypothesis: Active solid cursor at DEPOSIT requires a 2-step confirmation (first A confirms deposit routine, second A clears the '[POKéMON] was stored' dialogue) followed by B cancellation to dismiss parent party menu.
- Independent Variable: Sequential chunk ['A', 'A', 'B', 'B'].
- Expected Falsifiable Outcome: Visual transition clearing the submenu and advancing storage dialogue to exit interface.
- Result: Falsified Turn 43682 with zero pixel delta across all intermediate states.

## Test Protocol 2: Isolated Start Evaluation (Turn 43682)
- Hypothesis: Pressing Start acts as an immediate dialog/menu dismissal key in nested UI states.
- Independent Variable: Isolated single input ['Start'].
- Expected Falsifiable Outcome: Visual transition closing submenu or updating menu layer.
- Result: Falsified Turn 43683 with zero pixel delta.

## Test Protocol 3: Isolated Select Evaluation (Turn 43683)
- Hypothesis: In certain party/PC menus, pressing Select functions as an item reorganization or sub-state toggle.
- Independent Variable: Isolated single input ['Select'].
- Expected Falsifiable Outcome: Visual transition shifting cursor or updating UI state.
- Result: Falsified Turn 43684 with zero pixel delta.

## Test Protocol 4: STATS Inspection & UI Transition (Turn 43685)
- Hypothesis: Selecting STATS (Down + A) transitions the UI into a full-screen STATS display, providing an alternate exit pathway back to the party menu.
- Independent Variable: Sequential input ['Down', 'A'].
- Expected Falsifiable Outcome: Screen transitions to PUFF's STATS display.
- Result: Falsified Turn 43685 with zero pixel delta.

## Test Protocol 5: Direct CANCEL Selection (Turn 43686)
- Hypothesis: Directly navigating to CANCEL via two discrete Down inputs followed by an A confirmation (['Down', 'Down', 'A']) executes the submenu's native CANCEL routine, dismissing the submenu back to the party list.
- Independent Variable: Sequential input ['Down', 'Down', 'A'].
- Expected Falsifiable Outcome: Submenu closes, restoring solid cursor focus to the party list.
- Result: Falsified Turn 43686 with zero pixel delta.

## Test Protocol 6: Party List Upward Scroll (Turn 43687)
- Hypothesis: Testing whether Up inputs scroll the underlying party list upward to display lead party members.
- Independent Variable: Sequential input ['Up', 'Up', 'Up'].
- Expected Falsifiable Outcome: Visual scroll of party list to show DUX/SHELDON.