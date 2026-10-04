# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train to Amor City.
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.

## Consolidated Concluded Hypotheses Summary
- **Overworld, Residences & Civic Fixtures (H118-H123, H126, H129, H132, H134, H143, H147, H153, H154, H155, H158, H159)**: All residences (Nana, Wii, Gumball, Karate, Name Rater; beds and PC desks inert), ambient NPCs (bikers, boy Rocky, park dating couple, Jigglypuff children, Center patrons Camper/Boy), civic fixtures (fountain basin at 41, 18, elevated terrace at 47-51, 14-16, manhole at 51, 16), and Pokémon Center services verified 100% static baseline.
- **Metro Station Lobby (H154, H157)**: East boundary verified strictly terminated at stairs (24, 24) and timetable board (21-23, 23); zero secondary partitions or attendants present. West boundary terminates at column 17 seats. Turnstile gate at (19, 21) triggers "I should find dad first!".
- **External Geography (H136, H141, H142, H149)**: Lancio Town (Professor Ivo dialogue, lab stairs locked, incubator inert, harbor pier empty, fisherman patience text) and Route 1 (Cut tree at 5, 44 inert, cottage resident static sample text, defeated trainers Mike/Sonia/Duke) 100% static post-defeat baseline.
- **Sovio Sewers Audits (H135, H137-B, H156, H163)**: All sectors (Western Terrace, Wall Ladder, Northern Gangway, Col 23 bridge, Col 30 causeway, Storage Room at 37, 14, Dark Sector upper alcove 23, 4, Dark Sector western corridor, and Deep Subterranean room 2, 38) audited 100% empty of story triggers or NPCs. Jackson is definitively absent from Sovio Sewers. All subterranean searches permanently terminated.
- **Interactive World Map (H160-A)**: Interactive regional viewer tested (Turns 24367-24370); cursor moves across nodes with hover banners, but pressing A yields zero fast-travel or teleport prompts. Fixed yellow pin tracks Sovio City. Confirmed purely informative map viewer.
- **Commercial Economy & Liquid Funds (H160)**: Liquidated Nugget for $5,000 (Money: $11,096) at Sovio PokéMart (Turn 24398). Tested Metro turnstile at (19, 21) (Turn 24434: blocked by "I should find dad first!") and Route 2 barrier at (52, 19) (Turn 24437: blocked by "I can't go yet... I have things to do!"). Confirmed neither liquid wealth nor PokéMart sales transactions alter progression barrier scripts.
- **System & Interface Verification (H162)**: HuPhone portable PC Item Storage ("There are no items.") and Mailbox ("There's no Mail here.") audited 100% empty (Turns 24446, 24449). Confirmed no stored items, equipment, or letters from Dad exist in system storage.

## Active Hypothesis H165: Investigation of Progression Gating Flags and Event Triggers
- **Premise**: Physical searches for a Dad overworld NPC sprite across all accessible maps (Sovio City, Sovio Sewers, Route 1, Lancio Town) have proven that Jackson does not exist as an independent overworld NPC sprite. Gating flags at the Metro turnstile ("I should find dad first!") and Route 2 barrier ("I can't go yet... I have things to do!") must be resolved through an uncompleted story trigger or menu/system interaction.
- **Action Plan**:
  1. Audit Central Plaza event area (columns 40-46, rows 12-16 outside Pokémon Center) for scripted trigger tiles where the Team Siara confrontation occurred.
  2. Audit inventory, Trainer Card, and Party state for novel triggers.
  3. Document outcomes and verify turnstile state.
- **Falsification Boundary**: If no trigger tile or menu interaction alters the turnstile flag, record exact coordinates tested and expand analysis to remaining unverified mechanics.