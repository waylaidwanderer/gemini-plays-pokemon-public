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

## Active Hypotheses for Progression
### Hypothesis H84: Surface Gate & Progression Prerequisite Evaluation (Started: Turn 20042)
- **Premise**: All subterranean sewer areas are confirmed static baseline with zero progression flags. Progression is strictly gated at the surface: Metro Turnstile (19, 21) requiring finding Dad, and Route 2 (52, 19-22) requiring completing pending tasks ("I can't go yet... I have things to do!"). We exit the sewers and systematically investigate why the surface progression remains gated, testing untried surface mechanics, dialogue trees, and inventory interactions.
- **Protocol & Progress**:
  1. Flee wild battle, return up the stairs to Metro Station lobby (23, 24), and exit to Central Plaza (48, 18). [COMPLETED: Turn 20056]
  2. Test Route 2 barrier (52, 19) post-heal and post-Lv16. [COMPLETED: Turn 20057-20058. Falsified; displays 'I can't go yet... I have things to do!']
  3. Systematically evaluate unexamined surface triggers and potential prerequisite conditions.
- **Falsifiable Success Criteria**: Identifying the prerequisite condition that clears either gate.

## Bag Audit Results (Turn 20085)
- **Items Pocket**: Potion x1, Poison Barb x1, Antidote x1, Nugget x1.
- All pockets confirmed standard baseline. No key items, mail, or special items pending.
- Proceeding to Protocol 4: Comprehensive audit of Metro Station lobby boundaries and unexamined surface triggers.
## Metro Station Lobby Audit Results (Turn 20099)
- Turnstile (19, 21) confirmed firmly blocked by scripted prompt: "I should find dad first!", pushing Asher to (19, 22).
- Lobby and visible platform 100% verified empty.
- Proceeding to Protocol 5: Systematic investigation of Central Plaza and surface triggers.