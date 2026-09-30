# Scratchpad: Investigating Jackson's Whereabouts

## Verified Ground Truths
- Tremor occurred in Sovio Metro Station (Turn 1437); Jackson ran outside into Sovio City to investigate.
- Turnstile gate at (19, 21) in Metro lobby triggers: "I should find dad first!" and forces Asher 1 step Down to (19, 22) (empirically re-verified Turns 7150-7153, 9018).
- Route 2 exit at (52, 19-20) in Sovio City triggers: "I can't go yet... I have things to do!"
- "Machop's Toy" is an isolated side quest; per Engine.md, side quests are tracked separately from main progression flags and do not gate regional story barriers.
- Neither the Karate trainer nor the Old Man mentions Rock Smash or any HM.
- Macro-Traversal across Route 1 to Lancio Town is conclusively rejected: exhaustively checked multiple times (Turns 3167-3543, 4064-4337, 5152, 6892-7211, 7489-7635), all NPCs retain identical ambient dialogue. The roadblocks are local to Sovio City.
- Sewers Conclusively Verified Inert: All accessible sectors of Sovio Sewers (storage room, catwalks, dark sector, canal) have been repeatedly audited and confirmed inert. Grunts permanently retreated on Turn 2682; storage room displays generic inspection text.
- Northern Alcove Conclusively Enclosed (Turns 9097-9101): Alleyway along column 40 up to (40, 9) terminates in solid foundation walls between tan building, Pokémon Center, and house (39, 7). Zero exterior side passages exist.

## Active Analysis & Investigation Findings (Reconciled Turn 7982)
- Sub-Containers & Bag Audited (Turns 7994, 8559-8562, 8591, 8827-8831): PC Item Storage and Mailbox verified empty. TM Case contains TM17 (Protect) and TM48 (Work Up); zero HMs. Bag Items pocket contains: Potion x 1, Poison Barb x 1, Nugget x 1 (zero Repels). Poké Balls pocket: Timer Ball x 1. Key Items pocket contains ONLY HuPhone and TM Case. HuPhone audited: Item Storage (PC Item Storage & Mailbox), World Map, Quest Log; zero communication/call features. Someone's PC (Box 1) audited Turn 8869: completely empty (0 deposited Pokémon); party audited Turn 8927: Slot 1 Sirius (Riolu Lv14, HP 40/40), Slot 2 Zephyr (Pidgey Lv2, HP 13/13).

## Active Investigation Strategy & Focus
1. **Sewer Status Resolution**:
   - The sewers have been audited across multiple cycles with zero changes since Team Siara's retreat on Turn 2682.
   - Returning to the sewers without any new surface trigger or key item is an ungrounded circular traversal loop.
2. **Current Surface Focus**:
   - The roadblock is the turnstile ("I should find dad first!") and Route 2 ("I can't go yet... I have things to do!").
   - Ascend immediately to Sovio City surface to search for unexamined surface interactions, mechanics, or triggers outside the sewers.
