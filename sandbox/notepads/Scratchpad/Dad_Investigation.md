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

- **Quest Triggers & Bag/Map Items (H151 - CONCLUDED)**: Camper dialogue static with Antidote in bag. HuPhone World Map is visual only (pressing 'A' on nodes does nothing). Nugget 'Use' yields standard Ivo refusal text. TM17 taught to Zephyr. Digital and bag systems verified static baseline.

- **Party Lead Configuration (H152 - CONCLUDED)**: Leading with Zephyr (Lv2 Pidgey, Tackle + Protect) vs Sirius yields identical verbatim text at Metro turnstile ("I should find dad first!") and Route 2 barrier ("I can't go yet... I have things to do!"). Party lead order is not the gating variable.

## Active Hypothesis H153: Causal Audit of Sovio Unresolved Civilian Quests & Plaza Triggers
- **Premise**: Route 2 exit blocker ("I can't go yet... I have things to do!") indicates uncompleted town tasks or unfulfilled event prerequisites in Sovio City. Central Park contains an apparent unresolved interaction (Boy at 33, 22 and Blonde Girl at 43-45, 23-26 both lamenting being stood up/catfished on opposite sides of the pond), matching Quest Log entry 'Valentines Gift' (Quest 8). Furthermore, the elevated terrace at (49, 14) and adjacent Central Plaza fixtures may contain untried interaction flags.
- **Target Variables**:
  1. Terrace & House Audit (49, 14): Re-inspect elevated terrace floor, signpost rear at (51, 17), and residence fixtures (stove, fridge, TV) to confirm zero unexamined triggers.
  2. Central Park Dating Pair Causal Interaction: Speak sequentially to Blonde Girl (43-45, 23-26) and Boy in Pink Shirt (33, 22) within the same contiguous sequence to verify if cross-talking triggers dialogue progression, a delivery prompt, or quest registration.
  3. Re-verify Route 2 and Metro Turnstile: Check if resolving civilian dialogues alters "I have things to do!" or "I should find dad first!".
- **Causal Mechanism**: If Route 2's blocker "I have things to do!" is tied to town side quests or civilian resolution (such as uniting the dating couple in Central Park), completing these interactions will update the story flag or clear the barrier.
- **Stopping Boundary**: Execute targets 1 and 2, record exact dialogue responses, check Route 2 barrier, and conclude H153.