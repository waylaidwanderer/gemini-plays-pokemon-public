# Core Mechanics & Intro Pointers (Pokémon Monomyth - Region: Athanto)

## Intro Pointers (Verified at New Game start)
1. **Wilderness & Attrition:** Wilderness between settlements is wider than mainline Pokémon games, testing both battle skill and attrition. Always stock up on supplies (Potions, status heals, Poké Balls, etc.) before leaving civilization. Blacking out in the wild is costly, but money already spent is safe.
2. **Staged EXP Scaling (Soft Level Cap):** Experience gain slows down in stages based on progression, steering toward the intended challenge range. Focus on team balance, type coverage, and battle strategy rather than overleveling.
3. **Visual Color Variants:** Individual Pokémon have unique color/pattern variations (enabled in Options).
4. **Difficulty Modes:** Monomyth (intended, slightly harder than official games) vs Heroic (smarter/more switching AI, same opponent stats). We are playing on Monomyth difficulty.

## UI Mechanics
- **Dialogue:** `B` advances dialogue safely without confirming menus (verified turn 20).
- **Naming Screen (verified turns 24-25):**
  - Auto-switches from uppercase to lowercase after the 1st character.
  - Grid has 4 rows (0-3) with NO gap stop between col 2 and col 3, BUT there IS a space stop at col 6 on rows 0-1 before `.`/`,`:
    - Row 0: `a`(0) `b`(1) `c`(2) `d`(3) `e`(4) `f`(5) ` `(6) `.`(7)
    - Row 1: `g`(0) `h`(1) `i`(2) `j`(3) `k`(4) `l`(5) ` `(6) `,`(7)
    - Row 2: `m`(0) `n`(1) `o`(2) `p`(3) `q`(4) `r`(5) `s`(6)
    - Row 3: `t`(0) `u`(1) `v`(2) `w`(3) `x`(4) `y`(5) `z`(6)
  - `Start` jumps cursor to `OK`.

## Battle & Progression Mechanics (Verified)
- **Party EXP Share & Capture EXP:** Party EXP Share is active by default ("Everybody got their fair share!", verified turn 83) and catching wild Pokémon also grants EXP (verified turn 196).
- **Battle Item Limit:** Trainer Tips sign in Webbed Woods `(34, 19)` states it is against the rules to use more than **4 items** during a battle (verified turn 207).
- **Set Battle Style:** Trainer battles use Set mode (no free switch prompt between opponent Pokémon; verified turn 255).
- **Modern Move Mechanics:** String Shot lowers Speed harshly (-2 stages) and hits both foes in double battles (verified turn 80).
- **Bedroom PC:** Contains 1 free Potion (withdrawn turn 39).
- **Wall Clock:** Must be set in bedroom before going downstairs (defaults to No on confirmation prompt; verified turns 40-45).
- **Naming Screen Confirmation (verified turn 99):** Pressing `A` on `OK` ALWAYS opens an "Are you sure you want the name X? Yes / No" prompt inside the naming screen — press `A` (NOT `B`) after `OK` to confirm! Auto-switch from UPPER to LOWER after the 1st letter preserves `(col, row)` cursor position.
- **Pokémon Center Services (verified turns 94-110):**
  - 1F: Nurse Joy, PC, Name Rater + Move Relearner (bottom-left counter; Move Relearner did not request Heart Scales).
  - Mezzanine (up left stairs): Integrated Poké Mart (Poké Ball ₽200, Potion ₽300, Antidote ₽100, Paralyze Heal ₽250, Awakening ₽300) and Link counter (requires Pokédex).
- **Outdoor Stairs (verified turns 131, 150-151):** Outdoor staircases move at half speed, so traversing each stair tile consumes ~2 single directional presses (keep this in mind when batching movement across stairs!).
- **Poké Mart Menu Timing (verified turns 154-155):** Each Mart prompt ("How many?", "That will be ₽X", "Here you go!") takes ~700-800ms to type out; wait `sleep 1000` after each `A` confirmation before pressing `Up`/`Down`/`A`.
- **Nurse Joy Healing (verified turns 173-174, 270):** Nurse Joy has 3 text boxes before her Yes/No prompt (pressing `B` on the 3rd box declines healing). Use 4x `A` with `sleep 1000` between presses, followed by `sleep 5500` (longer with 4+ Pokémon) for the healing jingle, then `B` x 4 (`sleep 1000` between) to close cleanly.
- **PokéBall Catch Timing (verified turn 236):** Throwing a PokéBall from `Use` through 3 shakes + click + jingle takes ~`sleep 8500` to land directly on `"Yeehaw! X was caught!"`.
- **Overworld Doors:** After stepping onto a door horizontally, entering may need an extra `Up` press; wait `sleep 800` after a door warp before moving inside.
- **Pause & Summary Menu (verified turns 202-204, 225):** Pause menu is a 1D list (0: PokéDex, 1: Pokémon, 2: Bag, 3: Trainer Card, 4: Save, 5: Options, 6: Exit) split into two columns that does **NOT** wrap past Exit (press `Up` to move back up from Exit). Closing a Pokémon's Summary (`B`) returns to the `Summary/Switch/Item/Cancel` submenu inside Party, so exiting from Summary back to the overworld takes 3 `B` presses (`Summary -> Submenu -> Party -> Pause`) plus 1 `B` to close Pause.
- **Bag Battle Memory & Overworld Chain-Healing:** Bag remembers the last-used pocket across battle and overworld (Dot 1 = Items, Dot 2 = Medicine, Dot 3 = PokéBalls; verified turns 189-190, 229). Apricorns are stored in the PokéBalls pocket (turn 209). Using Medicine from Bag in the overworld stays on `"Use on which Pokémon?"` for chain-healing (verified turn 230).
