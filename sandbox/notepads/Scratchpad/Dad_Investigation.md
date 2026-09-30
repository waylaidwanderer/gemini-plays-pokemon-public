# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Current Blockers & Ground Truths
- Metro Station turnstile at (19, 21): Triggers "I should find dad first!" and repels player 1 step South.
- Route 2 exit at (52, 19-21): Triggers "I can't go yet... I have things to do!" and repels player 1 step West.
- Jackson last seen departing the Metro Station lobby into Sovio City following the seismic tremor (Turn 1437).
- Team Siara grunts permanently retreated from Sovio Sewers after Marie's broadcast (Turn 2682). All accessible sewer sectors confirmed fully cleared and inert.

## Hypotheses & Falsification Protocols

### Hypothesis 1: Side Quest State Dependency (CONVINCINGLY FALSIFIED)
- **Proposition**: Having the side quest "Lost Toy" actively open may be gating or interfering with other event flags or NPC interactions in Sovio City.
- **Empirical Findings**:
  - Cancelled "Lost Toy" quest on Turn 9358 by speaking to Old Man at (51, 15).
  - Re-tested Metro turnstile at (19, 21) (Turn 9376) and Route 2 barrier at (52, 19) (Turn 9409-9410); both continue to trigger roadblocks identically.
- **Conclusion**: Side quest state has zero bearing on regional roadblock scripts. 100% conclusively falsified and closed.

### Hypothesis 2: Surface NPC Persistence & Secondary Dialogue (CONVINCINGLY FALSIFIED)
- **Proposition**: An NPC in Sovio City possesses a secondary dialogue branch, item gift, or progression trigger activated only upon repeated or sequential interaction (similar to the Protect TM boy in Lancio Town).
- **Empirical Findings (Turns 9462-9538)**:
  - All surface residential civilian NPCs and structures across Sovio City (Three Bikers, Karate couple, Boy with Rocky, Gumball family 1F/2F, North Central house 1F/2F, and Terrace house Granddaughter/Nana) were systematically tested with persistent multi-textbox interactions and confirmed to cycle static ambient flavor text with zero secondary branches, item gifts, or progression flags.
- **Conclusion**: 100% conclusively falsified. No surface civilian NPC holds progression triggers.

### Hypothesis 3: Unchecked Environmental or Structural Features in Sovio City
- **Proposition**: An unmapped entrance, back door, or interactive object in Sovio City holds the clue or passage to Jackson.
- **Test Protocol**:
  1. Inspect the Metro Station lobby, turnstiles, and platform fixtures.
  2. Inspect Central Plaza, park boundaries, and unique fixtures.
- **Falsification Criteria**: If all fixtures confirm solid inert collision without script execution, structural triggers are ruled out.

### Hypothesis 4: Macro-Traversal & Level 15 Evolution (CONVINCINGLY FALSIFIED)
- **Proposition**: Traveling to Route 1 / Lancio Town to train Sirius to Lv15 will trigger an evolution or story progression event with Professor Ivo.
- **Empirical Findings**:
  1. Mechanics Check: Riolu's evolution is friendship/happiness-based, not tied to Level 15.
  2. Map Check: Route 1 and Lancio Town have been visited repeatedly across thousands of turns; Professor Ivo and all town NPCs exhibit static ambient dialogue with zero progression triggers.
  3. Roadblock Locality: Both roadblocks ('I should find dad first!' and 'I can't go yet... I have things to do!') are local to Sovio City and explicitly demand finding Dad.
- **Conclusion**: 100% conclusively falsified. Macro-traversal is completely ruled out.
