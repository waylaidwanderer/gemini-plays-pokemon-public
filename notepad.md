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
- **Caspian** (Mishimizu ♂, #007, Lv. 7, Water) — Nature: Adventurous | Ability: Torrent | Stats: HP 25, Atk 14, Def 13, SpA 12, SpD 13, Spe 14 | Moves: Scratch, Growl, Assist.
- **Ariadne** (Spinarak ♀, #017, Lv. 5, Bug/Poison) — Nature: Saucy | Ability: Swarm | Stats: HP 19, Atk 12, Def 9, SpA 10, SpD 10, Spe 9 | Moves: Constrict, String Shot, Poison Sting, Absorb.
- **Selene** (Sleepillar ♀, #025, Lv. 5, Bug/Psychic) — Nature: Zesty | Ability: Early Bird | Stats: HP 19, Atk 8, Def 8, SpA 10, SpD 9, Spe 9 | Moves: Struggle Bug, String Shot.
- **Orpheus** (Leonte ♂, #015, Lv. 5, Flying/Ground) — Nature: Conniving | Ability: Quick Feet | Stats: HP 21, Atk 11, Def 11, SpA 12, SpD 12, Spe 9 | Moves: Peck, Sand Attack, Foresight.

## Rivals' Starters
- **Monty:** Marmroot ♂ (Groundhog Pokémon)
- **Willow:** Crackliss (Crackling Pokémon)

## Badges / Milestones
- (None yet)

## Index of Sub-Notepads
- `Mechanics/Core.md`: Core game rules, intro pointers, difficulty, EXP scaling, UI/naming, and custom mechanics.
- `Locations/ChamomileTown.md`: Hometown map, landmarks, Pokémon Center & Mart inventory.
- `Locations/WebbedWoods.md`: Webbed Woods map, items, wild encounters, and trainers.


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
- **East Exit:** Leads to **Routes 1 & 2 (Forest Stroll)** and **Webbed Woods** (`Chamomile X = Route X + 54`, `Chamomile Y = Route Y + 11`; verified turn 268).


<hr>

<h1><code>Locations/WebbedWoods</code></h1>

# Webbed Woods

## Connections
- **West:** Route 1 (`Route 1 (19, 12)` going Right → `Webbed Woods (9, 12)`).

## Landmarks & Items
- `(14, 13)`: Empty wooden crate where Astra, Monty, and Willow found the three Edelweiss Labs starters (Mishimizu, Marmroot, Crackliss).
- `(20, 7)`: **Antidote** (collected turn 185).
- `x=21..29, y=12..17`: First large tall grass patch; path continues south/southeast around `x=30..32, y=15..18` west of a pond (`x=33..36, y=15..18`).
- `(34, 19)`: Trainer Tips stone sign ("against the rules to use more than four items during a battle").
- `(33, 22)`: **Blu. Apricorn Tree** (picked Blu. Apricorn turn 209; stored in PokéBalls pocket).
- `(40, 5)`: **Antidote** (northeast clearing past cobweb canopy at `x=42..44, y=11`; collected turn 227).
- `(47, 24)`: **Potion** (tucked in tall grass pocket east of pond; collected turn 244).
- `(19, 19)`: **PokéBall** (west pond alcove off `y=23..25` branch; collected turn 275).

## Wild Encounters Observed
- **Spinarak** (Bug/Poison, #017) — Lv. 2 (caught female silver-legged color variant, nicknamed **Ariadne**, turn 195).
- **Sleepillar** (Bug/Psychic, #025, Drowsy Pokémon) — Lv. 3 (caught female purple color variant, nicknamed **Selene**, turn 218; knows Struggle Bug).
- **Leonte** (Flying/Ground, #015, Thrasher Pokémon) — Lv. 3 (caught male, nicknamed **Orpheus**, turn 236; knows Peck).

## Trainers
- **Youngster Jimmy** `(32, 25)` (defeated turn 261): Kernut ♂ Lv. 3 (Grass?, knows Bide), Shope ♀ Lv. 4 (knows Tackle).
- **Bug Catcher Tim** `(24, 34)` (defeated turn 288): Spinarak ♀ Lv. 3, Joltik ♀ Lv. 4 (knows Absorb).


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


<hr>