<h1><code>Main</code></h1>

# Pokémon Monomyth — Main Dashboard

## Current Status
- **Game:** Pokémon Monomyth (`© 2026 TEAM MONOMYTH`) — Difficulty: `Monomyth`
- **Trainer:** Iris | **Rival/Friend:** Monty
- **Region:** Athanto
- **Progression:** Defeated Rival **Willow** on Route 1 (Turn 90); exploring **Webbed Woods** with 3 party members (**Seraph** `Crackliss` Lv7, **Anansi** `Spinarak` Lv3, **Psyche** `Sleepillar` Lv2) en route to **Catsear City** (Gym Leader: **Bastion**).
- **Badges:** 0

## Notepad Index
- [Mechanics Overview](Mechanics/Overview.md) — Verified game settings, Athanto survival/attrition & economy rules, Naming Screen grid, dialogue controls.
- [Party Roster](Party.md) — Active team types, custom natures, abilities, movesets, and matchup notes.
- [Home Town (Chamomile Town)](Locations/Home_Town.md) — Starting town notes, Iris's house, Pokémon Center/Mart, NPC gifts.
- [Routes 1 & 2 / Webbed Woods](Locations/Route_1_2_Webbed_Woods.md) — Route layout, wild encounters, trainers, items.
- `Scratchpad/` — Active routing, battle prep, and temporary testing notes.


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
- **NPCs & Landmarks:**
  - `(34, 19)`: **Trainer Tips Sign** — `"It's against the rules to use more than four items during a battle."` (Verified Turn 127).
  - `(32, 25)`: **Youngster Jimmy** — **DEFEATED Turn 164** (`Kernut` ♂ Lv3 (`Grass`, `Bide`) + `Shope` ♀ Lv4 (Jackalope Fakemon, `Tackle`, high crit rate?)).
- **Wild Encounters (`(21, 13)..(28, 24)` tall grass):**
  - **Spinarak** (`#017`, `Bug / Poison`, Lv2 — caught `Anansi` Turn 106).
  - **Sleepillar** (`#025`, original Fakemon, `Bug / Psychic`, Lv2, knows `Struggle Bug` — caught `Psyche` Turn 114).




<hr>

<h1><code>Mechanics/Overview</code></h1>

# Mechanics & System Overview — Pokémon Monomyth

## Region & Core Design Pointers (Verified Turns 6–7, New Game Pointers)
- **Region Name:** **Athanto**.
- **Built-in Pokémon Center Mega-Hubs (Verified Turns 55, 77–80):**
  - **1F (`y=8..15`):** Nurse Joy `(7, 10)` across counter `(7, 11)` (**player stands at `(7, 12)`**; verify dismissal by stepping to `y >= 13`!), PC `(10, 11)`, **Name Rater** `(1, 14)` (from `(3, 14)`), and **free Move Relearner** `(1, 15)` (from `(3, 15)`).
  - **2F Seamless Mezzanine (`y=0..7`, via left stairs `(1, 10)->(1, 7)`):** **Poké Mart** counter (`(2, 5)-(3, 5)` facing `Up`) and **Link Center**!
- **Stair Movement Timing (Verified Turns 76, 79):** Stair tiles animate slower than flat ground, causing rapid unspaced button lists (`["Up"] * N`) to drop steps on staircases. Always use a `while` loop checking `mgba.get_coordinates()` (or `"hold <Dir> <ms>"`) when climbing/descending stairs.
- **Menu/Dialogue Dismissal Guard & Bounded Loops in `run_code` (Verified Turns 78–79, 83, 94–95):**
  - **NEVER write unbounded `while` loops** in `run_code` (caused a 120s timeout on Turn 94 when Nurse Joy's closing box stayed open at `(7, 12)`). Always use bounded `for _ in range(N):` loops and break immediately when `npos == pos` (which also cleanly halts on wild encounters!).
  - Before chaining overworld walking after menus/NPCs, loop `["B", "sleep 800", "<FirstStepDir>"]` (up to 4–5 iterations) until `mgba.get_coordinates()` confirms a 1-tile delta from the starting tile.
- **Pause Menu Cursor Memory & 2-Column Layout (Verified Turns 93, 116–118):**
  - `PAUSE` remembers the last selected icon rather than resetting to top-left `(0,0)`. Always check `PAUSE` visually before pressing `A`.
  - Left column (3 items): `(0,0) PokéDex`, `(1,0) Pokémon`, `(2,0) Bag`.
  - Right column (4 items): `(0,1) <PlayerName>` (Trainer Card), `(1,1) Save`, `(2,1) Options`, `(3,1) Exit`. Pressing `Left` from `(0,1) <PlayerName>` lands on `(0,0) PokéDex`.
  - Inside **Pokémon Summary**, `Left`/`Right` flips across 5 Summary pages (`1: Info`, `2: Stats & Ability`, `3: Battle Moves`, `4: Contest Moves`, `5: Ribbons`) and `Up`/`Down` switches between party Pokémon on the same page. Exiting from Summary all the way back to the overworld requires **4** `B` presses (`Summary -> Sub-menu -> Party -> PAUSE -> Overworld`).
- **Item Ball / Apricorn Pickup Boxes (Verified Turn 125):** Overworld item pickups display **2** sequential text boxes (`"<Player> found one <Item>!"` with fanfare `~1800ms`, then `"<Player> put away the <Item> in the <Pocket>."`). Always press `B` **twice** (`["A", "sleep 2000", "B", "sleep 1200", "B", "sleep 800"]`) before attempting overworld movement.
- **Forest Tree Collision Footprint (Verified Turn 123):** Large forest trees occupy a 2-row collision base; always route along clear grass/dirt channels in `latest_grid.png` rather than stepping into tree-trunk shadow tiles.
- **Wilderness & Attrition:** Wilderness between settlements is much wider than in mainline games, testing both battle skill and attrition (HP/PP endurance).
- **Economy & Blackout Rule (Verified Turns 6–7, 146):** **Blacking out in the wild/trainer battle deducts 50% of current cash** (`¥150 -> lost ¥75` on Turn 146) and respawns you with full HP/PP (outside Iris's House `(40, 22)` in Chamomile Town). Money already spent on items is 100% safe—always spend spare cash before leaving civilization.
- **Soft Level Caps / Staged EXP:** Experience gain slows down in stages based on progression, steering teams toward the intended level range rather than over-leveling via raw stat disparities. Build a full balanced team and use strategy/synergy rather than solo-grinding.
  - **Built-in Party-Wide EXP Share & Capture EXP (Verified Turn 107):** Every battle and wild capture awards EXP to the entire party automatically (`"Everybody got their fair share!"`), including catching wild Pokémon!
- **Bag Pocket Memory (Verified Turn 105):** Both the Overworld Bag and Battle Bag remember the last viewed pocket across opens. Pocket order (8 pockets): `1:Items, 2:Medicine, 3:PokéBalls, 4:Battle Items, 5:TMs & HMs, 6:Berries, 7:?, 8:Key Items`.
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
  - Pressing `Start` jumps cursor directly to `OK`, and `A` opens an **in-screen confirmation prompt** (`"Are you sure you want the name <X>? > Yes / No"` — Verified Turn 58). You MUST press a **second `A`** (`["Start", "sleep 400", "A", "sleep 1200", "A", "sleep 1500"]`) to confirm `Yes` and exit the Naming Screen before sending any `B` dialogue-advance inputs!
  - **Safe Pathing Rule on Naming Grid:** Rows 0–1 only have letters in cols `0..5` whereas Rows 2–3 have letters in cols `0..6`. Always move **Left BEFORE Up/Down**, and **Up/Down BEFORE Right**, so the cursor never passes through unmapped cell `(0,6)` or `(1,6)`.
- **Filmstrip Pagination on Animated UIs (Verified Turns 14, 17, 51):** Screens with continuously pulsing cursors, scrolling Pokémon Center news tickers, or sleeping `Zzz` animations generate ~42 `[THINKING]` frames before inputs run, pushing the actual button-press frames into `filmstrip_2.png`+. Check `filmstripParts` in `<TurnVisualTimeline>` and read `filmstrip_2.png`+ directly when background animations are active.
- **Built-In `Set` Battle Style (Verified Turn 138):** Trainer battles automatically send in the opponent's next Pokémon without a `"Will <Player> change Pokémon?"` switch prompt (`Set` mode is always enforced).
- **Trainer Battle Single-Round Protocol (`Bide` Hazard, Verified Turn 135):** Early trainers carry punishment moves like **`Bide`** (e.g., Youngster Jimmy's `Kernut` Lv3). **NEVER** queue multiple attack rounds blindly in a Trainer battle—execute **1 battle round per turn** so you can read the foe's move (`"storing energy!"`) and either KO before unleash or use status/healing turns instead of feeding `Bide` double damage!
- **Battle Item Limit — Max 4 Items Per Battle (Verified Turn 127, Webbed Woods Sign `(34, 19)`):** `"Trainer Tips: It's against the rules to use more than four items during a battle."` You cannot stall indefinitely with healing items—plan switches, status cures, and healing turns within a strict 4-item budget per battle!
- **Battle Round Timing & Cursor Safety (Verified Turns 48–50, 121):**
  - With `Battle Anims: On`, even a Single Battle round with `Wrap` + stat-drop animations (`String Shot` / `Struggle Bug`) takes ~10–12s (`["sleep 3000", "B", "sleep 2500", "B", "sleep 2500", "B", "sleep 2500", "B", "sleep 2000"]`), and a 4-Pokémon Double/Multi-Battle round takes ~12–15s.
  - **Warning:** Sending directional inputs (`Up`/`Down`/`Left`/`Right`) before the previous round's end-of-turn animations finish will move the `Fight / Bag / Pokémon / Run` cursor! Whenever spamming a repeatable attack, move selection once to the top-left move slot (`Fight -> Slot 0`) and use ONLY `A`/`B` on subsequent rounds so the cursor can never drift onto `Bag` or `Run`.





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
- **Nature:** `Pompous` (Custom Monomyth nature!)
- **Ability:** `Blaze` (Ups Fire moves by 50% at or below 1/3rd HP)
- **Stats (Lv7, Turn 122):** HP 19/24 | Atk 12 | Def 13 | SpA 14 | SpD 13 | Spe 16
- **Current Moves:**
  - `Constrict` (Normal, 35 PP — lowers foe Speed)
  - `Leer` (Normal, 30 PP — lowers foe Defense)
  - `Wrap` (Normal, 20 PP)

## 2. Anansi — Spinarak (♂) — (#017)
- **Nickname:** `Anansi` (West African spider trickster god of stories; caught Lv2 in Webbed Woods on Turn 106–108)
- **Type:** `Bug / Poison` (Verified Turn 118 Summary)
- **Nature:** `Furtive` (Custom Monomyth nature)
- **Ability:** `Swarm` (Ups Bug moves by 50% at or below 1/3rd HP)
- **Stats (Lv4, Turn 164):** HP 17/17 | Atk 10 | Def 8 | SpA 9 | SpD 9 | Spe 8
- **Current Moves:**
  - `Constrict` (Normal, 35 PP)
  - `String Shot` (Bug, 40 PP)
  - `Poison Sting` (Poison, learned Lv3 on Turn 122)

## 3. Psyche — Sleepillar (♀) — (#025, Original Fakemon)
- **Nickname:** `Psyche` (Greek soul/butterfly goddess; caught Lv2 in Webbed Woods on Turn 114–116)
- **Type:** `Bug / Psychic` (Verified Turn 118 Summary)
- **Nature:** `Insane` (`+SpA, -Atk` — Verified Turn 160 Lv4 stat gains!)
- **Ability:** `Symbiosis` (Passes its item to an ally after it uses one)
- **Stats (Lv4, Turn 161):** HP 17/17 | Atk 6 | Def 8 | SpA 10 | SpD 8 | Spe 8
- **Current Moves:**
  - `Struggle Bug` (Bug, Special, 20 PP — damages & lowers foe Sp. Atk)
  - `String Shot` (Bug, Status, 40 PP — lowers foe Speed)



<hr>