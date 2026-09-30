# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Current Blockers & Ground Truths
- Metro Station turnstile at (19, 21): Triggers "I should find dad first!" and repels player 1 step South.
- Route 2 exit at (52, 19-21): Triggers "I can't go yet... I have things to do!" and repels player 1 step West.
- Jackson last seen departing the Metro Station lobby into Sovio City following the seismic tremor (Turn 1437).
- Team Siara grunts permanently retreated from Sovio Sewers after Marie's broadcast (Turn 2682).
- Eastern Storage Room at (36-37, 14): Audited inert Turn 8637 ("Its a simple storage room...").
- Dark Sector / Basement: Explored; contains rugged Rock Smash rock at (22, 10) and Nugget at (23, 4). All accessible sewer sectors confirmed cleared and inert.

## Falsified Hypotheses
- **Hypothesis 1 (Side Quest State Dependency)**: Falsified Turn 9376. Cancelling "Lost Toy" did not affect Metro or Route 2 roadblocks.
- **Hypothesis 2 (Surface NPC Persistence Audit)**: Falsified Turns 9462-9537. All surface civilian NPCs and residential structures in Sovio City strictly cycle ambient flavor dialogue with zero secondary branches or progression triggers.
- **Hypothesis 3 (Environmental & Structural Features in Sovio Metro & City)**: Falsified Turns 9637-9788. All accessible structural fixtures (park barrels, alley walls, boundary alcoves, timetable display, scanner pillars, decorative manholes) empirically tested with zero interaction triggers.
- **Hypothesis 4 (Macro-Traversal & Level 15 Evolution)**: Falsified. Riolu evolves via friendship, not level 15. Lancio Town and Route 1 NPCs exhibit static ambient dialogue.

## Active Priority: Hypothesis 5 (Inventory & Key Item Triggers / Bag Items / HuPhone Inspection)
- **Proposition**: A specific item interaction, inspection, or trigger in the Bag / Key Items / HuPhone is required to advance the story state, or a key item was obtained/needs to be used.
- **Protocol & Empirical Log**:
  1. HuPhone Apps:
     - Item Storage: Audited Turn 9856; confirmed empty ("There are no items.").
     - Mailbox: Audited Turn 9860; confirmed empty ("There's no Mail here.").
     - World Map: Inspected Turns 9866-9871. Displays regional geography, Route 2, and Amor City.
     - Quest Log: Pending inspection (Next step).
  2. Inspect all inventory items in Bag (Key Items, Items, TMs/HMs) to see if any have a 'USE' or interaction prompt.
  3. Falsification Criteria: If all items and apps produce standard UI responses without triggering any event flags, Hypothesis 5 is falsified.
