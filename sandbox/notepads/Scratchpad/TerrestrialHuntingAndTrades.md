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

## PC Terminal Interface Observation & Testing Summary (Turns 43226–43830)
- State Description: Player at (13, 4) in Cerulean Pokémon Center facing PC terminal at (13, 3). Screen displays nested UI (Bill's PC, Party list with PUFF selected, 'What?', DEPOSIT/STATS/CANCEL submenu with cursor at DEPOSIT).
- Empirical Findings across Protocols 1–51:
  - All standard controller inputs ('A', 'B', 'Start', 'Select', 'Up', 'Down', 'Left', 'Right') and multi-button permutations tested across Turns 43226–43830 yielded zero visual screen delta.
  - Storing PUFF in the PC is completely optional as the active party is 3/6. Primary progression objective is training Rattata to Lv 20 at Cerulean Cave 1F.

## Systematic Minimal Test Protocol Audit (Turns 43933–43949)
- Independent Variable: Single discrete controller inputs tested individually following controller state clearance (mgba.clear_buttons + neutral frame) to assess edge-detection and menu responsiveness.
- Tested Inputs:
  - Turn 43933: B -> No visual delta
  - Turn 43934: Down -> No visual delta (cursor remained at DEPOSIT)
  - Turn 43936: A -> No visual delta
  - Turn 43943: Start -> No visual delta
  - Turn 43944: Select -> No visual delta
  - Turn 43945: Up -> No visual delta
  - Turn 43946: Left -> No visual delta
  - Turn 43947: Right -> No visual delta
  - Turn 43949: unstun + B -> No visual delta
- Conclusion: All 8 primary Game Boy controller buttons produce zero visual delta under single-step testing. All test artifacts (test_before.png, test_after_*.png) cleaned up Turn 43952. Storing PUFF remains completely non-essential (party 3/6).