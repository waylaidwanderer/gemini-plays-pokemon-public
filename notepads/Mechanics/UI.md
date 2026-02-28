- Item Menu: The in-game Item menu order is chronological/manual, NOT alphabetical. Do not rely on Game State inventory order for navigation.
- Cursor Memory: The PKMN switch menu and FIGHT menu remember the last selected index per session/battle. ALWAYS visually verify the starting cursor position and pass it to custom tools (current_index) to prevent wrong selections.
- Gen 1 Menu Mechanics: The party menu and start menu both feature cursor memory (opening on the last selected item) and cursor wrapping (pressing Up at the top goes to the bottom). This breaks blind navigation macros, so always do menu navigation step-by-step or use state-aware tools.
- Cursor Memory: In Gen 1, the cursor position in menus (like the Party screen) is often remembered between opens. Always verify the blinking cursor position before mashing A or using a tool, especially when returning from a sub-menu, as it might wrap or stay where it was.
- [Turn 6149 Reflection] The party menu cursor remembers its last position even when accessed from the ITEM menu. Always verify cursor position before using an item!
- [Turn 6151 Reflection] CRITICAL: The Game State inventory list is ALPHABETIZED and does NOT match the in-game bag's chronological order. Never use Game State indices for item tools. Manual counting/scrolling is required!

# Menu Navigation
- Gen 1 Menus (Items, Pokemon, PC) have cursor memory! The cursor stays where you last left it. Always visually verify the cursor position or track it carefully before using tools that navigate menus blind.
- The Party Menu wraps around (pressing Up at the top goes to the bottom) and retains cursor memory. You cannot reset the cursor by mashing Up. Always track or visually confirm current_index before using tools.