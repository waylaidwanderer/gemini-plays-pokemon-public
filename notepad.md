<h1><code>Main</code></h1>

# Main Notepad - Pokémon Monomyth

## Game Info
- **Title:** Pokémon Monomyth (Team Monomyth, 2026)
- **Region:** Athanto
- **Trainer:** Astra (Friend: Monty, Bully/Rival: Willow)
- **Settings:** AI Difficulty = Monomyth (intended experience, slightly harder than mainline games); Color Variants = On; Battle/Pokémon Anims = On.

## Current Progression
- Chose starter Caspian (Mishimizu) from the forest crate in Webbed Woods; Monty got Marmroot, Willow took Crackliss. Defeated two wild Spinarak alongside Monty.
- Big Bro discovered the PokéBall belongs to **Edelweiss Labs** (Edelweiss City). Received **Pokédex**, **Potions**, and **PokéBalls** from Mom & Big Bro, and permission to journey.
- Big Bro suggested visiting his friend **Bastion**, Gym Leader of **Catsear City**, first (and calling Big Bro via **payphone** to update Pokédex progress!).

## Party
- **Caspian** (Mishimizu ♂, #007, Lv. 6, Water) — Nature: Adventurous | Ability: Torrent | Stats: HP 23, Atk 12, Def 12, SpA 11, SpD 12, Spe 13 | Moves: Scratch, Growl, Assist.

## Rivals' Starters
- **Monty:** Marmroot ♂ (Groundhog Pokémon)
- **Willow:** Crackliss (Crackling Pokémon)

## Badges / Milestones
- (None yet)

## Index of Sub-Notepads
- `Mechanics/Core.md`: Core game rules, intro pointers, difficulty, EXP scaling, UI/naming, and custom mechanics.
- `Locations/ChamomileTown.md`: Hometown map, landmarks, Pokémon Center & Mart inventory.


<hr>

<h1><code>Locations/ChamomileTown</code></h1>

# Chamomile Town (Hometown)

## Key Landmarks (Coordinates)
- **Pokémon Center:** Door at `(24, 21)` (exits to `(24, 22)`)
  - 1F: Nurse Joy, PC, Name Rater (`(1, 14)`), Move Relearner (`(1, 15)`).
  - Mezzanine (up left stairs): Integrated Poké Mart (Poké Ball ₽200, Potion ₽300, Antidote ₽100, Paralyze Heal ₽250, Awakening ₽300) and Link Counter.
- **Astra's House:** Door at `(40, 21)` (exits to `(40, 22)`).
  - 2F PC had 1 free Potion (withdrawn).
  - Note: Mom does NOT heal the party (use the Pokémon Center down the street).
- **Monty's House:** On top of Chamomile Hill (`(32, 9)`), reached via the staircases north of the main road.
- **East Exit:** Leads to **Routes 1 & 2 (Forest Stroll)** and **Webbed Woods** (`Chamomile X = Route X + 54`, `Chamomile Y = Route Y + 10`).


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
- **Party EXP Share & Capture EXP:** Party EXP Share is active by default ("Everybody got their fair share!", verified turn 83) and catching wild Pokémon also grants EXP (verified turn 196).
- **Modern Move Mechanics:** String Shot lowers Speed harshly (-2 stages) and hits both foes in double battles (verified turn 80).
- **Bedroom PC:** Contains 1 free Potion (withdrawn turn 39).
- **Wall Clock:** Must be set in bedroom before going downstairs (defaults to No on confirmation prompt; verified turns 40-45).
- **Naming Screen Confirmation (verified turn 99):** Pressing `A` on `OK` ALWAYS opens an "Are you sure you want the name X? Yes / No" prompt inside the naming screen — press `A` (NOT `B`) after `OK` to confirm! Auto-switch from UPPER to LOWER after the 1st letter preserves `(col, row)` cursor position.
- **Pokémon Center Services (verified turns 94-110):**
  - 1F: Nurse Joy, PC, Name Rater + Move Relearner (bottom-left counter; Move Relearner did not request Heart Scales).
  - Mezzanine (up left stairs): Integrated Poké Mart (Poké Ball ₽200, Potion ₽300, Antidote ₽100, Paralyze Heal ₽250, Awakening ₽300) and Link counter (requires Pokédex).
- **Outdoor Stairs (verified turns 131, 150-151):** Outdoor staircases move at half speed, so traversing each stair tile consumes ~2 single directional presses (keep this in mind when batching movement across stairs!).
- **Poké Mart Menu Timing (verified turns 154-155):** Each Mart prompt ("How many?", "That will be ₽X", "Here you go!") takes ~700-800ms to type out; wait `sleep 1000` after each `A` confirmation before pressing `Up`/`Down`/`A`.
- **Nurse Joy Healing (verified turns 173-174):** Nurse Joy has 3 text boxes before her Yes/No prompt (pressing `B` on the 3rd box declines healing). Use 4x `A` with `sleep 1000` between presses, followed by `sleep 4000` for the healing jingle, then `B` to close.
- **Overworld Doors:** After stepping onto a door horizontally, entering may need an extra `Up` press; wait `sleep 800` after a door warp before moving inside.


<hr>