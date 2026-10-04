# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train to Amor City.
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.

## Critical Ground Truth: Debunked Storage Room Hallucination
- **Storage Room (37, 14)**: Verified 100% empty storage room displaying verbatim: "Its a simple storage room..". There was NEVER any cutscene or event freeing Jackson inside this room, and Jackson was never held there. Jackson ran outside into Sovio City during the tremor. Any claims of Jackson being rescued at (37, 14) were context summarizer hallucinations.

## Consolidated Concluded Hypotheses Summary
- **Overworld & Civilians (H118-H123, H126, H129, H132, H134, H143, H147, H153)**: All residences (Nana, Wii, Gumball, Karate, Name Rater), ambient NPCs (bikers, boy Rocky, park dating couple, Jigglypuff children), and Pokémon Center patrons/facilities verified 100% static baseline.
- **External Geography (H136, H141, H142, H149)**: Lancio Town (Professor Ivo dialogue, lab stairs locked, incubator inert, harbor pier empty, fisherman patience text) and Route 1 (Cut tree at 5, 44 inert, cottage resident static sample text, defeated trainers Mike/Sonia/Duke) 100% static post-defeat baseline.
- **Sovio Sewers Audits (H135, H137-B)**: All sectors (Western Terrace, Wall Ladder, Northern Gangway, Col 23 bridge, Eastern Platform door at 37, 14, Dark Sector basement) 100% verified static baseline. Grunts permanently vacated; rugged rocks require equipment.
- **Hardware, Inventory & Party Systems (H124, H127, H128, H133, H137-A, H139, H140, H146, H148, H151, H152)**: HuPhone (Item Storage, Mailbox, World Map visual only), PC (empty), Mart inventory, Bag items (TM Case infinite use, Nugget sellable), and party lead configuration (Zephyr vs Sirius) verified static with zero delta on turnstile ("I should find dad first!") or Route 2 barrier ("I can't go yet... I have things to do!").

- **Civic Fixtures & Metro Lobby (H154 - CONCLUDED)**: Central Park fountain basin (41, 18) confirmed completely inert with zero interaction text. Metro lobby east boundary terminates at stairs (24, 24) and timetable board (21-23, 23) with zero secondary partitions. Static baseline.

## Active Hypothesis H155: Causal Audit of Unexamined Residential Fixtures (Karate Bed & Wii PC Desk)
- **Premise**: Progression blockers "I should find dad first!" and "I can't go yet... I have things to do!" may be gated by a time-of-day state (Metro schedule board lists AMOR 16:00, while current RTC clock is 22:56 night) or uninspected electronic fixtures. In custom ROM hacks with day/night cycles, beds frequently serve as rest/time-advancement mechanics. The bed at (2-3, 13-14) on 2F of the Karate House (14, 15) and the PC desk at (46, 11) on 2F of the Wii House (39, 7) have not been audited for interactive inspection triggers.
- **Target Variables**:
  1. Karate House 2F Bed (2-3, 13-14): Enter Karate House at (14, 15), ascend to 2F, face bed at (2-3, 13-14), and press 'A' to test for a sleep/rest/time-advance prompt.
  2. Wii House 2F PC Desk (46, 11): Enter house at (39, 7), ascend to 2F, face PC desk at (46, 11), and press 'A' to test for interaction prompts.
  3. Re-evaluate Progression Blockers: Check if resting or fixture inspection updates the Metro turnstile or Route 2 barrier text.
- **Causal Mechanism**: If advancing time or interacting with residential terminals updates story flags or clears the Metro departure condition, testing these fixtures will trigger state progression.
- **Stopping Boundary**: Complete testing of targets 1 and 2, record exact before/after responses, and conclude H155.