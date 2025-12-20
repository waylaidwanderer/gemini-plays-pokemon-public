# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.
- **Current Action:** Fix Kenya's Mail (Deleting Garbage & Typing " CAVE").
  1. **Status:** Screen text "DARKXJH?B".
  2. **Step 1:** Press `Start` (Jump to END), `Left` (Jump to DEL).
  3. **Step 2:** Press `A` x5 to delete "B?HJX" -> Restore "DARK".
  4. **Step 3:** Navigate from `DEL` to Space (Up, Up, Right, Right).
  5. **Step 4:** Type " CAVE" (Space, C, A, V, E).
  6. **Next:** Type " leads to another road".

## Strategy & Lessons
- **Critical Bug:** Do NOT press `Start` in the Mail menu. It triggers a "Printer Error 2" crash loop.
- **Input Strategy:** Use `slow_press` with `autopress_buttons=True` to mix directional and action inputs for efficient typing.
- **Typing Recovery:** If garbage is typed, navigate to `DEL` (Start -> Left) and backspace.
- **Quest Item Logic:** Do not alter quest items (e.g., mail messages) unless necessary. Original attributes often matter.
- **Fly Map:** List-based `Up`/`Down`. Order: New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod.

## Strategy & Lessons
- **Quest Item Logic:** Do not alter quest items (e.g., mail messages) unless necessary. Original attributes often matter.
- **Fly Map:** List-based `Up`/`Down`. Order: New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod.
- **Menu Cursor:** Always verify position.
- **Negative Results:** Mark NPCs with "Generic Text" or "Wrong Recipient" to avoid re-checking.