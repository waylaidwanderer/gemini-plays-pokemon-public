# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Current Blockers & Ground Truths
- Metro Station turnstile at (19, 21): Triggers "I should find dad first!" and repels player 1 step South.
- Route 2 exit at (52, 19-21): Triggers "I can't go yet... I have things to do!" and repels player 1 step West.
- Jackson last seen departing the Metro Station lobby into Sovio City following the seismic tremor (Turn 1437).
- Team Siara grunts permanently retreated from Sovio Sewers after Marie's broadcast (Turn 2682). All accessible sewer sectors confirmed fully cleared and inert.

## Active Hypotheses & Falsification Protocols

### Hypothesis 1: Side Quest State Dependency (CONVINCINGLY FALSIFIED)
- **Proposition**: Having the side quest "Lost Toy" actively open may be gating or interfering with other event flags or NPC interactions in Sovio City.
- **Test Protocol**:
  1. Navigate to the elevated terrace at (51, 15).
  2. Speak to the Old Man and select "Yes" to cancel the active "Lost Toy" quest (Completed Turn 9358).
  3. Re-test Metro turnstile at (19, 21) and Route 2 barrier at (52, 19) (Completed Turn 9376).
- **Empirical Result (Turn 9376-Present)**:
  - Metro turnstile at (19, 21): Tested post-cancellation on Turn 9376; continues to trigger "I should find dad first!" and repels player.
  - Route 2 barrier at (52, 19): Tested post-cancellation on Turn 9409-9410; triggers "I can't go yet... I have things to do!" and repels player 1 step West.
- **Conclusion**: Side quest state has zero bearing on regional roadblock scripts. Hypothesis 1 is 100% conclusively falsified and closed.

### Hypothesis 2: Exhaustive Surface NPC Persistence & Trigger Audit
- **Proposition**: An NPC in Sovio City possesses a secondary dialogue branch or progression trigger activated only upon repeated or sequential interaction (similar to the Protect TM boy in Lancio Town).
- **Test Protocol**:
  1. Systematically interact with every surface NPC in Sovio City (Bikers, boy with Rocky, Gumball family, Karate couple, park visitors, terrace residents).
  2. Test persistent dialogue (3+ presses of 'A') to check for multi-textbox shifts.
- **Falsification Criteria**: If all NPCs cycle to identical baseline dialogue strings with no flag updates, NPC interaction is ruled out.

### Hypothesis 3: Unchecked Environmental or Structural Features in Sovio City
- **Proposition**: An unmapped entrance, back door, or interactive object in Sovio City holds the clue or passage to Jackson.
- **Test Protocol**:
  1. Inspect the alleyways around Central Plaza and West Avenue.
  2. Test interaction on all unique objects (vending machines, decorative fixtures, notices).
- **Falsification Criteria**: If all fixtures confirm solid inert collision without script execution, structural triggers are ruled out.

### Hypothesis 4: Macro-Traversal & Level 15 Evolution (CONVINCINGLY FALSIFIED)
- **Proposition**: Traveling to Route 1 / Lancio Town to train Sirius to Lv15 will trigger an evolution or story progression event with Professor Ivo.
- **Empirical Findings & Falsification**:
  1. Mechanics Check: Riolu's evolution is friendship/happiness-based (with daytime requirement), not tied to Level 15. Level 15 assumption was completely unfounded.
  2. Map Check: Route 1 and Lancio Town have been visited repeatedly across thousands of turns; Professor Ivo and all town NPCs exhibit static ambient dialogue with zero progression triggers.
  3. Roadblock Locality: Both roadblocks ('I should find dad first!' and 'I can't go yet... I have things to do!') are local to Sovio City and explicitly demand finding Dad.
- **Conclusion**: Macro-traversal is completely ruled out. Riolu's evolution is friendship-based, and Lancio Town / Route 1 NPCs exhibit static ambient dialogue.

### Hypothesis 2: Exhaustive Surface NPC Persistence & Trigger Audit
- **Proposition**: An NPC in Sovio City possesses a secondary dialogue branch or progression trigger activated only upon repeated or sequential interaction (similar to the Protect TM boy in Lancio Town).
- **Test Protocol**:
  1. Systematically interact with every surface NPC in Sovio City (Bikers, boy with Rocky, Gumball family, Karate couple, park visitors, terrace residents).
  2. Test persistent dialogue (3+ presses of 'A') to check for multi-textbox shifts.
- **Falsification Criteria**: If all NPCs cycle to identical baseline dialogue strings with no flag updates, NPC interaction is ruled out.
- **Empirical Results (Turns 9462-9478)**:
  - Three Bikers (13, 21-23): Tested multi-textbox persistence on Biker 1 and Biker 2. Both cycle the exact same 2-line gang dialogue ("Jealous kid? / ultimate motorcycle gang!") followed by Asher's thought bubble; confirmed 100% ambient comedic NPCs with zero secondary branches.
  - Karate Couple (House 14, 15): Tested multi-textbox persistence on Karate trainer (3, 34) and girlfriend (3, 33). Both cycle the exact same 2-line martial arts debate ("debate over which fighting stlye is better / kickbox vs karate") and loop back to baseline; confirmed 100% ambient flavor text with zero secondary branches, battle challenges, or items.