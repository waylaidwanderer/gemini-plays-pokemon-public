<h1><code>Main</code></h1>

# Main Notepad - Pokémon Monomyth

## Game Info
- **Title:** Pokémon Monomyth (Team Monomyth, 2026)
- **Region:** Athanto
- **Trainer:** Astra (Friend: Monty, Bully/Rival: Willow)
- **Settings:** AI Difficulty = Monomyth (intended experience, slightly harder than mainline games); Color Variants = On; Battle/Pokémon Anims = On.

## Current Progression
- Chose starter Mishimizu from the mysterious forest crate outside hometown; Monty got Marmroot, Willow took Crackliss. Defeated two wild Spinarak alongside Monty.

## Party
- **Caspian** (Mishimizu ♂, #007, Lv. 5, Water) — Nature: Adventurous | Ability: Torrent | Stats: HP 21, Atk 11, Def 10, SpA 10, SpD 11, Spe 12 | Moves: Scratch, Growl, Assist.

## Rivals' Starters
- **Monty:** Marmroot ♂ (Groundhog Pokémon)
- **Willow:** Crackliss (Crackling Pokémon)

## Badges / Milestones
- (None yet)

## Index of Sub-Notepads
- `Mechanics/Core.md`: Core game rules, intro pointers, difficulty, EXP scaling, and custom mechanics.


<hr>

<h1><code>Locations/ChamomileTown</code></h1>

# Chamomile Town (Hometown)

## Key Landmarks (Coordinates)
- **Pokémon Center:** Door at `(24, 21)` (exits to `(24, 22)`)
  - 1F: Nurse Joy, PC, Name Rater (`(1, 14)`), Move Relearner (`(1, 15)`).
  - Mezzanine (up left stairs): Integrated Poké Mart (Poké Ball ₽200, Potion ₽300, Antidote ₽100, Paralyze Heal ₽250, Awakening ₽300) and Link Counter.
- **Astra's House:** Door at `(40, 21)` (exits to `(40, 22)`).
  - 2F PC had 1 free Potion (withdrawn).
- **East Exit:** Leads to Webbed Woods (wild Lv. 2 Spinarak, starter crate clearing).


<hr>

<h1><code>Mechanics/Core</code></h1>

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
- **Party EXP Share:** Active by default ("Everybody got their fair share!", verified turn 83).
- **Modern Move Mechanics:** String Shot lowers Speed harshly (-2 stages) and hits both foes in double battles (verified turn 80).
- **Bedroom PC:** Contains 1 free Potion (withdrawn turn 39).
- **Wall Clock:** Must be set in bedroom before going downstairs (defaults to No on confirmation prompt; verified turns 40-45).
- **Naming Screen Confirmation (verified turn 99):** Pressing `A` on `OK` ALWAYS opens an "Are you sure you want the name X? Yes / No" prompt inside the naming screen — press `A` (NOT `B`) after `OK` to confirm! Auto-switch from UPPER to LOWER after the 1st letter preserves `(col, row)` cursor position.
- **Pokémon Center Services (verified turns 94-110):**
  - 1F: Nurse Joy, PC, Name Rater + Move Relearner (bottom-left counter; Move Relearner did not request Heart Scales).
  - Mezzanine (up left stairs): Integrated Poké Mart (Poké Ball ₽200, Potion ₽300, Antidote ₽100, Paralyze Heal ₽250, Awakening ₽300) and Link counter (requires Pokédex).


<hr>