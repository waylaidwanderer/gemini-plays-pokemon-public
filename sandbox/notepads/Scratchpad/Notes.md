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
  - Checked pink-haired NPC in May's House 1F (`(9,5)`, Turns 33 & 59): flavor dialogue only (`"Hi, neighbor! Do you already have your own POKéMON?"` both before and after obtaining Bayou). Resolved.
- **Route 101 Starters & East Corridor (Turn 42):**
  - Birch's Bag holds the Hoenn trio: Left = Treecko, Middle = Torchic, Right = Mudkip. Choosing **Mudkip** (evolves to Marshtomp right at Roxanne's Lv 16 cap and gives Electric immunity for Wattson).
  - Confirmed a custom east exit corridor on Route 101 (`y=10..11, x >= 18`, visible in Turn 70 `#60`). **Visit immediately AFTER obtaining Poké Balls** in case it leads to a new named encounter area!
- **Multi-Warp Chaining:** Inserting `sleep 2200` after a stair/door warp step allows chaining movement across warps in one `press_buttons` call (verified Turn 36).
- **Starter Moveset Clue (Turn 44):** Lv 5 Mudkip (`♂`, 20 HP) starts with ONLY `Tackle` (35 PP) and **no `Growl`**—characteristic of Kaizo-style / competitive Emerald hacks where early stat-drop moves are stripped. Expect significantly buffed trainers and custom movesets!
- **Littleroot SE Pond NPC Lead (Turn 58):** Spotted a custom red-bun woman NPC wandering near the custom SE pond in Littleroot Town (`(16, 10)`–`(17, 12)`). Speak to her upon exiting May's House.
- **Start Menu & Bag Cursor Memory (Turns 63–64):**
  - The **Start Menu** persists its last selected row across indoor/outdoor warps (does NOT reset to top row `POKéMON`). Always verify or track which Start Menu entry was last used before pressing `Up`/`Down`.
  - The **Bag** persists both the last viewed **pocket** AND the last highlighted **item row** inside each pocket.
- **Littleroot SE Pond NPC Resolved (Turn 63):** The sprite at `(16, 10)` near the SE pond was the Little Girl with a red bow relocated from `(10, 1)` after Birch's rescue.