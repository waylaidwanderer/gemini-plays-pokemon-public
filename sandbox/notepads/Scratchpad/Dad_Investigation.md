# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Platform chairs verified 100% empty (turns 19364-19368); scanner pillars (18, 21) and (20, 21) verified 100% inert with zero interaction.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Concluded Hypotheses
- H60-H65 (Sewers, Lobby, Sovio City Exterior Corridors & NPCs - Turns 19100-19470): FALSIFIED. Sewers cleared, (37, 14) storage room static, exterior paths, barriers (52, 19), and civilians verified baseline.
- H66-H74 (Regional Anchors, Residences, Systems, Terrace, Corridor, PC & Sewers - Turns 19470-19838): FALSIFIED. Route 1/Lancio Town, all 5 residences, lobby fixtures, terrace/corridor walls, PC Box 1, and subterranean sewers re-verified static baseline with zero new items or triggers.
- H75-H82 (Quest Log, Level Milestone, Metro Lobby, Overworld Perimeters, Mailbox, Facades, Healing, Portal Fixtures - Turns 19871-20028): FALSIFIED. Audited HuPhone apps, level 16 scope, lobby timetable/chairs, all Sovio exterior perimeters, Southwest facade, Nurse Joy party heal, and portal threshold; confirmed static civilian baseline and persistent gate flags.

## Concluded Hypotheses Continued
- H84 (Surface Gate & Re-Sweep of Civilians / Bag / Lobby - Turns 20042-20130): FALSIFIED. Bag audited standard (no pending key items or letters), Metro lobby verified 100% empty with turnstile firmly gated by "I should find dad first!", Route 2 firmly gated by "I can't go yet... I have things to do!", and re-interrogating Central Park online dating couple (44, 24 and 31, 21), Boy Rocky (23, 17), and Karate House residents (14, 15) confirmed 100% static baseline with zero new items or triggers.

## Active Hypotheses for Progression
### Hypothesis H85: Early-Game Quest Givers & Equipment Acquisition (Medic! & Egg Research) (Started: Turn 20133)
- **Premise**: Main story progression remains gated by 'I should find dad first!' and 'I can't go yet... I have things to do!', while sewer progression is gated by rugged rocks requiring specialized equipment. Quest Log Page 1 lists 'Medic!' and 'Egg Research' as early-game uncompleted quests. In ROM hacks, sidequest rewards are standard sources of field equipment.
- **Isolated Variable**: Testing specific unstarted quest givers (Camper with poisoned Weedle at Sovio Pokémon Center (5, 7) for 'Medic!', and Professor Ivo for 'Egg Research').
- **Protocol**:
  1. Exit Karate House to West Avenue. [COMPLETED: Turn 20137]
  2. Travel east along West Avenue and northern boulevard to Sovio City Pokémon Center (44, 12).
  3. Speak to Straw-hat Camper at (5, 7) with Antidote in Bag to test if 'Medic!' sidequest initiates. [COMPLETED: Turn 20144-20145. FALSIFIED: Camper dialogue remains strictly identical ambient text ('My weedle got poisoned so I will need the Pokémon Center\'s service! Ironic isn\'t it?'), with zero quest prompt or item reaction. H85a falsified.]
  4. If Camper remains ambient flavor, travel through Route 1 to Lancio Town Lab to test Professor Ivo for 'Egg Research'.
- **Falsification Criteria**: If the Camper's dialogue remains strictly identical and no quest prompt is offered, H85a (Camper = Medic!) is falsified.
