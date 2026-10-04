# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Gates train to Amor City.
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.

## Critical Ground Truth: Debunked Storage Room Hallucination
- **Storage Room (37, 14)**: Verified 100% empty storage room displaying verbatim: "Its a simple storage room..". There was NEVER any cutscene or event freeing Jackson inside this room, and Jackson was never held there. Jackson ran outside into Sovio City during the tremor. Any claims of Jackson being rescued at (37, 14) were context summarizer hallucinations.

## Consolidated Concluded Hypotheses Summary
- **Overworld & Civilians (H118-H123, H126, H129, H132, H134, H143)**: Thoroughfares, residences (Nana, Wii, Gumball, Karate, Name Rater), and ambient NPCs confirmed static baseline.
- **Digital Systems & Facilities (H124, H128, H133, H137-A, H140)**: HuPhone (empty mailbox, 0 active quests, static map), PC (empty), Mart (standard stock), Trainer Card (ID 54592, 8 rounds), Timetable Board (scenic text) 100% verified static.
- **External Routes & Lancio Town (H136, H141, H142, H149)**: Lancio Town (Professor Ivo dialogue, lab stairs locked, incubator inert, harbor pier empty, fisherman patience text), Route 1 (Cut tree at 5, 44 inert, cottage resident static sample text, defeated trainers Mike/Sonia/Duke) 100% static post-defeat baseline.
- **Mechanical Level-Up (H127, H139)**: Sirius Lv17, Zephyr Lv2, inventory verified.
- **Sovio Sewers Audits (H135, H137-B - CONCLUDED)**: All sectors (Western Terrace, Wall Ladder, Northern Gangway, Col 23 bridge, Eastern Platform door at 37, 14, Dark Sector basement) 100% verified static baseline. Zero NPCs, zero story flags.
- **Non-Spatial System & In-Game Devices (H146 - CONCLUDED)**: HuPhone apps (Item Storage 0 items, Mailbox 0 messages, Quest Log 0 active, World Map verified), Trainer Card (Front: Asher ID 54592, 0 Badges, 8 round slots; Back: 6 crest silhouettes), Party summary (Sirius Lv17 Relaxed, Black Belt; Zephyr Lv2 Tackle) 100% verified static baseline.
- **Sovio Pokémon Center Facilities & State (H147 - CONCLUDED)**: Nurse Joy (standard heal & respawn checkpoint registered), Asher's PC (Mailbox empty verbatim, Item Storage empty verbatim), Someone's PC (Box 1 30-slot grid audited empty), Framed Town Map (functional regional map displaying player at Sovio City), and resident NPCs (Straw-hat Camper at 5, 7; Resident Boy at 8-10, 4-6) verified 100% static baseline.
- **Metro Station Partition & Turnstiles (H148 - CONCLUDED)**: Scanner pillars at (18, 21) and (20, 21) verified 100% inert. Turnstile passage at (19, 21) verified as the single trigger tile displaying verbatim "I should find dad first!" and forcing player south to (19, 22). Platform side chairs verified empty furniture per map documentation.

## Active Hypothesis H151: Active Causal Testing of Sovio City Quest Triggers & Items (Camper/Medic & HuPhone)
- **Premise**: The progression barriers ("I should find dad first!" and "I can't go yet... I have things to do!") are internal monologues reflecting unfulfilled progression conditions. Page 1 of the Quest Log lists early-game side quests: "Egg Research", "Medic!", and "Squirtle Gang". In the Sovio City Pokémon Center, the Camper at (5, 7) complains that his Weedle is poisoned while Asher holds an Antidote in the Bag. Furthermore, the HuPhone World Map and Bag items represent untried interactive mechanics.
- **Target Variables**:
  1. Camper Interaction (Medic! Quest): Confirmed static baseline per Turn 23913 audit; talking to Camper with Antidote in bag yields unchanged ambient joke dialogue. No item handoff prompt exists. Concluded static.
  2. HuPhone World Map: Empirically tested in Turn 24038; pressing 'A' on location nodes produces no action or menu. Visual display viewer only. Concluded inert.
  3. Bag & Item Interactive Prompts: [COMPLETED] TM Case confirmed infinite use (TM17 taught to Zephyr). Nugget "Use" yields Ivo refusal text ("This isn't the time to use that!"). Antidote/Potion standard medicine. Items pocket audited.
- **Causal Mechanism**: If progression is gated by town tasks ("I have things to do!") or registering/triggering specific quests (like "Medic!"), activating these causal variables will change the internal monologue state or provide actionable progression clues.
- **Outcome & Conclusion**: Target variables 1-3 evaluated. Camper dialogue static, World Map visual only, Bag items standard. Internal monologues ("I should find dad first!", "I can't go yet... I have things to do!") remain unchanged.