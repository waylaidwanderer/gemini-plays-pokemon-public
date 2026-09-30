# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Current Blockers & Ground Truths
- Metro Station turnstile at (19, 21): Triggers "I should find dad first!" and repels player 1 step South.
- Route 2 exit at (52, 19-21): Triggers "I can't go yet... I have things to do!" and repels player 1 step West.
- Jackson last seen departing the Metro Station lobby into Sovio City following the seismic tremor (Turn 1437).
- Team Siara grunts permanently retreated from Sovio Sewers after Marie's broadcast (Turn 2682). All accessible sewer sectors confirmed fully cleared and inert.

## Active Hypotheses & Falsification Protocols

### Hypothesis 1: Side Quest State Dependency
- **Proposition**: Having the side quest "Lost Toy" actively open may be gating or interfering with other event flags or NPC interactions in Sovio City.
- **Test Protocol**:
  1. Navigate to the elevated terrace at (51, 15).
  2. Speak to the Old Man and select "Yes" to cancel the active "Lost Toy" quest.
  3. Re-test Metro turnstile at (19, 21) and Route 2 barrier at (52, 19).
- **Falsification Criteria**: If turnstile continues to output "I should find dad first!" after quest cancellation, side quest state is definitively ruled out as the blocker.

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
