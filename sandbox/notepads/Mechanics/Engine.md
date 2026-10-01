## Status Conditions & Overworld Poison Mechanics (Verified Turn 659)

- **Overworld Poison Damage**: Overworld poison damage is completely DISABLED in Pokémon Sors v1.3 (aligns with Gen 5+ / CFRU engine rules).

- **Burden of Proof / Empirical Verification**: After being poisoned by wild Nidoran♀ on Turn 499, Sirius walked over 150 overworld steps across Route 1 without taking a single point of poison damage. On Turn 658-659, opening the party menu showed Sirius at full 22/22 HP (PSN), and using a Potion yielded 'It won't have any effect.'

- **Turn-in-Place Mechanic**: There is NO turn-in-place mechanic on foot; pressing a D-Pad direction always turns and attempts a forward step unless blocked by terrain collision.



## Facilities & PokéMarts (Verified Turns 795-805, 9706, 9743)

- **PokéMarts Inside Pokémon Centers**: In the Hupest region, PokéMarts are integrated directly inside Pokémon Centers on the upper mezzanine floor! Reached via the blue carpeted stairs/escalator in the northwest corner of the center. Verified functional with clerk in Sovio City (Turn 9706). (Note: Lancio Town Pokémon Center verified single-story on Turn 10057; contains no mezzanine staircase or PokéMart vendor).

- **Bulk Poké Ball Purchases & Premier Ball Mechanic**: In Pokémon Sors, purchasing 10 Poké Balls does NOT grant a bonus Premier Ball. Empirical verification on Turn 9743 showed Bag containing exactly 10 Poké Balls, 1 Timer Ball (obtained earlier), and 0 Premier Balls.

## Quests & Mission Engine (Verified Turn 1378-1381)

- **Single Active Quest Limit & Cancellation**: The player can only have ONE active side quest at a time in Pokémon Sors. When attempting to accept a new side quest while one is in progress, the NPC explains: "You are already doing a quest... In order to start a new quest, you need to cancel the one in progress!", followed immediately by an in-dialogue choice prompt: "Would you like to cancel you current quest? Yes/No" (cursor defaults to No).

## HuPhone Regional Device & Apps (Audited Turns 12375-12394)
- **Access**: Activated via SELECT button or through BAG Key Items pocket.
- **Main App Menu**:
  1. **Item Storage**: Launches portable PC terminal (contains Item Storage, Mailbox, Turn Off).
  2. **World Map**: Static regional map viewer of Hupest with town nodes.
  3. **Quest Log**: Active objective tracker and completed quest list.
  4. **Back**: Closes HuPhone.
- **Portable PC Interface (Item Storage app)**:
  - **Item Storage**: Submenu with Withdraw Item, Deposit Item, Toss Item, Cancel. 
  - **Mailbox**: Portable PC mailbox. 
  - **Turn Off**: Exits portable PC interface.
- **World Map**: Static regional map viewer of Hupest with town nodes; does not show active quest pins or arrows.
- **Quest Log Scope & Structure**:
  - Tracks side quests across 5 pages (23 named quests + 2 '- Not available -' slots). Main story progression milestones are NOT tracked in the Quest Log app.
  - 'Quest List': Lists side quests and marks completion status ('This Quest has been completed!' for finished quests like Lost Pidgey, or 'This Quest hasn't been completed yet!' for uncompleted quests).
  - 'Quest Status' (Empirically Verified Turns 12670-12672): Displays fixed system tutorial text across 3 textboxes: 'You are already doing a Quest. / If you want to start another one, cancel the current Quest. / You can cancel a quest at by talking to [the provider]'. It does NOT display quest titles, descriptions, coordinates, or objective hints. All quest details must be obtained from NPC dialogue.
  - HuPhone Menu & Quest Navigation: Neither the main HuPhone app menu nor the Quest List dismiss with the B button. The player must explicitly navigate down to 'Back' or 'Exit' and press A to close them.

## Pokémon Center Respawn Mechanics (Verified Turn 1815)

- **Whiteout / Blackout Respawn Point**: Respawn points are set only when speaking to Nurse Joy at the counter to heal. Simply entering a Pokémon Center without talking to Nurse Joy does NOT register a new checkpoint.

## Verified Inventory State & Field Move Capabilities (Audited Turns 9548-9551, 9743)

- **Poké Balls Pocket (Verified Turn 9743)**: Contains 10 Poké Balls (purchased at Sovio PokéMart Mezzanine) and 1 Timer Ball (11 catching balls total).

- **TMs & HMs Pocket**: Contains only TM17 (Protect) and TM48 (Work Up). Zero HMs (HM01 Cut, HM06 Rock Smash, Surf, Flash, etc.) in possession.

- **Key Items Pocket**: Contains HuPhone (registered to SELECT, indicated by the red marker icon) and TM Case. Zero keys, keycards, access badges, or event quest items held.

- **Items Pocket**: Repel, Poison Barb, Nugget, Potions. Zero progression-related tools.

- **Empirical Constraint**: Asher cannot interact with, cut, or smash any physical field obstacles (Cut trees on Route 1, cracked rocks in Sovio Sewers). All current progression gates are strictly event-flag / story-trigger based.

## Trainer Card Structure & Display (Verified Turns 11889-11890)
- **Front Layout**: Name (Asher), ID No. (54592), Money, Playtime. Features '*ROUNDS' row tracking 8 Pok� Ball icons for the Eclipse Tournament.
- **Back Layout**: Displays 6 dark badge/crest silhouettes, red geometric stripes, and regional circular crest.
- **Card Controls**: Pressing A on either side initiates a 3D flip animation between Front and Back. Pressing B when settled on the Front exits back to the Start Menu.

