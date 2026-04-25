Menu Cursor Memory: In many menus (like the Start menu and Party action menu), the cursor remembers its last selected position rather than resetting to the top. Always visually verify the cursor's starting position before executing blind button sequences (Verified Turn 449-451).
- Battle Item Menu: The cursor resets to the top (first item) at the start of a new battle. It only remembers its position *during* a single battle (Verified Turn 1338/1353). Attempting to use a key item like the Town Map triggers Professor Oak's warning and wastes a turn. Always verify cursor position!
- Party Menu Cursor: The cursor wraps around. Pressing Up from the 1st slot moves the cursor to the last slot (e.g., 5th slot) (Verified Turn 1251-1252).
- Battle Item Menu: Pressing A on an item in battle uses it immediately; there is no USE/TOSS sub-menu like in the overworld.
- Battle Move Menu: The move list is a single vertical column (1x4), NOT a 2x2 grid. Pressing Down moves down the list. Pressing Right does nothing. (Verified Turn 2089).
- Battle Move Menu: The cursor resets to the top (first move) at the start of a new battle, just like the Item menu. It only remembers its position *during* a single battle. (Verified Turn 2704: Started new battle, cursor was on Tackle, not Bubble/Water Gun).
- Party Swap Mechanic: In Gen 1, 'Select' does NOT swap party members in the overworld. You MUST press 'A' on a Pokémon, select 'SWITCH' from its sub-menu, move the cursor to the target Pokémon, and press 'A' again. Verified on Turn 6189.
- In-Battle Party Menu Cursor Memory: Confirmed (Turn 6281). When opening the 'PKMN' menu during a battle, the cursor remembers its last position from when the menu was previously accessed in that same battle (e.g., if you sent out slot 2 previously, the cursor starts on slot 2 next time you open the menu).
- Item Usage: Using an item from the bag on a Pokémon returns the game to the item menu after the effect text completes, NOT back to the party menu.

Gen 1 Menu Behaviors:
- Start Menu: Wraps around (Up from top goes to bottom). Remembers cursor position between uses.
- Party Menu: Remembers cursor position between uses.
- Because of wrapping and memory, blind macros for menus (like spamming Up to reach the top) DO NOT WORK. You must visually confirm cursor position.
- Overworld Item Menu: The cursor DOES NOT wrap around. Pressing Up at the top item (slot 1) does nothing. You must manually scroll down to reach items at the bottom. (Verified Turn 22113)
- Main Battle Menu Layout:
FIGHT  PKMN
ITEM   RUN
- The cursor ALWAYS resets to FIGHT at the start of every turn. It does NOT remember its position.
- Pressing Right from FIGHT goes to PKMN. Pressing Down from FIGHT goes to ITEM.
- Yes/No Prompts: The default cursor position for many Yes/No prompts (like "Press it?" for switches, or "Toss this item?") is "NO". To select "YES", you must explicitly input 'Up' before pressing 'A'. For the Mansion switch: YES outputs "Who wouldn't?". NO outputs "Not quite yet!".