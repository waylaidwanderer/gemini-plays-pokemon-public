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

## Concluded Hypotheses Summary (Categorical Synthesis)
- **H118-H159 (Surface Overworld Audits)**: All accessible civilian residences, ambient NPCs, civic fixtures, and service facilities across Sovio City, Route 1, and Lancio Town audited as invariant post-confrontation baselines. Falsified.
- **H160-H162 (Economic & System Storage Audits)**: PokéMart transactions, liquid wealth, and portable PC storage confirmed unrelated to gating flags. Falsified.
- **H163 (Subterranean Jackson Audit)**: Exhaustive physical audit of Sovio Sewers, Dark Sector basement, and deep room (2, 38) confirmed Jackson's absolute absence. Subterranean searches permanently terminated. Falsified.
- **H165 (Central Plaza Scripted Tiles & UI Audit)**: Paved confrontation area and all start menu subsystems verified clear of active triggers. Falsified.
- **H166 (Northeast Route 2 Boundary Audit)**: Collision tests against column 52 rows 17-18 confirmed continuous solid building facade east of signpost (51, 18). Bypass corridor non-existent. Falsified.

## Active Hypothesis H167: Metro Station Fixture & Interaction Mechanics Audit
- **Premise**: All surface residences, sewers, and external geography have been exhaustively categorized as static baselines. Testing whether any unverified mechanical interaction inside the Metro Station lobby (e.g. seating collision at column 17 chairs, directional interactions with turnstile pillars, or ticket purchase prompts) alters player state or triggers progression.
- **Action Plan**:
  1. Walk West to (18, 24) and test Left movement into chair (17, 24) to determine if sitting/waiting mechanic exists.
  2. Test chairs at (17, 23) and (17, 22).
  3. Probe scanner pillars at (18, 21) and (20, 21) from adjacent tiles with A.
- **Falsification Boundary**: If all three chairs exhibit standard solid obstacle collision with zero sitting animations, and scanner pillars remain inert, H167 is falsified, confirming all lobby fixtures are purely decorative.