# Scratchpad — UI, Routing & Active Leads

## Active Exploration Leads (Post-Poké Balls)
- ~~**Oldale Town Custom Grass (`(14..15, 2)`):**~~ Encountered `Lv 3 Growlithe` (packs `Roar` at Lv 3!); broke out of Ball #1 and Roared on Turn 110–111. Oldale Town encounter forfeited (not a dupe).
- ~~**Route 101 East Clearing (`x=16..19`):**~~ Verified closed by eastern border trees at `x=20..21` on Turn 104 `<CurrentScreen>`. Resolved.
- **Littleroot Custom West Area (`x < 0`):** Grassy area with signpost and NPC visible west of Littleroot's tree line *(Turn 31)*. Check how it connects (likely south/west of Route 101/102 or via later route).
- **Littleroot SE Pond (`x=18..19, y=12..14`):** Custom water pond inside Littleroot Town—save for Fishing/Surf encounter if no Littleroot gift is taken.

## Completed Town Checks
- **Littleroot Town:** Bedroom PC (`1x Potion` withdrawn), May's House 1F pink-haired NPC (flavor only both pre/post-starter), SE pond red-bow girl (relocated Route 101 blocker).
- **Oldale Town:** SE House (flavor), Mart Clerk (`1x Potion` free sample -> `Potion x 2`), NW House (flavor), Pokémon Center Gentleman (flavor).

## Verified UI & Spatial Mechanics
- **Screen Fades & Real-Time Thinking:** Fades take ~1.8s (`sleep 2200–2400` *within* the same turn's `press_buttons` sequence). Because the emulator runs in real time during `[THINKING]`, any fade still occurring at the end of Turn `N` finishes completely before Turn `N+1`'s first button executes—never prepend a dummy input/sleep at the start of a new turn to wait out a prior turn's fade!
- **Naming Screen:** `Select` page-flip takes ~500ms (`sleep 800+` required). Contiguous columns `0..5` (no blank col between `C` and `D`).
- **Options Binary Toggles:** `Left` and `Right` both wrap/toggle 2-state options; visually inspect before pressing.
- **Cursor Persistence:** Both **Start Menu** (last row) and **Bag** (last pocket + last item row) persist across indoor/outdoor warps. Using items via `BAG -> USE` keeps the Party cursor on the previously selected slot, whereas `Start -> POKéMON` resets to Slot 1.
- **Pokémon Center Nurse Joy Flow:** Requires **`4x A`** (`1: Talk` -> `2: "Hello..."` -> `3: "We restore..."` -> `4: "Would you like..." [YES]`), then `sleep 8500` for healing jingle, then `B` presses. Pressing only `3x A` followed by `B` selects `NO` without healing!
- **Safe Rare Candy Cycle (4 Full Moves):** `3x A` (`Candy -> Use -> Pokémon`) + `3x B` (`+Stats -> Total Stats -> dismiss`) + `sleep 2400` avoids exiting Bag if no move is learned and avoids overwriting Move Slot 1 if a move is learned.
- **Indoor Welcome Mats:** Approaching a south exit mat horizontally (`Left`/`Right`) requires TWO `Down` presses (first turns `Down`, second warps). Approach vertically from `(x, y-1)` whenever possible.
- **Multi-Warp Chaining:** Insert `sleep 2200` immediately after an indoor warp step to continue overworld movement on the destination map.
- **Poké Mart Purchase Flow (Turn 107):** After adjusting quantity spinner: `A` (opens `YES/NO`) -> `A` (`"Here you go! Thank you very much."`) -> `B` (returns directly to `BUY` list, or shows `"I'll throw in a PREMIER BALL, too."` on ≥10 Poké Balls requiring 1 more `B` to return to `BUY`). Pressing an extra `B` on `BUY` exits back to Cashier menu.
- **Poké Ball Catch & Nickname Timings (Turns 115–129):**
  - After a failed Poké Ball throw, battle cursor stays on `BAG` and Bag stays on `POKé BALLS` pocket (`A -> sleep 2300 -> A -> sleep 450 -> A` repeats throw).
  - From `"Gotcha! <PKMN> was caught! ▼"`, `["A", "sleep 1000", "A", "sleep 2500", "A", "sleep 2300", "A", "sleep 2300", "B"]` lands cleanly on an empty Naming Screen at `(0, 0)` `A`.
  - Exiting `SUMMARY` with `B` (`sleep 2500`) returns to `PARTY` **with the `SUMMARY/SWITCH/ITEM/CANCEL` popup STILL OPEN** (`►SUMMARY`)! Press a second `B` (`sleep 300`) to close the popup before moving `Up`/`Down` between party slots *(Verified Turn 133, `#75–#80`)*.

## Live Tactical State (Turn 158 — Route 102 Reconnaissance & Berry Priority)
- **Active Party Order (Cap = Lv 16):**
  1. **Matcha (`Lv 12 Gulpin ♀`, Lead):** `42 HP / 17 Atk / 18 Def / 17 SpA / 17 SpD / 16 Spe` (`Acid`, `Yawn`, `Fire Punch`, `Liquid Ooze`).
  2. **Girasol (`Lv 13 Sunflora ♀`):** `42 HP / 21 Atk / 20 Def / 34 SpA / 30 SpD / 15 Spe` (`Absorb`, `Growth [5 PP]`, `Mega Drain`, `Chlorophyll`).
  3. **Bayou (`Lv 13 Mudkip ♂`):** `36 HP / 24 Atk / 20 Def / 20 SpA / 16 SpD / 19 Spe` (`Tackle`, `Bubble`, `Mud Sport`, `Water Gun`). Keep below Lv 16 until Roxanne (`Lv 16 Marshtomp`)!
- **Route 102 Sightings:** Rotating trainer in north grass at `(38, 4)`; Youngster spotted at `(33, 14)` facing `Down` on the southwest road. Priority: reach Route 102's Berry patch (`Oran` & `Pecha` Berries) so Berries auto-refill to `99` for held-item healing!