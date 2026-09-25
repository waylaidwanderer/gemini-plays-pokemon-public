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
- Systematic Empirical Testing Log (Turns 43226–44010):
  - Discrete Single-Button Audit (Turns 43933–43947): Tested each standard Game Boy controller button individually following controller state clearance (mgba.clear_buttons):
    - B (Turn 43933), Down (Turn 43934), A (Turn 43936), Start (Turn 43943), Select (Turn 43944), Up (Turn 43945), Left (Turn 43946), Right (Turn 43947). Outcome: 0 pixel difference across all frames.
  - Directional & Navigation Sequences:
    - Down, Down, A (Turn 43964): Tested navigating to CANCEL; 0 pixel difference.
    - Down x4 (Turn 43967): Tested overworld turn-and-walk southward; 0 pixel difference, position remained (13, 4).
    - Down, A (Turn 43984): Tested opening STATS; 0 pixel difference.
    - Up, A (Turn 43989): Tested upward menu wrap to CANCEL; 0 pixel difference.
    - A, Down, Down, A (Turn 44004): Tested prompt clearing before CANCEL navigation; 0 pixel difference.
  - Multi-Layer Menu Dismissal Sequences:
    - B x3 (Turn 43938, 43992, 44006), B x5 (Turn 43973), B x2 (Turn 43987, 43994, 44001, 44008): Tested unwinding nested menus; 0 pixel difference.
    - B, A, B (Turn 43993), B, A (Turn 43995): Tested dual prompt-clear and cancellation; 0 pixel difference.
    - B, Down, A (Turn 44005), B, Down, B (Turn 44009), Down, B (Turn 44000): Tested multi-layer party exit; 0 pixel difference.
  - Confirmation Sequences:
    - A x3 (Turn 43996), A, A, B, B, B (Turn 43974): Tested confirming DEPOSIT and subsequent dialogue; 0 pixel difference.
    - A, B (Turn 44007): Tested action confirmation and prompt clear; 0 pixel difference.
  - Alternative Inputs & Reset Testing:
    - A, B, Start, Select (Turn 43959): Sequential soft reset attempt; 0 pixel difference.
    - Start, A, Start, A (Turn 43988), Select, B (Turn 43997): Shortcut and mode toggle testing; 0 pixel difference.
- Conclusion: Across 784 consecutive turns and dozens of independent variables, the nested PC submenu remains completely unchanged (0 pixel delta). The UI is visually static, but our active team is fully prepared for Cerulean Cave progression.