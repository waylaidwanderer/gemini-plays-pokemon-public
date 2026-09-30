## Status Conditions & Overworld Poison Mechanics (Verified Turn 659)
- **Overworld Poison Damage**: Overworld poison damage is completely DISABLED in Pokémon Sors v1.3 (aligns with Gen 5+ / CFRU engine rules).
- **Burden of Proof / Empirical Verification**: After being poisoned by wild Nidoran♀ on Turn 499, Sirius walked over 150 overworld steps across Route 1 without taking a single point of poison damage. On Turn 658-659, opening the party menu showed Sirius at full 22/22 HP (PSN), and using a Potion yielded 'It won't have any effect.'
- **Turn-in-Place Mechanic**: There is NO turn-in-place mechanic on foot; pressing a D-Pad direction always turns and attempts a forward step unless blocked by terrain collision.

## Facilities & PokéMarts (Verified Turns 795-805)
- **Lancio Town Pokémon Center**: Contains no PokéMart clerk or item vendor inside (verified by full room inspection). NPC dialogue claiming PokéMarts are inside centers does not apply to Lancio Town.
## Quests & Mission Engine (Verified Turn 1378-1381)
- **Single Active Quest Limit & Cancellation**: The player can only have ONE active side quest at a time in Pokémon Sors. When attempting to accept a new side quest while one is in progress, the NPC explains: "You are already doing a quest... In order to start a new quest, you need to cancel the one in progress!", followed immediately by an in-dialogue choice prompt: "Would you like to cancel you current quest? Yes/No" (cursor defaults to No).
## HuPhone Regional Device & Apps (Verified Turns 1520, 4012, 6028, 6198)
- **Item Storage**: Portable PC item storage (verified functional, audited empty Turn 4000).
- **Mailbox**: Portable PC mailbox (audited empty Turns 4005, 7127: "There's no Mail here.").
- **World Map**: Static regional map viewer of Hupest with town nodes; does not show active quest pins or arrows.
- **Quest Log Scope & Structure**:
  - Tracks side quests across 5 pages (23 named quests + 2 '- Not available -' slots). Main story progression milestones are NOT tracked in the Quest Log app.
  - 'Quest List': Lists side quests and marks completion status ('This Quest has been completed!' for finished quests like Lost Pidgey [Verified Turn 6550], or 'This Quest hasn't been completed yet!' for uncompleted quests).
  - 'Quest Status': Displays status for active quests without detailed objective hints.

## Pokémon Center Respawn Mechanics (Verified Turn 1815)
- **Whiteout / Blackout Respawn Point**: Respawn points are set only when speaking to Nurse Joy at the counter to heal. Simply entering a Pokémon Center without talking to Nurse Joy does NOT register a new checkpoint.
## Verified Inventory State & Field Move Capabilities (Audited Turns 9548-9551)
- **TMs & HMs Pocket**: Contains only TM17 (Protect) and TM48 (Work Up). Zero HMs (HM01 Cut, HM06 Rock Smash, Surf, Flash, etc.) in possession.
- **Key Items Pocket**: Contains only HuPhone and TM Case. Zero keys, keycards, access badges, or event quest items held.
- **Items Pocket**: Repel, Poison Barb, Nugget, Potions. Zero progression-related tools.
- **Empirical Constraint**: Asher cannot interact with, cut, or smash any physical field obstacles (Cut trees on Route 1, cracked rocks in Sovio Sewers). All current progression gates are strictly event-flag / story-trigger based.
