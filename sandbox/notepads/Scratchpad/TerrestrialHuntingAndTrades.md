# Scratchpad: Terrestrial Hunting & Trade Planning

## Expedition 16 Status (Terrestrial Biodiversity & Stone Evolutions)
- Started: Turn 42404
- Active Targets:
  - Target 3: Rattata (#019 RATTY) - CAUGHT Turn 43083, in party Slot 2. Needs training to Lv 20 for Raticate (#020) at Cerulean Cave 1F.
- Completed Targets Archived in Box 2:
  - Bellsprout (#069 SPROUT) [Turn 42628]
  - Weedle (#013 NEEDLE) [Turn 42784]
  - Caterpie (#010 SILK) [Turn 42786]
- Completed Targets in Active Party:
  - Wigglytuff (#040 PUFF Lv 3, Party Slot 3) [Evolved Turn 43213]
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

## PC Terminal Interface Observation & Empirical Testing Audit (Turns 43226–44010)
- State Description: Player at (13, 4) in Cerulean Pokémon Center facing PC terminal at (13, 3). Screen displays nested UI (Bill's PC, Party list with PUFF selected, 'What?', DEPOSIT/STATS/CANCEL submenu with cursor at DEPOSIT).
- Core Status: Storing Wigglytuff (PUFF) is 100% abandoned and non-essential. Active party is 3/6 (Mewtwo Lv 75, Rattata Lv 3, Wigglytuff Lv 3). Primary progression milestone is training Rattata to Lv 20 at Cerulean Cave 1F.
- Empirical Findings (Turns 43226–44042): Across all standard controller buttons and sequences tested following controller state clearance, the nested PC submenu remains completely unchanged (0 pixel delta). Baseline gameplay remains blocked at the PC terminal.

## Minimal Test Protocol Experiment (Turn 44044)
- Pre-Registered Hypothesis: Generation 1's HandleMenuInput requires a 0-to-1 edge transition in hJoyPressed to dismiss the submenu. Applying a single discrete B input tests whether edge-triggered cancellation is registered by the active game loop.
- Independent Variable: Single discrete 'B' controller input.
- Expected Falsifiable Outcome:
  - Positive: Submenu at bottom-right closes, restoring active solid cursor to party list.
  - Negative: Exactly 0 pixel delta across screen, falsifying the assumption that the active game loop is processing joypad inputs on this interface.
- Empirical Outcome (Turn 44046): Single 'B' input yielded exactly 0 pixel delta across both intermediate and final screen states.
- Conclusion: Hypothesis falsified. The active game loop is not evaluating edge-triggered menu cancellation via HandleMenuInput on this interface.

## Minimal Test Protocol Experiment 2 (Turn 44048)
- Pre-Registered Hypothesis: The active game loop is halted inside a text/dialogue wait routine for the 'What?' prompt box rather than HandleMenuInput, requiring an edge-triggered 'A' input to clear the text prompt state.
- Independent Variable: Single discrete 'A' controller input.
- Expected Falsifiable Outcome:
  - Positive: The 'What?' prompt box updates, clears, or advances, yielding a non-zero pixel delta.
  - Negative: Exactly 0 pixel delta across screen, falsifying the hypothesis that the active game loop is awaiting text confirmation on the 'What?' prompt box.
- Empirical Outcome (Turn 44050): Single 'A' input yielded exactly 0 pixel delta across both intermediate and final screen states.
- Conclusion: Hypothesis falsified. The active game loop is not halted inside a text/dialogue wait routine for the 'What?' prompt box.

## Minimal Test Protocol Experiment 3 (Turn 44051)
- Pre-Registered Hypothesis: The active menu handler is listening strictly for directional navigation (D-Pad Down) to update cursor position from DEPOSIT to STATS, while A/B buttons are inactive in the current sub-state.
- Independent Variable: Single discrete 'Down' controller input.
- Expected Falsifiable Outcome:
  - Positive: The solid cursor moves from DEPOSIT to STATS, yielding a non-zero pixel delta.
  - Negative: Exactly 0 pixel delta across screen, falsifying the hypothesis that directional cursor navigation is active on this interface.