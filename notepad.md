# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.
- **Current Action:** Buy Flower Mail.
  1. **Observation:** Fisher rejected current mail ("This MAIL isn't for me.").
  2. **Hypothesis:** Quest requires specific "Flower Mail" (original item held by Kenya).
  3. **Plan:**
     - Fly to Violet City (Mistral).
     - Buy Flower Mail at Mart.
     - Attach to Kenya.
     - Write: "DARK CAVE leads to another road."
     - Return to Fisher.

## Reflection (Turn 9200)
- **Execution:** Recovered from "Printer Error" loop (caused by pressing Start in Mail menu). Prioritized mail verification.
- **Hygiene:** Notepad is clean. Map markers are consistent.
- **Automation:** Using `slow_press` for menus. `type_text` available if rewrite needed.
- **Goal:** Verify Kenya's mail has the correct period (".").
- **Lesson:**
  1. **Bug:** Pressing `Start` in the Mail menu triggers a "Printer Error 2" crash loop. Use `B` to cancel.
  2. **Quest:** The Fisher likely requires exact punctuation ("DARK CAVE leads to another road.").
  3. **Tooling:** OCR can fail on menus; trust the visual state (screenshots) over empty text logs.

## Strategy & Lessons
- **Quest Precision:** Exact grammar and punctuation are critical.
- **Input Strategy:** Use `slow_press` for reliable menu navigation.
- **Fly Map Order:** New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod.

## Key Locations & mechanics
- **Route 31 Fisher:** Wants mail. Exact phrase: "DARK CAVE leads to another road."
- **Wade:** Bug Catcher on Route 31. Calls about berries/swarms.
- **Dark Cave:** Leads to Route 45/46 (Blackthorn side) or Route 31 (Violet side). needs Flash/Rock Smash/Surf.
## Tile Mechanics
- **FLOOR:** Standard traversable tile.
- **WALL:** Impassable.
- **TALL_GRASS / LONG_GRASS:** Traversable, potential wild encounters.
- **WATER:** Traversable with SURF.
- **CUT_TREE:** Impassable until removed with CUT.
- **HEADBUTT_TREE:** Impassable, interactable with HEADBUTT.
- **LEDGE_HOP_DOWN/RIGHT/LEFT:** One-way movement (jump over).
- **WARP_CARPET_LEFT/RIGHT/UP/DOWN:** Map transition.
- **CAVE:** Traversable, wild encounters.
- **ICE:** Sliding movement (continue until obstacle).
- **WHIRLPOOL:** Impassable until removed with WHIRLPOOL.
- **WATERFALL:** Impassable until climbed with WATERFALL.
- **Current Action:** Compose Mail.
  1. **Status:** Text is "lead t". Cursor at 'o' (1,4).
  2. **Method:** Manual typing via `slow_press`.
  3. **Plan:**
     - B x2 (Delete 't', ' '). Result: "lead".
     - Type "leads to " (s, Space, t, o, Space).
     - Type "another road." (Next).
  4. **Note:** Cursor ends at 'Space' (2,6).

## Maintenance
- **Tool Fix:** Manual typing continues.

## Reflection (Turn 9286)
- **Correction:** Previous turn resulted in "lead t" instead of "leads to". Missing 's' and typo 't'.
- **Action:** Fix "lead t" -> "leads to ".
- **Next:** Type "another road."