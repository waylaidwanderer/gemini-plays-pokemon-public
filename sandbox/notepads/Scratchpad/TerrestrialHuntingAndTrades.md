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

## PC Terminal Interface Observation & Empirical Testing Audit (Turns 43226–44102)
- State Description: Player at (13, 4) in Cerulean Pokémon Center facing PC terminal at (13, 3). Screen displays nested UI (Bill's PC, Party list with PUFF selected, 'What?', DEPOSIT/STATS/CANCEL submenu with cursor at DEPOSIT).
- Core Status: Storing Wigglytuff (PUFF) is abandoned. Active party is 3/6 (Mewtwo Lv 75, Rattata Lv 3, Wigglytuff Lv 3). Primary progression milestone is training Rattata to Lv 20 at Cerulean Cave 1F.
- Empirical Findings (Turns 43226–44102): Across all standard controller buttons and sequences tested (discrete single inputs of B, A, Down, Up, Start, Select; sequences ['A', 'A'] and ['Down', 'Down', 'A']), the nested PC submenu remains completely unchanged (0 pixel delta across all intermediate and final frames).

## Discrete Input Test History & Empirical Outcomes
- Discrete Inputs (Turns 44044–44060): Tested single taps of B (Turn 44046), A (Turn 44050), Down (Turn 44053), Up (Turn 44056), Start (Turn 44059), and Select (Turn 44060). Each produced exactly 0 pixel delta.
- Edge Transition Test (Turn 44082): Sent single discrete 'B' input after clearing controller state. Empirical Outcome: 0 pixel delta. Submenu remained open.
- Deposit Confirmation Test (Turn 44094): Theoretical hypothesis was that Box 2 had available capacity based on the prerequisite model. Sent ['A', 'A'] via press_buttons to test confirming DEPOSIT. Empirical Outcome: Exactly 0 pixel delta across both intermediate frames and final frame; menu state completely unchanged.
- Cancel Submenu Navigation Test (Turn 44099): Theoretical hypothesis was that navigating cursor to CANCEL via Down twice and confirming with A would dismiss submenu. Sent ['Down', 'Down', 'A'] via press_buttons. Empirical Outcome: Exactly 0 pixel delta across all three intermediate frames (turn_44100_0, turn_44100_1, turn_44100_2) and final frame (Turn 44102); menu state completely unchanged.

- Discrete Left Input Test (Turn 44103): Sent single discrete 'Left' input via press_buttons. Empirical Outcome: Exactly 0 pixel delta across intermediate (turn_44104_0) and final frame; menu state unchanged.
- Discrete Right Input Test (Turn 44104): Sent single discrete 'Right' input via press_buttons. Empirical Outcome: Exactly 0 pixel delta across intermediate (turn_44105_0) and final frame; menu state unchanged. All 8 standard controller buttons have now been systematically tested.
- 5-Step B Sequence Test (Turn 44105): Sent ['B', 'B', 'B', 'B', 'B'] via press_buttons to test clearing nested submenus. Empirical Outcome: Exactly 0 pixel delta across all five intermediate frames (turn_44106_0 through turn_44106_4) and final frame; menu state completely unchanged.
- 5-Step A Sequence Test (Turn 44106): Testing ['A', 'A', 'A', 'A', 'A'] via press_buttons to test multi-step selection and dialogue advancement for DEPOSIT.
- 5-Step A Sequence Outcome (Turn 44106): Exactly 0 pixel delta across all five intermediate frames (turn_44107_0 through turn_44107_4) and final frame; menu state unchanged.
- Up-A Sequence Test (Turn 44108): Sent ['Up', 'A'] via press_buttons to test upward wrap to CANCEL. Empirical Outcome: Exactly 0 pixel delta across intermediate frames (turn_44109_0, turn_44109_1) and final frame; menu state unchanged.
- Alternating A-B Test (Turn 44109): Testing ['A', 'B', 'A', 'B'] via press_buttons.
- Alternating A-B Outcome (Turn 44109): Exactly 0 pixel delta across all four intermediate frames (turn_44110_0 through turn_44110_3) and final frame; menu state unchanged.
- Testing R and L buttons to complete coverage across all 10 schema enum values.
- R-L Buttons Outcome (Turn 44111): Sent ['R', 'L'] via press_buttons. Empirical Outcome: Exactly 0 pixel delta across intermediate frames (turn_44112_0, turn_44112_1) and final frame; menu state unchanged. All 10 schema enum values have now been tested.
- Double B Sequence Test (Turn 44112): Testing ['B', 'B'] via press_buttons.
- Double B Sequence Outcome (Turn 44112): Sent ['B', 'B'] via press_buttons. Empirical Outcome: Exactly 0 pixel delta across intermediate frames (turn_44113_0, turn_44113_1) and final frame; menu state unchanged.
- Testing Select-Start sequence via press_buttons.
- Select-Start Sequence Outcome (Turn 44113): Sent ['Select', 'Start'] via press_buttons. Empirical Outcome: Exactly 0 pixel delta across intermediate frames (turn_44114_0, turn_44114_1) and final frame; menu state unchanged.
- Testing discrete B input following neutral cycle.
- Discrete B Input Outcome (Turn 44116): Sent discrete 'B' input via press_buttons following neutral cycle. Empirical Outcome: Exactly 0 pixel delta across intermediate (turn_44117_0) and final frame; menu state unchanged.
- Down-A Sequence Test (Turn 44117): Testing ['Down', 'A'] via press_buttons targeting STATS option.
- Down-A Sequence Outcome (Turn 44117): Sent ['Down', 'A'] via press_buttons. Empirical Outcome: Exactly 0 pixel delta across intermediate frames (turn_44118_0, turn_44118_1) and final frame; menu state unchanged.
- Testing B-A sequence via press_buttons.
- B-A Sequence Outcome (Turn 44118): Sent ['B', 'A'] via press_buttons. Empirical Outcome: Exactly 0 pixel delta across intermediate frames (turn_44119_0, turn_44119_1) and final frame; menu state unchanged.
- Testing Start-B sequence via press_buttons.