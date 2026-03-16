[Active Reflections]
- Door Checklist:
  - 3F: (DONE)
  - 4F: (DONE)
  - 5F: (DONE - TM09 acquired)
  - 6F: (DONE - HP UP acquired)
  - 7F: (DONE - TM03 acquired)
  - 8F: (4, 10)
  - 9F: (DONE)
  - 10F: (DONE - Opened central doors)
  - 11F: Check for any remaining.

[Turn 37795 Reflection]
- 50-Turn Check-in: I caught a Ponyta and named it COMET! It was sent to Box 2. I also learned that wild Vulpix can use Roar to force me to run away.
- Notepad Hygiene: Pruned outdated reflections from Cinnabar arrival, PC storage, and fossil revival using 'overwrite' to clean up the file safely.
- Custom Tools Brainstorm: 1) catch_pokemon automation, 2) check_pc_space alert, 3) map_mansion grid tracker, 4) smart_switch_pokemon (handling KO prompt), 5) fast_text_clearer.
- Map Hygiene: Marked the Mansion exit at (5, 27).
- Error Analysis: Text boxes about caught Pokemon and PC transfers take multiple A/B presses to clear. I must explicitly clear them before sending movement commands to prevent eating inputs.
[Turn 37847 Reflection]
- 50-Turn Check-in: Explored the East and West wings of Pokemon Mansion 1F. Found statues with glowing eyes at (13, 2), (15, 2), and (1, 4). Pressing 'A' from the front and sides hasn't worked. Will test interacting from the bottom tile.
- Map Hygiene: 1F layout is becoming clearer. Central hallway, east wing with stairs at (16, 7), west wing being explored now.
- Custom Tools: The `run_battle` tool failed with a JSON error when `autopress_buttons: true` was used. Need to review its script.
[Turn 37899 Reflection]
- 50-Turn Check-in: Fixed `run_battle` tool! Discovered electronic doors are toggled by hidden switches on the bottom tile of glowing-eye statues. The central/west wall at Y=9 is solid. The stairs to 2F at Y=10 must be accessed via the East Wing corridor (X=11/X=12) by traveling south past Y=6.
- Map Hygiene: Placed markers for the switch statue and electronic door.
- Notepad Hygiene: Corrected the hallucination about the stairs being at (4,6) and reaffirmed they are at Y=10.
- Custom Tools: Need to make a dedicated fast text clearer tool.
- Error Analysis: Visual hallucinations can override established facts if I'm not careful. Always trust previous empirical observations over new visual assumptions unless physically verified.
[Turn 38003 Reflection]
- 50-Turn Check-in: I explored the northern section of 3F via the (7, 10) stairs, battled a Burglar, and found a lore diary about Mewtwo! The southern half of 3F is walled off from that entry point, so I've returned to 2F. 
- Map Hygiene: Placed markers for the newly discovered stairs on 2F and 3F to ensure I don't get lost.
- Error Analysis & Navigation: The wall at Y=9 on 2F is not continuous! I just realized it ends at X=9. I can bypass it by walking through the gap at X=10/11.
- Custom Tools: Realized `safe_mash_b` and `use_item_in_battle` already fulfill the roles of a text clearer and catching automation. No new tools needed for these.