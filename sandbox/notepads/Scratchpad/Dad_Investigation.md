# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Scanner pillars (18, 21) and (20, 21) verified 100% inert with zero interaction.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Concluded Hypotheses
- H60-H65 (Sewers, Lobby, Sovio City Exterior Corridors & NPCs - Turns 19100-19470): FALSIFIED. Sewers cleared, (37, 14) storage room static, exterior paths, barriers (52, 19), and civilians verified baseline.
- H66-H74 (Regional Anchors, Residences, Systems, Terrace, Corridor, PC & Sewers - Turns 19470-19838): FALSIFIED. Route 1/Lancio Town, all 5 residences, lobby fixtures, terrace/corridor walls, PC Box 1, and subterranean sewers re-verified static baseline with zero new items or triggers.
- H75-H82 (Quest Log, Level Milestone, Metro Lobby, Overworld Perimeters, Mailbox, Facades, Healing, Portal Fixtures - Turns 19871-20028): FALSIFIED. Audited HuPhone apps, level 16 scope, lobby timetable/chairs, all Sovio exterior perimeters, Southwest facade, Nurse Joy party heal, and portal threshold; confirmed static civilian baseline and persistent gate flags.
- H84 (Surface Gate & Re-Sweep of Civilians / Bag / Lobby - Turns 20042-20130): FALSIFIED. Bag audited standard (no pending key items or letters), Metro lobby verified 100% empty with turnstile firmly gated by "I should find dad first!", Route 2 firmly gated by "I can't go yet... I have things to do!", and re-interrogating Central Park online dating couple (44, 24 and 31, 21), Boy Rocky (23, 17), and Karate House residents (14, 15) confirmed 100% static baseline with zero new items or triggers.
- H85 (Early-Game Quest Givers & Equipment Premise - Turns 20133-20162): FALSIFIED. Camper at (5, 7) has strictly ambient dialogue with zero quest prompt or reaction to Antidote/Potion. Furthermore, per Mechanics/Engine.md, sidequests are explicitly decoupled from main story milestones; the premise that optional sidequests gate main story progress or supply mandatory equipment is falsified. Aborted the ungrounded macro-loop trek to Lancio Town.
- H86 (Sovio City Building & Sewer Triggers - Turns 20162-20246): FALSIFIED. Eastern storage room platform at (37, 14) verified static inspection trigger with solid collision at (37, 15) and zero NPCs/items. Northern boulevard tan building facade at (32-37, 8-12) and shutters at (34-35, 12) confirmed solid collision with zero interactions or secret doors.
- H87 (Residential 2F Bedroom Sweep - Turns 20251-20283): FALSIFIED. House (39, 7) 2F (boy, TV Easter egg, inert PC/bed) and Gumball House (29, 14) 2F (sleeping bed, framed map, bookshelf, PC) confirmed 100% static civilian baselines. Pruned from investigation per critique instructions.
- H88 (Outdoor Seismic Impact Sites - Turns 20285-20301): FALSIFIED. Central Park southern perimeter (rows 27-28), Route 2 barrier (52, 19-22), and southwest building exterior confirmed standard baseline with zero physical fissures, altered NPCs, or tremor artifacts. Trash can at (30, 28) confirmed completely inert.
- H89 (Metro Station Attendant & Railing Interaction - Turns 20302-20308): FALSIFIED. North wall at columns 21-23 is solid brick with timetable board mounted; staircase at column 24 has solid side banister with zero open railing to interact with the seated officer on the platform. West wall lobby chairs (rows 22-25) confirmed non-interactive with zero dropped items. Passage to platform remains strictly gated by the (19, 21) turnstile trigger ("I should find dad first!").

## Active Hypotheses for Progression
### Hypothesis H90: Investigation of System State & Regional Quest Triggers (Started: Turn 20309)
- **Premise**: All physical overworld and subterranean baselines in Sovio City are verified exhausted (turnstiles firmly gated by "I should find dad first!", Route 2 gated by "I can't go yet... I have things to do!", sewers vacated, exterior civilians static). The gating flag must be linked to an uninspected system state or regional trigger outside the local macro-loop.
- **Isolated Variables**:
  1. Inspect HuPhone Quest Status and Quest Log for pending story or side objectives.
  2. Inspect Bag key items and party status for unread letters or hold items.
  3. Evaluate regional anchors (Professor Ivo's lab basement prerequisite or Route 1 cut tree).
- **Falsifiable Success Criteria**: Identifying an active quest objective, receiving a new story prompt, or clearing the turnstile prerequisite.
