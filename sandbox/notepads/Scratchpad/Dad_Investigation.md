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
- H78 (Sovio City Overworld Perimeter & Tremor Investigation - Turns 19963-19993): FALSIFIED. Systematic audit of all overworld perimeters: Protocol 1 (Elevated Terrace), Protocol 2 (Pokémon Center perimeters & northern alley), Protocol 3 (Route 2 covered corridor), and Protocol 4 (West Avenue & southwest sector) confirmed static civilian baseline with zero story triggers.
- H79 (HuPhone Mailbox & World Map Audit - Turns 19995-20000): FALSIFIED. HuPhone Item Storage > Mailbox displays 'There's no Mail here.' (zero messages). World Map shows standard Hupest topology with no quest markers.
- H80 (Southwest Building West Facade Audit - Turns 20004-20006): FALSIFIED. Navigated to sidewalk at (17, 26-27). Facing East into (18, 26) and (18, 27) and pressing A confirms solid, inert building facade with decorative blue windowpanes; zero doors, warps, or story triggers exist.

## Active Hypotheses for Progression
### Hypothesis H81: Pokémon Center Nurse Joy Healing & Event State Refresh (Started: Turn 20012)
- **Premise**: In Turn 1329, completing a party heal with Nurse Joy at the Sovio Pokémon Center counter was the exact prerequisite that advanced the story and spawned Dad at the Metro Station. In recent turns (e.g. Turn 19788-19803), the center was entered solely for PC Box 1 and Town Map audits without speaking to Nurse Joy. We execute a full party heal with Nurse Joy at the counter (7, 4) to verify if this refreshes the pending story event flag or clears the turnstile prerequisite.
- **Protocol**:
  1. Navigate east from West Avenue (15, 19) along row 18 and row 15 boulevard to Central Plaza (44, 15), then north into Pokémon Center at (44, 12).
  2. Approach counter at (7, 4) and speak to Nurse Joy to heal party to full health.
  3. Verify if new story dialogue occurs, and re-test Metro turnstile at (19, 21).
- **Falsifiable Success Criteria**: Nurse Joy dialogue change, new event sequence triggered, or turnstile block cleared.
