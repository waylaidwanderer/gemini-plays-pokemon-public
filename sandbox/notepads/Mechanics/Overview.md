# Mechanics & System Overview — Pokémon Monomyth

## Region & Core Design Pointers (Verified Turns 6–7, New Game Pointers)
- **Region Name:** **Athanto**.
- **Built-in Pokémon Center Mega-Hubs (Verified Turns 55, 77–80):**
  - **1F (`y=8..15`):** Nurse Joy `(7, 10)`, PC `(10, 11)`, **Name Rater** `(1, 14)` (from `(3, 14)`), and **free Move Relearner** `(1, 15)` (from `(3, 15)`).
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



