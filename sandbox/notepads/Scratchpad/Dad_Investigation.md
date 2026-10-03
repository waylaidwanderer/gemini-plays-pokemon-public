# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Scanner pillars (18, 21) and (20, 21) verified 100% inert; platform chairs verified empty per Turn 20098; north wall across columns 21-23 is solid brick with timetable board mounted.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Concluded Hypotheses
- H60-H91 (Comprehensive Baseline Sweeps - Turns 7232-20412): FALSIFIED. Sewers cleared and vacated post-Marie retreat (storage room 37, 14 static trigger; grunt platforms empty bare stone; rugged rocks equipment-gated). Surface residences verified static Easter eggs (Wii house 39, 7 Sonic game; Gumball house 29, 14 TV humor and 2F bed comedy dialogue 'Wait why am I all alone in a sleeping girl's room?!'; Karate house 14, 15 flavor; Terrace house 49, 14 cooking flavor; Name Rater 31, 26 service). Covered roof corridor (cols 47-51, row 22) verified dead-end connecting to Route 2 barrier. System state (Bag 4 items, HuPhone, TM Case; Party Sirius Lv16, Zephyr Lv2; Trainer Card; Quest Log 0 active) verified clean with zero pending items/quests.
- H92 (Outdoor Fringes & Regional Connections - Turns 20415-20431): FALSIFIED. Central Park south sidewalk entities (Boy at 35, 28, Jigglypuff at 34, 28, Little Girl at 33, 28) verified ambient flavor text. Southern Avenue (rows 28-40) verified open transit corridor to Route 1 with zero leads. Lancio Town trek aborted per Burden of Proof (no game state variables changed since Turn 243).

## Active Hypotheses for Progression
- H93 (Sovio Central Story Sites & Metro Gate Preconditions - Turns 20443-20488): FALSIFIED.
  - Variable 1 (Central Plaza tiles): Full sweep of columns 41-46 across rows 13-15 confirmed 100% devoid of hidden items, triggers, or interactions.
  - Variable 2 (Clock/Timetable correlation): In-game Start Menu clock is real-time ticking (RTC), unlinked to the static 16:00 timetable text. Timetable is ambient world-building.
  - Variable 3 (Metro Station lobby audit): Audited blue chairs, scanner pillars, and timetable board. Turnstile at (19, 21) reliably triggers "I should find dad first!" and pushes Asher down to (19, 22).
  - Conclusion: No hidden local triggers or clock mechanisms exist in Central Plaza or the Metro Station lobby.
