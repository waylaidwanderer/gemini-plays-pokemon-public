## Status Conditions & Overworld Poison Mechanics (Verified Turn 659)
- **Overworld Poison Damage**: Overworld poison damage is completely DISABLED in Pokémon Sors v1.3 (aligns with Gen 5+ / CFRU engine rules).
- **Burden of Proof / Empirical Verification**: After being poisoned by wild Nidoran♀ on Turn 499, Sirius walked over 150 overworld steps across Route 1 without taking a single point of poison damage. On Turn 658-659, opening the party menu showed Sirius at full 22/22 HP (PSN), and using a Potion yielded 'It won't have any effect.'
- **Turn-in-Place Mechanic**: There is NO turn-in-place mechanic on foot; pressing a D-Pad direction always turns and attempts a forward step unless blocked by terrain collision.

## Facilities & PokéMarts (Verified Turns 795-805)
- **Lancio Town Pokémon Center**: Contains no PokéMart clerk or item vendor inside (verified by full room inspection). NPC dialogue claiming PokéMarts are inside centers does not apply to Lancio Town.
- **Official In-Game Confirmation (Turn 1188)**: Sovio City Trainer Tips signpost at (15, 18) verbatim: "If your Pokémon gets poisoned, it will take damage during battles. However, it won't when you walk around."
## Quests & Mission Engine (Verified Turn 1378-1381)
- **Single Active Quest Limit & Cancellation**: The player can only have ONE active side quest at a time in Pokémon Sors. When attempting to accept a new side quest while one is in progress, the NPC explains: "You are already doing a quest... In order to start a new quest, you need to cancel the one in progress!", followed immediately by an in-dialogue choice prompt: "Would you like to cancel you current quest? Yes/No" (cursor defaults to No).
## HuPhone Regional Device & Apps (Verified Turns 1520, 4012, 6028, 6198)
- **Item Storage**: Portable PC item storage (verified functional, audited empty Turn 4000).
- **Mailbox**: Portable PC mailbox (audited empty Turn 4005).
- **World Map**: Static regional map viewer of Hupest with town nodes; does not show active quest pins or arrows.
- **Quest Log Scope & Structure**:
  - Exclusively tracks side quests ('Lost Pidgey', 'Lost Toy', 'Egg Research', 'Medic!', 'Squirtle Gang'). Main story progression milestones are NOT tracked in the Quest Log app.
  - 'Quest List': Lists side quests and marks completion status ('This Quest hasn't been completed yet!').
  - 'Quest Status': Displays canned message: 'You are already doing a Quest. If you want to start another one, cancel the current Quest. You can cancel a quest at by talking to its provider!' (does not display specific objective hints).
- **Quest Limit**: Only ONE active side quest can be in progress at a time; accepting a new quest prompts cancellation of the active quest.
## Pokémon Center Respawn Mechanics (Verified Turn 1815)
- **Whiteout / Blackout Respawn Point**: Respawn points are set only when speaking to Nurse Joy at the counter to heal. Simply entering a Pokémon Center without talking to Nurse Joy does NOT register a new checkpoint.
