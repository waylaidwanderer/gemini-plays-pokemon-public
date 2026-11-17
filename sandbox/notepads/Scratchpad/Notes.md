# Scratchpad — UI & Routing Notes

## Verified UI Timings
- **Screen Fades (Bag / Options / Naming):** ~1.8s. Append `sleep 2200` + a harmless input (e.g. `Up` at top of menu) so `<CurrentScreen>` settles after the fade completes rather than mid-black-screen.
- **Naming Screen (`Select` page toggle):** Animation takes ~500ms; use `sleep 800` after `Select` before moving cursor. Columns are contiguous (`A B C D E F` = cols `0..5`, no gap column between `C` and `D`). Saying `NO` to Birch's name confirmation resets back to Boy/Girl selection.
- **Options Menu Binary Toggles:** `Left` and `Right` both wrap/toggle 2-state options (`BATTLE STYLE`, `BATTLE SCENE`, `SOUND`, `BUTTON MODE`). Always visually inspect `OPTION` before pressing `Left`/`Right`. Options set on Title Screen Main Menu DO persist into `NEW GAME`.
- **Starting Bag:** All 5 pockets (`ITEMS`, `POKé BALLS`, `TMs & HMs`, `BERRIES`, `KEY ITEMS`) verified empty at game start (Turn 20).
- **Bedroom PC & Wall Clock (Turns 24–27):** 2F bedroom PC Item Storage held only `1x Potion` (withdrawn Turn 25). Wall Clock confirmation (`Is this the correct time?`) defaults cursor to `NO` (`Up` + `A` required for `YES`).
- **Custom Map Lead — West of Littleroot Town (Turn 31):** Overworld frame at `(5, 9)` revealed a custom grassy area with a signpost and NPC immediately west of Littleroot Town's western tree line (`x < 0`). Investigate how to access this area once we explore Littleroot/Route 101.
- **Custom Littleroot Pond & NPC (Turns 31–32):**
  - Spotted a custom 2x2 water pond in SE Littleroot Town (`x=16..17, y=11..12`, below May's house)—potential Littleroot Town fishing/Surf encounter later!
  - Spotted a custom pink-haired NPC in May's House 1F (`x=9, y=5`, top-right of pink rug). Talk using `A` + `B` advances so we don't blindly accept any unexpected prompt before reading it.