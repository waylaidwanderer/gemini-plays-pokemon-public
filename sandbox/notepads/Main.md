# Pokémon Emerald Nuzlocke — Main Dashboard

## Run Status
- **Game:** Pokémon Emerald (Emerald Kaizo / Modified ruleset: In-battle Bag healing items are DISABLED [Cancel only]; wild/trainer Pokémon have custom movesets & held items!)
- **Player Name:** ORION (Boy / Brendan)
- **Attempt:** #18
- **Badges:** 0 / 8

## Nuzlocke Rules & Level Caps
1. **Permadeath:** Fainted Pokémon (0 HP) are permanently dead and must be boxed in the Graveyard.
2. **First Encounter Only:** Catch only the first wild Pokémon encountered in each unique area once Poké Balls are obtained (`Locations/Encounters.md`).
3. **Nicknames:** Always give creative nicknames to every Pokémon caught/received.
4. **Level Caps:**
   - Gym 1 (Roxanne): **Lv. 16*** (Harness cap = `16`; Roxanne's ace is Lv. 15)
   - Gym 2 (Brawly): **Lv. 20*** (Harness cap = `20`; Brawly's ace is Lv. 19)
   - Gym 3 (Wattson): **Lv. 24**
   - Gym 4 (Flannery): **Lv. 29**
   - Gym 5 (Norman): **Lv. 31**
   - Gym 6 (Winona): **Lv. 33**
   - Gym 7 (Tate & Liza): **Lv. 42**
   - Gym 8 (Juan): **Lv. 46**
   - Elite Four / Champion: **Lv. 58**

## Key Tactical Rules (Learned from Attempts #1–#7)
- **Deterministic Bounded 2x2 Move Selection (Verified Turns 328, 2438):** Opening the Bag or Party menu in the overworld resets the in-battle move cursor to Slot 1 (`Tackle`). Because the 2x2 move grid does not wrap, **ALWAYS press `Down, Right` for Slot 4 (`Water Gun`), `Up, Right` for Slot 2 (`Bubble`), `Up, Left` for Slot 1 (`Tackle`), and `Left, Down` (NEVER `Down, Left` when Slot 4 `-` is empty!) for Slot 3 (`Secret Power` / `Toxic`)**!
- **Starter Claims Route 101 (Verified Turn 141):** Because the starter's summary reads `Met in ROUTE 101`, the Nuzlocke harness treats Route 101 as already used and blocks Poké Ball throws on Route 101.
- **Lowered Wild Catch Rates & Crit Range Rule (Turns 158–161, 252, 293, 1090):** Poké Balls thrown at **Green HP (`>50%`)** pop out on Shake 0 in this ROM. Always weaken wild encounters into **Yellow (`<50%`) or Red (`<20%`) HP** using **`Bubble` (`Up, Right`, 20 BP — never `Water Gun`!)** so a `1/16` crit cannot KO, and immediately `RUN` if HP drops into `2x` enemy attack damage (crit range).
- **Modified Move Mechanics (Turns 169, 384, 2225, 3243, 3896):**
  - `Yawn` is a direct sleep move (`EFFECT_SLEEP` with <100% accuracy, not delayed 2-turn sleep): when it hits, it inflicts Sleep (`SLP`) immediately on that turn; when it misses, it prints `"attack missed!"` with no delayed sleep effect.
  - `Silver Wind` (`Ledyba` on Route 103, `Illumise` in Petalburg Woods) and `AncientPower` boost all 5 stats (`+1 Atk/Def/SpA/SpD/Spd`).
  - `Sky Attack` is a 1-turn recoil move (`Foe X is hit with recoil!`) rather than a 2-turn charging move.
- **Route 102 Trainer Teams (Verified Turns 177–182, 303–328, 537–570, 1095–1127):**
  1. **Youngster Calvin `(33, 14)`:** 3 Lv. 6 Pokémon (`Sentret` [Assist->Rock Smash / Mud-Slap / Super Fang, Quick Attack], `Zigzagoon` [Swift, Sand-Attack], `Poochyena` [Super Fang, Rock Smash, Howl]).
  2. **Bug Catcher Rick `(25, 15)`:** 4 Lv. 5 Pokémon (`Caterpie` [holds `Berry Juice`], `Wurmple` [String Shot, Tackle], `Kakuna` [holds `Berry Juice`, Poison Sting, Harden], `Cascoon` [holds `Berry Juice`, Iron Defense, Poison Sting, Tackle]).
  3. **Lass Tiana `(15, 5)` (Mandatory trainer facing `Up` with a 3-tile sight range across `y=2..4`):** 3 Pokémon (`Lv. 6 Igglybuff` [`Cute Charm` contact infatuation, holds `Oran Berry`, uses `Present` — note that `Water Gun` and `Poison Sting` are non-contact moves in Gen 3 and bypass `Cute Charm`!], `Lv. 6 Sunkern` [pure Grass-type, holds `Berry Juice`, knows `Leech Seed` (16 PP), `Protect` (10 PP), `Mega Drain` (10 PP), `Synthesis` (8 PP) — weak to `Poison Sting` + `PSN`!], `Lv. 5 Togepi` [holds `Berry Juice`, knows `Hidden Power`, `Sing`, `Softboiled`/`Synthesis`, `Metronome` (`Lock-On`, `Smog`, `Sky Attack`, `Sunny Day` — if `Sunny Day` is active, use physical `Tackle` until sunlight fades and `Water Gun` returns to full power!)]).
  4. **Bug Catcher Allen `(13, 2)`:** Faces `Down` at the western exit of Route 102; has **4 Lv. 7 Pokémon** (`Weedle` [`Poison Sting`], `Silcoon` [holds `Sitrus Berry`, `Iron Defense`, `Poison Sting`], `Wurmple` [`Tackle`], `Metapod` [holds `Sitrus Berry`, `Iron Defense`]).
- **Route 104 (South) Trainer Teams & Berries (Verified Turns 599–653, 886–913):**
  - **Bird Keeper Billy `(23, 66)`:** Turns toward footsteps on sand; has 3 Lv. 7 Pokémon (`Pidgey` [`Sand-Attack`, `Quick Attack`], `Wingull` [holds `Oran Berry`, `Supersonic`, `Gust`, `Water Gun`], `Taillow`).
  - **Fisherman Darian `(15, 59)`:** Mandatory trainer facing `Right` across the 3-tile beach bottleneck `x=16..18, y=59`; has **4 Pokémon** (`Lv. 9 Magikarp` [`Bounce`, `Tackle`], `Lv. 8 Feebas` [holds `Sitrus Berry` +30 HP, knows `Yawn`/`Hypnosis`, `Water Pulse`, `Facade`, `Icy Wind`], `Lv. 7 Goldeen` [holds `Berry Juice`, `Rain Dance`, `Dive`, `Peck`, `Swift Swim`], and `Lv. 7 Luvdisc` [knows `Dive`, `Swift Swim`]).
  - **Northern Route 104 South Berries & Lady Cindy `(11, 40)`:** Berry trees at `(22, 41)` (`2 Oran Berries`) and `(24, 41)` (`2 Pecha Berries`) north of Mr. Briney's Cottage. **Lady Cindy `(11, 40)`** guards the Petalburg Woods entrance and has **3 Pokémon** (`Lv. 8 Cleffa ♀` [`Cute Charm`, `Pound`, `Charm`, `Encore`, `Metronome`], `Lv. 8 Pichu ♀` [`Thunder Wave`, `ThunderShock`, `Sweet Kiss`, `Thief`, `Static`], `Lv. 7 Azurill ♀` [pure Normal-type with `Huge Power` + Physical `Uproar`], `$1,400` payout).
- **Petalburg Woods Trainers (Verified Turns 920–925, 1561–1572, 2289–2299):**
  1. **Bug Maniac Lyle `(13, 35)`:** Faces `Up` near the south entrance; has **3 Lv. 8 Pokémon** (`Lv. 8 Spinarak` [holds `Berry Juice`, knows `Night Shade`, `Spider Web`], `Lv. 8 Ledyba` [knows `Protect`, `Supersonic`, `Gust`], `Lv. 8 Venonat` [knows `Stun Spore`, `Psybeam`, `Mega Drain`]).
  2. **Bug Catcher James `(10, 24)`:** Faces `Down`; has **3 Pokémon** (`Lv. 9 Paras` [knows `Spore`, `Aerial Ace`, 4x weak to Flying/Fire], `Lv. 8 Surskit` [knows `Mud Shot`, `Water Pulse`, `Psybeam`, `Mega Drain`], `Lv. 9 Nincada` [`Giga Drain`, `Aerial Ace`, `Scratch`; Base 90 Def vs Base 30 SpD]).
  3. **Team Magma Grunt `(26, 23)`:** Cutscene triggers along `x=26..28, y=23`; has **5 Pokémon** (`Lv. 8 Magnemite` [`Flash Cannon`, `Thunder Wave`, `ThunderShock`], `Lv. 8 Koffing` [`Toxic`, `Protect`, `Thief`], `Lv. 9 Houndour` [`Ember`, `Pursuit`, `Super Fang`, holds `Berry Juice`], `Lv. 8 Bagon` [`Headbutt`, `Twister`], and `Lv. 8 Duskull` [`Protect`, `Night Shade`, `Confuse Ray`, `Will-O-Wisp`, holds `Leftovers`]).
- **Route 104 (North) Trainers (Verified Turns 1601–1617, 2481–2489, 3700–3718):**
  1. **Rich Boy Winston `(21, 26)`:** Mandatory trainer facing `Up` with a 4-tile sight range across `(21, 22..25)`; has **3 Lv. 8 Pokémon** (`Lv. 8 Snubbull` [`Intimidate`, `Pay Day`, `Bite`, `Metronome`, holds `Oran Berry`], `Lv. 8 Electrike` [`ThunderShock`, `Quick Attack`, `Bite`, holds `Oran Berry`], `Lv. 8 Growlithe` [`Intimidate`, `Bite`, `Ember`, `Rock Smash`, holds `Oran Berry`]).
  2. **Lass Haley `(32, 22)`:** Faces `Left` across `(30..31, 22)` at the south end of the bridge; has **3 Lv. 9 Pokémon** (`Lv. 9 Skitty ♀` [`Assist`, `Attract`, `Quick Attack`, `Cute Charm`], `Lv. 9 Oddish ♀` [`Acid`, `Protect`, `Sleep Powder`/`Stun Spore`/`PoisonPowder`], `Lv. 9 Vulpix ♀` [`Confuse Ray`, `Ember`, `Bite`]).
  3. **Twins Gina & Mia `(27..28, 15)`:** Mandatory Double Battle facing `Down` across `(27..28, 16)` on the bridge (note: in Gen 3, Double Battle trainers cannot challenge you on sight if you only have 1 conscious Pokémon in your party, allowing a 1-Pokémon party to walk past `(27..28, 16)` without triggering them!); have **2 Lv. 8 Pokémon** (`Lv. 8 Smeargle ♂` [Left: `Focus Punch` (~26 damage), `Teeter Dance`] and `Lv. 8 Smeargle ♂` [Right: `Follow Me`, `Teeter Dance`, `Softboiled`/`Milk Drink`, `Light Screen`, holds `Sitrus Berry`]). **Solution:** Pair **`BASTET` (`Lv. 15 Meowth`, `33 Spd`, 60-BP STAB Physical `Swift` [`Left, Down`], a `TARGET_BOTH` 2-target spread move that bypasses `Follow Me`, ignores `Light Screen`, and causes Left `Smeargle`'s `Focus Punch` to fail every turn!)** in Slot 1 with **`NOCTUA` (`Lv. 15 Hoothoot`, `20 Spd`, 60-BP STAB Physical `Aerial Ace` [`Down, Right`])** in Slot 2!
  4. **PKMN Trainer Red `(29, 8)`:** Mandatory 5-Pokémon boss trainer with a Fisherman overworld sprite facing `Left` with a 5-tile sight range across `(24..28, 8)` at the north end of the bridge; has **5 Lv. 9 Pokémon**: `Lv. 9 Eevee ♂` (`31 HP`, `Curse`, `Rest`, `Snore`, holds `Sitrus Berry` — note `+1 Attack` `Snore` deals `13 damage` normal / `26 damage` crit to `20 Def`), `Lv. 9 Charmander ♂` (`Will-O-Wisp`, `Ember`, `Flame Wheel`, holds `Berry Juice` / `Oran Berry`), `Lv. 9 Pikachu ♂` (`Shock Wave`, `Surf`, `Thunder Wave`, holds `Sitrus Berry`, custom boosted stats `~36 HP` / `~21 Spd`), `Lv. 9 Bulbasaur ♂` (`Cut`, `Mega Drain`, `Sleep Powder`, holds `Sitrus Berry`), and `Lv. 9 Squirtle ♂` (`Fake Out`, `Water Pulse`, `Bite`, `Yawn`, holds `Berry Juice`). **Solution:** Lead with **`HYPNOS` (`Lv. 15 Drowzee`, `21 Spd`, `15-HP Seismic Toss` [Slot 3: `Left, Down`])** to burn `Eevee`'s `Sitrus Berry` on its first `Rest` cycle, then pivot to **`MARSHTOMP` (`Lv. 16`, `51/51 HP`, STAB Special `Water Gun` + STAB Physical `Mud Shot`)** on Sleep Turn 2 so `MARSHTOMP` 2HKOs `Eevee` with `Water Gun`, switch to **`NOCTUA` (`Lv. 15 Hoothoot`, `Aerial Ace`)** to beat `Bulbasaur` (which baits `Pikachu`'s `Shock Wave` into `MARSHTOMP`'s Ground immunity!), OHKO `Lv. 9 Pikachu` from 100% HP with `MARSHTOMP`'s `Mud Shot`, OHKO `Lv. 9 Charmander` from 100% HP with `MARSHTOMP`'s `Water Gun`, and switch **`BASTET` (`Lv. 15 Meowth`, `33 Spd`, `Swift`)** into `Lv. 9 Squirtle` on Turn 1 to absorb and waste `Squirtle`'s `Fake Out`!
- **Attempt #15 Level 16 Cap & Rare Candy Team Budgeting Rule (Roxanne Cap = Lv. 16):**
  - Keep all party members at or below **Level 16** before challenging Gym Leader Roxanne (Pokemon above the active level cap cannot battle in any wild, trainer, or Gym encounter).
  - Always weaken wild encounters **strictly 1 turn at a time** using neutral/resistant moves (`Mudkip`'s 20-BP `Bubble` or `Tackle`) so we preserve all 4 pre-Rustboro catches (Route 103, Route 102, Route 104 South, Petalburg Woods) and spread trainer EXP across 4–5 teammates, keeping everyone at **Level 14–15** entering Rustboro City.
  - Never queue multi-turn attack loops when poisoned (`PSN`) or confused (`Confuse Ray`/`Teeter Dance`).
- **Oldale, Petalburg & Rustboro Mart Prices (Turns 153, 593, 2816):** Poké Balls cost only **$10** each (10+ awards a Premier Ball); Potions cost $300; Super Potions (at Rustboro Mart `(16, 45)`) cost $700; Antidotes cost $100; Parlyz Heals cost $200; Awakenings/Burn Heals cost $250; Repels cost $350; Escape Ropes cost $550.
- **Heal in Overworld to 100% HP & Equip Oran Berries:** Bag Potions cannot be used in battle, but held `Oran Berries` (`(24, 2)` on Route 102 and `(22, 41)` on Route 104 South) activate automatically in battle!
- **Train Caught Teammates to Lv. 10–12 Before Trainers:** Never bring a base-level (Lv. 4–7) catch into Route 102 or Route 104 trainer battles. Train our caught teammates up to **Lv. 10–12** alongside the starter before challenging route trainers.

## Active Party
1. **HYPNOS** — Drowzee ♂ (Lv. 16, `0/50 HP` — **FALLEN Turn 4429 vs School Kid Tammy's Lv. 15 Rhyhorn**).
2. **SYLPH** — Hoppip ♀ (Lv. 16, `42/42 HP`, Grass/Flying, Stats: `42 HP / 17 Atk / 17 Def / 16 SpA / 24 SpD / 22 Spd`, Moves: `Confusion`, `Stun Spore`, `Mega Drain`, `Aerial Ace`) — Caught on Route 103.
3. **NOCTUA** — Hoothoot ♂ (Lv. 16, `0/47 HP` — **FALLEN Turn 4428 vs School Kid Tammy's Lv. 15 Rhyhorn**).
4. **BASTET** — Meowth ♀ (Lv. 16, `0/41 HP` — **FALLEN Turn 4425 vs School Kid Tammy's Lv. 11 Yanma**).
5. **TYPHON** — Grimer ♂ (Lv. 16, `0/52 HP` — **FALLEN Turn 4419 vs School Kid Tammy's Lv. 11 Yanma**, must be deposited in PC Graveyard after battle).
6. **MARSHTOMP** — Marshtomp ♀ (Lv. 16, `0/51 HP` — **FALLEN Turn 4423 vs School Kid Tammy's Lv. 11 Yanma**, must be deposited in PC Graveyard after battle).

## Boxed (Retired Until Cap Advances)
- *(None)*

## Notepad Index
- `Main`: High-level dashboard, party summary, level caps, and core tactical rules.
- `Locations/Encounters`: Route-by-route encounter tracking.
- `Mechanics/Graveyard`: Fallen Pokémon, wipe post-mortems, and run history.
- `Mechanics/UIAndControls`: Verified naming keyboard grid, warp/cutscene scripting patterns, Pokémon Center healing formula, and Littleroot/Route 101/Oldale/Route 103/Route 102 coordinates.