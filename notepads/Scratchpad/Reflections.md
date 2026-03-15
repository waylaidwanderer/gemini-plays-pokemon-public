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
- [Turn 35403 Error Analysis] I attempted to move Up then Left, but I bumped into a wall at (17, 1) because the tile at Y=1 is actually the wall of the elevator shaft, not a hallway. I need to move DOWN to Y=3 to bypass the elevator shaft before heading West.
[50-Turn Reflection (Turn 35405)]
- Error Analysis (Text Box Trap): I repeatedly failed to move on 6F because a post-battle text box ("No matter! My brothers will avenge me!") was still open, eating all my directional inputs. I incorrectly assumed I was bumping into walls or that auto-turn failed. I MUST visually confirm the absence of text boxes at the bottom of the screen before executing overworld movement sequences.
[50-Turn Reflection (Turn 35457)]
- Tool Maintenance: Battle tools are working, but I must remember `execute_battle_turn`'s `start_on_main` flaw when the cursor is already on FIGHT.
[50-Turn Reflection (Turn 35509)]
- Error Analysis (Menu Navigation): The `swap_pokemon` tool assumes the 'SWITCH' option is at index 2 of the sub-menu. However, if a Pokemon has a Field Move (like CUT or SURF), the Field Move is index 1, STATS is index 2, and SWITCH is index 3. This caused the tool to open Audrey's stats instead of swapping. I must visually verify the sub-menu layout or manually navigate when dealing with HM users.
[50-Turn Reflection (Turn 35561)]
- Error Analysis (Visual Hallucination): I mistakenly identified overlaid text/artifacts at (24, 11) on 6F as a Rocket Grunt. I must rely on the Game State Information's sprite list or confirm movement/interaction before assuming a static visual artifact is an NPC.
- Tool Maintenance: I successfully updated the `swap_pokemon` tool to accept a `has_field_move_a` flag to account for HM moves altering the sub-menu layout.
[50-Turn Reflection (Turn 35664)]
- Error Analysis (Elevator Warp): The elevator exit warp on Y=3 is NOT active across all X coordinates. Moving Down at X=0 failed to trigger the warp. It likely only exists at specific tiles (e.g., X=1, X=2, or X=3). I will sweep across the bottom row and test pressing Down at each coordinate to find the exact exit tiles.
- Strategy (Type Immunities): Leveraging type match-ups and AI moveset limitations is critical for survival.
[50-Turn Reflection (Turn 35717)]
- Verification: I verified in my PC storage that I already possess TM13, TM48, and TM49, confirming I previously completed the little girl's quest on the Roof.
- Error Analysis (Vending Machine): I anticipate the Vending Machine will have introductory text that could eat inputs if I try to macro the purchase. I will test the interaction manually first to map the text boxes before attempting any bulk-buy automation.
[Turn 35741 Error Analysis]
- Vending Machine Automation: The tool failed because my positional assumptions were wrong. I started at (12, 3). The first `Up` moved me to (12, 2), where `A` interacted successfully. However, the subsequent `Down` inputs in the tool's loop caused me to walk away from the machine because the menu had either failed to open or closed unexpectedly. I need to manually map the exact text box sequence and closure of the vending machine to understand why the loop desynced.