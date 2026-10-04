# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train to Amor City.
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.

## Consolidated Concluded Hypotheses Summary
- **Overworld, Residences & Civic Fixtures (H118-H123, H126, H129, H132, H134, H143, H147, H153, H154, H155, H158, H159)**: All residences (Nana, Wii, Gumball, Karate, Name Rater; beds and PC desks inert), ambient NPCs (bikers, boy Rocky, park dating couple, Jigglypuff children, Center patrons Camper/Boy), civic fixtures (fountain basin at 41, 18, elevated terrace at 47-51, 14-16, manhole at 51, 16), and Pokémon Center services verified 100% static baseline.
- **Metro Station Lobby (H154, H157)**: East boundary verified strictly terminated at stairs (24, 24) and timetable board (21-23, 23); zero secondary partitions or attendants present. West boundary terminates at column 17 seats. Turnstile gate at (19, 21) triggers "I should find dad first!".
- **External Geography (H136, H141, H142, H149)**: Lancio Town (Professor Ivo dialogue, lab stairs locked, incubator inert, harbor pier empty, fisherman patience text) and Route 1 (Cut tree at 5, 44 inert, cottage resident static sample text, defeated trainers Mike/Sonia/Duke) 100% static post-defeat baseline.
- **Sovio Sewers Audits (H135, H137-B, H156)**: Main sectors (Western Terrace, Wall Ladder, Northern Gangway, Col 23 bridge) verified static baseline. Storage Room Platform at (37, 14) re-verified Turn 24206-24207 with South facing ("Its a simple storage room..."), East (38, 14), and West (36, 14) confirmed completely inert with zero switches or items. Grunts permanently vacated; rugged rocks require equipment. Dark Sector basement contains Nugget at (23, 4), rugged rock at (22, 10), and red mat at (15, 9) to toy room (2, 38).
- **Hardware, Inventory & Party Systems (H124, H127, H128, H133, H137-A, H139, H140, H146, H148, H151, H152, H157)**: HuPhone (Item Storage empty, Mailbox empty, Quest Status idle, World Map visual only), PC (empty), Mart inventory, Bag items (Key Items has exclusively HuPhone and TM Case; Items has Potion x1, Poison Barb x1, Antidote x1, Nugget x1), and party status (Sirius Lv17 Riolu fully healed, Quick Feet, Black Belt held) verified static.

## Active Hypothesis H160: Unexamined Systems & Interactive World Map Functionality
- **Premise**: Physical overworld NPC searching across Sovio, Route 1, and Lancio Town is certified static baseline. Progression must be gated by unexamined system-level mechanics (World Map, commercial economy, civic boundaries).
- **Target Variables & Empirical Findings**:
  1. **Interactive World Map Audit (Completed Turns 24367-24370)**:
     - D-pad moves cursor across regional nodes with dynamic hover banners (Sovio City, Route 7, Route 4, Amor City).
     - Pressing 'A' on current location (Sovio City) and target hub (Amor City) yields zero interaction, no popups, and no fast-travel prompts.
     - Player position is tracked by fixed yellow pin on Sovio City.
     - Conclusion: HuPhone World Map is purely an informative viewer; no hidden teleport or fast-travel mechanics exist.
  2. **Commercial Economy Audit (Active)**:
     - Return to Sovio Pokémon Center mezzanine PokéMart.
     - Sell Nugget ($5,000) to acquire liquid capital and audit clerk dialogue/options for story triggers.
  3. **Physical Epicenter Boundary**: Test direct interaction on the eastern Route 2 boundary curb and Central Park fountain basin.
- **Action Plan**:
  1. Close World Map and HuPhone to return to overworld at (15, 39).
  2. Walk north along Southern Avenue (col 15) and east to Sovio Pokémon Center (44, 12).
  3. Ride mezzanine escalator to PokéMart clerk (5, 3) and sell Nugget.
