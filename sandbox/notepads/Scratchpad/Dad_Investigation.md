# Scratchpad: Post-Tremor Investigation & Progression Hypotheses

## Core Active Progression Barriers
- **Metro Turnstile (19, 21)**: Scripted barrier triggers verbatim "I should find dad first!" and forces Asher south to (19, 22). Gates train platform to Amor City.
- **Route 2 Eastern Exit (52, 19-22)**: Scripted barrier triggers verbatim "I can't go yet... I have things to do!" and forces Asher west.

## Distilled Physical Constraints & Verified Negative Facts
- **Metro Station Lobby & Platform**: Turnstile (19, 21) is a walk-over tripwire forcing step Down to (19, 22). Scanner pillars (18, 21) / (20, 21) and brick walls (cols 21-23, row 23) are solid obstacles. Platform attendant is seated at (21, 18) facing west, physically unreachable. Timetable board (cols 21-23, row 23) displays static destination flavor text.
- **Central Plaza Perimeter (Cols 41-46, Rows 12-16)**: Systematically swept confrontation perimeter outside Pokémon Center; 100% verified inert with zero hidden tripwires or story scripts.
- **Northern Alcove & Exterior (Cols 40-41, Rows 7-9)**: House (39, 7) alleyway and gap at (41, 8) confirmed dead-ends against building walls.
- **West Avenue Commercial Facade & Boundaries**: Columns 16-22 beneath the giant billboard audited with direct 'A' interaction (100% inert). Karate house entered at (14, 15). Western boundary along columns 11-12 (rows 16-24) confirmed continuous solid office building wall.
- **Sovio City Residential Interiors & Overworld NPCs**: All residences (Nana/granddaughter, elderly Wii man/son, Gumball family, Karate couple/Machop, Name Rater) and exterior NPCs (Bikers, Boy Rocky, Central Park dating couple, Jigglypuff family, Pokémon Center Camper/Boy) display static ambient dialogue.
- **Sovio Sewers**: Grunts vacated following Marie's radio directive. Eastern Storage Platform door (37, 14) displays "Its a simple storage room..". Rugged rocks at (10, 18) and (22, 10) require specialized smashing equipment. Entire sewer network confirmed physically exhausted.
- **Route 1 & Lancio Town**: All Route 1 trainers defeated, cottage resident gifted Max Repel. Lancio harbor pier has no boat moored. Professor Ivo lab basement stairs blocked ("I probably shouldn't head down here...").
- **Party State & Summaries (Turn 27306)**: Sirius (Lv17 Riolu) and Zephyr (Lv2 Pidgey) summary pages, moves, and held items inspected; standard status with zero progression triggers.
- **Sovio Pokémon Center PC Terminal (Turn 27326)**: Corner PC at (12, 1) verified 100% empty across Someone's PC (Box 1), Asher's PC (Item Storage & Mailbox), with no Professor's PC network option.
- **16:00 RTC Train Schedule (Turn 27332)**: Turnstile at (19, 21) tested at 16:03 RTC; still triggers verbatim "I should find dad first!". RTC train schedule hypothesis falsified.
- **HuPhone World Map & Quest Log (Turns 27333-27341)**: World Map node interactions (Sovio City / Metro Station) confirmed inert; Quest Status ("You aren't doing any Quest currently...") and Quest List Pages 1-3 verified static side-quest tracker with zero story triggers.
- **Sovio Pokémon Center Framed Town Map & Counter (Turns 27346-27351)**: Framed Town Map at (11, 0) verified identical to HuPhone World Map; Nurse Joy service counter at (7, 4) completed full healing cycle with standard dialogue.

## Structured Progression Decision Tree by System Type
1. **System 1: Party State & Pokémon Mechanics**
   - *Status*: Audited and verified negative (Turn 27306).
2. **System 2: Interactive World Objects & Facility Terminals**
   - *Hypothesis*: Progression flag is set via an interactive terminal or facility object rather than an overworld NPC sprite.
   - *Remaining Unverified Variables*: Lancio Lab incubator apparatus at (18-19, 5-6) (Sovio Pokémon Center PC, Framed Town Map, and Nurse Joy counter verified negative).
3. **System 3: HuPhone Apps & Communication Systems**
   - *Status*: Audited and verified negative (Turns 27333-27341).
4. **System 4: Story Script & Trigger Flags (Unverified NPC Dialogues)**
   - *Hypothesis*: Event triggers depend on front-facing NPC dialogue skipped during prior visits (e.g., elderly man at 41, 33 in House 39, 7; Karate House 14, 15 occupants).

## Active Empirical Investigation Plans
- **Audit Target 1 (System 4 - Unverified Front-Facing Interior Dialogues - Active)**: Exit Sovio Pokémon Center, enter House (39, 7) to test direct front-facing dialogue with the elderly man at (41, 33), then test front-facing dialogue with the occupants in Karate House (14, 15).
- **Audit Target 2 (System 2 - Lancio Lab Apparatus & Remaining Regional Terminals)**: If Sovio interior dialogues return negative, inspect remaining regional interactive objects.