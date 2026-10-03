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
### Hypothesis H76: Systematic Party Telemetry & Confrontation Plaza Re-Evaluation (Started: Turn 19887)
- **Premise**: Physical traversal across all surface and sewer corridors has repeatedly yielded static baseline dialogue across turns 19100-19886. The core story blocker remains 'I should find dad first!' at the Metro turnstile (19, 21) and 'I can't go yet... I have things to do!' at Route 2 (52, 19). We hypothesize that progression gating is tied to an internal game state flag (such as party readiness, starter telemetry, in-game clock transition, or an uninspected event trigger in Central Plaza where Dad and Mother originally confronted each other).
- **Protocol**:
  1. Open START Menu to record exact in-game clock time and audit party telemetry (Sirius & Zephyr).
  2. Navigate from (48, 18) into Central Plaza confrontation site outside the Pokémon Center (columns 42-45, rows 13-15).
  3. Sweep the confrontation perimeter to test if a physical or invisible event script triggers at the exact locus of Mother's Eclipse demonstration.
- **Falsifiable Success Criteria**: Discovering a new event trigger/cutscene at the confrontation site, or identifying an internal condition required to advance.
