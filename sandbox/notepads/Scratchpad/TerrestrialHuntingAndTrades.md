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

## PC Terminal Interface Testing Matrix & Empirical Findings (Turns 43226–43592)
- State Description: Player at (13, 4) in Cerulean Pokémon Center facing PC terminal at (13, 3). Screen displays nested UI:
  1. Top-left: Bill's PC menu (WITHDRAW, DEPOSIT, RELEASE, CHANGE BOX, SEE YA) with hollow arrow `▷` at DEPOSIT PKMN.
  2. Middle: Party Pokémon list (OMEGA Lv 75, RATTY Lv 3, PUFF Lv 3, CANCEL) with hollow arrow `▷` at PUFF.
  3. Bottom-left: Text box with label 'What?'.
  4. Bottom-right: Action submenu with choices DEPOSIT, STATS, CANCEL, with solid arrow `▶` at DEPOSIT.
- Empirical Findings & Tested Button Sequences (all resulting in 0 pixel delta):
  1. Single-step isolated inputs: A (Turn 43440, 43511, 43525), B (56+ turns including Turns 43512, 43526-43559, 43562-43589), Down (Turn 43461), Up (Turn 43499), Start (Turn 43497), Select (Turn 43498), Right (Turn 43502), Left (Turn 43503).
  2. Multi-button chunked inputs: ['Down', 'Down', 'A'] (Turns 43508, 43520), ['Up', 'Up', 'A'] (Turn 43509), ['Down', 'A'] (Turn 43514), ['A', 'A', 'A'] (Turn 43561), ['A']*5 (Turn 43479), ['Down']*5 (Turn 43468), ['B']*8 (Turn 43483), ['B']*20 (Turn 43518), ['B', 'B', 'B', 'B', 'A'] (Turn 43521).
  3. Interleaved dummy sequences: ['B', 'Right', ...] (Turn 43504), ['B', 'Select', ...] (Turn 43516), ['Start', 'Select', 'Right', 'Left'] (Turn 43474).
  4. Global reset sequence: ['A', 'B', 'Start', 'Select'] (Turn 43513) - sequential presses do not trigger soft reset.
  5. Directional walking: ['Down'x3, 'Left'x10, 'Down'x2] (Turns 43488, 43492) - confirmed menus block overworld grid movement.
- Analysis & Active Hypotheses:
  - Solid arrow at DEPOSIT verifies submenu possesses active focus.
  - Retraction: Prior assertion that Box 2 is full and causes 0-delta error tone on DEPOSIT was an unverified hypothesis. In retail Gen 1 pokered engine, BillsPC_Deposit checks box capacity and prints 'The BOX is full.' before displaying the party menu. The fact that the party menu opened confirms Box 2 is not full.
  - Plan: Press A to confirm DEPOSIT of PUFF into Box 2, advance through storage confirmation text, and exit PC to proceed to Cerulean Cave for RATTY training.