<h1><code>Locations/Encounters</code></h1>

# Nuzlocke Encounters (Attempt #1)

| Location | Pokemon | Nickname | Status | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Starter (Route 101) | Mudkip (M, Lv 10) | TRITON | Active | Bashful, Torrent; Moves: `Tackle`, `Bubble`, `Mud Sport`, `Water Gun`; Stats: 30/19/15/17/17/15 |
| Littleroot Town | TBD | TBD | Pending | Custom pond at `(17, 13..14)` — Old Rod fishing |
| Route 101 | TBD | TBD | Pending | Saw wild `Togepi` Lv 2 pre-Pokedex |
| Route 103 | TBD | TBD | Pending | Grass & Old Rod fishing available |
| Route 102 | TBD | TBD | Pending | Grass & Old Rod fishing available |

<hr>

<h1><code>Main</code></h1>

# Nuzlocke Dashboard — Attempt #1

## Active Rules & Status
- **Attempt**: #1
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configured & verified Turn 13; Text Speed `Fast`)
- **Unlimited Items**: Rare Candies & any acquired Berries auto-refill to 99 in the overworld.
- **Key Items Obtained**: `Pokedex`, `Running Shoes`, `Old Rod` (from Fisherman on Route 103 at `(20, 12)`).

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
- `Scratchpad/Routing`: Active early-game notes and routing

<hr>

<h1><code>Scratchpad/Routing</code></h1>

# Early Game Routing & Notes (Attempt #1)

## Littleroot Town
- **Protagonist**: AURORA (Female sprite -> Player house is East house; Rival Brendan's house is West house).
- **Bedroom (2F)**:
  - Stairs at `(1, 2)` (warp tile `(1, 1)`), Clock at `(3, 2)` facing Up (Note: Clock confirmation prompt defaults cursor to `NO`, must press `Up` to select `YES`).
  - PC at `(8, 2)` facing Up: Withdrew `Potion x1` (Note: takes 4 `B` presses after withdrawing to close the text box, item list, Item Storage menu, and top-level PC menu).
- **Town Landmarks**:
  - Player's House (East): `(14, 8)`; Rival's House (West): `(5, 8)`; Birch's Lab: `(7, 16)`.
  - Central vertical road runs along `x=10..11` from `y=17` north to `y=0` (Route 101).

## Route 101 — Starter Rescue
- **Starter Trio**: Treecko (Left), Torchic (Middle), Mudkip (Right). Chose **Mudkip**.
- **Birch Rescue Battle**: Wild `Zigzagoon Lv 2` knows `Swift` and holds `Berry Juice`; `Mudkip Lv 5` starts with only `Tackle` (no `Growl`). Takes 4 `Tackle`s total to KO through `Berry Juice`.
- **Route 101 Wild Table (Observed pre-Pokedex)**: `Togepi` (Lv 2).
- **Route 101 Grass-Free Path (South -> North)**: `(11, 19)` -> `Up x5` to `(11, 14)` -> `Left x4` to `(7, 14)` -> `Up x4` to `(7, 10)` -> `Right x6` to `(13, 10)` -> `Up` to `(13, 9)` -> `Right x2` to `(15, 9)` -> `Up` to `(15, 8)`, then through `(15, 7..5)` (3 grass tiles) to `(15, 4)` -> `Left x3` (2 grass tiles) to `(12, 4)` -> `Left` to `(10..11, 4)` -> `Up` into Oldale Town.
## Oldale Town
- Spoke to Poke Mart clerk at `(12, 14)` facing Right -> escorted to `(13, 8)` and received `Potion x1` (now `Potion x2`).
- Path to Route 103: From `(13, 8)`, walk `Left x3` to `(10, 8)` and `Up x9` onto Route 103.
## Route 103
- **Grass-Free Path (South -> North)**: From `(10, 21)`, walk `Up x8` to `(10, 13)`, `Right x4` to `(14, 13)`, `Up x3` to `(14, 10)`, and `Right x6` to `(20, 10)`.
- **Old Rod Fisherman**: Wanders in 2x2 box `(20..21, 11..12)` on the eastern beach of Route 103; speaking to him and answering `YES` grants the **`Old Rod`** early!
- **Path to Northern Plateau (Brendan at `(10, 3)`)**: From `(13, 7)`, walk `Left x7` to `(6, 7)` (or via `(6, 6)` to avoid the grass at `(5..6, 7)`), step to `(5, 6)`, walk `Up x3` along the grass-free gap at `x=5` (`y=6..3`) to `(5, 3)`, and `Right x4` to `(9, 3)` facing Brendan at `(10, 3)`.
- **Menu & Leveling Mechanics**:
  - Exiting Pokemon Summary takes 3 `B` presses to reach the Start menu (`Summary -> Party submenu -> Party slot list -> Start menu`) and a 4th `B` to close the Start menu.
  - Rare Candies can be chained from the Bag (`>RARE CANDY`) using `A` presses (`sleep 900`) as long as the target Pokemon has `< 4` moves.
  - Key Items submenu (`USE / REGISTER / CANCEL`) is arranged in 2 columns (`>USE` on left, `REGISTER` on right); press `A, Right, A` to register a Key Item to `Select` (press `Up` first if switching from an empty pocket like `BERRIES`, which clamps the cursor onto `CLOSE BAG`).
  - **Old Rod Timing**: Casting with `Select` prints 3–10 dots taking `2.0s–4.4s` before `"Oh! A bite!"` appears (which stays open for `1.0s`). Pressing `A` or `B` while dots are still printing cancels the cast (`"Not even a nibble..."`). Wait `~3500ms` after `Select` before pressing `A`.
- **Rival 1 Battle (Route 103)**: Defeated Brendan's `Treecko Lv 5` with Lv 10 `TRITON` (+69 EXP, +300 Pokedollars).
- **Fast Southbound Return (Route 103 -> Littleroot)**:
  - Route 103: From `(9, 3)`, step `Right` to `(10, 3)` and walk straight `Down` along `x=10` (jumping ledges at `y=5` and `y=12`) into Oldale Town `(10, 0)`.
  - Oldale Town: Walk straight `Down` along `x=10` (`y=0..19`) into Route 101 `(10, 0)`.
  - Route 101: Step `Left` to `(9, 0)`, walk straight `Down` along `x=9` (jumping ledges at `y=6` and `y=13`) to `(9, 14)`, then `Right x2` to `(11, 14)` and `Down x6` into Littleroot Town `(11, 0)`.

<hr>