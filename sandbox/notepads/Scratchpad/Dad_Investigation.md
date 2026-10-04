# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train to Amor City.
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.

## Consolidated Concluded Hypotheses Summary
- **Overworld, Residences & Civic Fixtures (H118-H123, H126, H129, H132, H134, H143, H147, H153, H154, H155, H158, H159)**: All residences (Nana, Wii, Gumball, Karate, Name Rater; beds and PC desks inert), ambient NPCs (bikers, boy Rocky, park dating couple, Jigglypuff children, Center patrons Camper/Boy), civic fixtures (fountain basin at 41, 18, elevated terrace at 47-51, 14-16, manhole at 51, 16), and Pokémon Center services verified 100% static baseline.
- **Metro Station Lobby (H154, H157)**: East boundary verified strictly terminated at stairs (24, 24) and timetable board (21-23, 23); zero secondary partitions or attendants present. West boundary terminates at column 17 seats. Turnstile gate at (19, 21) triggers "I should find dad first!".
- **External Geography (H136, H141, H142, H149)**: Lancio Town (Professor Ivo dialogue, lab stairs locked, incubator inert, harbor pier empty, fisherman patience text) and Route 1 (Cut tree at 5, 44 inert, cottage resident static sample text, defeated trainers Mike/Sonia/Duke) 100% static post-defeat baseline.
- **Sovio Sewers & Dark Sector Geometry (H135, H137-B, H156, H161)**: Main sectors (Western Terrace, Wall Ladder, Northern Gangway, Col 23 bridge) verified static baseline. Storage Room Platform at (37, 14) displays 'Its a simple storage room..'. Dark Sector basement (columns 13-32, rows 4-11) verified fully bounded (north wall row 7, south wall row 10, west wall column 12, mat at 14-15, 9 leading to 3x3 toy room at 2, 38). No hidden passages or secondary exits exist.
- **Hardware, Inventory & Party Systems (H124, H127, H128, H133, H137-A, H139, H140, H146, H148, H151, H152, H157)**: HuPhone (Item Storage empty, Mailbox empty, Quest Status idle), PC (empty), Mart inventory, Bag items (Key Items has exclusively HuPhone and TM Case; Items has Potion x1, Poison Barb x1, Antidote x1), and party status (Sirius Lv17 Riolu fully healed, Quick Feet, Black Belt held) verified static.
- **Interactive World Map (H160-A)**: Interactive regional viewer tested (Turns 24367-24370); cursor moves across nodes with hover banners, but pressing A yields zero fast-travel or teleport prompts. Fixed yellow pin tracks Sovio City. Confirmed purely informative map viewer.

## Active Hypothesis H160: Commercial Economy & Progression Gating Verification
- **Premise**: Nugget liquidated for $5,000 at Sovio PokéMart (Money: $11,096). Testing whether possessing sufficient travel funds / commercial transaction flags cleared the Metro turnstile blocker or Route 2 exit barrier.
- **Action Plan**:
  1. Return from Sovio Sewers to Metro Station lobby via stairs at (38, 22).
  2. Inspect Metro Station turnstiles at (19, 21) to verify if "I should find dad first!" remains or if access to Amor train platform is granted.
  3. If still blocked, inspect Route 2 eastern exit at (52, 19-22) on Sovio City surface.