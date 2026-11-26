# Route 10 South, Lavender Town & Route 8 — Verified Coordinates

## Route 10 South -> Lavender Town (Verified Turns 574–577)
- **Rock Tunnel South Exit**: `Rock Tunnel 1F (15, 33)` warps outside to **`Route 10 South (8, 54)`** *(Jr. Trainer♀ Heidi stands at `(7, 54)` facing `Down`)*.
- **Zero-Battle Path to Lavender Town**:
  1. Walk east `Right * 6` from `(8, 54)` -> `(14, 54)` and south `Down * 9` -> `(14, 63)`.
  2. **Pokémaniac Herman** stands at `(14, 64)` facing `Left`; slip behind his back via **`(15, 63) -> (15, 65) -> (11, 65)`**.
  3. Hop the south-facing ledge at **`(11, 67)`** -> `(11, 69)`, step west to `(9, 69)`, and walk south down `x = 9` into **`Lavender Town (9, 0)`**.

## Lavender Town (Verified Turns 577–579)
- **North Entrance**: `(9, 0)` (from Route 10).
- **Lavender Pokémon Center**: Door at **`(3, 5)`** *(Note: watch for wandering villager around `(7, 6..7)` when walking west along `y = 6`; verify `mgba.get_coordinates() == {'x': 3, 'y': 7}` upon entering)*.
- **Pokémon Tower**: East side `(12..17, 0..5)`, door at `(14, 5)`.
- **West Exit to Route 8**: Walk west along `y = 8..9` (`x = 0 -> Route 8 (59, 8)`).

## Route 8 (East -> West, Verified Turns 579–588)
- Enters from Lavender Town at **`Route 8 (59, 8)`**; upper `(53, 4)` is a closed flower alcove.
- Drop south through the fence gate at **`(54..55, 10)`** to **`y = 14`** and head west:
  - **Gambler Rich** (`Growlithe Lv 24, Vulpix Lv 24`): stands at `(46, 13)` facing `Down` across the fence and spots `(46, 14)` (defeated Turn 583).
  - At **`x = 42..43`**, the paved avenue turns north (`y = 14 -> y = 4..5`):
    - **Super Nerd Glenn** (`Grimer Lv 22, Muk Lv 22, Grimer Lv 22`): stands at `(42, 6)` facing `Up` and spots `(42, 4)` (Turns 584–588; note `Muk` & `Grimer` carry `Disable`, so wrap to a secondary move if `Slot 0` gets Disabled!).
  - Continue west along `y = 4` to **`(29, 4)`** (4-Trainer Wall):
    - **Super Nerd Leslie** (`Koffing Lv 26`) stands at `(26, 4)` facing `Right` and walks to `(28, 4)` (defeated Turn 590; `NAUTILUS` reached Lv. 33).
    - Step south to `(29, 5)`, west to `(27, 5)` *(trainer at `(26, 5)` faces `Left`!)*, and south down **`x = 27`** (**Lass Megan** at `(26, 6)`: `5x Lv 19` Pokémon, defeated Turn 593) to `(27, 14)`.
  - Walk west along `y = 14` to `(12..14, 14)`, bypass **Gambler Stan** (`(13, 9)` facing `Up`) via **`x = 14`**, and enter the **Underground Path (7–8) East Gatehouse at `(13, 3)`** (`indoor stairs at (4, 4)`).
- **Underground Path (7–8) & Route 7 -> Celadon City (Verified Turns 596–600)**:
  - Tunnel runs from **`(47, 2)`** (east) to **`(2, 4)`** (west stairs -> Route 7 Gatehouse `(4, 4)` -> exits to `Route 7 (5, 14)`).
  - On **Route 7**: walk around the east side of the gatehouse (`x = 8`) to `(4, 8)`, climb the **wooden stairs at `(4, 7)`** onto the upper plateau `(4, 3)`, and walk west (`x = 0, y = 3`) into **`Celadon City (49, 11)`**.
