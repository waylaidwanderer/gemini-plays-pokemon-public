# Early Game Routing & Verified Trainer Data

## Littleroot Town
- **Landmarks**: Player's House (East): `(14, 8)`; Rival's House (West): `(5, 8)`; Birch's Lab: door at `(7, 16)`, yellow doormat at `(7, 17)` (building covers `x=3..9, y=11..16`; tree at `(11, 17)`, so route between `(7, 17)` and the central road via `(10, 17)` -> `Up` along `x=10`).
- **Mom's Running Shoes Trigger**: After receiving the Pokedex in Birch's Lab, Mom stands at `(14, 9)` outside the Player's House. Interact with her from `(14, 10)` facing `Up` to receive the Running Shoes.
- **Custom Pond**: Located on the east side at `(18, 12..14)`; stand at `(17, 13)` facing `Right` to fish with the Old Rod (route from `(10, 12)` via `Right x7` along `y=12` to `(17, 12)`, then `Down` to `(17, 13)`).
- **Navigation Note**: Central vertical road runs along `x=10..11` from `y=17` north to `y=0` (Route 101). Use `x=12` (`y=10..15`) to bypass the wandering NPC near `(10..11, 12..14)`.

## Route 101
- **Observed Wild Species**: `Togepi` (Lv 2), `Caterpie` (Lv 2), `Igglybuff` (Lv 3), `Poochyena` (Lv 2).
- **Southern Tall Grass Patch**: Located at `x=5, y=14..16` (accessible from `(11, 14)` by walking `Left x6` to `(5, 14)`).
- **Grass-Free Path (Northbound)**: `(11, 19)` -> `Up x5` to `(11, 14)` -> `Left x4` to `(7, 14)` -> `Up x4` to `(7, 10)` -> `Right x6` to `(13, 10)` -> `Up` to `(13, 9)` -> `Right x2` to `(15, 9)` -> `Up` to `(15, 8)`, then through `(15, 7..5)` (3 grass tiles) to `(15, 4)` -> `Left x3` (2 grass tiles) to `(12, 4)` -> `Left x2` to `(10, 4)` -> `Up` into Oldale Town.
- **Grass-Free Path (Southbound)**: From `(10, 0)`, step `Left` to `(9, 0)`, walk straight `Down` along `x=9` (jumping ledges at `y=6` and `y=13`) to `(9, 14)`, then `Right x2` to `(11, 14)` and `Down x6` into Littleroot Town `(11, 0)`.

## Oldale Town & Route 103
- **Oldale Central Road**: `x=10` (`y=0..19`) is a straight vertical road between Route 101 and Route 103.
- **Route 103 Grass-Free Path (Northbound)**: From `(10, 21)`, walk `Up x8` to `(10, 13)`, `Right x4` to `(14, 13)`, `Up x3` to `(14, 10)` (east to `(20..21, 8..10)` for the **Old Rod Fisherman**, or north to `(13, 7)` -> `Left x7` to `(6, 7)` -> `Up` to `(6, 6)` -> `Left` to `(5, 6)` -> `Up x3` to `(5, 3)` -> `Right x4` to `(9, 3)` for the Rival battle at `(10, 3)`).
- **Route 103 Grass-Free Path (Southbound)**: From `(10, 3)`, walk straight `Down` along `x=10` (jumping ledges at `y=5` and `y=12`) into Oldale Town `(10, 0)`.
- **Oldale West Exit (to Route 102)**: From `(10, 9)`, step `Down x2` to `(10, 11)` (passing south of the scientist at `(8, 9)`) and walk `Left x11` onto Route 102.

## Route 102
- **Eastern Entrance**: Enters from Oldale Town at `(48, 11)`.
- **Trainers**:
  - **Youngster Calvin** `(33, 14)` facing `Down` (3 Pokemon: `Sentret` Lv 6 [`Assist`], `Poochyena` Lv 6 [`Super Fang`], `Zigzagoon` Lv 6 [`Swift`])
  - **Bug Catcher Rick** `(25, 15)` facing `Up` (4 Pokemon: `Caterpie` Lv 5, `Wurmple` Lv 5, `Kakuna` Lv 5, `Cascoon` Lv 5 [`Iron Defense`, holds `Berry Juice`])
  - **Lass Tiana** `(15, 5)` facing `Down` (3 Pokemon: `Igglybuff` Lv 6 [`Present`], `Sunkern` Lv 6 [`Protect`, `Leech Seed`], `Togepi` Lv 5 [`Softboiled`, `Metronome`])
  - **Bug Catcher Allen** `(13, 2)` facing `Down` (3 Pokemon: `Silcoon` Lv 7 [`Iron Defense`, `Shed Skin`, holds `Berry Juice`], `Wurmple` Lv 7, `Metapod` Lv 7 [`Iron Defense`, `Shed Skin`, holds `Sitrus Berry`])
  - **Trainer in tall grass** `(18, 12)` (avoidable via northern berry patch path).
- **Northern Berry Patch & Grass-Free Routes**:
  - **Grass-Free Path North**: `(25, 14)` -> `Up x4` to `(25, 10)` -> `Left x4` to `(21, 10)` -> `Up x2` to `(21, 8)` -> `Left x2` to `(19, 8)` -> `Up x3` to `(19, 5)`.
  - **Berry Trees**: Located at `(24, 2)` (`Oran Berry`) and `(25, 2)` (`Pecha Berry`) — harvest both and end a turn in the free overworld so they auto-refill to 99!
  - **Grass-Free Path to Petalburg City**: From `(13, 3)`, step `Left` to `(12, 3)`, `Down x4` to `(12, 7)`, `Left` to `(11, 7)`, `Down` to `(11, 8)`, and `Left x12` along `y=8` straight into Petalburg City.

## Petalburg City
- **Eastern Entrance**: Enters from Route 102 onto `y=18` (`x=29`).
- **Landmarks**:
  - **Pokemon Center**: Door at `(20, 16)`.
  - **Poke Mart**: Door at `(25, 12)` (`Poke Ball` $10, `Potion` $300, `Antidote` $100, `Parlyz Heal` $200, `Awakening` $250, `Escape Rope` $550, `Repel` $350, `X Speed` $350, `X Attack` $500, `X Defend` $550, `Orange Mail` $50).
  - **Petalburg Gym**: Door at `(15, 8)`; Norman at `(4, 107)` inside (triggers Wally tutorial event).
  - **Southern Pond**: Located at `x=6..11, y=22..25`; stand at `(12, 23)` facing `Left` at `(11, 23)` to fish with Old Rod (from `(16, 23)`, walk `Up x2` to `(16, 21)`, `Left x4` above the trees at `x=13..14` to `(12, 21)`, `Down x2` to `(12, 23)`, and `Left`).
  - **Western Exit (to Route 104)**: Straight west along `y=12..13` past `(8, 12)` to `x=0` (triggers Scott cutscene near `x=4`).

## Route 104 (South)
- **Eastern Entrance**: Enters from Petalburg City at `(36, 62)`.
- **Tall Grass Patch**: Located at `(22..24, 56..61)` (observed wild species: `Jigglypuff` Lv 7, `Cubone` Lv 7, `Natu` Lv 7).
- **Fast Grass-Free Southbound Shortcut (Petalburg Woods to Petalburg City)**: Going southbound from `(10, 39)` outside Petalburg Woods, walk `Down x5` to `(10, 44)`, `Right x10` to `(20, 44)`, `Down x4` to `(20, 48)`, `Right` to `(21, 48)`, `Down x5` to `(21, 53)`, `Right x4` to `(25, 53)`, `Down x9` along the grass-free `x=25` column (jumping the ledge at `(25, 55)` just east of the `(22..24, 56..61)` tall grass patch) to `(25, 62)`, and `Right x15` along `y=62` straight into Petalburg City `(0, 12)`.
- **Beach Staircase**: Located at `(28..29, 70)` (northern beach stairs at `(16..17, 55)`).
- **Trainers & NPCs**:
  - **Friendly Boy** at `(28, 74)` on the shoreline.
  - **Bird Keeper Billy** at `(23, 66)` facing `Left` (3 Pokemon: `Pidgey` Lv 7 [holds `Berry Juice`], `Wingull` Lv 7 [`Supersonic`, `Water Gun`, `Gust`], `Taillow` Lv 7).
  - **Friendly Fisherman** at `(15, 60)` facing `Right`.
  - **Fisherman Darian** at `(15, 59)` facing `Right` (mandatory trainer; 4 Pokemon: `Magikarp` Lv 9 [`Bounce`], `Feebas` Lv 8 [`Icy Wind`, `Facade`, holds `Sitrus Berry`], `Goldeen` Lv 7 [`Swift Swim`; `Rain Dance`, `Peck`, `Horn Attack`, `Dive`], `Luvdisc` Lv 7 [`Attract`, `Dive`, `Toxic`]).
- **Mr. Briney's Cottage & Northern Berry Patch**:
  - Cottage door at `(17, 51)`.
  - **Berry Trees**: Located at `(22, 41)` (`Oran Berry`) and `(24, 41)` (`Pecha Berry`).
  - **Lady Cindy** at `(11, 40)` facing `Left` outside Petalburg Woods (3 Pokemon: `Cleffa` Lv 8 [`Wish`, `Metronome`], `Pichu` Lv 8 [`Sweet Kiss`, `Thunder Wave`, `ThunderShock`], `Azurill` Lv 7 [`Uproar`]).

## Petalburg Woods
- **Southern Entrance**: Enters from Route 104 `(10..11, 38)` onto `(16, 38)` inside Petalburg Woods.
- **Tall Grass Patches (South)**:
  - South-East patch at `(20..25, 32..35)`.
  - **South-West patch at `(6..13, 27..33)`**: From `(17, 33)`, step `Down` to `(17, 34)`, walk `Left x11` along `y=34` (passing 1 tile north of Bug Maniac Lyle at `(13, 35)`) to `(6, 34)`, walk `Up x4` to `(6, 30)`, step `Left` to `(5, 30)`, walk `Up x4` along `x=5` to `(5, 26)` (`(5, 25)` is a tree), step `Right` to `(6, 26)`, and `Up` to `(6, 25)` for a 100% grass-free northbound corridor around the west edge of this patch.
- **NPCs, Trainers & Items**:
  - **Bug Maniac Lyle** at `(13, 35)` (spinning trainer west of southern entrance; 3 Pokemon: `Spinarak` Lv 8 [`Mega Drain`, `Spider Web`, holds `Berry Juice`], `Ledyba` Lv 8 [`Supersonic`, `Mach Punch`], `Venonat` Lv 8 [`Psybeam`, `Stun Spore`, `Confusion`]).
  - **Bug Catcher James** at `(9, 24)` (spinning trainer in straw hat north of south-west grass patch; 3 Pokemon: `Paras` Lv 9 [`Spore`, `Aerial Ace`], `Surskit` Lv 8 [`Water Pulse`, `Mud Shot`, `Mega Drain`], `Nincada` Lv 9 [`Aerial Ace`, `Giga Drain`]).
  - **Southeastern Exit (to Route 104 Plateau)**: Gate at `(36..37, 38..40)` exits to Route 104 `(32, 45)`; `Poke Ball` item ball at `(29, 53)`.
  - **Grass-Free Path to Central Clearing**: From `(6, 25)` (or `(9, 25)` below Bug Catcher James), walk `Right` along `y=25` to `(13, 25)` (north of the `(7..12, 26)` grass row; going southbound, walk `Left x7` along `y=25` from `(13, 25)` to `(6, 25)`, `Down` to `(6, 26)`, `Left` to `(5, 26)`, and `Down x4` along `x=5` to `(5, 30)`), step `Down` to `(13, 26)`, walk `Right x13` along `y=26` to `(26, 26)` (bypassing tall grass at `(18..24, 24..25)`), and walk `Up x3` along `x=26` to `(26, 23)`.
  - **Team Magma Grunt Ambush** at `(26, 23)` (Devon Researcher rewards `Great Ball`):
    - Team (5 Pokemon): `Magnemite` (Lv 8, `Flash Cannon`, `Thunder Wave`, `ThunderShock`), `Houndour` (Lv 9, `Super Fang`, `Pursuit` [AI predicts switches and always clicks `Pursuit` if you switch!], `Ember`), `Bagon` (Lv 8, `Headbutt`), `Koffing` (Lv 8, `Protect`, `Toxic`, `Thief`), `Duskull` (Lv 8, `Protect`, `Shadow Sneak`, `Will-O-Wisp`, holds `Leftovers`).
  - **Grass-Free Path to Northern Exit**: From `(26, 23)`, walk `Up x7` to `(26, 16)`, `Left x13` to `(13, 16)`, `Down x3` to `(13, 19)`, `Left x8` to `(5, 19)`, `Up x6` along `x=5` to `(5, 13)`, `Left` to `(4, 13)`, `Up x5` along `x=4` to `(4, 8)`, `Right x6` to `(10, 8)`, `Down` to `(10, 9)` (below signpost at `(11, 8)`), `Right x4` to `(14, 9)`, and `Up x5` through the northern exit gate at `(14..15, 5)` onto Route 104 North `(10, 29)`.
  - **Remaining Forest Items**: Eastern path (`x=32..37`, including item ball at `(32, 29)`) is blocked by two Cut trees at `(18, 10..11)` near the northern exit; return after obtaining `HM01 Cut` in Rustboro City.

## Route 104 (North)
- **Southern Entrance (from Petalburg Woods)**: Exits Petalburg Woods `(14..15, 5)` onto Route 104 North at `(10, 29)`.
- **Pretty Petal Flower Shop & Surroundings**:
  - **Flower Shop Door**: Located at `(5, 18)`, blocked by a boy standing at `(5, 19)`.
  - **TM09 Giver**: Boy at `(5, 19)` directly in front of the Flower Shop door gives `TM09` (`Bullet Seed`).
  - **Loamy Soil & Berry Trees**: Vertical 4-tile loamy soil column at `x=3, y=22..25` (stand at `x=4` facing `Left`):
    - `(3, 23)`: `Oran Berry` tree.
    - `(3, 25)`: `Cheri Berry` tree (CRITICAL: end a turn in the free overworld right after picking so `Cheri Berries` auto-refill from `2 -> 99`!).
- **Trainers & Bridge Path**:
  - **Rich Boy Winston** at `(21, 26)` facing `Up` (mandatory trainer watching `y=22..25`):
    - Team (3 Pokemon): `Snubbull` (Lv 8, `Intimidate`, `Pay Day`, `Metronome`, holds `Oran/Sitrus Berry`), `Growlithe` (Lv 8, `Intimidate`, `Rock Smash`, `Ember`, holds `Oran Berry` / `Berry Juice`), `Electrike` (Lv 8, `Thunder Wave`, `ThunderShock`, holds `Oran Berry`).
  - **Wooden Bridge & Cut Item**: Runs north from `x=30..31, y=21`. A Cut tree at `(35, 22)` east of the bridge blocks an item ball at `(37, 22)`.
  - **Lass Haley** at `(32, 22)` facing `Left` (mandatory trainer watching bridge entrance at `(30..31, 22)`):
    - Team (3 Pokemon): `Skitty` (Lv 9, `Sing`, `Assist`, `Cute Charm`), `Oddish` (Lv 9, `Protect`, `Acid`, `Mega Drain`), `Vulpix` (Lv 9, `Confuse Ray`, `Ember`, `Disable`).
  - **Twins Gina & Mia** at `(27..28, 15)` facing `Down` onto `(27..28, 16)` (mandatory Double Battle on horizontal bridge section):
    - Team (2 Pokemon): Left `Smeargle` (M, Lv 8, `Focus Punch`, `Super Fang`, `Light Screen`, holds `Oran Berry`) & Right `Smeargle` (M, Lv 8, `Follow Me`, `Teeter Dance`, `Milk Drink`, `Softboiled`, holds `Oran Berry`). Focus physical attacks (`Secret Power` / `Acid`) to break `Focus Punch` and overwhelm `Follow Me` recovery.
  - **PKMN Trainer Red** at `(29, 8)` facing `Left` across `(24..28, 8)` (mandatory 5-tile vision trainer at northern exit of bridge; defeated Turn 723):
    - Team (5 Pokemon):
      1. `Eevee` (M, Lv 9, 31 Max HP, `Curse`, `Rest`, `Snore`, `Quick Attack`, holds `Sitrus Berry`) — 2HKO with Special moves (`Water Pulse` / `Ice Beam`)
      2. `Pikachu` (M, Lv 9, `Thunder Wave`, `Shock Wave`, holds `Oran/Sitrus Berry`)
      3. `Charmander` (M, Lv 9, `Flame Wheel`, holds `Oran/Sitrus Berry`)
      4. `Bulbasaur` (M, Lv 9, holds `Oran Berry`)
      5. `Squirtle` (M, Lv 9, `Fake Out`)

## Rustboro City
- **Southern Entrance**: Enters from Route 104 North `(17..20, 0)` onto `(19, 59)`.
- **Landmarks**:
  - **Poke Mart**: Door at `(16, 45)` (building covers `x=14..17, y=42..45` with a streetlamp at `(18, 45)`; use `x=19..21` for the main vertical avenue).
  - **Pokemon Center**: Door at `(16, 38)`.
  - **Cutter's House**: Door at `(9, 38)`; Cutter at `(7, 5)` inside gives `HM01 Cut` (interact from `(7, 6)` facing `Up`).
  - **Pokemon Trainer's School**: Door at `(27, 34)` (fountain at `(27, 38)`); NPC at `(5, 3)` inside has no interaction script in this hack.
  - **House South-East of Gym**: Door at `(30, 28)` (building covers `x=28..32, y=25..28` with a fence blocking `x=24..35, y=25`; Trade Boy is inside at `(4, 4)`).
  - **Rustboro Gym & Adjacent House**: Rustboro Gym door at `(27, 19)`; house east of Gym has door at `(33, 19)` (doormat inside at `(5, 7)`).
  - **Eastern Exit (to Route 116)**: From the main avenue at `(21, 20)`, walk `Up x9` to `(21, 11)` and `Right x19` onto Route 116 `(0, 11)` (tall grass starts at `(4, 13..15)`).