# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Scanner pillars (18, 21) and (20, 21) verified 100% inert; platform chairs verified empty; north wall across columns 21-23 is solid brick with timetable board mounted.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Concluded Hypotheses
- **H60-H94 (Baseline Sweeps - Turns 7232-20521)**: FALSIFIED. Static audits across Sovio residences, plaza, Metro lobby, and sewer platforms confirmed zero triggers; Dad's rescue in sewers was unverified.
- **Route 1 Cut Tree (Turns 20616-20622)**: FALSIFIED. Cut tree at (5, 44) confirmed impassable without HM/Cut.
- **H95: Lancio Town Regional & Facility Audit (Turns 20616-20723)**: FALSIFIED. Lancio Town facilities, residents, and pier confirmed 100% static with no story triggers.
- **H96: Multi-Angle Decorative Tile Pixel-Hunting (Turns 20724-20760)**: FALSIFIED. Pixel-hunting orientation-dependent interaction on decorative road tiles is ungrounded in engine mechanics; abandoned per critique.
- **H97: Communication Channel, Inventory & Surface House Audit (Turns 20761-20820)**: FALSIFIED. Audited HuPhone apps, surface residences, and Route 2 barrier with zero triggers.
- **H98: Subterranean Investigation in Sovio Sewers (Turns 20821-20851)**: FALSIFIED. Full re-traversal of Sovio Sewers confirmed vacated corridors; storage room at (37, 14) remains static.
- **H99: Player Menus, Devices & Party State Audit (Turns 20886-20938)**: FALSIFIED. Verified inventory, party summaries, Trainer Card, and options; progression is not gated by unexamined menus.
- **H101: Overlooked Narrative Event Triggers Audit (Turns 20944-20982)**: FALSIFIED. Audited Pokémon Center cycle, PC storage, framed map, and Route 2 barrier; all static.
- **H102: South Sidewalk Westward Traversal to (22, 27-28) (Turns 20984-20995)**: FALSIFIED. Sidewalk terminates west at column 22 on rows 27-28 against building foundation collision.
- **H103: Southern Avenue Thoroughfare & Route 1 Connection (Turns 21032-21041)**: FALSIFIED. Southern Avenue (columns 14-15) is an open connection to Route 1 with zero barrier text. Route 1 trainers (Duke at 45, 12; Sonia at 27, 15) remain in static defeated post-battle text. Early-route trainers and southern border do not advance the Sovio Metro tremor plot; macro-traversal south to Lancio Town is redundant and falsified.

## Active Hypotheses for Progression
### Hypothesis H104: Sovio Metro Station Turnstile Interaction & Lobby Boundary Audit
- **Premise**: Main story progression is explicitly gated at the Metro turnstile: "I should find dad first!". Prior audits of the Metro lobby focused only on the central axis and stepping directly onto (19, 21). Unexamined variables remain:
  1. Interacting with the station attendant sitting on the platform side across the turnstile from (19, 22), (18, 22), or (20, 22).
  2. Inspecting the east and west boundary tiles of the Metro lobby for unvisited fixtures or NPCs.
- **Audit Steps**:
  1. Return north from Route 1 to Sovio City via Southern Avenue.
  2. Enter Sovio Metro Station at (48, 17).
  3. Approach turnstiles at (19, 22) and test facing North/Northwest/Northeast to interact with the station attendant.
  4. Inspect east/west lobby perimeter tiles.
- **Falsifiable Success Criteria**: Triggering new dialogue from the station attendant or advancing the train departure flag.
- **Falsifiable Failure Criteria**: Attendant is completely non-interactive across the turnstile, and lobby perimeter tiles are confirmed static walls.
