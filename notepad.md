<h1><code>Main</code></h1>

# Main Notepad

## Game Info
- **Version:** Pokémon Blue Version (colorized GBC ROM with battle EXP bar visible under HP; verify any QoL features in-game)
- **Trainer:** NEON | **Rival:** RED
- **Options:** Text Speed FAST, Battle Animation OFF, Battle Style SHIFT (verified turn 16)
- **Progress:** Delivered Oak's Parcel and received Pokédex in Pallet Town (turn 75); returning north via Route 1 to Viridian City to heal and buy Poké Balls/Antidotes before Route 22 & Viridian Forest

## Harness / Input Notes
- Emulator runs continuously during thinking/fade transitions; transitions like stairs/fades complete quickly after landing on the warp tile (adding a trailing `sleep 500` after a warp lets the new map settle).
- `B` advances Gen 1 dialogue without accidentally selecting menu options; `hold B 500` + `B` fast-forwards multi-box dialogue safely.
- In battle: the cursor inside `FIGHT` persists on the last used move. Include `sleep 200` between `A` (open `FIGHT`) and `A` (confirm move) so both presses register reliably. Stat-change messages and `Critical hit!` display a `▼` prompt requiring a button press (`B`/`A`).
- In `run_code`: `mgba.get_coordinates()` still returns the last overworld coordinates during a battle; to verify a battle ended mid-script, issue a single movement step and confirm coordinates actually changed before running a multi-step walk.
- Overworld tiles: flat brown tile with two tiny white dashes embedded in a ledge row is a walkable gap/passage (verified Route 1 `(5,19)` turn 55 and Viridian City `(19,27)` turn 68).
- Pokémon Center Nurse Joy (at `(3,3)` facing Up): requires 6 `A` presses spaced by ~500ms to get past `"Welcome..."`, `"We heal your POKéMON"`, `"back to perfect health!"`, and select `HEAL`, followed by ~4.5s for healing animation, then `B` presses to finish (verified turn 83 filmstrip).

## Party
- **RIPTIDE** (Squirtle) - Lv 8 (HP 25, Atk 14, Def 16, Spd 12, Spc 13; Tackle, Tail Whip, Bubble) — learned Bubble at Lv 8 on Route 1 (turn 82)

## Badges
- 0/8

## Notepad Index
- `notepads/Main.md` - High-level dashboard and index


<hr>