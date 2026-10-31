<h1><code>Locations/Encounters</code></h1>

# Nuzlocke Encounters (Attempt #2)

| Location | Pokemon | Nickname | Status | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Starter (Route 101) | Mudkip (M, Lv 7) | POSEIDON | Active | Moves: `Tackle`, `Growl`, `Bubble` (Lv 6), `Mud Sport` (Lv 7); Stats: 25/16/13/12/12/10 |
| Littleroot Town | TBD | TBD | Pending | Custom pond at `(18, 12..14)`; stand at `(17, 13)` facing `Right` with Old Rod |
| Route 101 | Poochyena (F, Lv 2) | AHECATE | Active | Caught at `(5, 15)` on Turn 546 |
| Route 103 | TBD | TBD | Pending | Observed species: `Hoppip`, `Spearow` |
| Route 102 | TBD | TBD | Pending | Observed species: `Meowth` |
| Petalburg City | TBD | TBD | Pending | Pond at `x=6..11, y=22..25`; stand at `(12, 23)` facing `Left` with Old Rod (observed: `Azurill`) |
| Route 104 | TBD | TBD | Pending | Tall grass at `(22..24, 56..61)` (observed: `Jigglypuff`) |
| Petalburg Woods | TBD | TBD | Pending | Tall grass at `(20..25, 32..35)` (observed: `Oddish`) |

## Attempt #1 Encounter History
- **Starter**: `Mudkip` (`TRITON`, Lv 11) — Fainted to Petalburg Woods Magma Grunt's Lv 9 `Houndour` (`Super Fang` + `Pursuit`)
- **Route 101**: `Caterpie -> Butterfree` (`MORPHEUS`, Lv 15, `Compound Eyes`; learned `Confusion` Lv 10, `PoisonPowder` Lv 13, `Supersonic` Lv 14, `Aerial Ace` Lv 15) — Fainted to Red's Lv 9 `Eevee`
- **Route 103**: `Hoppip` (`ZEPHYR`, Lv 14; learned `Confusion`, `PoisonPowder`, `Mega Drain`, `Gust`) — Fainted to Red's Lv 9 `Eevee`
- **Route 102**: `Meowth` (`MIDAS`, Lv 11) — Fainted to Petalburg Woods Magma Grunt's Lv 8 `Koffing`
- **Petalburg City (Old Rod)**: `Azurill` (`CALYPSO`, Lv 10, `Thick Fat`) — Fainted to Petalburg Woods Magma Grunt's Lv 9 `Houndour`
- **Route 104**: `Jigglypuff` (`LYRA`, Lv 15; learned `Seismic Toss` at Lv 14) — Fainted to Red's Lv 9 `Eevee`
- **Petalburg Woods**: `Oddish` (`ARTEMISIA`, Lv 8; knew `Acid`, `Mega Drain`) — Boxed

<hr>

<h1><code>Main</code></h1>

# Nuzlocke Dashboard — Attempt #2

## Active Rules & Status
- **Attempt**: #2
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configured & verified Turn 505; Text Speed `Fast`)
- **Unlimited Items & In-Battle Bag Restriction**: Rare Candies & any Berries currently in the Bag (`Cheri Berry` cures Paralysis, `Pecha Berry` cures Poison, `Oran Berry` +10 HP) auto-refill to 99 at the **turn boundary** in the overworld (never consume the last copy `x 1 -> x 0` of a newly harvested Berry before ending a turn in the free overworld!). **Using Berries/healing items directly from the Bag during battle is disabled** (selecting a Berry in battle only shows `>CANCEL`; Berries work as held items in battle or from the Bag in the overworld).
- **Key Items Obtained**: `Pokedex`, `Running Shoes` (need to re-talk to Fisherman on Route 103 with `A` instead of `B` to answer `YES` and receive `Old Rod`).

## Attempt #1 Post-Mortem & Key Tactical Lessons
- **Result**: Wiped at Turn 497 against **PKMN Trainer Red** (`(29, 8)` on Route 104 North, 8 tiles south of Rustboro City).
- **Root Causes & Fixes for Attempt #2**:
  1. **Pre-Level Before Ambush Bosses**: In Attempt #1, we entered the 5-Pokemon **Team Magma Grunt ambush** at `(26, 23)` in Petalburg Woods (`Magnemite` Lv 8, `Houndour` Lv 9 with `Super Fang` + `Pursuit` + `Ember`, `Bagon` Lv 8, `Koffing` Lv 8 with `Protect` + `Thief`, `Duskull` Lv 8 with `Protect` + `Shadow Sneak` + `Leftovers`) at Lv 10–12 and lost 3 party members (`Triton`, `Calypso`, `Midas`). In Attempt #2, use unlimited Rare Candies to pre-level our full 6-Pokemon party to **Lv 14–15** with held `Oran Berries` *before* fighting the Team Magma Grunt!
  2. **Keep a Full 6-Pokemon Active Party**: We have 7+ available encounters before Petalburg Woods/Route 104 North (`Starter`, `Littleroot Pond`, `Route 101`, `Route 103`, `Route 102`, `Petalburg City Pond`, `Route 104 South`, `Petalburg Woods`). Never enter Petalburg Woods or Route 104 North with empty/fainted party slots when healthy encounters are available in the Petalburg City PC (`(20, 16)`).
  3. **Cheri Berry Auto-Refill (`(3, 25)` on Route 104 North)**: Immediately after harvesting the `Cheri Berry` tree at `(3, 25)` outside the Pretty Petal Flower Shop, end a turn in the free overworld (with no textbox or menu open) so `Cheri Berries` auto-refill from `2 -> 99`!
  4. **Countering PKMN Trainer Red (`(29, 8)` on Route 104 North)**: Red has a 6-Pokemon team leading with `Eevee` (M, Lv 9, 31 Max HP, holds `Sitrus Berry`, moves: `Curse`, `Rest`, `Snore`, `Quick Attack`). The AI spams `Curse` + `Rest`/`Snore` until `+1` priority `Quick Attack` enters KO range or `Curse` is maxed. Do NOT let `Eevee` stack `Curse` boosts—hit it hard on the Special side (since `Curse` only boosts physical `Defense`, not `Sp.Def`), use Fighting moves / `Leech Seed` / `Encore`, or finish it from `> 50%` HP before it can `Rest`.

## Level Cap Schedule
1. **Roxanne (Rustboro Gym)**: Lv 16
2. **Brawly (Dewford Gym)**: Lv 20
3. **Wattson (Mauville Gym)**: Lv 29
4. **Flannery (Lavaridge Gym)**: Lv 42
5. **Norman (Petalburg Gym)**: Lv 48
6. **Winona (Fortree Gym)**: Lv 55
7. **Tate & Liza (Mossdeep Gym)**: Lv 70
8. **Wallace / Juan (Sootopolis Gym)**: Lv 77
9. **Champion (Pokemon League)**: Lv 100

## Notepad Index
- `Locations/Encounters`: Route-by-route Nuzlocke encounter tracking & status
- `Mechanics/UI_And_Tools`: Verified menu, Bag, fishing, and overworld mechanics
- `Scratchpad/Routing`: Verified early-game maps, trainers, and routing

<hr>

<h1><code>Mechanics/UI_And_Tools</code></h1>

# UI, Menu, and Tool Mechanics

## Menu & Cursor Mechanics
- **New Game Options Reset & Wall Clock UI**: Configuring `OPTION` on the Title Screen before `NEW GAME` is overwritten by `StartNewGame()`; always configure `TEXT SPEED: FAST` and `BATTLE STYLE: SET` via the Start menu after arriving in the moving truck. On the bedroom Wall Clock UI, pressing `A` opens `"Is this the correct time?"` with the cursor on `>NO`; press `A, Up, A` to select `YES`.
- **Start Menu Cursor Memory**: The Start menu preserves its last-used index across openings. When `POKEMON` or `POKEDEX` is added at index 0, the stored index shifts relative to older items.
- **Pokemon Summary Exit**: Takes 3 `B` presses to return from Summary to the Start menu (`Summary -> Party submenu -> Party slot list -> Start menu`) and a 4th `B` to close the Start menu.
- **PC Item Withdrawal Exit**: Takes 4 `B` presses after withdrawing an item to return to the overworld (`Dismiss text -> Item list -> Item Storage submenu -> Top-level PC menu`).
- **Bag Pocket Navigation & Cursor Clamping**:
  - Bag pockets (`1: ITEMS`, `2: POKE BALLS`, `3: TMs & HMs`, `4: BERRIES`, `5: KEY ITEMS`) wrap around between `ITEMS` and `KEY ITEMS`.
  - Switching through an empty pocket (`TMs & HMs` or `BERRIES`) clamps the item cursor onto `>CLOSE BAG`; since `Up` never wraps past index 0 inside a Bag pocket or Poke Mart list, pressing `Up` multiple times deterministically clamps to index 0 (and `Up, Up, Down` deterministically selects index 1).
  - Giving a held item (`GIVE`) to a Pokemon already holding an item takes **4 `A` presses** on the Party screen: `1st A` selects the slot (`"[POKEMON] is already holding one [ITEM].♥"`), `2nd A` advances to `"Would you like to switch the two items? [>YES / NO]"`, `3rd A` confirms `YES` (`"The [OLD ITEM] was taken and replaced with the [NEW ITEM]."`), and `4th A` dismisses the text and fades back to the Bag (`~1200ms`).
  - In `KEY ITEMS`, the `USE / REGISTER / CANCEL` submenu is arranged in 2 columns (`>USE` on left, `REGISTER` on right); press `A, Right, A` to register a Key Item to `Select`.
  - In `BERRIES`, berries are sorted numerically by Berry ID (`index 0: No03 PECHA BERRY`, `index 1: No07 ORAN BERRY`), so clamping with `Up, Up` selects `PECHA BERRY` and `Up, Up, Down` selects `ORAN BERRY`. In the overworld, the submenu is a 2-column grid (`Row 0: >CHECK TAG`; `Row 1: USE | GIVE`; `Row 2: TOSS | CANCEL`); press `A, Down, A` to `USE` a Berry or `A, Down, Right, A` to `GIVE` a Berry. **In battle, `USE` is disabled on Berries (only `>CANCEL` appears).**
- **Rare Candy Chaining & Move Replacement**:
  - Each Rare Candy takes **6 `A` presses** when no move is learned: `1st A` selects `>RARE CANDY` (`sleep 400`), `2nd A` selects `>USE` (`sleep 1000` fade into Party), `3rd A` selects the Party slot (`sleep 2500` level-up chime + `"elevated to Lv. X"`), `4th A` opens stat deltas (`sleep 600`), `5th A` shows new total stats (`sleep 600`), and `6th A` closes the stat box and fades back to the Bag (`sleep 1400`).
  - From the Bag (`>RARE CANDY` at index 0), pressing `A` repeatedly (`sleep 900`) automatically chains Rare Candies onto Party Slot 1 as long as `gPartyMenu.slotId == 0` and that Pokemon does not trigger a 5th-move replacement prompt.
  - When replacing a move on a Pokemon with 4 moves, selecting the move to forget triggers **4 sequential text boxes**: `"1, 2, and... ... ... Poof!♥"` (`~2500ms`) -> `"[POKEMON] forgot how to use [MOVE].♥"` (`~1500ms`) -> `"And...♥"` (`~1200ms`) -> `"[POKEMON] learned [NEW MOVE]!"` (`~3000ms` fanfare + `A`/`B` to return to Bag).
- **Naming Screen Helper (`naming.py`) & NPC `YES / NO` Prompts**: Use `naming.get_naming_buttons(name, confirm=True, start_pos=(0, 0))` to generate exact button inputs for uppercase nicknames. Never use `B` when approaching a gift/capture nickname `YES / NO` prompt or an NPC gift `YES / NO` prompt (such as the Route 103 Old Rod Fisherman's `"Do you like to fish?"`), as `B` selects `NO`. From `"Gotcha! [POKEMON] was caught!♥"`, it takes **4 `A` presses** (`Gotcha! -> Pokedex text -> Pokedex entry -> Give a nickname [>YES]`) to open the naming screen; if `"Gotcha!"` was already dismissed with `B` so the screen is on `"[POKEMON]'s data was added to the POKEDEX.♥"`, it takes **3 `A` presses** (`["A", "sleep 2000", "A", "sleep 1500", "A", "sleep 2500"]`) to open the naming screen with 0 stray characters typed. When a 7th+ Pokemon is sent to the PC after nicknaming, the `"It was placed in BOX 'BOX1.'"` message on the naming screen requires **`A`** (not `B`) to dismiss.

## Overworld & Fishing Mechanics
- **NPC Sprite Coordinates**: Gen 3 NPC sprites are 32px tall (2 vertical tiles); their true collision/interaction tile is always the bottom half (feet/shadow), while their head overlaps `y - 1`.
- **Turn-in-Place Delay**: When turning to face an adjacent obstacle/NPC without stepping onto a new tile, include `"sleep 300"` between the directional input and `"A"`, otherwise `"A"` fires during the 8-frame turn animation and is ignored.
- **Old Rod Timing (`Task_Fishing`)**:
  - Cast animation before the 1st dot takes ~1.5s, and each of the 3..10 dots takes ~0.33s (`3 dots = 2.5s` .. `10 dots = 4.8s`), with a ~0.55s `"Oh! A bite!"` window.
  - **Battle-Safe Multi-Cast Loop**: Chaining `Select, sleep <3300..4800>, A, sleep 1200, B, sleep 1000` across multiple casts in a single `press_buttons` call is 100% battle-safe: once a cast hooks a fish (`"A"` -> `"A POKEMON's on the hook!"` -> `"B"` starts the battle), any remaining `A` + `B` pairs harmlessly open and close the `FIGHT` menu without using a move (verified Turn 182 when hooking Lv 5 Azurill at `4500ms`).
- **Pokemon Center Healing**: Standing at `(7, 4)` facing `Up` at Nurse Joy, it takes **4 `A` presses** (`1st A` interacts, `2nd A` advances `"Welcome..."`, `3rd A` advances `"Would you like me to rest your POKEMON?"` to `>YES`, `4th A` confirms `>YES` and starts the `~4500ms` healing fanfare), followed by **3 `B` presses** (`sleep 800` apart) to finish her farewell dialogue, and `Down x5` to exit the Pokemon Center.
- **Poke Mart Purchasing**: Entering a Poke Mart places the player at `(3, 7)`; walk `Up x4` to `(3, 3)` and face `Left` (`sleep 300, A`) to speak with the clerk across the counter at `(2, 3)`. Poke Balls cost only `$10` each (`$100` for 10 + 1 bonus Premier Ball). After pressing `A` on an item in the `BUY` list, wait `sleep 800` for `"How many would you like?"` and the `x01` box to open before pressing `Right` (`+10`) or `Up` (`+1`). After confirming a 10+ ball purchase, it takes **6 `B` presses** (`Thank you -> Premier Ball -> BUY list -> Anything else -> QUIT -> Please come again!`) to return to overworld control, and `Down x5` from `(3, 3)` exits the Mart.
- **Party Menu Fade-In & Navigation**:
  - Opening the Party menu (`Start -> POKEMON` or `BAG -> USE`) takes ~800ms to fade in; directional inputs sent within 300ms of opening are ignored during the fade-in.
  - `BAG -> USE` remembers the last active Party `slotId` (including slots selected during a prior `GIVE`), whereas `Start -> POKEMON` and `BAG -> GIVE` always open at `slotId = 0` (Slot 1).
  - `Down` steps sequentially (`Slot 1 -> Slot 2 -> ... -> Last Slot -> CANCEL -> Slot 1`), `Up` steps in reverse (`Slot 1 -> CANCEL -> Last Slot`), and `Left` from any slot (`Slots 1..6`) deterministically clamps the cursor onto `Slot 1` (`slotId = 0`).
- **Battle Menu Action Cursor, Move Clamping & Bag/Battle Exit Timing**: At the start of every new battle turn (`What will [POKEMON] do?`), the action cursor always resets to `>FIGHT` (top-left, index 0). It only remains on `>BAG` or `>POKEMON` if you cancel out of the Bag or Party screen with `B` during the same turn, or after a failed Poke Ball throw (`>BAG`). Inside `FIGHT`, the 2x2 move grid (`1: Top-Left`, `2: Top-Right`, `3: Bottom-Left`, `4: Bottom-Right`) resets to Slot 1 (`Top-Left`) when a Pokemon switches in from the back row and **never wraps**, so always clamp explicitly (`Up, Left` for Slot 1, `Up, Right` for Slot 2, `Down, Left` for Slot 3, `Down, Right` for Slot 4). Closing the Bag in battle with `B` takes `~1000ms` to fade back to the battle menu; exiting a trainer battle back to the overworld after `"got $X for winning!"` takes `~2500ms` before `Start` or movement inputs are accepted.
- **Berry Tree Harvesting & Auto-Refill Rule**: Interacting with a Berry Tree takes **3 `A` presses** (`Interact -> "You found N [X] BERRIES!" -> "Do you want to pick the [X] BERRIES? [>YES]"`), followed by `sleep 3500` for the fanfare and **2-3 `B` presses** (`sleep 1500` apart) to dismiss the put-away and loamy-soil messages.
  - **Auto-Refill Trigger**: The harness refills any Berry currently in the Bag (`quantity >= 1`) to 99 at the **turn boundary** in the overworld. Never consume the last copy (`x 1 -> x 0`) of a newly picked Berry before ending a turn in the overworld, or it will be removed from the Bag before auto-refilling.
  - **Loamy Soil `USE` Trap**: Selecting `USE` on a Berry in the `BERRIES` pocket while facing a soft, loamy soil patch in the overworld automatically plants the Berry into the soil and exits the Bag/Start menu to the overworld instead of opening the Party menu. Always turn away or step off the loamy soil before selecting `USE` on a Berry.
- **Overworld Item Balls**: Picking up an item ball displays **2 text boxes**: `"[PLAYER] found one [ITEM]!"` (`~2500ms` fanfare + `A`/`B`) followed by `"[PLAYER] put away the [ITEM] in the [POCKET]."` (`~1000ms` + `A`/`B`).

<hr>

<h1><code>Scratchpad/Routing</code></h1>

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
  - **Youngster Calvin** `(33, 14)`
  - **Bug Catcher Rick** `(25, 15)`
  - **Lass Tiana** `(15, 5)`
  - **Bug Catcher Allen** `(13, 2)`
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
  - **Southern Pond**: Located at `x=6..11, y=22..25`; stand at `(12, 23)` facing `Left` at `(11, 23)` to fish with Old Rod.
  - **Western Exit (to Route 104)**: Straight west along `y=12..13` past `(8, 12)` to `x=0` (triggers Scott cutscene near `x=4`).

## Route 104 (South)
- **Eastern Entrance**: Enters from Petalburg City at `(36, 62)`.
- **Tall Grass Patch**: Located at `(22..24, 56..61)`.
- **Beach Staircase**: Located at `(28..29, 70)` (northern beach stairs at `(17..18, 55)`).
- **Trainers & NPCs**:
  - **Friendly Boy** at `(28, 74)` on the shoreline.
  - **Bird Keeper Billy** at `(23, 66)` facing `Left` (3 Pokemon: `Pidgey` Lv 7 [holds `Berry Juice`], `Wingull` Lv 7 [`Supersonic`, `Water Gun`, `Gust`], `Taillow` Lv 7).
  - **Friendly Fisherman** at `(15, 60)` facing `Right`.
  - **Fisherman Darian** at `(15, 59)` facing `Right` (4 Pokemon: `Magikarp` Lv 9 [`Bounce`], `Feebas` Lv 8 [`Icy Wind`, `Facade`, holds `Sitrus Berry`], `Goldeen` Lv 7 [`Swift Swim`; `Rain Dance`, `Peck`, `Horn Attack`, `Dive`], `Luvdisc` Lv 7 [`Attract`]).
- **Mr. Briney's Cottage & Northern Berry Patch**:
  - Cottage door at `(17, 51)`.
  - **Berry Trees**: Located at `(22, 41)` (`Oran Berry`) and `(24, 41)` (`Pecha Berry`).
  - **Lady Cindy** at `(11, 40)` facing `Left` outside Petalburg Woods (3 Pokemon: `Cleffa` Lv 8 [`Metronome`], `Pichu` Lv 8 [`Thunder Wave`, `ThunderShock`], `Azurill` Lv 7 [`Uproar`]).

## Petalburg Woods
- **Southern Entrance**: Enters from Route 104 `(10..11, 38)` onto `(16, 38)` inside Petalburg Woods.
- **Tall Grass Patches (South)**:
  - South-East patch at `(20..25, 32..35)`.
  - South-West patch at `(7..13, 27..33)`: column `x=6` (`y=35 -> 24`) is a grass-free northbound corridor around the west edge of this patch.
- **NPCs, Trainers & Items**:
  - **Bug Maniac Lyle** at `(13, 35)` (spinning trainer west of southern entrance; 3 Pokemon: `Spinarak` Lv 8 [`Mega Drain`, `Spider Web`, holds `Berry Juice`], `Ledyba` Lv 8 [`Supersonic`, `Mach Punch`], `Venonat` Lv 8 [`Stun Spore`, `Confusion`]).
  - **Bug Catcher James** at `(10, 24)` (spinning trainer in straw hat north of south-west grass patch; 3 Pokemon: `Paras` Lv 9 [`Spore`, `Aerial Ace`], `Nincada` Lv 9 [`Aerial Ace`, `Giga Drain`], `Surskit` Lv 8 [`Mega Drain`]).
  - **Southeastern Exit (to Route 104 Plateau)**: Gate at `(36..37, 38..40)` exits to Route 104 `(32, 45)`; `Poke Ball` item ball at `(29, 53)`.
  - **Grass-Free Path to Central Clearing**: From Bug Catcher James at `(10, 25)`, step `Down` to `y=26`, walk `Right` along `y=26` to `(26, 26)` (bypassing tall grass at `(18..24, 24..25)`), and walk `Up` along `x=26` to `(26, 23)`.
  - **Team Magma Grunt Ambush** at `(26, 23)` (Devon Researcher rewards `Great Ball`):
    - Team (5 Pokemon): `Magnemite` (Lv 8, `Flash Cannon`, `Thunder Wave`, `ThunderShock`), `Houndour` (Lv 9, `Super Fang`, `Pursuit`, `Ember`), `Bagon` (Lv 8, `Headbutt`), `Koffing` (Lv 8, `Protect`, `Thief`), `Duskull` (Lv 8, `Protect`, `Shadow Sneak`, holds `Leftovers`).
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
    - Team (3 Pokemon): `Snubbull` (Lv 8, `Metronome`, holds `Oran/Sitrus Berry`), `Growlithe` (Lv 8, `Rock Smash`, `Ember`, holds `Berry Juice`), `Electrike` (Lv 8, `ThunderShock`, holds `Oran Berry`).
  - **Wooden Bridge & Cut Item**: Runs north from `x=30..31, y=21`. A Cut tree at `(35, 22)` east of the bridge blocks an item ball at `(37, 22)`.
  - **Lass Haley** at `(32, 22)` facing `Left` (mandatory trainer watching bridge entrance at `(30..31, 22)`):
    - Team (3 Pokemon): `Skitty` (Lv 9, `Sing`, `Assist`), `Oddish` (Lv 9, `Protect`, `Acid`, `Mega Drain`), `Vulpix` (Lv 9, `Ember`, `Disable`).
  - **Twins Gina & Mia** at `(27..28, 15)` facing `Down` onto `(27..28, 16)` (mandatory Double Battle on horizontal bridge section):
    - Team (2 Pokemon): `Smeargle` (M, Lv 8, `Follow Me`) & `Smeargle` (M, Lv 8, `Focus Punch`).
  - **PKMN Trainer Red** at `(29, 8)` facing `Left` across `(24..28, 8)` (mandatory 5-tile vision trainer at northern exit of bridge):
    - Team (6 Pokemon): Lead `Eevee` (M, Lv 9, 31 Max HP, `Curse`, `Rest`, `Snore`, `Quick Attack`, holds `Sitrus Berry`), plus 5 remaining Pokemon.

<hr>