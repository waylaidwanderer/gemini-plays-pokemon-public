# Scratchpad: Progression Gating & Investigation Constraints

## Core Active Progression Barriers
- **Metro Turnstile (19, 21)**: Scripted barrier triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train platform to Amor City.
- **Route 2 Eastern Exit (52, 17-22)**: Continuous boundary blockage (rows 14-18 solid building facade collision; rows 19-22 trigger story barrier "I can't go yet... I have things to do!").
- **Professor Ivo's Lab Basement Stairs (12, 7)**: Red mat trigger displays "I probably shouldn't head down here..." in Lancio Town.

## Categorical Exhaustion & Invariant Baselines
- **Subterranean Sewers**: 100% audited across all sectors (Upper catwalks, ladders, storage room 37, 14, Dark Sector basement, deep room 2, 38, southern canal). Team Siara grunts permanently vacated. No NPCs or story triggers present.
- **Overworld Civilians & Residences**: All residential interiors (Nana, Wii, Gumball, Karate, Name Rater) and overworld civilians across Sovio City, Route 1, and Lancio Town are verified static post-defeat baselines.
- **Regional Geography & Obstacles**: Route 1 (Cut tree 5, 44, cottage resident, defeated trainers) and Lancio Town (Professor Ivo dialogue, incubator, harbor dock) are verified static baselines.
- **System, Economy & Inventory**: HuPhone Item Storage and Mailbox are 100% empty. Liquid wealth ($11,096) and PokéMart transactions have zero effect on story flags. Trainer Card (8 empty round icons, 6 crest silhouettes) and party profiles verified standard.
- **Central Plaza Event Tiles**: Ground tiles outside Pokémon Center (rows 13-16, cols 40-46) have zero active scripted triggers.

## Concluded Specific Feature Audits
- **H166 (Northeast Route 2 Boundary Audit)**: Collision tests against column 52 rows 17-18 confirmed continuous solid building facade east of signpost (51, 18). Bypass corridor non-existent. Falsified.
- **H167 (Metro Lobby Fixtures & Seating Audit)**: Tested all three west chairs at col 16 (rows 22-24); confirmed solid obstacle collision, zero seating mechanics, zero text. Probed scanner pillars at (18, 21) and (20, 21) with A; confirmed completely inert decorative fixtures. Platform verified empty. Falsified.
- **H168 (Central Park Southeast Hedge Alcove Audit)**: Navigated into dead-end alcove at (42, 30); probed South, West, and East pine hedge perimeter tiles with A; confirmed 100% inert tree collision with zero hidden items, triggers, or environmental changes. Falsified.

## Active Hypotheses & Strategic Planning
- **H169 (Rock Smash Equipment & Progression Gating Audit)**:
  - **Premise**: Rugged rocks in Sovio Sewers explicitly state: "It's a rugged rock, but with some equipment, I could smash it." Asher is gated at Metro turnstiles by "I should find dad first!". Prior summary claims that Jackson was rescued at turn 2279 were hallucinatory; the sewer storage room door at (37, 14) remains locked/closed ("Its a simple storage room.."). We need to determine if Rock Smash equipment or a progression flag exists on Route 1 / Lancio Town (e.g. Professor Ivo, Route 1 Cottage, or Lancio residents).
  - **Variables**: NPC dialogues, Key Items, equipment triggers, lab basement access.
  - **Falsification Criteria**: If Professor Ivo, Route 1 Cottage resident, and Lancio Town NPCs provide zero new dialogue, items, or equipment triggers, Route 1/Lancio Town will be definitively falsified as sources of progression tools, proving the gating flag or equipment must originate in Sovio City or Sewers.