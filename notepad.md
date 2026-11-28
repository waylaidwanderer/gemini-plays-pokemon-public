<h1><code>Main</code></h1>

# Pokémon Monomyth — Main Dashboard

## Current Status
- **Game:** Pokémon Monomyth (`© 2026 TEAM MONOMYTH`) — Difficulty: `Monomyth`
- **Trainer:** Iris | **Rival/Friend:** Monty
- **Region:** Athanto
- **Progression:** Nicknamed starter **Seraph** (`Crackliss`, `Fire/Poison`); received **PokéDex**, **Poké Balls**, and **Potions** from Mom & Big Bro in **Chamomile Town** (Turn 65). Heading out toward **Webbed Woods** and **Catsear City** (Gym Leader: **Bastion**).
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
- **Northern Terrace & Hilltop:**
  - Stairs at `(31, 18)-(33, 18)` lead to upper terrace; NPC at `(35, 16)` gave **1x Sharp Beak** (Turn 71, boosts Flying moves).
  - Further stairs `(27, 14)-(28, 14)` and `(32, 11)` lead to **Monty's House** at `(32, 9)`.
- **Exits:**
  - **East Exit (`x > 45`):** Leads to **Webbed Woods** (toward **Catsear City**).
  - **South Exit (`(27, 43)-(28, 43)`):** Stairs leading south into tall grass (unexplored route/area!).
  - **West Limit:** Dead-ends at trees at `(7, 22)`.
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
- **Webbed Woods Entrance:** East warp arrow at `(20, 12)-(20, 13)`.



<hr>

<h1><code>Mechanics/Overview</code></h1>

# Mechanics & System Overview — Pokémon Monomyth

## Region & Core Design Pointers (Verified Turns 6–7, New Game Pointers)
- **Region Name:** **Athanto**.
- **Built-in Pokémon Center Mega-Hubs (Verified Turns 55, 77–80):**
  - **1F (`y=8..15`):** Nurse Joy `(7, 10)` across counter `(7, 11)` (**player stands at `(7, 12)`**; verify dismissal by stepping to `y >= 13`!), PC `(10, 11)`, **Name Rater** `(1, 14)` (from `(3, 14)`), and **free Move Relearner** `(1, 15)` (from `(3, 15)`).
  - **2F Seamless Mezzanine (`y=0..7`, via left stairs `(1, 10)->(1, 7)`):** **Poké Mart** counter (`(2, 5)-(3, 5)` facing `Up`) and **Link Center**!
- **Stair Movement Timing (Verified Turns 76, 79):** Stair tiles animate slower than flat ground, causing rapid unspaced button lists (`["Up"] * N`) to drop steps on staircases. Always use a `while` loop checking `mgba.get_coordinates()` (or `"hold <Dir> <ms>"`) when climbing/descending stairs.
- **Menu/Dialogue Dismissal Guard in `run_code` (Verified Turns 78–79, 83):** Shop `Buy` fade-outs (~1000ms) and multi-box NPC dialogues can absorb trailing `B` presses. Before chaining overworld walking in `run_code`, loop `["B", "sleep 800", "<FirstStepDir>"]` until `mgba.get_coordinates()` confirms the player actually moved 1 tile!
- **Wilderness & Attrition:** Wilderness between settlements is much wider than in mainline games, testing both battle skill and attrition (HP/PP endurance).
- **Economy & Blackout Rule:** **Blacking out in the wild is costly, but money already spent is safe.** Always spend spare money stocking up on healing items, Poké Balls, and supplies before leaving civilization.
- **Soft Level Caps / Staged EXP:** Experience gain slows down in stages based on progression, steering teams toward the intended level range rather than over-leveling via raw stat disparities. Build a full balanced team and use strategy/synergy rather than solo-grinding.
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
- **Battle Round Timing (Verified Turns 48–50):** With `Battle Anims: On`, a 4-Pokémon Double/Multi-Battle round takes ~10–15s (especially with stat-drop animations like Constrict/String Shot). Interleaving `["B", "sleep 2500"] * 5` after selecting our move/target cleanly resolves full rounds and EXP messages.





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
- **Stats (Lv6, Turn 91):** HP 22 | Atk 11 | Def 12 | SpA 12 | SpD 12 | Spe 14
- **Current Moves:**
  - `Constrict` (Normal, 35 PP — lowers foe Speed)
  - `Leer` (Normal, 30 PP — lowers foe Defense)
  - `Wrap` (Normal, 20 PP)


<hr>