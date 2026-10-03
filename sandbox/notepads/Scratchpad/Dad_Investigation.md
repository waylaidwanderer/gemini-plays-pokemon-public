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

## Active Hypotheses for Progression

### Hypothesis H69: Untracked Game Systems, Bag Pockets & Equipment Audit (Started: Turn 19714)
- **Premise**: With all overworld maps (Sovio City, Route 1, Lancio Town, Sovio Sewers), NPCs, residences, and Metro lobby fixtures empirically verified as static/baseline, progress is gated by an untracked game system, inventory interaction, Key Item, or equipment mechanic (e.g. equipment to smash rugged rocks, registered key items, or Start Menu options).
- **Protocol**:
  1. Dismiss timetable textbox and open Start Menu.
  2. Open Bag and audit every pocket (Items, Key Items, Poké Balls, TMs, Berries).
  3. Inspect party Pokémon (Sirius, Zephyr) for held items, forms, or interactions.
  4. Test overworld button controls (L button, R button, Select).
  5. Inspect Options menu for engine features (e.g. Auto-run, DexNav, Quick-save).
- **Falsifiable Success Criteria**: Discovering an unused Key Item, equipment tool, app feature, or control toggle that enables field obstacle clearance or narrative advancement.
- Bag Audit (Turn 19722): 100% completed. Items: Potion x1, Poison Barb x1, Antidote x1, Nugget x1. Poké Balls: Timer Ball x1, Poké Ball x10. Key Items: HuPhone (Select), TM Case. Confirmed zero equipment or keys in Bag.
- Option Menu Audit (Turn 19735): Standard 7-item Gen 3 Option menu (Text Speed: Fast, Battle Scene: On, Battle Style: Shift, Sound: Stereo, Button Mode: Help, Frame: Type 1, Cancel). Confirmed zero custom engine toggles, auto-run settings, or difficulty modes.
