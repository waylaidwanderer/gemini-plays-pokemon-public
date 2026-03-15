[100-Turn Reflection]
- Error Analysis: The "input eating" mechanic of text boxes continues to be a major factor in macro failures. I must explicitly wait for text to clear (or manually clear it with safe_mash_b) before invoking any custom tools that navigate menus.
- Map Hygiene: Placed a marker for the Celadon City warp on Route 16.

[50-Turn Reflection (Turn 34884)]
- Error Analysis (TM/HM Input Eating): When using an HM/TM, the text "Teach [MOVE] to a POKeMON?" appears simultaneously with the party menu. Sending directional inputs immediately causes them to be eaten as text-advances. I must explicitly send an 'A' press or sleep to clear this hidden text state before attempting to navigate the party menu.
[50-Turn Reflection (Turn 34937)]
- Error Analysis (Fly Map Navigation): I initially hypothesized the Fly map was a 1D list and that my inputs were just being eaten by lag. By systematically testing single D-pad presses (e.g., pressing Down from Pewter moved the cursor to Viridian; pressing Right from Viridian moved it to Celadon), I empirically proved the Fly map uses strict GEOGRAPHICAL navigation. It snaps to the nearest unlocked city in the pressed direction.
- Strategic Adjustment: When exploring and getting trapped behind one-way ledges (like on Route 7), using Fly to reset to the nearest city is a highly efficient way to bypass tedious backtracking (like the Underground Path).
[50-Turn Reflection (Turn 34989)]
- Navigation: Discovered that Saffron City is highly segmented by fences and the massive Silph Co. building in the center. Navigating requires following the perimeter roads.
- Error Analysis (Fly Map): Corrected my understanding of the Fly Map. It is definitively a 1D vertical list (Up moves forward, Down moves backward) that wraps around, not a geographical map.
[50-Turn Reflection (Turn 35042)]
- Strategy: Switch-training Audrey against the Fighting Dojo trainers is yielding excellent EXP. Hydro is easily sweeping with Surf.
- Error Analysis (Notepad/Map Markers): I recognized that logging exact coordinates of generic defeated trainers in permanent notepads causes unnecessary bloat. I have transitioned to using map markers (☠️) exclusively for this purpose, keeping the notepads focused on layout, static encounters, and major points of interest.
- Execution: Battle tools are functioning smoothly. I am actively managing the "input eating" text box issue by manually clearing text or using `spam_button` to ensure inputs are registered correctly.
[100-Turn Reflection (Turn 35093)]
- Notepad Hygiene: Fighting Dojo notes were simplified, relying on Map Markers for defeated trainers.
- Map Hygiene: Kept track of defeated trainers with map markers.
- Custom Tools: Custom tools for battling (switch_pokemon_in_battle, safe_mash_b, spam_button) are working perfectly.
- Error Analysis: Text box input eating is still a minor issue but is being managed effectively by manually clearing text before invoking complex macros.
[50-Turn Reflection (Turn 35145)]
- Notepad/Map Hygiene: Created Locations/SilphCo to track the complex layout (elevators, stairs, electronic doors). Placed map marker for 5F elevator.
- Error Analysis: Realized map 0_236 is the *interior* of the elevator, not the 2nd floor itself. You select a floor at the panel (3,0) and walk South to exit. This clarifies the navigation significantly!
- Tools: Battle macros are functioning perfectly.
[50-Turn Reflection (Turn 35249)]
- Error Analysis: Identified that Gen 1's 2x2 main battle menu wraps in all directions, making blind resets impossible. I must track or visually confirm the cursor position (FIGHT/PKMN/ITEM/RUN) before navigating.
[50-Turn Reflection (Turn 35301)]
- Notepad/Map Hygiene: Documented warp connections between 5F and 3F/9F with map markers and notes. Removed redundant reflection logs as requested by overwatch.
- Tools: Fixed execute_battle_turn's main_cursor wrapping bug.
[50-Turn Reflection (Turn 35353)]
- Progress: Mapped out a partitioned section of 9F accessible via the 5F warp pad at (9, 15). It's a dead end requiring a Card Key. Now heading to the 5F warp pad at (27, 3).
- Error Analysis: Assumed beds on 9F were healing pads without interacting with them first. I must verify interactable objects before logging their function.