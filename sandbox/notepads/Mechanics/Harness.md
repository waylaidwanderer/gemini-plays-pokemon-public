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
- **Catching & Nickname Safety (Verified Turns 66–75, 173–175, 230)**:
  - Never spam `B` after throwing a Poké Ball (`B` cancels `"give a nickname?"` as `NO`). Wait `"sleep 9500"` after throwing a Ball to inspect catch outcome.
  - Once `"All right! <POKEMON> was..."` appears, wait `"sleep 5500"` + `A` -> `"will be added for <POKEMON>!"`, then `["A", "sleep 2500", "A", "sleep 1200", "A", "sleep 1800", "A", "sleep 1200"]` lands directly on `"give a nickname?"` `►YES / NO`.
- **High-Density Cave Chunking & NPC Facing (Verified Turns 213, 228)**:
  - High-encounter floors (e.g., Mt. Moon B2F) trigger wild battles every ~6–8 steps; cap `run_code` cave marches at **18–20 steps max** so wild-flee animations never approach the 120s script timeout.
  - Rocket Grunts showing a solid horizontal orange stripe across the back of a black cap are facing **Up** (not Down).
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
  - **Pokémon Center Nurse Joy (`(3, 3)` facing `Up` — Max `sleep 10000` Cap, Poison-Faint Guard & Verify!)**:
  - **CRITICAL**: `"sleep <ms>"` has a strict **10,000 ms maximum** (`"sleep 10500"` / `"sleep 11500"` rejects the entire `press_buttons` call — root cause of failed heals in Turns 259 & 266!). To wait ~12s for a 4–6 Pokémon heal jingle without consecutive sleeps, use `"A", "sleep 9500", "B", "sleep 2500"`.
  - **Overworld Poison-Faint Edge Case (Turn 290)**: Poison ticks 1 HP every 4 steps; if a poisoned Pokémon hits `0` HP on the exact step onto `(3, 3)`, `"<POKEMON> fainted!"` opens and consumes the 1st `"A"`, causing the 5th `"A"` to stop on `►HEAL / CANCEL` where `"B"` cancels! Always visually verify green HP bars in `Start -> POKéMON` after healing.
  - After arriving cleanly at `(3, 3)` from `(3, 4)` + `"sleep 500"`, run `["A", "sleep 1000"] * 4 + ["A", "sleep 9500", "B", "sleep 2500"]` followed by `["B", "sleep 700"] * 3` and `Down * 5` (`(3,3) -> (3,7) -> outside`).
- **4-Move TM / Level-Up Move Replacement Sequence (Verified Turns 235–237)**:
  - Prompts: `"trying to learn <NEW>! ▼"` -> `"can't learn more than 4 moves! ▼"` -> `"Delete an older ▼"` -> `"move to make room for <NEW>?"` (`►YES / NO` — note the TWO line-scrolls!) -> `"Which move should be forgotten?"` (`Down * k`, `A`) -> `"1, 2 and... Poof! ▼"` -> `"forgot <OLD>! ▼"` -> `"And... ▼"` -> `"learned <NEW>! ▼"`.
- **Cave Exit Mats vs. Building Exit Mats (Verified Turn 187)**:
  - Cave exit mats (e.g., Mt. Moon 1F `(14, 35)`) warp **immediately upon stepping onto the tile**, whereas building exit mats (e.g., Pokémon Center `(3, 7)`) require pressing `Down` while standing on the mat.
- **Multi-Round Battle Loop Pitfalls & Timeout Guardrails (Verified Turns 181–186, 198)**:
  - Cap automated battle loops in `mcp_game_run_code` at **3–4 rounds max (~40–55s)** so slow enemy moves/status text never approach the 120s script wall-clock timeout.
  - If the lead Pokémon faints during an automated `["A", "A", "B"*8]` battle loop, `"Use next POKéMON?"` opens the Party list where `A` sends out Slot 1 (or repeats `"There's no will to fight!"` if cursor is on the fainted Pokémon).
  - **Safe Switch-Training**: Always place the low-level trainee in Slot 0 *before* battle and switch *out* on Turn 1 (zero damage taken by trainee), rather than switching a frail trainee *in* mid-battle into an incoming attack.
- **Ladder `back_d` Pitfall & `known_open_move` (Verified Turns 202–205)**:
  - Never run a `back_d` wall-probe when standing 1 tile off a ladder warp (`back_d` steps right back onto the ladder and re-warps floors!). First step 2+ tiles clear of any ladder using `known_open_move` (which flees wild encounters in place without stepping backward).

## Navigation Scripting Guardrails & Cave Primitives (Verified Turns 53, 60, 152, 165–166)
- Always use bounded `for _ in range(N):` loops rather than unbounded `while` loops so an unexpected wall/NPC cannot trip the 150-button script abort limit.
- Never dodge `Down` when walking directly above a south-facing ledge (e.g., Viridian `y = 26`).
- **Gen 1 Menu Wrapping Summary (Verified Turns 124, 155, 184)**:
  - `Start` menu (`POKéDEX .. EXIT`) **wraps** vertically (`Up` from `POKéDEX` jumps to `EXIT`, `Down` from `EXIT` jumps to `POKéDEX`). Fighting a battle resets `Start` back to Slot 0 (`POKéDEX`, verified Turn 290), whereas healing at Nurse Joy without a battle leaves `Start` on its previous slot (Turn 270).
  - `POKéMON` party list remembers its last cursor slot in overworld `Start -> POKéMON`, **EXCEPT at the start of every new battle**, where in-battle `PKMN` **resets to Slot 0** just like `FIGHT` (verified Turn 280! Thus Turn-1 switch from Slot 0 to Slot 1 in a new battle is ALWAYS `Right, A, Down, A, A`). Within the same battle, selecting Slot `k` via `PKMN` OR `"Use item on which POKéMON?"` updates the in-battle Party cursor to Slot `k` (verified Turn 287).
  - **Verified Direct-Talk Trainer Intro Recipe (13.5s, Turn 280)**: Talking to a trainer with `A` takes ~12.6s to reach `►FIGHT` (shorter sleeps drop Turn-1 switch inputs during `"Go! <PKMN>!"`, Turn 277). Use `["A", "sleep 1000", "B", "sleep 1000", "B", "sleep 4000", "B", "sleep 1200", "B", "sleep 2500", "B", "sleep 3000", "B", "sleep 800"]` to land cleanly on `►FIGHT`.
  - Battle `FIGHT` move menu **wraps** vertically.
  - `ITEM` bag menu **clamps** (does NOT wrap) at Slot 0 (`Up` at top stays on Slot 0). Using an overworld Bag item without evolution keeps the Bag cursor on the same slot, whereas **any item-triggered evolution (`Rare Candy` or `Moon Stone`) auto-returns to the Bag after the fanfare and resets the Bag cursor to Slot 0** (verified Turns 326 & 328).
  - Battle 2x2 command menu (`FIGHT / PKMN / ITEM / RUN`) **clamps** (`Left, Up` always lands on `►FIGHT`). Probing `Left` or `Up` onto a known-open overworld tile after an attack round is a **100% pure no-op** if still on `►FIGHT` (no restore press needed!).
  - The 2x2 battle command menu (`FIGHT / PKMN / ITEM / RUN`) does **not** wrap, so `["Left", "sleep 150", "Up", "sleep 150"]` deterministically resets the cursor to `►FIGHT` from any quadrant, and pressing `Left` or `Up` while already on `►FIGHT` is a pure no-op in battle.
  - When a step `d` from `b` fails (`after == b`), clearing potential battle intro (`["sleep 1200"] + ["B", "sleep 700"] * 8`) and probing `back_d` (the known-open tile you just came from) cleanly distinguishes a **wall** (`pos != b`) from an active **battle** (`pos == b`), and in Gen 1 `PlayerSpeed >= EnemySpeed` guarantees 100% first-try escape via `RUN`.



