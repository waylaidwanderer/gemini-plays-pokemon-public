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
- H76 (Starter Level Milestone to Lv16): REJECTED. Riolu evolves via daytime Friendship, not Lv16; Professor Ivo checks no level target. Walking to Route 1 is an ungrounded scope violation repeating the exhausted 800-turn loop.

- H77 (Metro Station Lobby Audit - Turns 19932-19962): FALSIFIED. Audit of Metro Station lobby re-verified that timetable is flavor text, seating is decorative, and turnstile check ('I should find dad first!') is strictly an external prerequisite. Jackson ran outside into Sovio City during the tremor and was never in the sewers.

## Active Hypotheses for Progression
### Hypothesis H78: Sovio City Overworld Perimeter & Tremor Investigation (Started: Turn 19963)
- **Premise**: Jackson ran outside into Sovio City during the seismic tremor to investigate what caused it. Turnstiles remain blocked until Dad is found. Having cleared distant locations (Route 1, Lancio) and subterranean sewers, we systematically audit Sovio City overworld for the source of the tremor, unvisited tiles, off-screen perimeters, and untriggered events.
- **Audit Findings**:
  - **Protocol 1 (Elevated Terrace, cols 47-51, rows 13-17 - Turns 19965-19971)**: FALSIFIED. Terrace floor extends east to column 51 on rows 14-16. Modern high-rise building starts at column 52 with solid collision at (52, 15) and (51, 14). Decorative manhole at (51, 16) is inert. Behind signpost at (51, 17) dead-ends against signpost back (51, 18).
  - **Protocol 2 (Pokémon Center East Flank & Northern Alcove, cols 38-46, rows 7-13 - Turns 19971-19975)**: FALSIFIED. Tile (46, 12) is solid curb/wall corner of Pokémon Center; zero north passage. Northern alleyway along column 40 runs from (40, 15) to house (39, 7) at (40, 9); fully enclosed by Pokémon Center west wall and tan building east wall with zero side alleys.
  - **Protocol 3 (Covered Corridor & Route 2 Approach, cols 47-52, rows 19-23 - Turns 19976-19977)**: FALSIFIED. Covered corridor beneath roof graphic connects rows 19-22 east to column 52, which triggers story barrier ("I can't go yet... I have things to do!").
  - **Protocol 4 (West Avenue & Southwest Sector, cols 11-26, rows 16-30 - Turns 19990-19993)**: FALSIFIED. West Avenue terminates west at column 11 into solid office building wall. Three Bikers at (13, 21-23), Karate house at (14, 15), Boy Rocky at (23, 17), Gumball house at (29, 14), and rear biker lane/southwest lawn confirmed static civilian baseline with zero story triggers.
- **Conclusion**: H78 FALSIFIED. Sovio City overworld perimeters and civilians contain zero triggers for Dad's whereabouts or the turnstile prerequisite.
