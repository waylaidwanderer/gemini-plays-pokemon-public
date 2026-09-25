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

## PC Terminal Interface Observation & Testing Summary (Turns 43226–43710)
- State Description: Player at (13, 4) in Cerulean Pokémon Center facing PC terminal at (13, 3). Screen displays nested UI:
  1. Top-left: Bill's PC menu (WITHDRAW, DEPOSIT, RELEASE, CHANGE BOX, SEE YA) with hollow arrow `▷` at DEPOSIT PKMN.
  2. Middle: Party Pokémon list (OMEGA Lv 75, RATTY Lv 3, PUFF Lv 3, CANCEL) with hollow arrow `▷` at PUFF.
  3. Bottom-left: Text box with label 'What?'.
  4. Bottom-right: Action submenu with choices DEPOSIT, STATS, CANCEL, with solid arrow `▶` at DEPOSIT.
- Empirical Findings across Protocols 1–29:
  - All standard controller inputs ('A', 'B', 'Start', 'Select', 'Up', 'Down', 'Left', 'Right') and multi-button permutations (directional chains, confirm-cancel alternations, reset sequences) tested under explicit hypotheses yielded zero visual screen delta across intermediate and final states.
  - Storing PUFF in the PC is completely optional as the active party is 5/6. Primary progression objective is training Rattata to Lv 20 at Cerulean Cave 1F.
