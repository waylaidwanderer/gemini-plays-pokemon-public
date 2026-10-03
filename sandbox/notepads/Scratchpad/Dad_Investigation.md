# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Scanner pillars (18, 21) and (20, 21) verified 100% inert; platform chairs verified empty per Turn 20098; north wall across columns 21-23 is solid brick with timetable board mounted.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Concluded Hypotheses
- H60-H91 (Comprehensive Baseline Sweeps - Turns 7232-20412): FALSIFIED. Sewers cleared and vacated post-Marie retreat (storage room 37, 14 static trigger; grunt platforms empty bare stone; rugged rocks equipment-gated). Surface residences verified static Easter eggs (Wii house 39, 7 Sonic game; Gumball house 29, 14 TV humor and 2F bed comedy dialogue 'Wait why am I all alone in a sleeping girl's room?!'; Karate house 14, 15 flavor; Terrace house 49, 14 cooking flavor; Name Rater 31, 26 service). Covered roof corridor (cols 47-51, row 22) verified dead-end connecting to Route 2 barrier. System state (Bag 4 items, HuPhone, TM Case; Party Sirius Lv16, Zephyr Lv2; Trainer Card; Quest Log 0 active) verified clean with zero pending items/quests.

## Active Hypotheses for Progression
### Hypothesis H92: Audit of Outdoor Sectors and Regional Progression Triggers
- **Premise**: With civilian residences and vacated sewers verified static, progression requires an unexamined outdoor event trigger, NPC dialogue update, or regional connection.
- **Findings (Turn 20422-20431)**:
  - Variable 1 Evaluated: Central Park south sidewalk entities (Boy at 35, 28, Jigglypuff at 34, 28, Little Girl at 33, 28) audited in-game. Verified 100% ambient flavor text ('Yeah Jigglypuff!', 'Jigglypuff: Puff Puff!', Moon Stone dialogue) with zero story triggers.
  - Variable 2 Evaluated: Southern Avenue (rows 28-40) audited in-game. Verified open grassy lane with zero NPCs or items, transitioning directly into Route 1 at (53, 0).
  - Variable 3 Falsified: Aborting ungrounded 100-turn trek to Lancio Town per critique. No causal game state variable (item, flag, milestone) has changed since Turn 243 to alter Professor Ivo's documented ambient dialogue ('Hey, Ashi, how's your new Pokémon?').
- **Conclusion**: H92 concluded. Outdoor residential fringes and southern transit corridors hold zero active triggers.

### Hypothesis H93: Resolution of Sovio Central Plaza & Metro Turnstile Preconditions
- **Premise**: Progression is gated specifically by "I should find dad first!" at the Metro turnstile and "I can't go yet... I have things to do!" at Route 2. The trigger must be grounded in the immediate vicinity of the central story sites: Central Plaza (confrontation site outside Pokémon Center) or the Metro Station lobby fixtures.
- **Isolated Variables**:
  1. Inspect the exact ground tiles in Central Plaza outside the Pokémon Center (rows 12-15, cols 42-46) where the Siara confrontation took place.
  2. Audit Camper and interactions inside the Pokémon Center.
  3. Inspect Metro Station lobby fixtures and examine exact turnstile condition.
- **Falsifiable Success Criteria**: Uncovering a physical trigger/item in Central Plaza, updating an interaction, or clearing the turnstile blocker.
