<h1><code>Main</code></h1>

# Main Notepad

## Game Info
- **Version:** Pokémon Blue Version (colorized GBC ROM with battle EXP bar visible under HP; verify any QoL features in-game)
- **Trainer:** NEON | **Rival:** RED
- **Options:** Text Speed FAST, Battle Animation OFF, Battle Style SHIFT (verified turn 16)
- **Progress:** Defeated Gym Leader Brock in Pewter City Gym (turn 180) for the **Boulder Badge** and **TM34 (Bide)**; heading out to heal/restock in Pewter City and traverse Route 3 & Mt. Moon toward Cerulean City.

## Harness / Input Notes
- Emulator runs continuously during thinking/fade transitions; transitions like stairs/fades complete quickly after landing on the warp tile (adding a trailing `sleep 500` after a warp lets the new map settle).
- `B` advances Gen 1 dialogue without accidentally selecting menu options; `hold B 500` + `B` fast-forwards multi-box dialogue safely.
- In battle: the cursor inside `FIGHT` persists on the last used move. Include `sleep 200` between `A` (open `FIGHT`) and `A` (confirm move) so both presses register reliably. Stat-change messages and `Critical hit!` display a `▼` prompt requiring a button press (`B`/`A`).
- In `run_code`: `mgba.get_coordinates()` still returns the last overworld coordinates during a battle; to verify a battle ended mid-script, issue a single movement step and confirm coordinates actually changed before running a multi-step walk.
- Overworld tiles: flat brown tile with two tiny white dashes embedded in a ledge row is a walkable gap/passage (verified Route 1 `(5,19)` turn 55 and Viridian City `(19,27)` turn 68).
- Pokémon Center Nurse Joy (at `(3,3)` facing Up): requires 6 `A` presses spaced by ~500ms to get past `"Welcome..."`, `"We heal your POKéMON"`, `"back to perfect health!"`, and select `HEAL`, followed by ~4.5s for healing animation, then `B` presses to finish (verified turn 83 & 86 filmstrips).
- Poké Mart BUY flow: `A` (open qty `x01`) -> `Up`*(N-1) -> `A` (`"That will be ▼"`) -> `A` (`"¥XXXX. OK?" YES/NO`) -> `A` (confirm `YES` -> `"Here you are! Thank you!"`) -> `B` (return to item list) (verified turn 86 filmstrip).
- Battle `PKMN` switch cursor persists on the last switched-in slot, so swapping back to slot 1 after switch-training slot 2 requires `Up` before `A` (verified turn 122-123).
- Wild battle RUN timing: after pressing `B` on `"Wild X appeared!"`, `"Go! <PKMN>!"` takes ~3.2s before the Battle Menu accepts inputs (`sleep 3500`, then `Down`, `sleep 200`, `Right`, `sleep 200`, `A`, `sleep 1000`, `B`, `sleep 1500`) (verified turn 139).

## Party
- **RIPTIDE** (Squirtle) - Lv 13 (30/35 HP; Atk 20, Def 23, Spd 16, Spc 18; Tackle, Tail Whip, Bubble) — swept Brock's Geodude & Onix (turn 180)
- **KAISER** (Nidoran♂) - Lv 3 (16/16 HP; Leer, Tackle; caught Route 22, switch-trained vs Bug Catcher #1 Caterpie, turn 125; evolve to Nidorino at Lv 16 -> Nidoking with Mt. Moon Moon Stone)

## Badges
- 1/8: **Boulder Badge** (Pewter City, turn 180)

## Notepad Index
- `notepads/Main.md` - High-level dashboard and index


<hr>