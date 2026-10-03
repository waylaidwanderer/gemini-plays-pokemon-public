# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Platform chairs verified 100% empty (turns 19364-19368); scanner pillars (18, 21) and (20, 21) verified 100% inert with zero interaction.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Concluded Hypotheses
- H60-H65 (Sewers, Lobby, Sovio City Exterior Corridors & NPCs - Turns 19100-19470): FALSIFIED. Sewers cleared, (37, 14) storage room static, exterior paths, barriers (52, 19), and civilians verified baseline.
- H66-H74 (Regional Anchors, Residences, Systems, Terrace, Corridor, PC & Sewers - Turns 19470-19838): FALSIFIED. Route 1/Lancio Town, all 5 residences, lobby fixtures, terrace/corridor walls, PC Box 1, and subterranean sewers re-verified static baseline with zero new items or triggers.
- H75 (HuPhone Quest Log Audit - Turns 19871-19884): FALSIFIED. Empirically tested uncompleted quest entries in Quest List (e.g. Egg Research); confirmed they verbatim display 'This Quest hasn't been completed yet!' without providing objective telemetry, targets, or equipment clues. Side quest objectives must be acquired from NPC quest givers in the overworld.

## Active Hypotheses for Progression
### Hypothesis H76: Starter Level Milestone & Growth Evaluation (Started: Turn 19887)
- **Premise**: Protocol 1 completed: Sirius audited at Lv15 (HP 42/42, Atk 28, Def 29, Sp. Atk 20, Sp. Def 23, Speed 20) with 2505 EXP, needing exactly 30 EXP to reach Lv16. In-game clock recorded at 23:33 (night). Critiques confirm physical exploration across Sovio City and sewers is exhausted (H60-H75). We isolate the starter growth variable: Professor Ivo specifically asks 'Hey, Ashi, how's your new Pokémon?'. We hypothesize that raising Sirius to Lv16 (a standard starter milestone) triggers new dialogue from Professor Ivo or satisfies a progression flag.
- **Protocol**:
  1. Close Start Menu to return to overworld at (48, 18).
  2. Navigate south via Southern Avenue to Route 1 grass.
  3. Win ONE wild battle to earn >= 30 EXP and level Sirius to Lv16.
  4. Inspect any new move prompts or evolution checks upon leveling up.
- **Falsifiable Success Criteria**: Sirius leveling to Lv16, triggering new dialogue with Professor Ivo in Lancio Town, or changing game state flags.
