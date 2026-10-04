# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train to Amor City.
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.

## Critical Ground Truth: Debunked Storage Room Hallucination
- **Storage Room (37, 14)**: Verified 100% empty storage room displaying verbatim: "Its a simple storage room..". There was NEVER any cutscene or event freeing Jackson inside this room, and Jackson was never held there. Jackson ran outside into Sovio City during the tremor. Any claims of Jackson being rescued at (37, 14) were context summarizer hallucinations.

## Consolidated Concluded Hypotheses Summary
- **Overworld & Civilians (H118-H123, H126, H129, H132, H134, H143)**: Thoroughfares, residences (Nana, Wii, Gumball, Karate, Name Rater), and ambient NPCs confirmed static baseline.
- **Digital Systems & Facilities (H124, H128, H133, H137-A, H140)**: HuPhone (empty mailbox, 0 active quests, static map), PC (empty), Mart (standard stock), Trainer Card (ID 54592, 8 rounds), Timetable Board (scenic text) 100% verified static.
- **External Routes & Lancio Town (H136, H141, H142)**: Lancio Town, Lab main floor, Route 1 (Cut tree at 5, 44, cottage, defeated trainers Mike/Sonia/Duke) 100% static post-defeat baseline.
- **Mechanical Level-Up (H127, H139)**: Sirius Lv17, Zephyr Lv2, inventory verified.
- **Sovio Sewers Audits (H135, H137-B - CONCLUDED)**: All sectors (Western Terrace, Wall Ladder, Northern Gangway, Col 23 bridge, Eastern Platform door at 37, 14, Dark Sector basement) 100% verified static baseline. Zero NPCs, zero story flags.

## Concluded Hypothesis H146: Non-Spatial System & In-Game Device Audit (CONCLUDED - FALSIFIED)
- **Premise**: Progression gated by non-spatial system triggers (HuPhone apps, party inspection, or Trainer Card state).
- **Findings (Turns 23822-23866)**:
  - HuPhone Item Storage: 0 items deposited.
  - HuPhone Mailbox: 0 messages.
  - HuPhone Quest Log: 0 active quests ("You aren't doing any Quest at the moment!").
  - HuPhone World Map: Fully browsed; static regional nodes (Solare Island marker, Divampa Cave, Mulberry Town verified).
  - Trainer Card: Front (Asher ID 54592, 0 badges, 8 tournament round slots); Back (6 dark crest silhouettes).
  - Party Summary: Sirius Lv17 Relaxed (OT Asher 54592, met Lancio Lv5, Held Item: Black Belt; moves: Metal Claw, Quick Attack, Work Up, Mach Punch). Zephyr Lv2 Pidgey (Mild, Keen Eye, Tackle).
- **Conclusion**: Falsified. No non-spatial flags, unread messages, or menu triggers unlock progression.

## Active Hypothesis H147: Sovio Pokémon Center PC & Facility State Audit
- **Premise**: Progression blocker "I should find dad first!" may require checking in-game communications, PC mail/storage, or an internal trigger in Sovio Pokémon Center.
- **Target Variables**:
  1. Nurse Joy counter interaction at (7, 3): Check heal dialogue and respawn registration.
  2. Corner PC Terminal at (12, 1): Inspect Asher's PC (Mailbox & Item Storage) and Someone's PC boxes.
  3. Resident NPCs: Camper at (5, 7) and Resident Boy at (8, 6).
  4. Framed Town Map at (11, 0).
- **Testing Criteria**: Confirm whether PC terminal, mailbox, or NPCs exhibit any state changes post-sewers.
- **Stopping Boundary**: Complete inspection of targets 1-4 inside Pokémon Center, record exact findings, and conclude H147.
## H147 Audit Execution Progress (Turns 23885-23909)
- Target 1 (Nurse Joy at 7, 3): Verified standard heal dialogue, full HP/PP restored, Sovio Center respawn checkpoint registered.
- Target 2 (PC Terminal at 12, 1):
  - Asher's PC Mailbox: Audited empty verbatim ("There's no Mail here.").
  - Asher's PC Item Storage: Audited empty verbatim ("There are no items.").
  - Someone's PC Box Storage: Audited empty (Box 1 30-slot grid visually inspected; 0 stored Pokémon).
- Target 4 (Framed Town Map at 11, 0): Verified functional interactive regional Town Map displaying player marker at Sovio City.
- Target 3 (Resident NPCs): Resident Boy at (8, 6)/(9, 5) verified. Camper at (5, 7) pending final check to conclude H147.