# Harness & Emulator Mechanics (Verified)

## Tool Sequencing (Verified Turns 2–4)
- Top-level tool calls execute sequentially in the order emitted.
- Calling `mcp_game_press_buttons` followed by `read_file` on `screenshots/latest.png` in the same turn reliably reads the newly settled screen produced at the end of `press_buttons`.

## Real-Time Emulation Clock (Verified Turn 3 `filmstrip_1.png`)
- The emulator runs continuously in real time during `[THINKING]` (observed `#01 +0.00s` -> `#03 +28.53s` in Turn 3).
- Implications:
  - Keep deliberation concise to avoid unnecessary real-time drift in areas with wandering NPCs.
  - Static menus, dialogue prompts, and battle command menus safely wait for input regardless of elapsed thinking time.

## Gen 1 Dialogue Safety
- Pressing `B` advances standard `▼` text boxes and accelerates text scrolling without accidentally confirming `YES/NO` prompts (defaults to `NO`/cancel) or list menus like `YOUR NAME?` that disallow `B` cancellation.

## Gen 1 Naming Screen Grid (Verified Turn 6)
9 columns (`0..8`) x 5 character rows (`0..4`), cursor starts at `(0, 0)` (`A`):
- Row 0: `A B C D E F G H I`
- Row 1: `J K L M N O P Q R`
- Row 2: `S T U V W X Y Z [space]`
- Row 3: `× ( ) : ; [ ] PK MN`
- Row 4: `- ? ! ♂ ♀ / . , ED` (where `(8, 4)` is `ED` = End/Confirm; Note: filling max length auto-jumps cursor to `ED`!)
- Row 5: `lower case` toggle across bottom row.
- Reusable Python generator (for names shorter than max length: <7 for trainer/rival, <10 for Pokémon):
```python
ROWS = ["ABCDEFGHI", "JKLMNOPQR", "STUVWXYZ "]
def name_buttons(word):
    cx, cy, seq = 0, 0, []
    for ch in word:
        for ry, r in enumerate(ROWS):
            if ch in r: tx, ty = r.index(ch), ry; break
        seq += (["Right"]*(tx-cx) if tx>cx else ["Left"]*(cx-tx))
        seq += (["Down"]*(ty-cy) if ty>cy else ["Up"]*(cy-ty)) + ["A"]
        cx, cy = tx, ty
    return seq + ["Right"]*(8-cx) + ["Down"]*(4-cy) + ["A"]
```

## Event & Fanfare Timings (Verified Turns 2–41)
- **ROM Variant**: Colorized Pokémon Blue enhancement with GBC palettes and a live blue EXP bar under player HP in battle (verified Turn 27). Maps, items, and encounters match Pokémon Blue.
- **Battle Move Cursor Memory**:
  - **New Battle (Turn 1)**: BOTH the top-level command menu (`►FIGHT`) AND the `FIGHT` move submenu (`►Slot 1`) **reset to Slot 1** at the start of every new battle (verified Turn 97 `filmstrip_1.png` — earlier assumption that `FIGHT` remembered across battles was false!).
  - **Same Battle (Turn 2+)**: Within the same battle, the top-level command menu, `FIGHT` submenu, and `ITEM` submenu all remember their last selected positions (verified Turns 21, 67, 73).
  - *(Tip — Verified `Select` Swap Mechanics, Turns 110, 121, 125)*:
    - In the **`FIGHT` move menu**, `Select -> Down * k -> Select` swaps Slot `k` into Slot 0 and **automatically resets the cursor onto Slot 0** (and note: `FIGHT` wraps vertically, so pressing `Up` from Slot 0 wraps to the bottom move!).
    - In the **`ITEM` bag menu**, `Select -> Down * k -> Select` leaves the cursor at Slot `k`; always verify the highlighted item before pressing `A` after reordering items.
  - In `SHIFT` trainer battles, `B`-clearing between attack rounds safely declines `"Will COBALT change POKéMON?"` (`NO`). Use 8–10 `B` presses (`"sleep 650"`) per round when stat-drop or poison ticks occur (Turns 83, 95).
- **Catching & Nickname Safety (Verified Turns 66–75)**:
  - Never spam `B` after throwing a Poké Ball (`B` cancels `"give a nickname?"` as `NO`). Wait `"sleep 9500"` after throwing a Ball to inspect catch outcome, then advance Pokédex Page 1 & Page 2 with `A` up to the `►YES / NO` nickname prompt.
- **Evolution `B`-Cancel Warning & Verified Safe Evolution Recipe (Verified Turn 146)**:
  - Pressing `B` during a post-battle evolution animation (`"What? <POKEMON> is evolving!"`) **cancels the evolution** in Gen 1!
  - Evolution ONLY triggers **after the entire battle ends** (never mid-battle when KOing an earlier trainer Pokémon, and never if the evolving Pokémon faints before the battle ends).
  - Verified recipe when KOing the final opposing Pokémon on an evolution battle: execute the attack (`["A", "sleep 400", "A", "sleep 3500"]`), then use **ONLY `A`** (`["A", "sleep 1100"] * 6 + ["A", "sleep 10000", "A", "sleep 6000", "A", "sleep 1500", "A", "sleep 1500"]`) — `A` advances victory dialogue without ever cancelling evolution.
- **Gen 1 Battle Quirks (Verified Turns 137–139)**:
  - `Bubble` is 20 BP (half of `Water Gun`'s 40 BP), and 100%-accurate moves in Gen 1 still have a `1/256` miss chance (observed on `Water Gun` in Turn 139 `filmstrip_1.png` `#18`). Always verify KO outcomes before assuming fixed hit counts.
- **Coordinate Behavior in Battles & Warps**:
  - `mgba.get_coordinates()` continues returning the underlying overworld `(x, y)` during battles (`<GameState>` omits `<Position>` when in battle).
  - Step-by-step `before == after` comparison reliably detects wild encounters in tall grass; following a blocked grass step with `["sleep 800", "B"] * 8` (~6.4s) lands cleanly on `►FIGHT`.
  - Door warps have a ~0.5s white fade; ending a script immediately on a door step can capture the white transition frame before indoor coordinates update (Turn 41). Call `tools.observe()` or include a short post-warp settle when inspecting a new room.
- **Title Screen**: Pressing `Start` during a starter sprite swap is ignored; wait or append `"sleep 1500"` for the starter cry to finish before Main Menu input.
- **Pokémon Obtained Fanfare**: Lasts ~4.5 seconds before `"received a <POKEMON>!"` accepts `A`/`B` dismissal (`"sleep 3500"` was slightly early in Turn 18).
- **Cutscene Clearing**: Spacing `B` presses with `"sleep 700"`–`"sleep 900"` safely clears multi-box dialogues and lands cleanly on `►FIGHT` (in battles) or `YOUR NAME?` without triggering unwanted `YES` confirmations or attacks.

## Poké Mart & Pokémon Center Recipes (Verified Turns 52–62)
- **Poké Mart Buying (Requires THREE `A`s after Quantity!)**:
  1. Select item with `A`, `"sleep 900"` -> opens `×01` (`Up` increments quantity).
  2. `A` #1 (`"sleep 900"`) -> `"<ITEM>? ▼"`
  3. `A` #2 (`"sleep 900"`) -> `"That will be ¥<PRICE>. OK?"` `►YES / NO`
  4. `A` #3 (`"sleep 900"`) -> `"Here you are! Thank you! ▼"` (always verify `MONEY` box decreased before pressing `B`!).
  *(Misstep fixed in Turn 62: pressing only two `A`s before `B` cancels `YES/NO` as `NO`.)*
- **Pokémon Center Nurse Joy (`(3, 3)` facing `Up` — Requires FIVE `A`s & FOUR `B`s!)**:
  - `["A", "sleep 900"] * 4 + ["A", "sleep 8500"] + ["B", "sleep 700"] * 4` before stepping `Down` (verified Turn 162: only 3 `B`s left `"We hope to see you again!"` open during the `Down` loop).

## Navigation Scripting Guardrails & Cave Primitives (Verified Turns 53, 60, 152, 165–166)
- Always use bounded `for _ in range(N):` loops rather than unbounded `while` loops so an unexpected wall/NPC cannot trip the 150-button script abort limit.
- Never dodge `Down` when walking directly above a south-facing ledge (e.g., Viridian `y = 26`).
- **Gen 1 Menu Wrapping Summary (Verified Turns 124, 155, 184)**:
  - `Start` menu (`POKéDEX .. EXIT`) **wraps** vertically (`Up` from `POKéDEX` jumps to `EXIT`, `Down` from `EXIT` jumps to `POKéDEX`), and catching a new Pokémon resets `Start` to `POKéDEX`.
  - Battle `FIGHT` move menu **wraps** vertically.
  - `ITEM` bag menu **clamps** (does NOT wrap) at Slot 0 (`Up` at top stays on Slot 0).
  - Battle 2x2 command menu (`FIGHT / PKMN / ITEM / RUN`) **clamps** (`Left, Up` always lands on `►FIGHT`).
  - The 2x2 battle command menu (`FIGHT / PKMN / ITEM / RUN`) does **not** wrap, so `["Left", "sleep 150", "Up", "sleep 150"]` deterministically resets the cursor to `►FIGHT` from any quadrant, and pressing `Left` or `Up` while already on `►FIGHT` is a pure no-op in battle.
  - When a step `d` from `b` fails (`after == b`), clearing potential battle intro (`["sleep 1200"] + ["B", "sleep 700"] * 8`) and probing `back_d` (the known-open tile you just came from) cleanly distinguishes a **wall** (`pos != b`) from an active **battle** (`pos == b`), and in Gen 1 `PlayerSpeed >= EnemySpeed` guarantees 100% first-try escape via `RUN`.



