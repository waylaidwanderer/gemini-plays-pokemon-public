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
  - Ground **Item Balls** display **2** text boxes (`"<Player> found one <Item>!"` -> `"<Player> put away..."`). **Blue-capped Item Balls** hold Battle/Held Items (e.g. `Silver Powder` at Secret Webbed Woods `(32, 21)`, Turn 223).
  - Standalone **round green bushes** can hold hidden items when interacted with `A` (e.g. `1x Repel` at Route 2 `(10, 19)`, Turn 212).
  - **Apricorn Trees** display **4** text boxes (`"It's an Apricorn Tree..."` -> `"Hey! There's an Apricorn growing!"` -> `"<Player> found one <Apricorn>!"` -> `"<Player> put away..."`). Always use a bounded coordinate-checked dismissal guard after plucking an Apricorn.
- **Forest Tree Collision Footprint (Verified Turn 123):** Large forest trees occupy a 2-row collision base; always route along clear grass/dirt channels in `latest_grid.png` rather than stepping into tree-trunk shadow tiles.
- **Wilderness & Attrition:** Wilderness between settlements is much wider than in mainline games, testing both battle skill and attrition (HP/PP endurance).
- **Economy & Blackout Rule (Verified Turns 6–7, 146):** **Blacking out in the wild/trainer battle deducts 50% of current cash** (`¥150 -> lost ¥75` on Turn 146) and respawns you with full HP/PP (outside Iris's House `(40, 22)` in Chamomile Town). Money already spent on items is 100% safe—always spend spare cash before leaving civilization.
- **Soft Level Caps / Staged EXP:** Experience gain slows down in stages based on progression, steering teams toward the intended level range rather than over-leveling via raw stat disparities. Build a full balanced team and use strategy/synergy rather than solo-grinding.
  - **Built-in Party-Wide EXP Share & Capture EXP (Verified Turn 107):** Every battle and wild capture awards EXP to the entire party automatically (`"Everybody got their fair share!"`), including catching wild Pokémon!
- **Shared Bag Pocket Memory & 3x2 Item Sub-Menu (Verified Turns 105, 199, 246):**
  - Overworld Bag and Battle Bag share a **single global** last-pocket pointer (`1:Items, 2:Medicine, 3:PokéBalls, 4:Battle Items, 5:TMs & HMs, 6:Berries, 7:?, 8:Key Items`). Switching to `PokéBalls` in battle causes Overworld Bag to open on `PokéBalls` next time.
  - Selecting an item in the Overworld Bag opens a **3x2 sub-menu**: `(0,0) Use | (0,1) Register`, `(1,0) Toss | (1,1) Give`, `(2,0) Free Space | (2,1) Cancel`. Thus equipping a Held Item requires `Right, Down, A` (`Give`), NOT `A` (`Use`).
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
  - **Battle Menu Cursor After Throwing a PokéBall (Verified Turn 229):** If a thrown PokéBall breaks open, `"What will <Lead> do?"` keeps the cursor on **`> Bag` `(0, 1)`** (and `Bag` stays on `PokéBalls -> > PokéBall`). Press `Left` to return to `Fight`, or `A` to throw another Ball directly.
  - **Safe Post-Capture Progression (Verified Turns 107, 197, 230):** Never press `B` after throwing a PokéBall. Once `"Yeehaw! <Pokémon> was caught!"` appears, send 4 spaced `A` presses (`["A", "sleep 2500", "A", "sleep 2500", "A", "sleep 3500", "A", "sleep 2500"]`) to advance through EXP share and PokéDex registration safely without skipping 4-move-slot level-up prompts or declining the Nickname prompt.



