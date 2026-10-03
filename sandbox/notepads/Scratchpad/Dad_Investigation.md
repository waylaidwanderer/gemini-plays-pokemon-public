# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Conductor in blue uniform observed seated on platform side.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Jackson & Narrative Status Audit
- **Narrative Truth**: Jackson ran outside the Sovio Metro Station into Sovio City to investigate the seismic tremor.
- **Route 1 & Lancio Town Falsification**: Route 1 and Lancio Town are baseline starting areas with zero link to Jackson's disappearance.
- **Sovio Metro Lobby Audits**: Timetable board is decorative flavor text. Turnstile passage at (19, 21) triggers "I should find dad first!".

## Concrete Falsifiable Hypotheses for Progression
### Hypothesis H60: Night Cycle NPC & Event Changes in Sovio City
- **Premise**: In-game time has transitioned into nighttime (past 20:00). NPC locations, dialogue trees, or accessible areas in Sovio City may update at night.
- **Test Protocol**:
  1. Exit Metro Station to Sovio City surface.
  2. Inspect Central Plaza, Central Park, and West Avenue NPCs at night.
  3. Falsified if all NPC positions and dialogues remain completely identical to daytime baseline.

### Hypothesis H61: Inventory / Key Item Environmental Triggers
- **Premise**: An item in possession (HuPhone, TM Case, or held item) triggers story progression when inspected or activated at a specific location.
- **Test Protocol**:
  1. Audit Key Items and Bag functions.
  2. Test SELECT registration and item usage in Metro lobby and Central Plaza.
  3. Falsified if no unique interactions or prompts occur.

- **Night Test (Turn 19176)**: Route 2 barrier at (52, 19) displays identical baseline text ('I can't go yet... I have things to do!'). Barrier remains active at night.
- **Night Test (Turn 19182)**: Central Park blonde girl displays identical baseline text ('I'm supposed to meet someone here, but he doesn't seem to show up... Was I catfished?'). Night cycle does not alter dialogue.
- **Night Test (Turn 19188)**: Central Park boy in pink shirt displays identical baseline text ('I'm supposed to meet a girl here...'). Hypothesis H60 is completely FALSIFIED: night cycle is purely cosmetic and does not alter NPC scripts or progression flags.
