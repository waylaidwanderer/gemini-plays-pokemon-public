# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Platform chairs verified 100% empty (turns 19364-19368); scanner pillars (18, 21) and (20, 21) verified 100% inert with zero interaction.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Jackson & Narrative Status Audit
- **Narrative Truth**: Jackson ran outside the Sovio Metro Station into Sovio City to investigate the seismic tremor.

## Concluded Hypotheses
- H60 (Night Cycle - Turns 19100-19150), H61 (Inventory/Triggers - Turns 19150-19200), H62 (Corridor - Turns 19200-19250), H63 (Lobby & Storage Room - Turns 19250-19300): FALSIFIED. Verified (37, 14) displays static text "Its a simple storage room..." with zero warps or triggers. Sewers fully cleared.
- H65 (Sovio City Exterior Paths & NPCs - Turns 19440-19470): FALSIFIED. Exterior corridors, Route 2 barrier (52, 19), West Ave rear lane (col 12), and Central Park NPCs (Boy in pink shirt, Little Girl, Jigglypuff, east walkway) verified static with zero progression flags.
- H66 (Southern Regional Anchors & Route 1 Civilians): FALSIFIED. Route 1 trainers (Duke, Sonia, Mike), Cottage, and all civilians (Grass boy at 11, 48; Camper at 17, 44; Pidgey boy at 34, 37; Science guy at 39, 37) audited as baseline flavor text. Lancio Town Lab (basement restricted, Prof Ivo and machine baseline) and Harbor Dock (pier empty, zero boats) verified 100% baseline.
- H67 (Sovio City Residential Interiors): FALSIFIED. All 5 residential houses (Karate/Machop, Gumball, Wii, Nana's Terrace, Name Rater) audited baseline. Private civilian houses confirmed devoid of progression flags.
- H68 (Sovio Metro Station Lobby & Turnstiles Deep Audit): FALSIFIED. West chairs (17, 23-24) and scanner pillars (18, 21; 20, 21) are decorative. Timetable board (21-23, 23) displays static destinations text. Turnstile (19, 21) remains strictly blocked ('I should find dad first!'). Platform chairs verified empty. Lobby contains zero active progression triggers or hidden switches.
- H69 (Untracked Game Systems, Bag Pockets & Equipment Audit): CONCLUDED. Bag 100% audited (Potion x1, Poison Barb x1, Antidote x1, Nugget x1; Timer Ball x1, Poké Ball x10; HuPhone, TM Case; zero equipment/keys). Party verified with visual proof (Turn 19780: Sirius Lv15 Black Belt, Relaxed nature, Quick Feet, moves: Metal Claw, Quick Attack, Work Up, Mach Punch; Zephyr Lv2; zero field moves). Options menu verified (standard Gen 3, Button Mode: Help, zero custom toggles). HuPhone PC Item Storage empty ('There are no items.'), Mailbox empty ('There's no Mail here.'), Quest Status empty ('You aren't doing any Quest currently...'). Overworld L and R buttons tested inert.
- H70 (Sovio City Elevated Terrace & Vantage Point Deep Audit): FALSIFIED. Swept all terrace floor tiles (cols 47-51, rows 14-16), tested round emblem at (50, 16) (decorative), windows, and perimeter railings. Terrace is completely devoid of NPCs, switches, or script triggers.

## Active Hypotheses for Progression
### Hypothesis H73: Sovio City Pokémon Center PC Telemetry & Town Map Deep Audit (Started: Turn 19786)
- **Premise**: With all Bag pockets, overworld paths, residential houses, and the terrace verified baseline, we audit the physical PC terminal at (12, 1) inside the Sovio Pokémon Center. The HuPhone only accesses Item Storage; the physical terminal hosts Someone's PC (Pokémon Storage System) and Professor evaluation. We will inspect Pokémon Storage (Boxes 1-14, Move Items) for deposited/gift Pokémon or stored items, and examine the framed Town Map at (11, 0) for regional story cues.
- **Protocol**:
  1. Dismiss Route 2 barrier text with B, navigate out of covered corridor to Central Plaza (44, 15).
  2. Enter Pokémon Center at (44, 12).
  3. Access PC at (12, 1): check Someone's PC (Boxes, Move Items) and Professor evaluation.
  4. Access Town Map at (11, 0): inspect regional node descriptions.
- **Falsifiable Success Criteria**: Finding a deposited/gift Pokémon, stored item, or narrative cue on the PC or Town Map.
- Someone's PC Audit (Turn 19795): Box 1 visually confirmed completely empty (0/30 slots occupied, PKMN Data gray/blank). Zero deposited or gift Pokémon.
