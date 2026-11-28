<h1><code>Main</code></h1>

# Pokémon Monomyth — Main Dashboard

## Current Status
- **Game:** Pokémon Monomyth (`© 2026 TEAM MONOMYTH`) — Difficulty: `Monomyth`
- **Trainer:** Iris | **Rival/Friend:** Monty
- **Region:** Athanto
- **Progression:** Woke up in Iris's Bedroom (Turn 20); Monty is waiting outside to show us a glowing blue crate in the forest.
- **Badges:** 0

## Notepad Index
- [Mechanics Overview](Mechanics/Overview.md) — Verified game settings, Athanto survival/attrition & economy rules, Naming Screen grid, dialogue controls.
- [Home Town](Locations/Home_Town.md) — Starting town notes, Iris's house, Big Bro & Monty intro context.
- `Party.md` — Active team roster, nicknames, movesets, and roles (to be created upon receiving starter).
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
- **Stairs to 1F:** Green mat at `(8, 2)`, stair warp at `(7, 2)`.



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
- **Safe Dialogue Advance (`B` button, Verified Turn 11):** Pressing `B` with `~1400ms` sleep advances standard dialogue boxes and stops safely without confirming choice prompts or typing letters on naming screens.
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