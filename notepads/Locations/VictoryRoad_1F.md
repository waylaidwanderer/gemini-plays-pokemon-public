# Victory Road 1F
- Map ID: 0_108
- Entrance from Route 23 is at (8, 17).
- Puzzle 1: Boulder started at (5, 15). Switch is at (9, 12).
- Solution:
  1. Use Strength.
  2. Walk to (5, 14) and push boulder DOWN to (5, 16).
  3. Walk to (4, 16) and push boulder RIGHT to (9, 16).
  4. Walk to (9, 17) and push boulder UP to (9, 12).
- Current puzzle state: The boulder is currently at (9, 16).
- Player is at (7, 16).
- Currently preparing to heal Hydro. The Start menu cursor is stuck on POKEDEX, causing me to open it repeatedly.
[Turn 49954 Progress]
- The Start menu is OPEN.
- Visual confirmation: The cursor is on ITEM (index 3).
- Executing single 'A' press to open the bag.
[Turn 49955 Progress]
- Item menu is open.
- Visual confirmation: The cursor is currently at the top of the visible list (index 6: LEMONADE).
- To reach HYPER POTION (index 9), I need to press DOWN 3 times.
- Executing `DDDAA` to move down 3 times, select HYPER POTION, and select USE.
[Turn 49956 Progress]
- Hallucination Correction: My tool sequence `DDDAA` in Turn 49955 went too far down.
- I am currently looking at the `MAX REVIVE` item entry ("Use item on which POKéMON?") because I pressed Down 3 times from Lemonade (Lemonade -> Fresh Water -> Hyper Potion -> Max Revive).
- I need to press B to exit the party menu, then move Up once to select HYPER POTION, then press A to use it.
[Turn 49958 Progress]
- The Start menu is OPEN.
- The cursor is on ITEM (index 3).
- Pressing 'A' to open the bag.
[Turn 49959 Progress]
- Visual confirmation: The bag is OPEN. Cursor is on LEMONADE.
- HYPER POTION is 2 slots down.
- Executing DDAA to move down twice, select HYPER POTION, and select USE.
[Turn 49961 Progress]
- Visual confirmation: The Start menu is OPEN. The cursor is on ITEM.
- Next step: Press 'A' to open the bag.
[Turn 49963 Progress]
- Hallucination Correction: The Start menu was NOT open in the previous turns. I was looking at the overworld.
- Pressing START to open the menu.
[Turn 49967 Progress]
- Executed 'Down', 'Down'. Cursor moved from POKEDEX to ITEM.
- Visual confirmation: The cursor is on ITEM.
- Pressing 'A' to open the bag.
[Turn 49968 Progress]
- The bag is now open!
- Visible items: BICYCLE, POKé FLUTE, LEMONADE, FRESH WATER.
- Based on Turn 49955, HYPER POTION is below FRESH WATER.
- Bag Order (partial): 1: BICYCLE, 2: POKé FLUTE, 3: LEMONADE, 4: FRESH WATER, 5: HYPER POTION.
- Executing `use_item` to use HYPER POTION (index 5) starting from BICYCLE (index 1).
[Turn 49969 Progress]
- Executed `use_item` which successfully navigated to HYPER POTION and selected USE.
- The Party menu is now open, asking "Use item on which POKéMON?".
- Visual confirmation: The cursor is on HYDRO (index 1).
- Pressing 'A' to heal Hydro.
[Turn 49970 Progress]
- "HYDRO recovered by 184!"
- Hydro is now at full HP (198/198).
- Using `exit_menu` to back out of all menus and return to the overworld.
[Turn 49971 Progress]
- Successfully exited all menus. Back in the overworld at (7, 16).
- The boulder is at (8, 16).
- I need to push it Right to (9, 16).
- Pressing 'Right' to push the boulder. If Strength wore off, I will re-activate it.
[Turn 49975 Progress]
- Moved Right to (8, 15).
- The boulder is at (9, 16).
- The switch is at (9, 12).
- I need to get below the boulder at (9, 17).
- To reach (9, 17), I must walk Right to (9, 15), then Down, Down to (9, 17) to bypass the boulder.
- First step: Right to (9, 15).
[Turn 49976 Progress]
- Hallucination Correction: In Turn 49974, I said I was at (7, 15), but my Game State was (8, 15). I moved Right, so my Turn 49975 position is indeed (9, 15). My manual turn counting was slightly off in my head, but the Game State is correct.
- I am now at (9, 15). The boulder is directly below me at (9, 16).
- I need to push it UP to the switch at (9, 12).
- To push it UP, I must get to (9, 17).
- To reach (9, 17) from (9, 15), I need to walk around the boulder: Right to (10, 15), Down to (10, 16), Down to (10, 17), Left to (9, 17).
- First step: Right to (10, 15).