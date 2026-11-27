# Cinnabar Island & Pokémon Mansion — Verified Coordinates & Notes

## Route 21 Water Route (`Pallet Town -> Cinnabar Island`, Verified Turns 1081–1084)
- From `Pallet Town (5, 6)`, walk around the `(4..7, 9)` fence via `(3, 8) -> (3, 12) -> (5, 13)` and `Surf` south onto `(5, 14)`.
- Bypass the `(4..7, 24..25)` fishing pier on the east via `x = 9` (`y = 23..28`), return to `x = 5`, and pass behind the Swimmer at `(5, 71)` (facing `Right`) via **`x = 4`** down to `Route 21 (4, 89)`.
- Surf east along `y = 89` to `(11, 89)` and south into **`Cinnabar Island (11, 7)`** with zero trainers fought.

## Cinnabar Island Landmarks (Verified Turns 1084–1085, 1864–1866)
- **Pokémon Mansion**: Door at **`(6, 3)`** (`spawns at 1F (5, 27)`). Note `Cinnabar Lab` occupies `(4..9, 6..9)` with a signpost at `(9, 11)` blocking `x = 9` from the south.
- **Cinnabar Pokémon Center**: Door at **`(11, 11)`**.
- **Cinnabar Poké Mart**: Door at **`(15, 11)`** (`exit mat at (3..4, 7)`; sells `0: Ultra Ball ¥1200, 1: Great Ball ¥600`).
- **Cinnabar Gym**: Door at **`(18, 3)`** *(requires `Secret Key` from Pokémon Mansion B1F)*.
- **Cinnabar `Super Rod` Spot**: Stand at **`(4, 11)` facing `Down`** at north-shore water curb `(4, 12)` (`open neighbor (5, 11)` to the right).

## Pokémon Mansion (`Secret Key` Route, Verified Turns 1085–1091)
- **1F -> 2F**: Walk straight north up the grand carpet `(5, 27) -> (5, 10)` -> arrives at **`2F (5, 11)`** (`zero trainers`).
- **2F -> Northern 3F**: Gate at `2F (9, 4..5)` is open by default; walk `(5, 11) -> (10, 11) -> (10, 4) -> (6, 4) -> (6, 1)` -> arrives at **`3F (6, 2)`** *(note: `2F (7, 10)` leads only to an isolated 3F diary alcove)*.
- **3F -> Southeast 1F -> B1F (`Turns 1091–1112`)**:
  - **Statue Facing Rule**: Statues ONLY respond from the **front tile `(sx, sy + 1)` facing `Up`** (`side interaction is a silent no-op`).
  - Walk `(6, 2) -> (8, 3) -> (11, 3) -> (13, 6) -> (10, 6)` facing `Up` to toggle **`3F (10, 5)`**, then walk `(13, 6) -> (13, 11) -> (16, 11) -> (16, 14)` to drop into **southeast `1F (16, 14)`**.
  - On **southeast `1F`**, walk `(12, 14) -> (12, 24) -> (20, 24) -> (20, 21)` *(optional `Full Restore` at `(18, 21)`)* -> `(21, 16) -> (21, 23)` down-stairs into **`B1F (23, 22)`**.
  - **Zero-Trainer `B1F` Route (`Turns 1110–1124`)**: Walk `(22, 22) -> (22, 9) -> (12, 9) -> (12, 15) -> (16, 15) -> (16, 19) -> (18, 19) -> (18, 23)` *(pick up `TM14 Blizzard` at `(19, 25)`)* -> pass behind Burglar Lewis `(16, 23)` via `x = 17` to `(18, 26)` and toggle **`B1F (18, 25)`**. Exit west over Lewis's head through **`(13, 22)`**, loop east over the journal room `(10, 22) -> (10, 15) -> (24, 15) -> (24, 18) -> (26, 18)`, and walk north up **`x = 26`** through `(26, 17)` (past Scientist Ivan at `(27, 11)`) to **`(26, 6)`**.
  - **Western `B1F` Vault (`Turns 1115–1124`)**: From `(26, 6)`, walk west `(26, 4) -> (12, 4)` and stand at **`(13, 6)` facing `Up`** to toggle **`B1F (13, 5)`** (opens gate `(5..6, 8)`). Note: the table ball at `(5, 4)` is **`TM22 (SolarBeam)`**, whereas the **`SECRET KEY`** sits south through `(5..6, 8)` on the pedestal at **`B1F (5, 13)`**! Use `Dig` immediately after collecting `Secret Key` to warp straight outside Cinnabar Center `(11, 12)`.

## Cinnabar Gym — 6-Quiz Zero-Trainer Route (`Turns 1124–1133`)
- Unlock `(18, 3)` with `Secret Key` and enter at `(16, 16)`.
- **Quiz Answering Recipes**:
  - **`YES`**: `["A", "sleep 1100"] * 12 + ["B", "sleep 900"] * 4`
  - **`NO`**: `["A", "sleep 900"] + ["B", "sleep 800"] * 15`
- **All 6 Quiz Machines & Answers**:
  1. **Room #1 `(15, 7)`** (from `(15, 8)` facing `Up`): *"CATERPIE evolves into BUTTERFREE?"* -> **`YES`** -> opens `(18..19, 6)` (`walk (18, 6) -> (18, 1) -> (12, 1)`).
  2. **Room #2 `(10, 1)`** (from `(10, 2)` facing `Up`): *"There are 9 certified POKéMON LEAGUE BADGEs?"* -> **`NO`** -> opens `(12..13, 6)`.
  3. **Room #3 `(9, 7)`** (via `(12, 7) -> (10, 7) -> (10, 8) -> (9, 8)` facing `Up`, behind Trainer `(11, 8)`): *"POLIWAG evolves 3 times?"* -> **`NO`** -> opens `(12..13, 12)`.
  4. **Room #4 `(9, 13)`** (via `(12, 13) -> (10, 13) -> (10, 14) -> (9, 14)` facing `Up`, behind Trainer `(11, 14)`): *"Are thunder moves effective against ground element-type POKéMON?"* -> **`NO`** -> opens `(8, 16..17)` west into `(5, 16)`.
  5. **Room #5 `(1, 13)`** (via `(5, 16) -> (5, 13) -> (2, 13) -> (2, 14) -> (1, 14)` facing `Up`, behind Trainer `(3, 14)`): *"POKéMON of the same kind and level are not identical?"* -> **`YES`** -> opens `(4..5, 12)`.
  6. **Room #6 `(1, 7)`** (via `(4, 10) -> (4, 7) -> (2, 7) -> (2, 8) -> (1, 8)` facing `Up`, behind Trainer `(3, 8)`): *"TM28 contains TOMBSTONER?"* -> **`NO`** -> opens `(4..5, 6)` into **Gym Leader Blaine's Chamber (`Blaine at (3, 3)`)**.
  - Dedicated straight exit corridor runs south down **`x = 7`** (`(7, 1) -> (7, 16)`).

## `Fly` Town Map Fixed Internal Order (`Verified Turns 1115–1116`)
- Town Map `Fly` follows internal `MapId` order (`Saffron City` `0x0A` is LAST, after `Cinnabar Island` `0x08`):
  - `Up * 1` from `0 Pallet` = **`Viridian City`**
  - `Up * 6` from `0 Pallet` = **`Celadon City`**
  - `Down * 1` from `0 Pallet` = **`Saffron City`**
  - `Down * 2` from `0 Pallet` = **`Cinnabar Island`**

## Cinnabar Pokémon Lab & Fossil Revival (`Verified Turns 1534–1550`)
- **Cinnabar Lab Entrance**: Door at **`Cinnabar Island (6, 9)`** (`spawns in hallway at (2, 7)`).
- **Fossil Research Room (`3rd Door`)**: Walk `(2, 7) -> (2, 5) -> (16, 5) -> Up` into `(16, 4)` (`spawns at (2, 7)`).
  - *Note*: `(7, 6)` is the `Ponyta <-> Seel` NPC trader; the **Fossil Scientist** wanders across the entire top band **`x = 0..7, y = 2..3`** (the green vertical-striped tiles `(0..3, 2..3)` are walkable lab rugs!).
  - Handing over a fossil (`Helix Fossil`, `Dome Fossil`, or `Old Amber` from Pewter Museum Back Entrance `Pewter (19, 5)` via `(31, 7)` stairs + `(26, 4)` `Cut` bush -> Scientist at `(15, 2)`) requires stepping outside Cinnabar Lab to `(6, 10)` and re-entering to claim the `Lv. 30` revived Pokémon *(and stepping outside once more before reviving a second fossil)*.
