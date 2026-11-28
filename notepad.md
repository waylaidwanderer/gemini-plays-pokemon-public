<h1><code>Main</code></h1>

# Pokémon Monomyth — Main Dashboard

## Current Status
- **Game:** Pokémon Monomyth (`© 2026 TEAM MONOMYTH`) — Difficulty: `Monomyth`
- **Trainer:** Iris | **Rival/Friend:** Monty
- **Region:** Athanto
- **Progression:** Recovered **Gym Leader Bastion's `Flint & Steel`** inside **Catsear Industrial Glassworks** (also caught **`Chroma`** `Tagling` `#044` `Poison / Dark` for PC Box 1, and leveled **Seraph** to Lv10 & **Electra** to Lv6); Bastion returned to **Catsear City Gym**! Heading back across upper **Route 3** to **Catsear City** for Badge #1.
- **Badges:** 0

## Notepad Index
- [Mechanics Overview](Mechanics/Overview.md) — Verified game settings, Athanto survival/attrition & economy rules, Naming Screen grid, dialogue controls.
- [Party Roster](Party.md) — Active team types, custom natures, abilities, movesets, and matchup notes.
- [Home Town (Chamomile Town)](Locations/Home_Town.md) — Starting town notes, Iris's house, Pokémon Center/Mart, NPC gifts.
- [Routes 1 & 2 / Webbed Woods](Locations/Route_1_2_Webbed_Woods.md) — Route layout, wild encounters, trainers, items, Secret Webbed Woods Sub-Map.
- [Catsear City](Locations/Catsear_City.md) — First Gym city layout, Post Office, Pokémon Center/Mart, NPCs, Catsear Gym.
- [Route 3 & Abandoned Glass Factory](Locations/Route_3_Glass_Factory.md) — Route 3 wild encounters, trainers, items, and Glass Factory quest.
- `Scratchpad/` — Active routing, battle prep, and temporary testing notes.


<hr>

<h1><code>Locations/Catsear_City</code></h1>

# Catsear City

## Connections
- **North Connection (`(17, 0)-(20, 0)`):** Seamless transition back to **Route 2** (`(13, 44)`).
- **East Connection (`(41, 18)-(41, 19)`):** Seamless transition onto **Route 3** (`(0, 18)`) toward the **Abandoned Glass Factory** (Verified Turn 286).
- **South Connection (`(28, 41)-(30, 41)`):** Currently blocked by apple-crate workers until Badge #1 is earned.

## Key Landmarks & Buildings (Exploration In Progress)
- **Northern Boulevard (`x=17..20`):**
  - Overworld **Gulpin** at `(16, 4)` beside small pond `(12, 3)-(14, 4)`.
  - **Trash Can at `(16, 7)`:** Yielded **1x Oran Berry** (3 text boxes; collected Turn 256).
  - **Post Office (`POST` sign, door `(23, 5)`):** Custom Monomyth Friend Code & profile-sharing facility (requires obtaining a **PokéNav** first; Verified Turn 285).
  - **Town Sign at `(12, 17)`:** `-Catsear City- Raise a glass to quiet living.` (Turn 284).
  - **Willow Outside Pokémon Center `(32, 17)` (Verified Turn 270):** Reveals Catsear's **Gym Leader** is currently missing from the Gym, and **Monty** went out to **Route 3** to track the Gym Leader down! (`(27, 9)` on northern street is a regular blonde townsman.)
  - **Catsear Pokémon Center & 2F Mart:** Red-roofed building at `x=27..31, y=13..17` (door at `(29, 17)`, via eastern stairs `(32, 11)-(33, 11)`).
    - **1F NPC `(11, 13)`:** Mentions his buddy on **Route 7** loans out a **Fishing Rod** (Turn 261).
    - **2F Shopper `(1, 6)` & News Ticker:** Warn that weird guys are hanging around the **Abandoned Glass Factory** **east of Catsear City** (Turn 267).
  - **Catsear Gym (`x=17..23, y=13..17`, door `(20, 17)`, `Natu` on roof, sign `(24, 17)`):**
    - **Gym Sign `(24, 17)` (Verified Turn 273):** `Catsear City Pokémon Gym — Leader: Bastion, The Scorching Hot Craftsman!` (**Fire-type / glassblower specialist!** Critical note: `Anansi`, `Psyche`, `Demeter`, and `Electra` are all 2x weak to Fire, whereas `Seraph` resists Fire 2x and is Burn-immune; recruit a Water/Rock/Ground answer on Route 3 before the Gym battle!)
    - Stepping onto `(20, 18)` in front of the door automatically triggers `"The Gym's doors are locked..."` and pushes Iris south to `(20, 19)` (Verified Turn 272 — route along `y=19`, not `y=18`, when passing the Gym!).
  - **Trash Can at `(18, 21)`:** Empty (`"Eh, just some trash."`, Turn 272).
  - **West House `(12, 25)`:** Couple watching a TV show about `"Cosmic Pokémon"` / aliens (Turn 277).
  - **Trash Can at `(20, 36)`:** Empty (Turn 278).
  - **South-Central House `(22, 35)` (Former Glassworks Owners):** Elderly couple who owned the old glassworks on the edge of town; **Gym Leader Bastion** was Grandpa's apprentice, and their grandson `(5, 3)` confirms **Bastion goes looking for glass scrap at the old factory all the time** (Turn 279)!
  - **South-East House `(29, 35)` (Ditto Researcher):** Helmeted researcher surrounded by 4 Ditto (`"Did you know Ditto can match any other Pokémon's breeding patterns? Unfortunately, they also happen to match each other's... What am I gonna do with all these Ditto?"` — check back after badges in case he gifts a Ditto; Turn 281).
  - **Southern Exit Roadblock `(28, 41)-(30, 41)`:** Blocked by two workers with an apple crate; Old Man `(31, 37)` advises earning our first Gym Badge before taking the arduous road south past Catsear City (Turn 280).


<hr>

<h1><code>Locations/Home_Town</code></h1>

# Chamomile Town (Starting Town)

## Town Layout & Key Buildings
- **Pokémon Center & 2F Mart:** Door at `(24, 21)` (player exits to `(24, 22)`).
  - **1F:** Nurse Joy at `(7, 10)`, PC at `(10, 11)`, **Name Rater** at `(1, 14)` (talk from `(3, 14)`), **Move Relearner** at `(1, 15)` (talk from `(3, 15)`), exit mat at `(7, 15)`.
  - **2F Mezzanine (via stairs `(1, 10)->(1, 7)`):** **Poké Mart** (`(2, 5)` facing `Up`: PokéBall ¥200, Potion ¥300, Antidote ¥100, Paralyze Heal ¥250, Awakening ¥300) & Link Center! Stocked up on Turn 82 (now holding 10 PokéBalls, 8 Potions, 2 Antidotes, 1 Paralyze Heal, ¥50 left).
- **Iris's House:** Door at `(40, 21)` (exits to `(40, 22)` — 16 tiles east of Pokémon Center along `y=22`).
- **Southern Houses (`y=38`):**
  - **South-East House `(36, 38)`:** Woman `(3, 5)` taught Mom a sock-knitting pattern; Man `(6, 4)` offers an **In-Game Trade**: wants **`Cottonee`** in exchange for **`Dolleep`** (original wool/doll-sheep Fakemon — Verified Turn 150!).
  - **South-West House `(28, 38)`:** Grandma `(3, 4)` gifts **1x Potion** (`Turn 152`); child `(1, 6)` and Grandpa `(6, 4)` have flavor dialogue.
  - *(Note: Confirmed Turn 152 there is NO wild tall grass anywhere in southern Chamomile Town.)*
- **Northern Terrace & Hilltop:**
  - Stairs at `(31, 18)-(33, 18)` lead to upper terrace; NPC at `(35, 16)` gave **1x Sharp Beak** (Turn 71, boosts Flying moves).
  - Further stairs `(27, 14)-(28, 14)` and `(32, 11)` lead to **Monty's House** at `(32, 9)`.
- **Exits:**
  - **East Exit (`x > 45`):** Leads to **Webbed Woods** (toward **Catsear City**).
  - **South Exit (`(27, 43)-(28, 43)`):** Stairs lead to a secluded southern trail (`y=48`) ending at a house `(37, 46)` with a Zangoose `(39, 47)` outside (checked Turn 86–87; flavor dialogue only, dead end).
  - **West Limit:** Dead-ends at trees at `(7, 22)`.
  - **Note on Mom (`(8, 7)`):** Verified Turn 92 that Mom does *not* heal our party after starting our journey; heal at Chamomile Pokémon Center `(24, 21)`.
- **East Connection:** Leads to **Webbed Woods** clearing (wild **Spinarak** Lv2 confirmed with color/pattern variants; starter crate gave Iris **Crackliss** (`Seraph`, Fire/Poison), Willow **Marmroot** (Grass), Monty **Mishimizu** (Water, knows `Growl` & `Assist`)).
- **Lore / Quest Lead (Turns 61–65):**
  - Starter Poké Balls have **Edelweiss Labs** stamped on the bottom (located out in **Edelweiss City**).
  - Mom & Big Bro gave us early 16th birthday gifts: **Potions**, **Poké Balls**, and the **PokéDex**! (Regional Dex has >360 Pokémon: "over thirty dozen").
  - **First Gym Target:** Big Bro's friend **Bastion** is the Gym Leader in **Catsear City** (beyond **Webbed Woods**).

## Story Context & Key NPCs (Verified Turns 10–20)
- **Iris (Player):** Birthday is right around the corner; Big Bro is registering Iris's ID application with the Post Office while out at the Mart.
- **Big Bro:** Encourages Iris's goal of becoming a Pokémon Trainer; mentions Monty has been waiting outside in the heat.
- **Monty (Friend/Rival):** Left three morning voicemails (8:42 AM, 9:08 AM, 9:56 AM). Found a mysterious crate in the forest outside town that started glowing blue when he pressed the top of it; waiting outside Iris's house.

## Iris's Bedroom (2F)
- Spawned at `(4, 5)` on the bedroom rug (Turn 20).
- **PC at `(0, 5)`** (accessed from stool `(0, 6)`): Withdrew **1x Potion** from Item Storage (Turn 24; PC storage now empty).
- **Wall Clock at `(5, 1)`**: Required setting before going downstairs (`Yes/No` confirmation defaults cursor to `No`, so press `Up` then `A`; synced to 5:36 PM on Turn 28).
- **Stairs to 1F:** Green mat at `(8, 2)`, stair warp at `(7, 2)`.

## Iris's House (1F) & Outside Road
- **1F Layout:** Stairs at `(7, 2)`, Mom at `(8, 7)` in kitchen, sleeping pet Growlithe at `(2, 9)`, front door exit at `(5, 9)-(6, 9)` -> exits to town `(40, 22)`.
- **Outside Ambush & Forest Clearing (Turns 31–40):**
  - Met **Monty** outside `(40, 22)`, walked east onto adjoining map `(1, 11)`, ambushed by town bully **Willow** (green beanie, purple hair).
  - Entered forest clearing `(12, 13)`–`(13, 13)` with the glowing blue crate containing 3 Poké Balls.
  - Won Rock-Paper-Scissors with **Paper** (both Monty and Willow threw Rock!), earning first pick of the three custom Monomyth starters.




<hr>

<h1><code>Locations/Route_1_2_Webbed_Woods</code></h1>

# Routes 1 & 2 ("Forest Stroll") & Webbed Woods

## Route 1 (East of Chamomile Town)
- **West Connection:** Chamomile Town (`y=22` transitions to Route 1 `y=11..12`).
- **Signpost at `(3, 10)`:** `-Routes 1 & 2- Forest Stroll`
- **Northern Ledge `(6, 8)`:** Small decorative flower garden `(1, 5)..(4, 6)`.
- **Rival Ambush at `(2, 12)`:** Defeated **Willow** (`Marmroot` ♀ Lv5 — knew `Growl` & `Tackle`; prize `¥100`, Seraph reached Lv6) on Turn 90.
- **Trainer Tips Sign at `(17, 11)`:** Warns that Athanto has wider wilderness between towns than Kanto/Hoenn; stock Potions, Antidotes, and Revives.
- **Webbed Woods Entrance:** East warp arrow at `(20, 12)-(20, 13)` -> warps to Webbed Woods `(9, 12)`. (South side of Route 1 `(17, 15)` is blocked by trees.)

## Webbed Woods
- **West Entrance:** `(9, 12)` (returns to Route 1). Starter crate clearing at `(14, 13)`.
- **Signpost at `(16, 10)`:** `-Webbed Woods- Watch for falling arachnids`
- **Items & Trees Found:**
  - `(20, 7)` (via north-west clearing `(15, 8) -> (20, 8)`): **1x Antidote** (collected Turn 104).
  - `(19, 19)` (north-west bank of pond via south-west channel `(22, 24) -> (17, 24) -> (17, 21) -> (19, 20)`): **1x PokéBall** (collected Turn 125).
  - `(33, 22)` (east clearing below pond): **Apricorn Tree** — yielded **1x Blu. Apricorn** (collected Turn 110).
  - `(40, 5)` (north-east dead-end clearing via `(38, 14) -> (42, 14) -> (42, 7) -> (40, 6)`; yellow flower tufts break automatically when stepped on!): **1x Antidote** (collected Turn 129).
  - `(47, 24)` (south-east dead-end grass pocket via `(38, 21) -> (47, 21) -> (47, 23)`, camouflaged inside tall grass): **1x Potion** (collected Turn 132).
  - `(15, 35)` (south-west grass pocket via `(22, 42) -> (15, 42) -> (15, 36)`, exits via `(20, 36)` shortcut ledge): **1x Paralyze Heal** (collected Turn 177).
  - `(39, 48)` (deep south-east pocket via `(44, 42) -> (44, 49) -> (40, 48)`): **1x PokéBall** (collected Turn 184).
- **NPCs & Landmarks:**
  - `(34, 19)`: **Trainer Tips Sign** — `"It's against the rules to use more than four items during a battle."` (Verified Turn 127).
  - `(32, 25)`: **Youngster Jimmy** — **DEFEATED Turn 164** (`Kernut` ♂ Lv3 (`Grass`, `Bide`) + `Shope` ♀ Lv4 (Jackalope Fakemon, `Tackle`, high crit rate?)).
  - `(39, 30)-(41, 30)`: One-way shortcut ledge east of southern tall grass.
  - `(24, 34)`: **Bug Catcher Tim** — **DEFEATED Turn 175** (`Spinarak` ♀ Lv3 + `Joltik` ♀ Lv4 (`Unnerve`, `Absorb`)).
  - **Southern Loop Routing:** From `(33, 33)` go west on `y=34` past Tim `(24, 34)`, south on `x=22` to `(22, 42)`, east through grass `(25, 42)..(37, 42)` to `(44, 42)`, then north `(46, 41)..(46, 35)` to **Bug Catcher Skip** at `(49, 35)` — **DEFEATED Turn 189** (`Combee` ♂ Lv5, OHKO'd by `Ember`).
  - **East Exit Warp:** From `(46, 34)` go east to `(52, 34)`, south to `(52, 43)`, and east into `(56, 43)-(56, 44)` -> warps out to **East Route 1 `(32, 12)`**! (Note: Return shortcut goes `(46, 34) -> (46, 27) -> (40, 27)` over the `(39, 30)-(41, 30)` ledge!)
- **Wild Encounters:**
  - **Northern Webbed Woods (`(21, 13)..(28, 24)`):** **Spinarak** (`#017`, `Bug / Poison`, Lv2–3 — caught `Anansi`), **Sleepillar** (`#025`, Fakemon, `Bug / Psychic`, Lv2–3 — caught `Psyche`).
  - **Southern Webbed Woods (`(33, 26)..(47, 49)`):** **Spinarak** (Lv3), **Sleepillar** (Lv2–3), **Leonte** (Lv3 original Griffin-cub Fakemon — spotted at `(44, 47)` on Turn 184!).

## East Route 1 (Beyond Webbed Woods Exit `(32, 12)`)
- **West Warp `(32, 12)-(32, 13)`:** Re-enters Webbed Woods `(55, 43)`.
- **South Connection `(38, 32)`:** Seamless transition onto **Route 2 `(16, 0)`**.
- **Wild Encounters (`(40, 14)..(41, 29)` tall grass):**
  - **Kernut** (`#012`, Kernel Pokémon, `Grass`, Lv3, Ability `Chlorophyll`, moves `Bide` & `Growth` — caught `Demeter` Turn 196).

## Route 2 (South/East Toward Catsear City)
- **North Connection `(16, 0)`:** Connects to East Route 1 `(38, 32)`.
- **Upper & Middle Terraces:**
  - Grass `(21, 1)..(30, 4)` (below a north-to-south ledge at `(26, -1)-(27, -1)`) -> stairs `(28, 5)-(29, 5)` -> grass `(22, 7)..(29, 9)`.
  - **Lass Jane** at `(20, 11)` — **DEFEATED Turn 208** (`Caroot` ♀ Lv4 + `Shope` ♀ Lv4).
  - **Apricorn Tree** at `(15, 11)` — yielded **1x Blk. Apricorn** (Turn 209).
- **Lower Fork (via stairs `(17, 15)-(18, 15)`):**
  - **Youngster Sonny** at `(16, 22)` — **DEFEATED Turn 212** (`Leonte` ♀ Lv5 — confirmed `Flying` type, knows `Peck`!).
  - Western grass `(11, 18)..(14, 25)` contains **1x Repel** hidden in round bush `(10, 19)` (Turn 212) and **1x Burn Heal** item ball at `(10, 21)` (Turn 213). (Tip: standalone round green bushes can hold hidden items!)
  - Staircase ascending east cliff at `(22, 17)-(22, 18)`:
    - `(29, 16)`: **Apricorn Tree** — yielded **1x Pnk. Apricorn** (Turn 215).
    - `(35, 13)`: Hidden forest entrance warp into **Secret Webbed Woods Sub-Map** at `(10, 45)` (Turn 216).
  - **South Exit to Catsear City:** Paved road continues south from `(17, 18)` down stairs `(17, 32)-(18, 32)` -> west along `y=34` to `(13, 34)` -> south along `x=13..14` through `(13, 44)`, seamlessly transitioning into **Catsear City `(18, 0)`** (Turn 253).

## Secret Webbed Woods Sub-Map (Entered via Route 2 `(35, 13)`)
- **Entrance Warp `(10, 45)`:** Returns to Route 2 eastern cliff `(35, 13)`.
- **Paved Fork at `(20, 35)`:**
  - **East Branch:** Leads to `(26, 36) -> (31, 30)`, northern tall grass `(30, 20)..(33, 25)`, and south-east flower-tuft corridor `(32, 35)..(32, 49)`.
  - **West Branch (`y=35` -> `(10, 35) -> (8, 31)`):** Ends at a **Cuttable Bush at `(8, 30)`** (`"This bush looks like it can be cut down!"`, Verified Turn 241) blocking access to the upper-west pond area (`x <= 24, y <= 29`, which exits via one-way ledge `(25, 27)-(25, 29)`). Return here once HM/TM **Cut** is unlocked!
- **Items & Trees Verified:**
  - `(32, 30)`: **Apricorn Tree** — yielded **1x Ylw. Apricorn** (Turn 219).
  - `(23, 31)`: **1x Awakening** item ball (Turn 220).
  - `(32, 21)`: **1x Silver Powder** (blue-capped Battle Item ball camouflaged in tall grass; Turn 223).
  - `(31, 49)` (down south-east flower-tuft corridor `x=32, y=35..49`): **1x PokéBall** (Turn 239).
- **Wild Encounters (`(30, 20)..(33, 25)` tall grass):**
  - **Joltik** (`Bug / Electric`, Lv3 — encountered at `(31, 22)` on Turn 223).




<hr>

<h1><code>Locations/Route_3_Glass_Factory</code></h1>

# Route 3 & Abandoned Glass Factory

## Connections
- **West Connection (`(0, 18)`):** Seamless transition back to **Catsear City** (`(41, 19)`).

## Landmarks, Items, & Trainers
- **Route Signpost at `(5, 17)`:** `-Route 3- Catsear Industrial Glassworks ahead` (Verified Turn 300).
- **Apricorn Tree at `(9, 14)`:** Yielded **1x Ylw. Apricorn** (Turn 301).
- **Northern Terrace (`(11, 11)-(12, 11)` stairs):**
  - `(7, 7)`: **1x Awakening** camouflaged in tall grass `(8..11, 6..10)` (collected Turn 303).
  - `(16, 7)`: Female Trainer facing `Down` beside small pond `(14..15, 8..9)`; upper path continues east via `(16..18, 8)`.
- **Lower East Path (`y=17..19`):**
  - `(14, 18)`: **Youngster Paulie** — **DEFEATED Turn 311** (`Poliwag` ♂ Lv7 — knew `Water Gun` & `Water Sport`, swept by `Demeter` ending at `22/22` HP! Post-battle hint: `"A Poliwhirl can evolve into a bunch of different kinds of Pokémon."`).
  - **Berry Patch at `(23, 14)-(24, 14)`:** `(23, 14)` yielded **2x Oran Berries** (Turn 320); `(24, 14)` yielded **2x Cheri Berries** (Turn 319).
  - **Southern Pond `(23..25, 22..24)`:** Underwater Wooper visual at `(22, 23)`; **Item Ball at `(25, 26)`** on south bank (blocked from east by cliff along `x=32, y=22..27` — Surf-gated!).
  - **Outside Catsear Industrial Glassworks (`x >= 35`):**
    - `(35, 20)`: **Apricorn Tree** — yielded **1x Grn. Apricorn** (Turn 328).
    - `(37, 18)`: **Bug Catcher Jamie** — **DEFEATED Turn 382** (`Sleepillar` ♂ Lv5 + `Venipede` ♂ Lv6 — swept cleanly with zero damage by `Seraph`'s `Ember`).
    - `(38, 11)-(39, 11)`: Stairs connecting down from northern Route 3 path (`(18..38, 7..11)` unexplored stretch leading west to unbeaten Female Trainer at `(16, 7)`).
    - `(38, 26)-(39, 26)`: Factory sign beside twisted sculpture `(38..39, 24)` (`Catsear Industrial Glassworks`, Verified Turn 335).
    - **`(41, 26)`:** Front entrance door into **Catsear Industrial Glassworks**!
- **Wild Encounters Verified:**
  - **Venipede** (`Bug / Poison`, Lv4 — encountered at `(23, 15)` on Turn 320).
  - **Leonte** (`#015`, **Thrasher Pokémon**, **`Flying / Ground`**!! Lv4 — caught **`Athena`** at `(36, 25)` on Turn 329–331!).
- **Rival Battle — PKMN Trainer Monty at `(5, 18)` (DEFEATED Turn 297):**
  - Ambush triggers automatically when stepping past `x=5` on the western entrance road.
  - **Team (1 Pokémon):** `Mishimizu` ♂ Lv6 (`Water`, knows `Scratch`) — defeated cleanly via `Psyche` (`Struggle Bug` x2) -> `Demeter` (`Absorb` KO; `Demeter` reached Lv7 & learned `Ingrain`, `Electra` reached Lv4).

## Catsear Industrial Glassworks
- **Entrance (`(1, 24)-(2, 24)`):** Connects back to Route 3 `(41, 26)`.
- **Gym Leader Bastion at `(1, 19)` (Verified Turns 339–341, Quest Completed Turn 375):**
  - Recognizes Iris from Chamomile Town! Lost his **Flint & Steel** inside the factory and could not light the kiln in Catsear City Gym without it.
  - **COMPLETE (Turn 375):** Delivered the **Flint & Steel** from `(14, 15)` back to Bastion at `(1, 19)`; Bastion returned to **Catsear City Gym** to await Iris's challenge!
- **1F West Entrance & Kiln Area:**
  - **Encounter Mechanic (Verified Turn 345):** Entire factory interior floor (including plain grey brick tiles!) has cave-style wild encounters, not just mossy/weed patches.
  - **Wild Encounters Verified:**
    - **Slugma** (`Fire`, Lv6 — encountered at `(8, 17)` on Turn 345).
    - **Tagling** (`#044`, **Infraction Pokémon**, **`Poison / Dark`**!! Lv6 — encountered at `(11, 7)` on Turn 349 & caught **`Chroma`** on Turn 356; knows `Acid` and `Gastro Acid`; PokéDex notes they are companions to thugs/hoodlums).
  - `(2, 14..18)`: Ladder climbing north brick wall behind Bastion onto elevated upper catwalk `(0..4, 6..14)`.
  - **Upper North Catwalk (`y=6..9`, Verified Turns 348–368):**
    - `(6..7, 7..8)` & `(13..14, 7..8)`: Giant ventilation fans; walkable path passes behind them along `y=6` (`(4, 6) -> (16, 6)`), then descends ladder `(17, 7..13)` to mid-terrace (broken ladder `(15, 13..14)` is impassable).
    - Mid-terrace leads east `(18, 12) -> (24, 13) -> (28, 10)` (north side `(21..28, 8)` ends at north brick wall with `"CLEFF"` mural at `(23..24, 4..6)`, confirming eastern section `x >= 35` / `(38, 24)` doorway is entered externally) to downward ladder `(29, 10..15)` onto lower east floor.
    - Lower floor loops south around furnace `(26..27, 22)` along `y=24` (`(29, 24) -> (23, 24)`), north under the overhead pipe `(23, 21..17)`, and west to **`(14, 15)` Purple Item Ball = `Flint & Steel` (Key Item — COLLECTED Turn 371!)**.
  - `(6..7, 10..12)` & `(10..11, 10..12)`: Two unlit glass-blowing furnaces; cyan spiral graffiti tag at `(14, 10..11)` and purple-capped Item Ball visible on east terrace at `(14, 15)`.



<hr>

<h1><code>Mechanics/Overview</code></h1>

# Mechanics & System Overview — Pokémon Monomyth

## Region & Core Design Pointers (Verified Turns 6–7, New Game Pointers)
- **Region Name:** **Athanto**.
- **Built-in Pokémon Center Mega-Hubs (Verified Turns 55, 77–80):**
  - **1F (`y=8..15`):** Nurse Joy `(7, 10)` across counter `(7, 11)` (**player stands at `(7, 12)`**; requires **4** `A` presses — `["A", "sleep 2400", "A", "sleep 2200", "A", "sleep 2200", "A", "sleep 5500", "B", "sleep 1800", "B", "sleep 1500"]` — because `A #1` opens `"Hello..."`, `A #2` opens `"We restore..."`, `A #3` opens `"Would you like to rest...? > Yes"`, and **`A #4` confirms `Yes`**, Verified Turn 300 `filmstrip_3.png`! Always verify dismissal by stepping to `y >= 13`!), PC `(10, 11)`, **Name Rater** `(1, 14)` (from `(3, 14)`), and **free Move Relearner** `(1, 15)` (from `(3, 15)` — opens a custom `< Pokémon >` browser where `Left`/`Right` cycles directly through every party member's relearnable move list, Verified Turn 263).
  - **2F Seamless Mezzanine (`y=0..7`, via left stairs `(1, 10)->(1, 7)`):** **Poké Mart** counter (`(2, 5)-(3, 5)` facing `Up`) and **Link Center**!
- **Stair Movement Timing (Verified Turns 76, 79):** Stair tiles animate slower than flat ground, causing rapid unspaced button lists (`["Up"] * N`) to drop steps on staircases. Always use a `while` loop checking `mgba.get_coordinates()` (or `"hold <Dir> <ms>"`) when climbing/descending stairs.
- **Menu/Dialogue Dismissal Guard & Bounded Loops in `run_code` (Verified Turns 78–79, 83, 94–95):**
  - **NEVER write unbounded `while` loops** in `run_code` (caused a 120s timeout on Turn 94 when Nurse Joy's closing box stayed open at `(7, 12)`). Always use bounded `for _ in range(N):` loops and break immediately when `npos == pos` (which also cleanly halts on wild encounters!).
  - Before chaining overworld walking after menus/NPCs, loop `["B", "sleep 800", "<FirstStepDir>"]` (up to 4–5 iterations) until `mgba.get_coordinates()` confirms a 1-tile delta from the starting tile.
- **Pause Menu Cursor Memory & 2-Column Layout (Verified Turns 93, 116–118):**
  - `PAUSE` remembers the last selected icon rather than resetting to top-left `(0,0)`. Always check `PAUSE` visually before pressing `A`.
  - Left column (3 items): `(0,0) PokéDex`, `(1,0) Pokémon`, `(2,0) Bag`.
  - Right column (4 items): `(0,1) <PlayerName>` (Trainer Card), `(1,1) Save`, `(2,1) Options`, `(3,1) Exit`. Pressing `Left` from `(0,1) <PlayerName>` lands on `(0,0) PokéDex`; pressing `Down` on `(2,0) Bag` wraps directly to `(0,1) <PlayerName>`!
- **Verified Wild Flee (`Run`) Timing Macro (Turns 182–184):** From overworld encounter trigger (`npos == pos`), use `["sleep 3500", "B", "sleep 2800", "Down", "Right", "sleep 250", "A", "sleep 1800", "B", "sleep 2200"]` (`"sleep 2200"` after the 1st `B` was too short for the send-out animation; `"sleep 2800"` reliably opens `What will <X> do?` before `Down, Right`).
  - Inside **Party Menu** (`Pokémon`), the 6 party plates form a **3x2 grid**: `(0,0) Slot 0 | (0,1) Slot 1`, `(1,0) Slot 2 | (1,1) Slot 3`, `(2,0) Slot 4 | (2,1) Slot 5` (`Down` from Slot 0 highlights Slot 2; `Right` highlights Slot 1 — Verified Turn 248).
  - Inside **Pokémon Summary**, `Left`/`Right` flips across 5 Summary pages (`1: Info`, `2: Stats & Ability`, `3: Battle Moves`, `4: Contest Moves`, `5: Ribbons`) and `Up`/`Down` switches between party Pokémon linearly (`0 -> 1 -> 2 -> 3 -> 4 -> 5`). Exiting from Summary all the way back to the overworld requires **4** `B` presses (`Summary -> Sub-menu -> Party -> PAUSE -> Overworld`), and exiting Overworld `Bag` after healing also requires **4** `B` presses (`Heal text -> Party target -> Bag -> PAUSE -> Overworld`).
- **Map Transition Detection & `latest_grid.png` Availability (Verified Turns 154–155, 167):**
  - Detect east/south warps by checking for a coordinate drop (`npos["x"] < pos["x"]`), never `pos["x"] == 9` alone.
  - `screenshots/latest_grid.png` is ONLY written when the settled screen is in the overworld; omit batch-reading `latest_grid.png` whenever a script might stop inside a battle or menu.
- **Gen 6+ Critical Hit Multiplier (`1.5x`) & Active Battle Slot-0 Reordering (Verified Turns 141, 144–145):**
  - Critical hits (`"Bullseye! Critical hit!"`) deal **1.5x** damage. Inside battle, replacing a fainted Pokémon moves the newly active Pokémon into **Slot 0 (top-left)** of `Use on which Pokémon?` for the remainder of that battle, while overworld Party order resets afterward.
- **Item Ball, Blue Item Ball, Hidden Bush, & Apricorn Tree Pickups (Verified Turns 125, 209, 212, 223):**
  - Ground **Item Balls** display **2** text boxes (`"<Player> found one <Item>!"` -> `"<Player> put away..."`). **Blue-capped Item Balls** hold Battle/Held Items (e.g. `Silver Powder` at Secret Webbed Woods `(32, 21)`, Turn 223), and **Purple-capped Item Balls** hold Key Items (e.g. `Flint & Steel` at Catsear Industrial Glassworks `(14, 15)`, Turn 371).
  - Standalone **round green bushes** can hold hidden items when interacted with `A` (e.g. `1x Repel` at Route 2 `(10, 19)`, Turn 212).
  - **Apricorn Trees** display **4** text boxes (`"It's an Apricorn Tree..."` -> `"Hey! There's an Apricorn growing!"` -> `"<Player> found one <Apricorn>!"` -> `"<Player> put away..."`).
  - **Berry Trees (Verified Turn 319):** Require **3 `A` presses** followed by **3 `B` presses** (`["A", "sleep 2000", "A", "sleep 1800", "A", "sleep 2000", "B", "sleep 1800", "B", "sleep 1800", "B", "sleep 1200"]`), because box 2 is `"Do you want to pick the <X> Berries? > Yes / No"` (pressing `B` declines picking!) and box 5 is `"The soil returned to its soft and loamy state."` Never run a multi-step `["B", "<Dir>"]` dismissal loop onto a **tall grass** tile, since a wild encounter keeps coordinates unchanged.
- **Forest Tree Collision Footprint (Verified Turn 123):** Large forest trees occupy a 2-row collision base; always route along clear grass/dirt channels in `latest_grid.png` rather than stepping into tree-trunk shadow tiles.
- **Wilderness & Attrition:** Wilderness between settlements is much wider than in mainline games, testing both battle skill and attrition (HP/PP endurance).
- **Economy & Blackout Rule (Verified Turns 6–7, 146):** **Blacking out in the wild/trainer battle deducts 50% of current cash** (`¥150 -> lost ¥75` on Turn 146) and respawns you with full HP/PP (outside Iris's House `(40, 22)` in Chamomile Town). Money already spent on items is 100% safe—always spend spare cash before leaving civilization.
- **Soft Level Caps / Staged EXP:** Experience gain slows down in stages based on progression, steering teams toward the intended level range rather than over-leveling via raw stat disparities. Build a full balanced team and use strategy/synergy rather than solo-grinding.
  - **Built-in Party-Wide EXP Share & Capture EXP (Verified Turn 107):** Every battle and wild capture awards EXP to the entire party automatically (`"Everybody got their fair share!"`), including catching wild Pokémon!
- **Shared Bag Pocket Memory & 3x2 Item Sub-Menu (Verified Turns 105, 199, 246):**
  - Overworld Bag and Battle Bag share a **single global** last-pocket pointer (`1:Items, 2:Medicine, 3:PokéBalls, 4:Battle Items, 5:TMs & HMs, 6:Berries, 7:?, 8:Key Items`). Switching to `PokéBalls` in battle causes Overworld Bag to open on `PokéBalls` next time.
  - Selecting an item in the Overworld Bag opens a **3x2 sub-menu**: `(0,0) Use | (0,1) Register`, `(1,0) Toss | (1,1) Give`, `(2,0) Free Space | (2,1) Cancel`. Equipping a Held Item requires `Right, Down, A` (`Give`), NOT `A` (`Use`), and returning to the overworld after `"<Pokémon> was given the <Item> to hold."` takes **3** `B` presses (`Give text -> Bag -> PAUSE -> Overworld`, Verified Turn 249 — vs **4** `B` presses after using a Potion).
- **Individual Visual Uniqueness:** Every individual Pokémon has unique color and pattern variations (controlled by `Color Variants` in Options).

## Verified Game Settings (Turn 4, Options Menu)
- **ROM Hack:** Pokémon Monomyth (`© 2026 TEAM MONOMYTH`).
- **AI Difficulty:** Default is `Monomyth` ("The intended Monomyth experience. Slightly harder than mainline games." / "Monomyth difficulty remains the official recommended experience."). Alternative option is `Heroic` (does not alter opponent stats, only makes AI switch more often and play competitively; can downgrade Heroic -> Monomyth anytime, cannot upgrade mid-run). Selected `Monomyth` on Turn 9.
- **Color Variants:** Default `On` ("Pokémon colors change somewhat depending on the individual."). Note: Subtle palette/pattern differences between individuals are normal and do not necessarily indicate a Shiny Pokémon.
- **Text Speed:** No Text Speed setting exists in Options (built-in fast/fixed speed).
- **Animations & Audio:** `Battle Anims: On`, `Pokémon Anims: On`, `Bicycle Music: Off`, `Surf Music: Off`, `Dex Units: Imperial`, `Button Mode: Normal`.

## UI & Controls Verified Mechanics
- **Safe Dialogue Advance (`B` button, Verified Turns 11, 32):** Pressing `B` with `~1400ms` sleep advances standard dialogue boxes and stops safely without confirming choice prompts (e.g. Rock-Paper-Scissors, Starter Choice). **Caveat (Turn 32):** If a Naming Screen opens with a pre-filled default name (e.g. `Monty`, `Willow`), trailing `B` presses act as Backspace and erase letters from the default name. Keep `B` batches moderate when approaching potential character/Pokemon naming screens.
- **`Yes/No` Initial Cursor Position (Verified Turn 27):** Not all `Yes/No` boxes start with the cursor on `Yes` (e.g., the bedroom clock prompt starts on `No`). Always check the cursor arrow visually before confirming.
- **Original Fakemon Dex (Verified Turn 41):** Pokémon Monomyth features original Fakemon species! Never assume types, stats, abilities, or learnsets—always verify via the in-game Summary screen and battle text.
  - **Starter Trio (Forest Crate, Turn 41):**
    - Left Ball: **Marmroot** (Groundhog Pokémon)
    - Middle Ball: **Crackliss** (Crackling Pokémon)
    - Right Ball: **Mishimizu** (Rookie Pokémon — blue underwater-panther cub with fish tail)
- **Naming Screen Grid (Verified Turn 14):**
  - Starts on `(0,0) = 'A'` in UPPERCASE. Typing the 1st character **automatically switches** the keyboard to lowercase (`SELECT` then switches to `Accent`, so do NOT press `SELECT` after letter 1).
  - Contiguous letter coordinates `(row, col)` with NO gap between col 2 and col 3:
    - Row 0: `(0,0)a (0,1)b (0,2)c (0,3)d (0,4)e (0,5)f`
    - Row 1: `(1,0)g (1,1)h (1,2)i (1,3)j (1,4)k (1,5)l`
    - Row 2: `(2,0)m (2,1)n (2,2)o (2,3)p (2,4)q (2,5)r (2,6)s`
    - Row 3: `(3,0)t (3,1)u (3,2)v (3,3)w (3,4)x (3,5)y (3,6)z`
  - Pressing `Start` jumps cursor directly to `OK`, and `A` opens an **in-screen confirmation prompt** (`"Are you sure you want the name <X>? > Yes / No"` — Verified Turn 58). You MUST press a **second `A`** (`["Start", "sleep 400", "A", "sleep 1200", "A", "sleep 1500"]`) to confirm `Yes` and exit the Naming Screen before sending any `B` dialogue-advance inputs! When your 6-slot party is full, `"<Name> was transferred to the PC Box Server."` -> `"It was placed in Box \"Box 1.\""` renders on top of the Naming Screen where **`B` is ignored** (`Turn 361`) — use **`A`** (`["A", "sleep 1800", "A", "sleep 3500"]`) to dismiss the PC Box transfer text back to the overworld!
  - **Safe Pathing Rule on Naming Grid:** Rows 0–1 only have letters in cols `0..5` whereas Rows 2–3 have letters in cols `0..6`. Always move **Left BEFORE Up/Down**, and **Up/Down BEFORE Right**, so the cursor never passes through unmapped cell `(0,6)` or `(1,6)`.
- **Filmstrip Pagination on Animated UIs (Verified Turns 14, 17, 51):** Screens with continuously pulsing cursors, scrolling Pokémon Center news tickers, or sleeping `Zzz` animations generate ~42 `[THINKING]` frames before inputs run, pushing the actual button-press frames into `filmstrip_2.png`+. Check `filmstripParts` in `<TurnVisualTimeline>` and read `filmstrip_2.png`+ directly when background animations are active.
- **Built-In `Set` Battle Style (Verified Turn 138):** Trainer battles automatically send in the opponent's next Pokémon without a `"Will <Player> change Pokémon?"` switch prompt (`Set` mode is always enforced).
- **Trainer Battle Single-Round Protocol (`Bide` Hazard, Verified Turn 135):** Early trainers carry punishment moves like **`Bide`** (e.g., Youngster Jimmy's `Kernut` Lv3). **NEVER** queue multiple attack rounds blindly in a Trainer battle—execute **1 battle round per turn** so you can read the foe's move (`"storing energy!"`) and either KO before unleash or use status/healing turns instead of feeding `Bide` double damage!
- **Battle Item Limit — Max 4 Items Per Battle (Verified Turn 127, Webbed Woods Sign `(34, 19)`):** `"Trainer Tips: It's against the rules to use more than four items during a battle."` You cannot stall indefinitely with healing items—plan switches, status cures, and healing turns within a strict 4-item budget per battle!
- **Battle Round Timing & Cursor Safety (Verified Turns 48–50, 121):**
  - With `Battle Anims: On`, even a Single Battle round with `Wrap` + stat-drop animations (`String Shot` / `Struggle Bug`) takes ~10–12s (`["sleep 3000", "B", "sleep 2500", "B", "sleep 2500", "B", "sleep 2500", "B", "sleep 2000"]`), and a 4-Pokémon Double/Multi-Battle round takes ~12–15s.
  - **Warning:** Sending directional inputs (`Up`/`Down`/`Left`/`Right`) before the previous round's end-of-turn animations finish will move the `Fight / Bag / Pokémon / Run` cursor! Whenever spamming a repeatable attack, move selection once to the top-left move slot (`Fight -> Slot 0`) and use ONLY `A`/`B` on subsequent rounds so the cursor can never drift onto `Bag` or `Run`.
  - **Move Menu Cursor Memory (Verified Turns 225, 308):** At the start of every new battle, each Pokémon's `Fight` move cursor resets to **`(0, 0)` (Slot 0)**, and then remembers the last move selected for the remainder of that battle.
  - **Battle Menu Cursor After Throwing a PokéBall (Verified Turns 229, 354):** If a thrown PokéBall breaks open, `"What will <Lead> do?"` keeps the cursor on **`> Bag` `(0, 1)`** (and `Bag` stays on `PokéBalls -> > PokéBall`). Press `Left` to return to `Fight`, or throw another Ball directly with `["A", "sleep 900", "A", "sleep 600", "A", "sleep 10000"]` (`A #1` opens Bag, `A #2` opens `Use/Cancel`, `A #3` confirms `Use`; note `"sleep <ms>"` max is `10000` per entry).
  - **Safe Post-Capture & Post-KO Level-Up Progression (Verified Turns 107, 197, 230, 314):** Never press `B` after throwing a PokéBall or when a party member might evolve. However, keep `A` batches to **2–3 presses max** whenever a 4-move-slot Pokémon (`Seraph`, `Anansi`, `Demeter`) levels up, because 5+ `A` presses will automatically confirm `Delete a move? > Yes -> Slot 0` (`Turn 314`). (Any overwritten level-up move can be freely restored at any Pokémon Center 1F Move Relearner.)





<hr>

<h1><code>Party</code></h1>

# Active Party Roster — Pokémon Monomyth

## 1. Seraph — Crackliss (♂) — Starter (#004)
- **Nickname:** `Seraph` (Hebrew *śārāf* = "burning serpent"; nicknamed at Chamomile Town Name Rater on Turn 58)
- **Type:** `Fire / Poison` (Verified Turn 53 Summary)
  - **Immunities:** Burn, Poison / Badly Poisoned, Poison Powder
  - **4x Resistances:** Grass, Bug, Fairy
  - **2x Resistances:** Fire, Ice, Fighting, Poison, Steel
  - **Weaknesses:** **4x Ground**, 2x Water, 2x Rock, 2x Psychic
- **Nature:** `Pompous` (`+SpA` or `+Spe` — Verified Turn 357 Lv10 `+2 SpA, +2 Spe` gain!)
- **Ability:** `Blaze` (Ups Fire moves by 50% at or below 1/3rd HP)
- **Stats (Lv10, Turn 358):** HP 31/31 | Atk 15 | Def 17 | SpA 18 | SpD 17 | Spe 21
- **Current Moves (FULL 4 SLOTS):**
  - `Constrict` (Normal, 35 PP — lowers foe Speed)
  - `Leer` (Normal, 30 PP — lowers foe Defense)
  - `Wrap` (Normal, 20 PP)
  - `Ember` (Fire, Special, 25 PP — learned Lv8 on Turn 180!)

## 2. Anansi — Spinarak (♂) — (#017)
- **Nickname:** `Anansi` (West African spider trickster god of stories; caught Lv2 in Webbed Woods on Turn 106–108)
- **Type:** `Bug / Poison` (Verified Turn 118 Summary)
- **Nature:** `Furtive` (`+Atk` — Verified Turn 206 Lv6 stat gains!)
- **Ability:** `Swarm` (Ups Bug moves by 50% at or below 1/3rd HP)
- **Stats (Lv7, Turn 312):** HP 23/23 | Atk 14 | Def 11 | SpA 12 | SpD 12 | Spe 11
- **Current Moves (FULL 4 SLOTS):**
  - `Constrict` (Normal, 35 PP)
  - `String Shot` (Bug, 40 PP)
  - `Poison Sting` (Poison, 35 PP — learned Lv3)
  - `Absorb` (Grass, 25 PP — learned Lv5 on Turn 175!)

## 3. Psyche — Sleepillar (♀) — (#025, Original Fakemon)
- **Nickname:** `Psyche` (Greek soul/butterfly goddess; caught Lv2 in Webbed Woods on Turn 114–116)
- **Type:** `Bug / Psychic` (Verified Turn 118 Summary)
- **Nature:** `Insane` (`+SpA, -Atk` — Verified Turn 160 Lv4 stat gains!)
- **Ability:** `Symbiosis` (Passes its item to an ally after it uses one)
- **Held Item:** `Silver Powder` (+20% Bug-type move power; equipped Turn 249)
- **Stats (Lv7, Turn 313):** HP 23/23 | Atk 8 | Def 11 | SpA 14 | SpD 10 | Spe 11
- **Current Moves:**
  - `Struggle Bug` (Bug, Special, 20 PP — damages & lowers foe Sp. Atk)
  - `String Shot` (Bug, Status, 40 PP — lowers foe Speed)
  - `Rest` (Psychic, Status, learned Lv7 on Turn 313 — full HP heal bypassing the 4-item battle limit!)

## 4. Demeter — Kernut (♀) — (#012, Original Fakemon)
- **Nickname:** `Demeter` (Greek goddess of grain, seeds & harvest; caught Lv3 on East Route 1 on Turn 196–198)
- **Type:** `Grass` (Verified Turn 197 PokéDex — "Kernel Pokémon")
- **Nature:** `Narrow-minded` (`+Def, -Atk` — Verified Turn 296 Lv7 `+2 Def` gain!)
- **Ability:** `Chlorophyll` (Doubles Speed in sunshine — great synergy with Fire-types!)
- **Stats (Lv8, Turn 313):** HP 23/23 | Atk 7 | Def 14 | SpA 10 | SpD 13 | Spe 10
- **Current Moves (FULL 4 SLOTS):**
  - `GrassWhistle` (Grass, Status, 15 PP — puts foe to Sleep! Learned Lv8 on Turn 314 over `Bide`; great for wild captures!)
  - `Growth` (Normal, 20 PP — raises Atk & SpA)
  - `Absorb` (Grass, Special, learned Lv4 on Turn 208!)
  - `Ingrain` (Grass, Status, learned Lv6 on Turn 296 — passive HP recovery every turn!)

## 5. Electra — Joltik (♀) — (#019)
- **Nickname:** `Electra` (Greek myth *Ēlektra* = "shining/amber", root of electricity; caught Lv3 in Secret Webbed Woods Sub-Map on Turn 230–232)
- **Type:** `Bug / Electric` (Verified Turn 231 PokéDex & Turn 235 Summary)
- **Nature:** `Gracious` (`+SpD` — Verified Turn 315 Lv5 `+2 Sp. Def` gain!)
- **Ability:** `Unnerve` (Prevents opposing Pokémon from eating held Berries!)
- **Stats (Lv6, Turn 359):** HP 22/22 | Atk 10 | Def 11 | SpA 11 | SpD 12 | Spe 12
- **Current Moves:**
  - `Absorb` (Grass, Special, 25 PP)
  - `String Shot` (Bug, Status, 40 PP)
  - `ThunderShock` (Electric, Special, learned Lv5 on Turn 315!)

## 6. Athena — Leonte (♀) — (#015, Original Fakemon)
- **Nickname:** `Athena` (Greek goddess of wisdom & tactical warfare; caught Lv4 on Route 3 outside Catsear Industrial Glassworks on Turn 329–331)
- **Type:** `Flying / Ground` (Verified Turn 330 PokéDex "Thrasher Pokémon" & Turn 335 Summary)
  - **Immunities:** Ground (covers `Seraph`'s 4x Ground weakness!), Electric
  - **Resistances:** Fighting, Poison, Bug
  - **Weaknesses:** **4x Ice**, 2x Water
- **Nature:** `Uncaring` (`+Def` — Verified Turn 383 Lv5 `+2 Def` gain!)
- **Ability:** `Quick Feet` (Boosts Speed by 50% if affected by a status condition; ignores Paralysis Speed drop!)
- **Held Item:** `Sharp Beak` (+20% Flying-type move power; equipped Turn 333)
- **Stats (Lv5, Turn 383):** HP 21/21 | Atk 9 | Def 11 | SpA 11 | SpD 11 | Spe 9
- **Current Moves:**
  - `Peck` (Flying, Physical, 35 PP — boosted by STAB + `Sharp Beak`)
  - `Sand Attack` (Ground, Status, 15 PP — lowers foe Accuracy)
  - `Foresight` (Normal, Status, 40 PP — enables Normal/Fighting hits on Ghost & ignores evasion)

---

## Boxed Pokémon (PC Box Server)
- **Chroma — Tagling (♀, Lv6, `#044` Infraction Pokémon):** **`Poison / Dark`** (caught at Catsear Industrial Glassworks `(11, 7)` on Turn 356–360; only weak to Ground, immune to Psychic; observed moves: `Acid`, `Gastro Acid`).





<hr>