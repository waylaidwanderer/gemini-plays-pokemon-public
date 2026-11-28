<h1><code>Main</code></h1>

# Pokémon Monomyth — Main Dashboard

## Current Status
- **Game:** Pokémon Monomyth (`© 2026 TEAM MONOMYTH`) — Difficulty: `Monomyth`
- **Trainer:** Iris | **Rival/Friend:** Monty
- **Region:** Athanto
- **Progression:** Obtained starter **Crackliss** (`Fire/Poison`); back in starting town Pokémon Center `(7, 12)` (Turn 53). Next: ask Mom at home for permission to challenge the **Catsear City Gym Leader**.
- **Badges:** 0

## Notepad Index
- [Mechanics Overview](Mechanics/Overview.md) — Verified game settings, Athanto survival/attrition & economy rules, Naming Screen grid, dialogue controls.
- [Party Roster](Party.md) — Active team types, custom natures, abilities, movesets, and matchup notes.
- [Home Town](Locations/Home_Town.md) — Starting town notes, Iris's house, Pokémon Center/Mart, Webbed Woods intro.
- `Scratchpad/` — Active routing, battle prep, and temporary testing notes.


<hr>

<h1><code>Locations/Home_Town</code></h1>

# Starting Town & Iris's House

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

<h1><code>Mechanics/Overview</code></h1>

# Mechanics & System Overview — Pokémon Monomyth

## Region & Core Design Pointers (Verified Turns 6–7, New Game Pointers)
- **Region Name:** **Athanto**.
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
  - Pressing `Start` jumps cursor directly to `OK`, and `A` submits the name.
- **Filmstrip Pagination on Animated UIs (Verified Turns 14, 17):** Screens with continuously pulsing cursors (such as the Naming Screen) generate ~42 `[THINKING]` frames before inputs run, pushing the actual button-press frames into `filmstrip_2.png`. Check `filmstripParts` in `<TurnVisualTimeline>` and read `filmstrip_2.png` when `filmstrip_1.png` contains only `[THINKING]` frames.





<hr>

<h1><code>Party</code></h1>

# Active Party Roster — Pokémon Monomyth

## 1. Crackliss (♂) — Starter (#004)
- **Nickname Target:** `Seraph` (missed Monty's 1-time prompt on Turn 51 due to `B`-advance; checking Summary/Name Rater to apply ASAP — **remember: do NOT use `B`-advance right after catching wild Pokémon so we never miss the capture nickname prompt!**)
- **Type:** `Fire / Poison` (Verified Turn 53 Summary)
  - **Immunities:** Burn, Poison / Badly Poisoned, Poison Powder
  - **4x Resistances:** Grass, Bug, Fairy
  - **2x Resistances:** Fire, Ice, Fighting, Poison, Steel
  - **Weaknesses:** **4x Ground**, 2x Water, 2x Rock, 2x Psychic
- **Nature:** `Pompous` (Custom Monomyth nature!)
- **Ability:** `Blaze` (Ups Fire moves by 50% at or below 1/3rd HP)
- **Base Stats at Lv5:** HP 20 | Atk 10 | Def 11 | SpA 11 | SpD 11 | Spe 13 (Next Lv: 26 EXP)
- **Current Moves:**
  - `Constrict` (Normal, 35 PP — lowers foe Speed)
  - `Leer` (Normal, 30 PP — lowers foe Defense)
  - `Wrap` (Normal, 20 PP)


<hr>