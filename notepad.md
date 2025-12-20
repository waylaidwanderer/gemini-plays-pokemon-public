# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.
- **Current Action:** Fix Kenya's Mail (Typing Message).
  1. **Current Text:** "DARK CAVE"
  2. **Cursor:** On 'E'.
  3. **Step 1:** Use `slow_press` to type " leads".
  4. **Step 2:** Continue typing " to another road".
  5. **Step 3:** Confirm with "END".

## Strategy & Lessons
- **Critical Bug:** Do NOT press `Start` in the Mail menu. It triggers a "Printer Error 2" crash loop.
- **Input Strategy:** Use `slow_press` with `autopress_buttons=True` to mix directional and action inputs for efficient typing.
- **Quest Item Logic:** Do not alter quest items (e.g., mail messages) unless necessary. Original attributes often matter.
- **Fly Map:** List-based `Up`/`Down`. Order: New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod.

## Strategy & Lessons
- **Quest Item Logic:** Do not alter quest items (e.g., mail messages) unless necessary. Original attributes often matter.
- **Fly Map:** List-based `Up`/`Down`. Order: New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod.
- **Menu Cursor:** Always verify position.
- **Negative Results:** Mark NPCs with "Generic Text" or "Wrong Recipient" to avoid re-checking.