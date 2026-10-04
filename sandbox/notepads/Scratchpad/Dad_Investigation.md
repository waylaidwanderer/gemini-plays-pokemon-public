# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train to Amor City.
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.

## Consolidated Concluded Hypotheses Summary
- **Overworld, Residences & Civic Fixtures (H118-H123, H126, H129, H132, H134, H143, H147, H153, H154, H155, H158, H159)**: All residences (Nana, Wii, Gumball, Karate, Name Rater; beds and PC desks inert), ambient NPCs (bikers, boy Rocky, park dating couple, Jigglypuff children, Center patrons Camper/Boy), civic fixtures (fountain basin at 41, 18, elevated terrace at 47-51, 14-16, manhole at 51, 16), and Pokémon Center services verified 100% static baseline.
- **Metro Station Lobby (H154, H157)**: East boundary verified strictly terminated at stairs (24, 24) and timetable board (21-23, 23); zero secondary partitions or attendants present. West boundary terminates at column 17 seats. Turnstile gate at (19, 21) triggers "I should find dad first!".
- **External Geography (H136, H141, H142, H149)**: Lancio Town (Professor Ivo dialogue, lab stairs locked, incubator inert, harbor pier empty, fisherman patience text) and Route 1 (Cut tree at 5, 44 inert, cottage resident static sample text, defeated trainers Mike/Sonia/Duke) 100% static post-defeat baseline.
- **Sovio Sewers & Dark Sector Geometry (H135, H137-B, H156, H161)**: Main sectors (Western Terrace, Wall Ladder, Northern Gangway, Col 23 bridge) verified static baseline. Storage Room Platform at (37, 14) displays 'Its a simple storage room..'. Dark Sector basement (columns 13-32, rows 4-11) verified fully bounded (north wall row 7, south wall row 10, west wall column 12, mat at 14-15, 9 leading to 3x3 toy room at 2, 38). No hidden passages or secondary exits exist.
- **Interactive World Map (H160-A)**: Interactive regional viewer tested (Turns 24367-24370); cursor moves across nodes with hover banners, but pressing A yields zero fast-travel or teleport prompts. Fixed yellow pin tracks Sovio City. Confirmed purely informative map viewer.
- **Commercial Economy & Liquid Funds (H160)**: Liquidated Nugget for $5,000 (Money: $11,096) at Sovio PokéMart (Turn 24398). Tested Metro turnstile at (19, 21) (Turn 24434: blocked by "I should find dad first!") and Route 2 barrier at (52, 19) (Turn 24437: blocked by "I can't go yet... I have things to do!"). Confirmed neither liquid wealth nor PokéMart sales transactions alter progression barrier scripts.

## Active Hypothesis H162: System-Level Item & Interface Verification (HuPhone PC & Party)
- **Premise**: All accessible physical overworld NPC interactions and commercial wealth have failed to clear the turnstile blocker ("I should find dad first!"). Testing whether progression is gated by an unexamined system mechanism: HuPhone portable PC Item Storage (checking for stored items/tickets/equipment from Dad), Mailbox, or Party/Item interactions.
- **Action Plan**:
  1. Open HuPhone via SELECT.
  2. Access Item Storage app -> check 'Withdraw Item' to verify if any items, tickets, or equipment are stored. [TESTED Turn 24446: Displays "There are no items." Confirmed empty].
  3. Check 'Mailbox' on HuPhone PC.
  4. Inspect Party summary and held item states.