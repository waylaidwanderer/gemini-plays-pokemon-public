<h1><code>Locations/Encounters</code></h1>

# Encounter Tracker — Attempt #1

## Rules Reminder
- One encounter per "Met in" location (shared across grass, water, fishing, starter, and gifts).
- Dupes Clause active across evolution families obtained in Attempt #1.

## Locations & Encounters
*(None recorded yet)*

<hr>

<h1><code>Main</code></h1>

# Nuzlocke Dashboard — Attempt #1

## Run Status
- **Attempt:** #1
- **ROM Hack:** TBD (verifying on title screen)
- **Active Level Cap:** Lv 16 (Roxanne — Rustboro Gym)
- **Battle Style:** `SET` & Text Speed `FAST` (Verified in-game Start Menu Turn 19)

## Level Cap Schedule
- Roxanne (Rustboro): Lv 16
- Brawly (Dewford): Lv 20
- Wattson (Mauville): Lv 29
- Flannery (Lavaridge): Lv 42
- Norman (Petalburg): Lv 48
- Winona (Fortree): Lv 55
- Tate & Liza (Mossdeep): Lv 70
- Wallace / Juan (Sootopolis): Lv 77
- Champion: Lv 100

## Notepad Index
- `Locations/Encounters` — Nuzlocke encounter tracker by "Met in" location & Dupes Clause registry

<hr>

<h1><code>Scratchpad/Notes</code></h1>

# Scratchpad — UI & Routing Notes

## Verified UI Timings
- **Screen Fades (Bag / Options / Naming):** ~1.8s. Append `sleep 2200` + a harmless input (e.g. `Up` at top of menu) so `<CurrentScreen>` settles after the fade completes rather than mid-black-screen.
- **Naming Screen (`Select` page toggle):** Animation takes ~500ms; use `sleep 800` after `Select` before moving cursor. Columns are contiguous (`A B C D E F` = cols `0..5`, no gap column between `C` and `D`). Saying `NO` to Birch's name confirmation resets back to Boy/Girl selection.
- **Options Menu Binary Toggles:** `Left` and `Right` both wrap/toggle 2-state options (`BATTLE STYLE`, `BATTLE SCENE`, `SOUND`, `BUTTON MODE`). Always visually inspect `OPTION` before pressing `Left`/`Right`. Options set on Title Screen Main Menu DO persist into `NEW GAME`.
- **Starting Bag:** All 5 pockets (`ITEMS`, `POKé BALLS`, `TMs & HMs`, `BERRIES`, `KEY ITEMS`) verified empty at game start (Turn 20).

<hr>