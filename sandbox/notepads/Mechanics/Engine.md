## Status Conditions & Overworld Poison Mechanics

- **Overworld Poison Damage**: Overworld poison damage is completely DISABLED in Pokémon Sors v1.3 (aligns with Gen 5+ / CFRU engine rules).

- **Turn-in-Place Mechanic**: There is NO turn-in-place mechanic on foot; pressing a D-Pad direction always turns and attempts a forward step unless blocked by terrain collision.

## Facilities & PokéMarts

- **PokéMarts Inside Pokémon Centers**: In the Hupest region, PokéMarts are integrated directly inside Pokémon Centers on the upper mezzanine floor! Reached via the blue carpeted stairs/escalator in the northwest corner of the center. Verified functional with clerk in Sovio City. (Note: Lancio Town Pokémon Center also features the northwest mezzanine escalator).

- **Bulk Poké Ball Purchases & Premier Ball Mechanic**: In Pokémon Sors, purchasing 10 Poké Balls does NOT grant a bonus Premier Ball.

## Quests & Mission Engine

- **Single Active Quest Limit & Cancellation**: The player can only have ONE active side quest at a time in Pokémon Sors.
  - **At the Current Quest's Provider**: Speaking to the NPC who gave the currently active quest repeats their quest hint and then prompts: *"If you find this too hard you can just say no too... / Wanna cancel the Quest? Yes/No"* (cursor defaults to **Yes**; pressing A selects Yes and cancels the quest with *"Its okay, it seems like a difficult task anyway..."*, verified at Route 2 `40, 21` in Turn 28402).
  - **At Any Other Quest Provider**: Attempting to accept a normal side quest from a different NPC while a normal quest is already active displays verbatim: *"You are already doing a Quest! Cancel the Quest in progress at the provider to start a new one."* without offering a cancellation prompt—you must return to the original quest provider to cancel an active quest (verified with Roark in Mt. Gerhana, Turn 28087).

  - **Special Quests Exception**: Quests marked with a yellow speech bubble icon (such as Quest #11 "Oak's Research") are **Special Quests**: *"These quests have a different icon from the rest. They are far more complicated than the normal quests you can take. Completing them might take longer than an ordinary quest. These quests usually have multiple tasks for multiple rewards, and their fullest completion might arc through the entire game! They can't be cancelled, however this doesn't affect other Quests! Special Quests can be in progress besides pending Quests!"* (verified Turn 28502).

## HuPhone Regional Device & Apps
- **Access**: Activated via SELECT button or through BAG Key Items pocket.
- **Main App Menu**:
  1. **Item Storage**: Launches portable PC terminal (contains Item Storage, Mailbox, Turn Off).
  2. **World Map**: Interactive regional map viewer of Hupest navigated via D-pad (+Move). Dynamically displays location hover banners (e.g. Solare Island, Divampa Cave, Mulberry Town) in the top-left corner.
     - **Dynamic Banners**: Hovering over location nodes displays town/route names and subtitles in top-left (e.g., "Sovio City / Metro Station", "Amor City / Amor Dept.", "Route 4", "Route 16").
     - **Player Location Pin**: Asher's current position is tracked by a yellow pin with a black tip.
     - **Interactivity & Fast Travel**: Node interaction with button 'A' is inert; no fast travel or town info cards exist. The World Map functions strictly as a regional topological reference.
     - **Controls**: D-pad moves cursor; START button immediately snaps cursor to bottom-right '[X]' ('Close Map'); pressing A on '[X]' or B button exits back to the HuPhone menu (resetting the main HuPhone cursor to the top option `Item Storage`, so closing the HuPhone after exiting the World Map requires `Down 3 -> A` to select `Back`, verified Turn 32620).
  3. **Quest Log**: Active objective tracker and completed quest list.
  4. **Back**: Closes HuPhone.
- **Portable PC Interface (Item Storage app)**:
  - **Item Storage**: Submenu with Withdraw Item, Deposit Item, Toss Item, Cancel.
  - **Mailbox**: Portable PC mailbox (no mail present). 
  - **Turn Off**: Exits portable PC interface.
- **Quest Log Scope & Structure**:
  - Tracks side quests across 5 pages (23 named quests + 2 '- Not available -' slots). Main story progression milestones are NOT tracked in the Quest Log app.
  - **Page 1 Quests**:
    1. Lost Pidgey (Completed)
    2. Lost Toy (Completed)
    3. Egg Research (Completed in Turn 29330 — caught a wild Happiny holding an Oval Stone at Route 2 `52-53, 26`, moved the Oval Stone to the Bag via the Day-Care PC `10, 8`, and delivered it to the scientist at Route 2 `40, 21`; rewarded a **Pokémon Egg** sent to Box 1; **7 Poké Balls** remaining and **12 Owned species** in PokéDex)
    4. Medic! (Completed in Turn 28495 — delivered Cure Flower from Route 2 `45, 14` to Old Gentleman at Azluf Town Lighthouse `52, 5`; rewarded **Exp. Share**)
    5. Squirtle Gang (Completed in Turn 31891 — reunited the lost Squirtle from Samurion City `33, 25` with its family at `(46, 13)` on Route 4 South/Central via the eastern southbound branch `cols 44-46` of Route 4 North; rewarded **Itemfinder**)
  - **Page 2 Quests**:
    6. Lost Eevee (Paused at Explorer `42, 12` in Destino Mine 1F in Turn 32613 after auditing all accessible tiles of 1F, 2F, and the Inner Den; frees the single active quest slot for Route 12 and Jarro Town until western Destino City unlocks)
    7. Kaboom (Completed in Turn 32170 — found the lost Dynamite in the southwestern sand patch at Route 6 `27, 34`, defeated the ambushing Lv20 Gible, and delivered the Dynamite to the Coworker at Route 6 `43, 19` to blast open the collapsed Route 6 mine entrance at `44, 18-19`; rewarded **Rocky Helmet**)
    8. Valentines Gift (Active — accepted from the boy in blue overalls at Route 12 Main `16, 75` in Turn 32745; objective is to find 3 missing flowers [standard Poké Ball sprites] across Route 12, with `Flower 3` collected at `18, 47` into Key Items Pocket in Turn 32835)
    9. Angry Cubone Kid (Provider located at Jarro Town `22, 15` in front of the fenced Cubone pen `23, 13`; observed Turn 32928)
    10. Push it!
  - **Page 3 Quests**:
    11. Oak's Research (Special Quest — accepted at Azluf Town `40, 7` in Turn 28501; Task 1 [10 Pokémon caught] completed in Turn 28681, rewarding **Bulbasaur**; Task 2 [25 Pokémon caught] completed in Turn 29958, rewarding **Charmander**; Task 3 [45/50 Pokémon caught] completed in Turn 31043, rewarding **Squirtle** and bringing Owned species to **51 Hupest / 20 Colen**; Professor Oak now states *"Thank you, this will be enough, but come back later, I might have some more tasks for you!"* and `Quest Status` reports *"You aren't doing any Quest currently..."*, while `Page 3 -> 11. Oak's Research` still displays *"This Quest hasn't been completed yet."*, verified Turns 31045-31051)
    12. Elm's Research
    13. Rowan's Research
    14. Cynthia's Research
    15. Help for Barry
  - **Page 4 Quests**:
    16. - Not available -
    17. - Not available -
    18. Roark's Opal (Completed in Turn 28444; rewarded all 11 Fossils)
    19. Pokédex!
    20. Marine Point Hunter
  - **Page 5 Quests**:
    21. Hugh's Pokémon
    22. Silver's Deal
    23. Back to the...
    24. Outcasts
    25. The Mods of Cord
  - 'Quest Status': When a quest is active, displays the currently tracked quest status and system instructions. When no quest is active, displays 'You aren't doing any Quest at the moment!'.
  - HuPhone Menu & Quest Navigation: Neither the main HuPhone app menu nor the Quest List dismiss with the B button. The player must explicitly navigate down to 'Back' or 'Exit' and press A to close them.

## Pokémon Center Respawn Mechanics

- **Whiteout / Blackout Respawn Point**: Respawn points are set only when speaking to Nurse Joy at the counter to heal. Simply entering a Pokémon Center without talking to Nurse Joy does NOT register a new checkpoint.

## Verified Inventory State & Field Move Capabilities

- **Items Pocket (Audited Turn 32758)**: Contains **Destiny Knot x1** (received from Professor Ivo in Lancio Town at 50 Owned species in Turn 31109), **Water Stone x1** (collected at `(16, 14)` in the Closed Segment of Mt. Gerhana in Turn 31654), **Thunder Stone x1** (collected at Route 6 `23, 21` in Turn 32168), **Rocky Helmet x1** (rewarded at Route 6 `43, 19` for completing Quest #7 "Kaboom" in Turn 32170), **Repel x0**, **Super Repel x2** (verified `Super Repel x5` in Bag on Turn 32530; used 1 at `50, 14` in Turn 32576 and auto-renewed 2 inside Destino Mine), **Super Potion x1** (`Super Potion x2` confirmed in Bag in Turn 32515; used 1 on Sirius in Turn 32515), **Oval Stone x1** (collected at Route 4 `39, 20` in Turn 31853), **TinyMushroom x1** (collected at Route 6 `41, 28` in Turn 32053), **King's Rock x1** (collected at Route 6 `23, 13` in Turn 32098), **Red Shard x1** (collected at Destino Mine `40, 13` in Turn 32208), **Fire Stone x1** (collected at Destino Mine 2F `29, 21` in Turn 32381), **Hyper Potion x0** (collected from potion bottle sprite at Destino Mine 2F `47, 20` in Turn 32445 and used on Sirius in Turn 32530), **Clear Shard x1** (obtained at Destino Mine Inner Den `13, 15` in Turn 32471), **Iron x1** (collected at Destino Mine 1F `42, 40` in Turn 32582), **Revive x1** (collected from hidden rock cone at Route 12 Main `35, 62` in Turn 32758), **Burn Heal x1** (collected from spray bottle sprite at Route 12 Main `33, 46` in Turn 32830), **X Special x1** (collected from capsule sprite behind passable tree canopy at Route 12 Main `19, 19` in Turn 32870), **Link Cable x1** (collected from capsule sprite at Route 12 Main `23, 10` in Turn 32884), and **Odd Keystone x1** (gifted by Sinnoh Champion Cynthia outside the Jarro Town Pokémon Center at `14, 30` in Turn 32911; fits the ancient stone tower in the secret Route 6 section of Destino Mine 1F).
- **Key Items Pocket (Audited Turn 32170)**: Contains **HuPhone**, **TM Case**, **Metro Pass**, **Eclipse Band**, **Fishing Rod**, **Rare Opal** (retained in Key Items after completing Quest #18), **Itemfinder** (rewarded at Route 4 `46, 13` for completing Quest #5 in Turn 31891; **Dynamite** was delivered to the Coworker at Route 6 `43, 19` in Turn 32170), and **Flower 3** (collected at Route 12 Main `18, 47` for Quest #8 in Turn 32835).
- **Repel Auto-Renewal Prompt**: When an active Repel expires on a step, the engine automatically displays: "Repel's effect wore off... Use another? Yes/No" (cursor defaults to Yes; pressing A immediately consumes and applies the next Repel without opening the Bag, verified Turn 27448).
- **Bag Structure (Audited Turn 27862)**: Features 3 main horizontal pockets from left to right: **Items** (Pocket 1), **Key Items** (Pocket 2), and **Poké Balls** (Pocket 3; does not wrap around when pressing Right).
- **Poké Balls Pocket (Audited Turn 32754)**: Contains **Poké Ball x8**, **Great Ball x8**, and **Ultra Ball x1** (collected at Route 12 Main `33, 71` in Turn 32754; caught Lv18 Numel at `46, 14` in Turn 32212, nicknamed **Etna**, Lv18 Diglett at `47, 14` in Turn 32219, nicknamed **Gaia**, Lv14 Trapinch at `42, 49` in Turn 32246, nicknamed **Dune**, and Lv17 Teddiursa at Route 12 Main `18, 97` in Turn 32653, nicknamed **Ursa**, bringing Owned species to **62** in PokéDex).
- **Key Items Pocket (Audited Turn 27862)**:
  - **HuPhone** (registered to `[SELECT]`): *"A convenient smartphone that has many features to use."*
  - **TM Case**: *"A case that holds TMs and HMs. It is attached to the Bag's compartment for important items."*
  - **Metro Pass**: *"Its a card that can be used at the e-ticket reader gates to travel on the Hupest Metro Line."*
  - **Eclipse Band**: *"A special band designed to channel the power of Eclipse Shards to allow Eclipsing!"* (received from Professor Ivo in Azluf Town, Turn 27799).
  - **Fishing Rod**: *"A new, high-quality fishing rod. Use it by any body of water to fish for wild Pokémon."* (received from Fisherman at `37, 30` in Azluf Town, Turn 27854). Casting into water prints `. . .` dots and automatically resolves to either *"A Pokémon's on the hook!"* (requiring a single A/B press to start the wild battle, with no timing minigame) or *"Not even a nibble..."* (verified Turn 27865).
- **TMs & HMs Pocket**: Contains TM03 (collected at Route 4 `53, 17` in Turn 31892), TM17 (Protect), TM37 (Sandstorm, collected in Destino Mine 1F at `32, 35` in Turn 32317), TM39 (Rock Tomb, collected in Upper Mt. Gerhana at `43, 9` in Turn 31547), and TM48 (Work Up). Zero HMs in possession.

- **Empirical Constraint & Equipment Mechanic**: Interacting with cracked/rugged rocks in Sovio Sewers displays verbatim: "It's a rugged rock, but with some equipment, I could smash it." Confirmed that smashing rugged rocks is mechanic-gated by specialized equipment rather than traditional HM Rock Smash (verified at `6, 23` and `22, 10` in Sovio Sewers, Turns 27495 & 27512).

## Trainer Card Structure & Display
- **Front Layout**: Name (Asher), ID No. (54592), Money, Playtime. Features '*ROUNDS' row tracking 8 Poké Ball icons for the Eclipse Tournament.
- **Back Layout**: Displays 6 dark badge/crest silhouettes, red geometric stripes, and regional circular crest.
- **Card Controls**: Pressing A on either side initiates a 3D flip animation between Front and Back. Pressing B when settled on the Front exits back to the Start Menu.
## Start Menu Structure & Pokédex Status
- **Start Menu Entries & Cursor Memory**: Displays Pokédex, Pokémon, Bag, Asher (Trainer Card), Save, Option, Exit. The Start Menu persists its last highlighted row across openings in the overworld rather than resetting to the top entry (verified Turn 32738). In battle, switching a Pokémon out (including via forced switch moves like `Roar`) and sending it back in later in the same battle resets its Fight menu cursor to Slot 1 (verified Turn 32734).
- **Empirical Pokédex Status & Special Function**: Asher received the **PokéDex** from Professor Ivo in Azluf Town in Turn 27801 (commissioned for Asher by Jackson). In addition to standard entries, the PokéDex registers the **stats**, **abilities**, and **habitat** of caught Pokémon (verified Turn 27802).
- **Pokédex Table of Contents (Audited Turn 27859)**: Tracks `Seen` and `Owned` counts across two regional dex categories (`Colen` and `Hupest`), with 54 Hupest species and 17 Colen species pre-marked as `Seen` upon receipt.
- **In-Game Real-Time Clock**: Displayed in top-left HUD box when Start Menu is open; synchronizes with host system clock.
- **TM Reusability**: Confirmed infinite use in Pokémon Sors v1.3; TM48 (Work Up) remains in the TM Case after being taught to Sirius.

## Custom Emulator SDK & Sandbox Execution Limits
- **Script Button Accumulator Limit**: The sandbox Python environment enforces a cumulative session limit on button commands executed via Python scripts/mgba. When this limit is reached, any script attempting button commands will abort with 'Maximum cumulative limit of 100 buttons per script execution exceeded'. Controller button commands should strictly use the native press_buttons tool.
- **Tool Limitation (stun_npc)**: The `stun_npc` tool fails with 'Error: Map objects data is unavailable' on this ROM/engine build. Do not invoke `stun_npc`.
## Hupest Metro Line Transit Mechanics
- **Boarding the Train**: With the **Metro Pass** in the Key Items pocket, stepping into a station's entry turnstile lane (e.g. `17, 24` in Amor Metro Station, verified Turn 27572) prompts *"Do you want to use the Hupest Metro Line? Yes/No"*. Selecting *Yes* walks the player onto the platform into the train car (`11, 8`) with the announcement *"Please mind the closing doors!"* (verified Turn 27574).
- **Train Interior Layout (`cols 1-24, rows 4-8`, verified via `latest_grid.png` Turns 27575, 27578, 27581)**:
  - **Western Car (`cols 1-6`)**: Green door mat at `(2-4, 8)` (inert while moving); elderly man at `(1, 8)` (*"The Hupest Metro Lines are very famous for foreigners..."*, Turn 27581); Italian woman at `(3, 5)` (*"Vengo da una regione lontana! E tu?"*, Turn 27581); German man at `(4, 8)` (*"Früher waren Spiele originell!..."*, Turn 27581).
  - **West Gangway (`7-8, 7`)**: Connects Western and Middle cars along row 7; glasses passenger at `(7, 6)` (*"He's texting something on a messaging app... 'Day 69 of asking for a dating sim in sors.'"*, Turn 27576).
  - **Middle Car (`cols 9-14`)**: Green door mat at `(10-12, 8)` (arrival spawn at `11, 8`); Hungarian blonde girl at `(9, 5)` (*"Kíváncsi vagyok mikor jön ki a Pokémon Sors teljes verziója..."*, Turn 27580); passenger at `(14, 6)` refreshing a game site showing a fella in a red fedora talking to a Darkrai (Turn 27578).
  - **East Gangway (`15-16, 7`) & Eastern Car (`cols 17-22`) & Far-East Gangway (`23-24, 7`)**: Green door mat at `(18-20, 8)`; Japanese passenger in Team Siara suit at `(22, 8)` (*"Watashi wa Joto kara kimashita..."*, Turn 27578); eastern end terminates at `(24, 7)` (Turn 27579).
- **Selecting a Destination Inside the Train Car (`4, 5` Seat Trigger)**: Stepping `Left` from `(5, 5)` into the purple passenger seat at `(4, 5)` sits Asher down and prints: *"Which city do you want to go to?"* (which requires an `A`/`B` press plus `sleep 800` to open the 8-station list box: `0: Amor`, `1: Sovio`, `2: Samurion`, `3: Destino`, `4: Galinor`, `5: E.S.`, `6: Colen`, `7: Dis Bay`; verified Turn 32996). Selecting a station not yet unlocked displays *"You can't go to that city yet!"*, while selecting an unlocked station (`Amor`, `Sovio`, `Samurion` [exits to `37, 25` in Samurion City], or `Destino` [exits to `45, 14` in Destino City]) announces *"The next station is... <City>!"* and warps to `(22, 17)` on the destination station platform (`Left 3, Down 7, Right 5` exits any Metro station to the overworld; verified Turn 32996).

## Battle UI & Type Effectiveness Indicators
- **Move Box Effectiveness Highlighting**: In the CFRU battle Fight menu, the selected move's box dynamically changes color to indicate type effectiveness against the active opponent (e.g. highlights **light green** when a move is super-effective, such as Steel-type Metal Claw against Fairy-type Cleffa or Psychic/Fairy-type Ralts; verified Turn 27656).

## Eclipsing & The Eclicizer Machine
- **True Eclipsing Requirements**: Requires a worthy bloodline wielder (such as Asher or Frio), the **Eclipse Band**, and a powered **Eclite Shard** (which breaks upon a single use and permanently transforms the target Pokémon into its Eclipsed form).
- **The Eclicizer (Professor Ivo's Basement Lab in Lancio Town)**:
  1. Restores powerless **Clear Shards** into active **Eclite Shards**.
  2. Combines smaller **Eclite Pieces** into a single fully powered **Eclite Shard**.
  - Professor Ivo noted that Eclite Pieces / Clear Shards can also be obtained from the giant Eclite crystal in Upper Mt. Gerhana (`27, 14`).

## UI & Transition Timing Mechanics (Verified Turns 31758-31768)
- **Nicknaming Screen Layout & PC Transfer Dismissal (`A` Required)**:
  - **7x4 Keyboard Grid `(col, row)`**:
    - **Row 0**: `(0,0)=A/a`, `(1,0)=B/b`, `(2,0)=C/c`, `(3,0)=D/d`, `(4,0)=E/e`, `(5,0)=F/f`, `(6,0)=.`
    - **Row 1**: `(0,1)=G/g`, `(1,1)=H/h`, `(2,1)=I/i`, `(3,1)=J/j`, `(4,1)=K/k`, `(5,1)=L/l`, `(6,1)=,`
    - **Row 2**: `(0,2)=M/m`, `(1,2)=N/n`, `(2,2)=O/o`, `(3,2)=P/p`, `(4,2)=Q/q`, `(5,2)=R/r`, `(6,2)=S/s`
    - **Row 3**: `(0,3)=T/t`, `(1,3)=U/u`, `(2,3)=V/v`, `(3,3)=W/w`, `(4,3)=X/x`, `(5,3)=Y/y`, `(6,3)=Z/z`
  - **Page Flip & Two-Part PC Box Transfer**: Pressing `Select` to toggle uppercase/lowercase requires `sleep 800` before subsequent D-Pad inputs. After pressing `Start` -> `A` to confirm a nickname when the party is full, two sequential messages appear (`"<Name> was transferred to Someone's PC.▼"` followed by `"It was placed in Box 'Box2.'"`), both of which ignore `B` presses and require pressing **`A`** twice (`A, sleep 1800, A, sleep 2500`) to return to the overworld (verified Turn 32248).
- **Battle Bag Fade-In Delay (`3000ms`), Cross-Battle Cursor Memory, & Safe Switch-Decline Timing**: Pressing `A` on `Bag` during battle requires a `sleep 3000` pause for the Bag UI fade-in animation to complete before D-Pad or `A` inputs register (`2500ms` can be ~100ms too short; verified Turns 32393 & 32397). The Bag remembers both the last opened pocket and the last highlighted item row even across separate battles (verified Turn 32515). On the 2x2 battle menu, pressing `Up` when the cursor is on the top row (`Fight` or `Bag`) is a safe no-op for waiting out end-of-turn animations, and `A, sleep 2000, B, sleep 1200, B, sleep 4500` safely advances EXP text and declines the `"Will Asher change Pokémon? Yes/No"` prompt without risking opening the Party screen if a move misses or fails (verified Turns 32516-32532).
- **Side-Facing Wooden Staircase Collision (`3-Tile Tall Graphic`)**: On 3-tile tall side-facing wooden staircases (such as `25, 22-24` in Destino Mine 2F), the tile adjacent to the top railing (`24, 22`) has solid cliff collision; approach along the row aligned with the middle step (`24, 23 -> 25, 23`), which automatically steps diagonally onto the top step (`25, 22`; verified Turns 32379-32380).
- **Samurion City Pokémon Center Exit Routing**: Stepping `Down` off `(7, 8)` inside the Samurion City Pokémon Center requires `sleep 2500` for the door warp to settle at `(23, 48)`, followed by `Right 2` to `(25, 48)` -> `Down 1` to `(25, 49)` -> `Right 3` to `(28, 49)` to bypass the Pokémon Center window (`24, 47`) and southern house roof peak (`24, 50`) (verified Turns 31757-31760).