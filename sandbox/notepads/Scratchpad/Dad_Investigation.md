# Scratchpad: Investigating Jackson's Whereabouts

## Verified Ground Truths
- Tremor occurred in Sovio Metro Station (Turn 1437); Jackson ran outside into Sovio City to investigate.
- Turnstile gate at (19, 21) in Metro lobby triggers: "I should find dad first!" and forces Asher 1 step Down to (19, 22) (empirically re-verified Turns 7150-7153, 9018).
- Route 2 exit at (52, 19-20) in Sovio City triggers: "I can't go yet... I have things to do!"
- "Machop's Toy" is an optional side quest given by Old Man (51, 15); cancelling it on Turn 3162 did NOT alter the turnstile or Route 2 barrier. It has no verified link to the main storyline.
- Neither the Karate trainer nor the Old Man mentions Rock Smash or any HM.
- Macro-Traversal across Route 1 to Lancio Town is conclusively rejected: exhaustively checked multiple times (Turns 3167-3543, 4064-4337, 5152, 6892-7211, 7489-7635), all NPCs retain identical ambient dialogue. The roadblocks are local to Sovio City.

## Active Analysis & Investigation Findings (Reconciled Turn 7982)
- Sub-Containers & Bag Audited (Turns 7994, 8559-8562, 8591, 8827-8831): PC Item Storage and Mailbox verified empty. TM Case contains TM17 (Protect) and TM48 (Work Up); zero HMs. Bag Items pocket contains: Potion x 1, Poison Barb x 1, Nugget x 1 (zero Repels). Poké Balls pocket: Timer Ball x 1. Key Items pocket contains ONLY HuPhone and TM Case. HuPhone audited: Item Storage (PC Item Storage & Mailbox), World Map, Quest Log; zero communication/call features. Someone's PC (Box 1) audited Turn 8869: completely empty (0 deposited Pokémon); party audited Turn 8927: Slot 1 Sirius (Riolu Lv14, HP 40/40), Slot 2 Zephyr (Pidgey Lv2, HP 13/13).

## Active Investigation Leads & Hypotheses
1. **Hypothesis: Overlooked Outdoor Sector in Sovio City**:
   - Mechanic/Entity: Jackson, Valora, or a story trigger located in an unexplored or re-triggered outdoor overworld tile in Sovio City (e.g. northern perimeter behind buildings, rows 0-6, alleyways).
   - Test Method: Systematically search Sovio City outdoor sectors beyond the central plaza and west avenue.
   - Falsification: If all outdoor sectors terminate in solid perimeter walls without NPCs or triggers, move to internal structure audit.

2. **Hypothesis: Unresolved Sewer Event / Alternative Storage Room**:
   - Mechanic/Entity: An uninspected sector or interactive feature in Sovio Sewers that directly resolves Dad's kidnapping cutscene.
   - Test Method: Audit sewer corridors for any branch or tile interaction missed during previous sweeps.
   - Falsification: If all reachable tiles have been probed with 'A' and remain inert, focus entirely on Sovio City surface.
