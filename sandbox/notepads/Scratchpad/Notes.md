# Scratchpad — UI, Routing & Active Leads

## Active Exploration Leads (Post-Poké Balls)
- **Littleroot Custom West Area (`x < 0`):** Grassy area with signpost and NPC visible west of Littleroot's tree line *(Turn 31)*. Check how it connects (likely south/west of Route 101/102 or via later route).
- **Littleroot SE Pond (`x=18..19, y=12..14`):** Custom water pond inside Littleroot Town—save for Fishing/Surf encounter if no Littleroot gift is taken.

## Completed Town Checks
- **Littleroot Town:** Bedroom PC (`1x Potion` withdrawn), May's House 1F pink-haired NPC (flavor only both pre/post-starter), SE pond red-bow girl (relocated Route 101 blocker).
- **Oldale Town:** SE House (flavor), Mart Clerk (`1x Potion` free sample -> `Potion x 2`), NW House (flavor), Pokémon Center Gentleman (flavor).
- **Petalburg City:** Pokémon Center `(20, 16)` (standard NPCs), Poké Mart `(25, 12)` (`Repel ¥350`, `Escape Rope ¥550`), SE House `(20, 24)` (flavor), SW House `(10, 19)` (flavor), `(8, 22)` pond boy & `(20, 9)` NE pond Gentleman (flavor), Petalburg Gym `(15, 8)` (Norman & Wally catching tutorial completed Turn 222 — Wally caught `Lv 5 Ralts` with `Confusion`), Wally's House `(7, 5)` (pre-Surf flavor verified Turn 224).

## Verified UI & Spatial Mechanics
- **Screen Fades & Real-Time Thinking:** Fades take ~1.8s (`sleep 2200–2400` *within* the same turn's `press_buttons` sequence). Because the emulator runs in real time during `[THINKING]`, any fade still occurring at the end of Turn `N` finishes completely before Turn `N+1`'s first button executes—never prepend a dummy input/sleep at the start of a new turn to wait out a prior turn's fade!
- **Naming Screen:** `Select` page-flip takes ~500ms (`sleep 800+` required). Exact grid (`cols 0..6`):
  - Row 0: `0:A 1:B 2:C 3:D 4:E 5:F 6:.` | Row 1: `0:G 1:H 2:I 3:J 4:K 5:L 6:,`
  - Row 2: `0:M 1:N 2:O 3:P 4:Q 5:R 6:S` | Row 3: `0:T 1:U 2:V 3:W 4:X 5:Y 6:Z` *(Verified Turn 234)*; `Start -> A` confirms `OK`.
- **Options Binary Toggles:** `Left` and `Right` both wrap/toggle 2-state options; visually inspect before pressing.
- **Cursor Persistence & Auto-Refill Reordering:** Both **Start Menu** (last row) and **Bag** (last pocket + last item row) persist across indoor/outdoor warps. `BAG -> USE` keeps the Party cursor on the previously selected slot, whereas **`BAG -> GIVE` and `Start -> POKéMON` always reset the Party cursor to Slot 1** *(Verified Turn 184 `#167`)*. **Caution:** Overworld auto-refill places `RARE CANDY x99` at **Row 0** of `ITEMS`, shifting other items down *(Turn 153 `#51`)*.
- **Battle KO & `B`-Button Idempotency:** Because `B` is a harmless no-op on both `"What will <PKMN> do?"` and the overworld, chaining `sleep 7800 -> B` (`fainted!`, covering super-effective text too) -> `sleep 4500 -> B` (`EXP!`) -> `sleep 4500 -> B` (mid-trainer send-out, or `sleep 4000 -> B -> sleep 2500 -> B -> sleep 2500 -> B -> sleep 3000 -> B` on a trainer's final Pokémon) safely clears OHKOs straight to the next Pokémon or overworld while staying harmless if the foe survives *(Verified Turns 173–188)*.
- **Pokémon Center Nurse Joy Flow:** Requires **`4x A`** (`1: Talk` -> `2: "Hello..."` -> `3: "We restore..."` -> `4: "Would you like..." [YES]`), then `sleep 8500` for healing jingle, then `B` presses. Pressing only `3x A` followed by `B` selects `NO` without healing!
- **Berry Tree Harvest & `BERRIES` Pocket UI:**
  - **Harvesting:** Requires **`3x A`** (`1: Interact` -> `2: "You found X BERRIES!"` -> `3: "Do you want to pick...?" [YES]`), then `sleep 3500` for jingle, then **`3x B`** (use `B` afterward to avoid opening replant prompt) *(Turn 178–179)*.
  - **`BERRIES` Pocket Popup Grid (`2x3`):** `(0,0) CHECK TAG` | `(0,1) USE`, `(1,1) GIVE` | `(0,2) TOSS`, `(1,2) CANCEL` — from `CHECK TAG`, `USE` is `Down` and `GIVE` is `Down, Right` (`Down, Down` is `TOSS`!) *(Verified Turn 183)*. **Loamy Soil Quirk:** Selecting `USE` on a Berry while facing empty loamy soil plants the Berry instead of opening the Party screen (`GIVE` always opens Party; step off loamy soil before selecting `USE`!) *(Turn 183 `#08`)*.
- **Safe Rare Candy Cycle (4 Full Moves):** `3x A` (`Candy -> Use -> Pokémon`) + `3x B` (`+Stats -> Total Stats -> dismiss`) + `sleep 2400` avoids exiting Bag if no move is learned and avoids overwriting Move Slot 1 if a move is learned.
- **Indoor Welcome Mats:** Approaching a south exit mat horizontally (`Left`/`Right`) requires TWO `Down` presses (first turns `Down`, second warps). Approach vertically from `(x, y-1)` whenever possible.
- **Multi-Warp Chaining:** Insert `sleep 2200` immediately after an indoor warp step to continue overworld movement on the destination map.
- **Poké Mart Interior & Purchase Flow:** Entry mat is `(3, 7)`; Cashier counter is **4 steps `Up`** at `(3, 3)` facing `Left` *(Turn 207)*. Talking to Cashier requires **`3x A`** (`1: Talk` -> `2: "Welcome!"` -> `3: [►BUY]`) + `sleep 2400` for fade into `BUY` *(Turn 207–208)*. After adjusting quantity spinner: `A` (`YES/NO`) -> `A` (`"Here you go!..."`) -> `B` (returns to `BUY`, or 2x `B` if ≥10 Poké Balls triggers Premier Ball). Pressing `B` on `BUY` fades (`sleep 2400`) back to Cashier menu.
- **Poké Ball Catch & Nickname Timings (Turns 115–129, 232):**
  - All **5 Bag pockets** (`0: ITEMS`, `1: POKé BALLS`, `2: TMs & HMs`, `3: BERRIES`, `4: KEY ITEMS`) remain present in battle (`BERRIES -> POKé BALLS` is **`2x Left`**!).
  - After a failed Poké Ball throw, battle cursor stays on `BAG` and Bag stays on `POKé BALLS` pocket (`A -> sleep 2300 -> A -> sleep 450 -> A` repeats throw). Use harmless `"Up"` (never `A`/`B`) when waiting out a Poké Ball throw so you never skip the nickname prompt on a catch!
  - From `"Gotcha! <PKMN> was caught! ▼"`, `["A", "sleep 1000", "A", "sleep 2500", "A", "sleep 2300", "A", "sleep 2300", "B"]` lands cleanly on an empty Naming Screen at `(0, 0)` `A`.
  - Exiting `SUMMARY` with `B` (`sleep 2500`) returns to `PARTY` **with the `SUMMARY/SWITCH/ITEM/CANCEL` popup STILL OPEN** (`►SUMMARY`)! Press a second `B` (`sleep 300`) to close the popup before moving `Up`/`Down` between party slots *(Verified Turn 133, `#75–#80`)*.
  - **Python Script Hygiene:** Keep `run_code` scripts bounded (`<60` buttons, `<40s` total sleeps) and step to an open floor row before horizontal welcome-mat alignment inside NPC houses *(Turns 215, 224)*.

## Live Tactical State (Turn 227 — Scouting Route 104 South & New Encounter!)
- **Active Party Order (All Holding `ORAN BERRY`, Cap = Lv 16):**
  1. **Matcha (`Lv 14 Gulpin ♀`, Lead, `47/47 HP`, `ORAN BERRY`):** `Acid`, `Yawn` *(0-damage 100% Sleep catcher!)*, `Fire Punch [15/15 PP]`, `Sludge Bomb [10/10 PP]` (`Liquid Ooze`).
  2. **Girasol (`Lv 13 Sunflora ♀`, `42/42 HP`, `ORAN BERRY`):** `Absorb`, `Growth [5 PP]`, `Mega Drain` (`Chlorophyll`).
  3. **Bayou (`Lv 13 Mudkip ♂`, `36/36 HP`, `ORAN BERRY`):** `Tackle`, `Bubble`, `Mud Sport`, `Water Gun`. Keep below Lv 16 until Roxanne (`Lv 16 Marshtomp`)!
- **Route 104 South (`Position x=38 y=62`):** Stepping to `(32, 59)` to inspect the `(30..32, 58)` Berry patch and locate Route 104 South's tall grass for our **Route 104 Nuzlocke Encounter** (shared across Route 104 South & North!).