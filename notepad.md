# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.
- **Current Action:** Fix Kenya's Mail (Step 12: Select Give & Choose Kenya).
  1. **Status:** Selected Flower Mail in Pack. Now giving it to Kenya.
  2. **Step 1:** Open Item Menu (A).
  3. **Step 2:** Select GIVE (Assume 1st option, press A).
  4. **Step 3:** Select Kenya (Down x5 -> A).
  5. **Step 4:** Write "DARK CAVE leads to another road."

## Strategy & Lessons
- **Quest Precision:** Exact grammar and punctuation are critical for text-based quests. Missing a period can fail the quest.
- **Critical Bug:** Do NOT press `Start` in the Mail menu. It triggers a "Printer Error 2" crash loop.
- **Input Strategy:** Use `slow_press` with `autopress_buttons=True` for efficient, mixed-input typing.
- **Typing Recovery:** Use `B` button to backspace quickly.
- **Menu Navigation:** Always verify cursor position before pressing A.
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