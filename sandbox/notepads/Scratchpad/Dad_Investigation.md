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

## Structured Progression Decision Tree by System Type
1. **System 1: Party State & Pokémon Mechanics**
   - *Hypothesis*: Progression requires a specific party condition, move, or Sirius mechanic.
   - *Variables*: Sirius (Lv17 Riolu, custom Torn Scarf sprite, Black Belt, moves: Metal Claw/Quick Attack/Work Up/Mach Punch), Zephyr (Lv2 Pidgey, moves: Tackle/Protect).
   - *Test Plan*: Inspect Pokémon summary screens, move details, and verify if any party member or held item interacts with world objects.
2. **System 2: Interactive World Objects & Facility Terminals**
   - *Hypothesis*: Progression flag is set via an interactive terminal, PC, or facility object rather than an overworld NPC sprite.
   - *Variables*: Sovio Pokémon Center corner PC terminal at (12, 1), Framed Town Map at (11, 0), Pokémon Center service counter, Lancio Lab incubator apparatus at (18-19, 5-6).
   - *Test Plan*: Systematically access each PC menu option (Someone's PC, Asher's PC, Professor's PC) and facility terminal to check for unread messages, logs, or network triggers.
3. **System 3: HuPhone Apps & Communication Systems**
   - *Hypothesis*: The HuPhone contains an unactivated trigger or regional reference that updates story state.
   - *Variables*: Item Storage, World Map hover nodes, Quest Log (Pages 1-5).
   - *Test Plan*: Verify all app submenus and examine whether interacting with specific regional map nodes or key items produces new prompts.
4. **System 4: Story Script & Trigger Flags**
   - *Hypothesis*: The event "find dad" is not a physical NPC search, but a specific prerequisite interaction that changes Asher's internal dialogue or Metro attendant behavior.

## Active Empirical Investigation Plans
- **Audit Target 1 (Facility Terminals)**: Exit Metro Station to Sovio Pokémon Center; access corner PC terminal at (12, 1) and test all PC options (Someone's PC, Asher's PC, Professor's network).
- **Audit Target 2 (Party & Sirius Inspection)**: Open Pokémon menu from Start Menu to inspect Sirius and Zephyr status and held items.