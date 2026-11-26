# Main Notepad

## Game Info
- **Version:** Pokémon Blue Version (colorized GBC ROM with battle EXP bar visible under HP; verify any QoL features in-game)
- **Trainer:** NEON | **Rival:** RED
- **Options:** Text Speed FAST, Battle Animation OFF, Battle Style SHIFT (verified turn 16)
- **Progress:** Defeated Brock (turn 180, Boulder Badge + TM34), healed/restocked in Pewter City, and trained KAISER from Lv 3 to Lv 11 on Route 3 trainers (Colton, Ben, Greg); pushing east across Route 3 to Mt. Moon Pokémon Center.

## Harness / Input Notes
- Emulator runs continuously during thinking/fade transitions; transitions like stairs/fades complete quickly after landing on the warp tile (adding a trailing `sleep 500` after a warp lets the new map settle).
- `B` advances Gen 1 dialogue without accidentally selecting menu options; `hold B 500` + `B` fast-forwards multi-box dialogue safely.
- In battle: the cursor inside `FIGHT` persists on the last used move. Include `sleep 200` between `A` (open `FIGHT`) and `A` (confirm move) so both presses register reliably. Stat-change messages (`Harden`, `String Shot`, `Screech`, etc.) take ~4.5–5.0s total before printing their `▼` prompt, so allow `sleep 4800` before pressing `B` when chaining turns (verified turns 231–235).
- In `run_code`: `mgba.get_coordinates()` still returns the last overworld coordinates during a battle; to verify a battle ended mid-script, issue a single movement step and confirm coordinates actually changed before running a multi-step walk.
- Overworld tiles: flat brown tile with two tiny white dashes embedded in a ledge row is a walkable gap/passage (verified Route 1 `(5,19)` turn 55 and Viridian City `(19,27)` turn 68).
- Pokémon Center Nurse Joy (at `(3,3)` facing Up): requires 6 `A` presses spaced by ~500ms to get past `"Welcome..."`, `"We heal your POKéMON"`, `"back to perfect health!"`, and select `HEAL`, followed by ~4.5s for healing animation, then `B` presses to finish (verified turn 83 & 86 filmstrips).
- Poké Mart BUY flow: `A` (open qty `x01`) -> `Up`*(N-1) -> `A` (`"That will be ▼"`) -> `A` (`"¥XXXX. OK?" YES/NO`) -> `A` (confirm `YES` -> `"Here you are! Thank you! ▼"`) -> `B` (returns to BUY item list with cursor **reset to Slot 1**!) (verified turns 86 & 188 filmstrips).
- Battle Shift prompt: `"<TRAINER> is about to use <PKMN>!"` splits across two `▼` presses before `"Will NEON change POKéMON?"` YES/NO (verified turn 178 filmstrip).
- Pewter City navigation: Pewter Gym (`(16,17)`) is bounded south by a `y=21` tree wall (`x=4..17`) and east fence (`x=18, y=18..21`); travel north of the Gym (`x=10, y=13 -> x=19, y=13`) and down the main east avenue `x=19` to reach Pewter Pokémon Center (`(13,25)`) and Poké Mart (`(23,17)`) (verified turn 186).
- Battle `PKMN` and SHIFT (`"Bring out which POKéMON?"`) switch cursors both persist on the last switched-in slot within a battle (verified turns 122–123 & 198). Use `Left, Up` / `Right, Up` to reliably select `FIGHT` / `PKMN` regardless of previous Battle Menu cursor.
- Overworld Bag healing: after `A` heals a Pokémon (`"...recovered by 20!"`), 4 `B` presses exit cleanly (dismiss message -> close Party -> close Bag -> close Start Menu) (verified turn 208 filmstrip). Start Menu cursor resets to `POKéDEX` after battles/map transitions (verified turn 206).
- Wild battle RUN timing: after pressing `B` on `"Wild X appeared!"`, `"Go! <PKMN>!"` takes ~3.2s before the Battle Menu accepts inputs (`sleep 3500`, then `Down`, `sleep 200`, `Right`, `sleep 200`, `A`, `sleep 1000`, `B`, `sleep 1500`) (verified turn 139).

## Party
- **KAISER** (Nidoran♂, Lead/Slot 1) - Lv 11 (20/34 HP; Atk 18, Def 15, Spd 16, Spc 14; Leer, Tackle, Horn Attack [3/25 PP]; ~75% to Lv 12; evolve to Nidorino at Lv 16 -> Nidoking with Mt. Moon Moon Stone)
- **RIPTIDE** (Squirtle, Slot 2) - Lv 13 (30/35 HP; Atk 20, Def 23, Spd 16, Spc 18; Tackle, Tail Whip, Bubble [16/30 PP]; learns Water Gun at Lv 15, Wartortle at Lv 16)
- **Bag:** Poké Ball x9, TM34 (Bide), Potion x2, Antidote x3 | **Cash:** ~¥600+

## Badges
- 1/8: **Boulder Badge** (Pewter City, turn 180)

## Notepad Index
- `notepads/Main.md` - High-level dashboard and index
