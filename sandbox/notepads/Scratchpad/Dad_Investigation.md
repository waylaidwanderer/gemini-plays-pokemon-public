# Scratchpad: Investigating Jackson's Whereabouts

## Verified Ground Truths
- Tremor occurred in Sovio Metro Station (Turn 1437); Jackson ran outside into Sovio City to investigate.
- Turnstile gate at (19, 21) in Metro lobby triggers: "I should find dad first!"
- Route 2 exit at (52, 19-20) in Sovio City triggers: "I can't go yet... I have things to do!"
- "Machop's Toy" is an optional side quest given by Old Man (51, 15); cancelling it on Turn 3162 did NOT alter the turnstile or Route 2 barrier. It has no verified link to the main storyline.
- Neither the Karate trainer nor the Old Man mentions Rock Smash or any HM.

## Active Analysis & Investigation Findings (Reconciled Turn 7982)
- Sub-Containers & Bag Audited (Turns 7994, 8559-8562, 8591, 8827-8831): PC Item Storage and Mailbox verified empty. TM Case contains TM17 (Protect) and TM48 (Work Up); zero HMs. Bag Items pocket contains: Potion x 1, Poison Barb x 1, Nugget x 1 (zero Repels). Poké Balls pocket: Timer Ball x 1. Key Items pocket contains ONLY HuPhone and TM Case. HuPhone audited: Item Storage (PC Item Storage & Mailbox), World Map, Quest Log; zero communication/call features. Someone's PC (Box 1) audited Turn 8869: completely empty (0 deposited Pokémon); party audited Turn 8927: Slot 1 Sirius (Riolu Lv14, HP 40/40), Slot 2 Zephyr (Pidgey Lv2, HP 13/13).

## Explicit Falsifiable Story Hypotheses
1. **Hypothesis: Metro Attendant / Platform Trigger** [FALSIFIED - Turn 9018]:
   - Empirical Result: Interacting with turnstile gate (19, 21) facing North with 'A' returns no prompt. Stepping onto (19, 21) triggers verbatim 'I should find dad first!' and forces Asher 1 step Down to (19, 22). Attendant at (22, 19) remains unreachable on platform side. Gated strictly behind story event flag of finding Jackson.

2. **Hypothesis: Overlooked Sewer Trigger / Valora Presence**:
   - Mechanic/Entity: Valora or a secondary sewer trigger that updates the quest state post-grunt retreat.
   - Test Method: Systematically re-verify whether any NPC (e.g. Valora) or interactive tile exists in the sewers that was missed, specifically inspecting the storage room entrance at (36, 14) and (37, 14) and the ladder sectors.
   - Falsification: If all accessible sewer tiles contain zero NPCs and the storage room continues to display "Its a simple storage room...", this location is fully inert.

3. **Hypothesis: External Route / Professor Ivo Callback**:
   - Mechanic/Entity: Professor Ivo in Lancio Town or an external trigger on Route 1.
   - Test Method: Check if Professor Ivo has updated dialogue now that Riolu is officially named Sirius, or if an NPC on Route 1 / Lancio reacts to the post-tremor state.
   - Falsification: If Professor Ivo continues to give default ambient dialogue ("Hey, Ashi, how's your new Pokmon?"), this lead is falsified.
