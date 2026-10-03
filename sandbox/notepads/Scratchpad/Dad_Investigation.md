# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train to Amor City.
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.

## Concluded Hypotheses Summary (Pruned)
- **H118-H120 City, Terminal & Road Fixtures**: Fully audited outdoor sectors, inert manholes/shutters, PC Box 1 empty, platform verified empty of NPCs, Camper Weedle ambient.
- **H121-H122 Sewers & City Post-Sewer Resurvey**: Col 27 vertical corridor mapped; all Sovio residences (Nana, Wii, Gumball, Karate) and outdoor civilians confirmed ambient.
- **H123 Outdoor Tremor & Physical Audit**: Central Plaza, park, southwest lawn, rear biker lane, and sewers storage door (37, 14) ("Its a simple storage room..") verified static.
- **H124 Non-Spatial Audit**: Verified Bag items/Key Items (HuPhone, TM Case, Potion, Antidote, Nugget), Sirius Lv16 Info, Mailbox/PC empty.
- **H125 Metro Lobby & Turnstile**: Floor mat (23, 24-25) and scanner pillars (18, 21)/(20, 21) confirmed inert scenery. Turnstile (19, 21) re-confirms blocker ('I should find dad first!').

## Concluded Hypothesis H126: Sovio City Quest Trigger Investigation
- **Results**: Verified Straw-hat Camper (5, 7) in Center repeats ambient Weedle dialogue under 0 active quests (does not trigger 'Medic!'). Verified Bikers (13, 21-23) on West Avenue repeat ambient motorcycle flavor text under 0 active quests (does not trigger 'Squirtle Gang'). Page 1 side quests are not triggered by these NPCs.

## Active Hypothesis H127: Mechanical Pre-Condition & Party State Investigation
- **Premise**: Spatial search exhausted. Testing unexamined mechanical game state variables: party lead reordering, trainer card metrics, TM compatibility, and team size.
- **Milestones**:
  1. Dismiss Biker textbox and open Start Menu -> COMPLETE (Turn 22506).
  2. Inspect Trainer Card (ASHER) for money, rounds, and trainer stats -> IN PROGRESS.
  3. Test party lead reordering (switch Zephyr Pidgey to Slot 1) and test TM17 Protect compatibility.
  4. Test if party configuration resolves Metro Turnstile blocker.