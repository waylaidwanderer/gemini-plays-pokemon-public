# Littleroot Town — Coordinates & Points of Interest

## Overworld Coordinates
- **Player's House Door (Left House):** `(5, 8)`
- **Rival May's House Door (Right House):** `(14, 8)`
- **Clear East-West Path between Houses:** `y = 9` from `x = 5` to `x = 14`

## Player's House
- **1F Stairs to 2F:** `(8, 2)`
- **1F Exit Mat:** `(8, 8)` / `(9, 8)`
- **2F Stairs to 1F:** `(7, 1)` (arrives at `(7, 2)`)
- **2F Wall Clock:** `(5, 1)` (interact from `(5, 2)` facing Up; confirmation defaults to `NO`, press `Up` then `A` for `YES`)
- **2F Desk PC:** `(0, 1)` (interact from yellow chair at `(0, 2)` facing Up; free Potion x1 withdrawn on Turn 17)

## Rival May's House (Professor Birch's House)
- **1F Entrance Mat:** `(1, 8)` / `(2, 8)` (exiting steps automatically to `(14, 9)` outside)
- **1F Stairs to 2F:** `(2, 2)`
- **2F Stairs to 1F:** `(1, 1)` (arrives at `(1, 2)`)
- **2F May's Poké Ball:** `(5, 4)` (interacting from `(4, 4)` triggers May's entrance and introduction)

## Northern Exit to Route 101
- **North Road:** `x = 10` (or `x = 11`), walking north from `y = 9` to `y = 0` transitions into Route 101.

## Professor Birch's Pokémon Lab
- **Exterior Door:** `(7, 16)` in Littleroot Town (exiting steps to `(7, 17)`)
- **Interior Center Aisle:** `x = 6` from `y = 5` (Professor Birch at `(6, 4)`) straight south to the exit mat at `(6, 12)`.

## Post-Hall of Fame Littleroot Town Events
- **2F Bedroom (`LittlerootTown_BrendansHouse_2F`):** Continuing from the Title Screen after the Hall of Fame credits places the player at `(4, 2)` with the entire party fully healed and original party order restored. Walk `Right` 3 and `Up` 1 onto `(7, 1)` to descend to 1F.
- **1F S.S. Ticket & Roaming Eon Pokémon TV Broadcast (`LittlerootTown_BrendansHouse_1F`):** Descending to 1F triggers **Norman** to give the **S.S. Ticket** (`KEY ITEMS POCKET`) before departing through `(8, 8)`. The player then watches a TV emergency news flash about an unidentified flying Pokémon; **Mom** walks over to `(6, 5)` and asks its color (`[RED / BLUE]` — choosing `RED` releases roaming **Latias**, choosing `BLUE` releases roaming **Latios**) [Completed — **S.S. Ticket** obtained & **RED (Latias)** selected]. Because Mom stands at `(6, 5)` afterwards, walk around the left side of the dining table via `(5, 5) -> (2, 5) -> (2, 8) -> (8, 8)` to exit.
- **National Pokédex Upgrade (`LittlerootTown` & `LittlerootTown_ProfessorBirchsLab`):** Stepping outside Player's House into Littleroot Town automatically triggers **Professor Birch** and **Rival May** to escort the player into Professor Birch's Lab, where Professor Birch upgrades the Pokédex to **National Mode** [Completed].
- **Post-Reboot Turn-in-Place Note:** After the post-credits title screen reboot, `mgba.get_coordinates()` returns `None`, so the harness no longer auto-inserts turn-in-place taps; whenever changing facing direction in the overworld, include **1 extra directional tap** (`1` to turn in place + `N` to step `N` tiles).