# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Platform chairs verified 100% empty (turns 19364-19368); scanner pillars (18, 21) and (20, 21) verified 100% inert with zero interaction.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Jackson & Narrative Status Audit
- **Narrative Truth**: Jackson ran outside the Sovio Metro Station into Sovio City to investigate the seismic tremor.

## Concluded Hypotheses
- H60 (Night Cycle), H61 (Inventory/Triggers), H62 (Corridor), H63 (Lobby & Storage Room): FALSIFIED. Verified (37, 14) displays static text "Its a simple storage room..." with zero warps or triggers. Sewers fully cleared.
- H65 (Sovio City Exterior Paths & NPCs): FALSIFIED. Exterior corridors, Route 2 barrier (52, 19), West Ave rear lane (col 12), and Central Park NPCs (Boy in pink shirt, Little Girl, Jigglypuff, east walkway) verified static with zero progression flags.
- H66 (Southern Regional Anchors & Route 1 Civilians): FALSIFIED. Route 1 trainers (Duke, Sonia, Mike), Cottage, and all civilians (Grass boy at 11, 48; Camper at 17, 44; Pidgey boy at 34, 37; Science guy at 39, 37) audited as baseline flavor text. Lancio Town Lab (basement restricted, Prof Ivo and machine baseline) and Harbor Dock (pier empty, zero boats) verified 100% baseline.
- H67 (Sovio City Residential Interiors): FALSIFIED. All 5 residential houses (Karate/Machop, Gumball, Wii, Nana's Terrace, Name Rater) audited baseline. Private civilian houses confirmed devoid of progression flags.
- H68 (Sovio Metro Station Lobby & Turnstiles Deep Audit): FALSIFIED. West chairs (17, 23-24) and scanner pillars (18, 21; 20, 21) are decorative. Timetable board (21-23, 23) displays static destinations text. Turnstile (19, 21) remains strictly blocked ('I should find dad first!'). Platform chairs verified empty. Lobby contains zero active progression triggers or hidden switches.
- H69 (Untracked Game Systems, Bag Pockets & Equipment Audit): CONCLUDED. Bag 100% audited (Potion x1, Poison Barb x1, Antidote x1, Nugget x1; Timer Ball x1, Poké Ball x10; HuPhone, TM Case; zero equipment/keys). Party verified (Sirius Lv15 Black Belt, Zephyr Lv2, zero field moves). Options menu verified (standard Gen 3, Button Mode: Help, zero custom toggles). HuPhone PC Item Storage empty ('There are no items.'), Mailbox empty ('There's no Mail here.'), Quest Status empty ('You aren't doing any Quest currently...'). Overworld L and R buttons tested inert.

## Active Hypotheses for Progression

### Hypothesis H70: Sovio City Elevated Terrace & Vantage Point Deep Audit (Started: Turn 19754)
- **Premise**: When the tremor occurred, Dad ran outside the Metro Station to investigate. The elevated wooden terrace at columns 47-51, rows 13-17 is situated directly above the Metro portal, serving as the prime vantage point overlooking the city. Only Nana's door at (49, 14) was previously checked; the remaining terrace tiles (cols 47-51, rows 14-17) have never been fully swept.
- **Protocol**:
  1. Ascend Metro stairs at (24, 24) to Central Plaza (48, 18).
  2. Ascend terrace curb at (47, 15).
  3. Systematically sweep all terrace tiles (columns 47-51, rows 13-17) and inspect railings, corners, and east perimeter.
- **Falsifiable Success Criteria**: Finding Jackson, an NPC, or triggering an overworld script cutscene on the terrace.
