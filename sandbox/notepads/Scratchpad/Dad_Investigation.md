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
- **Residential Fixtures & Beds (H155 - CONCLUDED)**: Karate House 2F Bed (2-3, 13-14), Wii House 2F PC Desk (46-47, 11-12), and Wii House 2F Bed (46, 14) inspected directly with 'A'. 100% verified completely inert with zero dialogue, zero rest/time-advancement mechanics, and zero progression flags. Static baseline.

## Active Hypothesis H156: Systematic Investigation of Sovio Sewers Story Flag Triggers
- **Premise**: Gating script at Metro turnstile (19, 21) ("I should find dad first!") and Route 2 barrier ("I can't go yet... I have things to do!") requires triggering Jackson's location/rescue flag. Prior audits established that all Sovio City residences, civilians, and external towns (Lancio, Route 1) are static baselines. The sewer storage room at (37, 14) and the sewer sectors where Team Siara was active represent the canonical narrative source of the tremor and Jackson's abduction.
- **Independent Variables**:
  1. Re-inspect the Sewer Storage Room doorway at (37, 14) with specific directional interactions (facing South, East, West) and check for hidden triggers or key items.
  2. Comprehensive audit of the Dark Sector basement (cols 13-31, rows 3-12) to verify if unvisited tiles or hidden passages exist beyond the spotlight perimeter.
  3. Check if any sewer NPC or item trigger was left uncollected.
- **Causal Mechanism**: If Jackson's presence or a progression flag in the sewers triggers the completion of the tremor investigation, activating it will update the Metro turnstile script and allow departure to Amor City.
- **Stopping Boundary**: Complete targeted re-audit of the sewers (Storage Room platform 37, 14 and Dark Sector perimeter), document exact responses, and return to Metro turnstile to evaluate gating state.