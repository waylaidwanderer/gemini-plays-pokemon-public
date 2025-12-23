# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
- Train XENON (Gastly) to Lv 13 to learn Mean Look.
- Evolve to Haunter (Lv 25) and train to ~Lv 38-40. While Haunter has a higher Base Speed (95) than Suicune (85), at Lv 25 it will be slower than the Lv 40 Suicune. Haunter needs to be faster than Suicune to use Mean Look before it flees; Lv 38-40 ensures we outspeed Suicune's potential 73-110 Speed range.
- Track Suicune using Pokedex AREA map.
- Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Great Balls.
- Status Requirement: Status conditions are mandatory for Suicune.
- Item Goal: Upgrade to Ultra Balls (2.0x multiplier) at Goldenrod or Blackthorn Marts.
- Contingency: If Hypnosis fails, consider switching to KIMCHI (Gloom) for Sleep Powder (75% accuracy in Gen 2).

## Game Mechanics & Lessons
- Ghost-type Moves: Lick (Ghost) does not affect Normal types.
- Ghost-type Resistances: Leech Life (Bug) is "not very effective" against Ghost types.
- Accuracy/Status: Status moves like Supersonic can hit Ghost types (not immune).
- Status Moves: "It didn't affect" is the message for a miss or blocked status move (e.g. Hypnosis missing Wooper).
- Switching: Clears confusion and resets stat changes.
- Sweet Scent: Triggers immediate encounters on valid grass tiles.
- Type Effectiveness: Use `get_type_effectiveness_gen2` tool for verified matchups.
- Menu Wrapping: 
    - Start Menu (8 items): ONE-WAY WRAP. Up at POKEDEX (1) goes to EXIT (8). Down at EXIT (8) does NOT wrap. (Verified Turn 14303). Reset to EXIT (8) with Down 8 times.
    - Party Menu (7 items: 1-6 + CANCEL): FULLY WRAPS. Both Up at 1 and Down at 7 wrap. (Verified Turn 14328). No absolute reset; must track current index.
    - PKMN Pop-up Menu (variable size): WRAPS. For KIMCHI (2 field moves), it has 7 items: 1.SWEET SCENT, 2.CUT, 3.STATS, 4.SWITCH, 5.MOVE, 6.ITEM, 7.CANCEL.
    - Battle Move Menu (4 items): WRAPS. (Verified Turn 14288). 
    - Move Selection: In the overworld pop-up menu, field moves are listed at the top. The 'MOVE' option (#5 for KIMCHI) is for reordering.
- Phone Calls: Incoming calls interrupt button sequences. Tools must start with B-presses to clear dialogue.

## Training Plan: XENON (How)
- Method: Use Sweet Scent at (18, 15) grass patch.
- Strategy: Use Lick against Gastly and Bellsprout. RUN from Normal-types (Rattata, Hoothoot, Pidgey) and low-EXP targets (Zubat) to conserve PP and health.
- Maintenance: Heal with Fresh Water/Lemonade when HP < 10.

## Tile Mechanics (Route 32)
- FLOOR: Standard traversable ground. Verified.
- TALL_GRASS: Encounter-eligible ground. Verified.
- WALL/HEADBUTT_TREE: Impassable boundaries. Verified.
- LEDGE_HOP_DOWN: One-way jumpable ledge (South). Verified at (16, 15).
- LEDGE_HOP_RIGHT: One-way jumpable ledge (East). Verified at (17, 12).
- WATER: Impassable without Surf. Verified.
- DOOR/DOOR_04/CAVE: Warp entry points. Verified.
- COUNTER: Interaction point for NPCs; impassable. Verified.
- NPC: Map objects that block movement. Verified.
- WARP_CARPET_LEFT: Map transition point. Verified.
## Reflection (Turn 14332)
- Deferral Check: No tasks deferred; menu issues addressed immediately with tool refinement.
- Notepad Hygiene: Sections organized; redundant logs removed; training task turn recorded (14146).
- Map Hygiene: Signs and NPCs marked; training spot marked.
- Automation Strategy: use_pokemon_move_v1 refined with absolute resets for reliability.
- Goal Clarity: Goals reflect WHAT, notepad reflects HOW.
- Error Analysis: Menu wrapping verified for Start, Party, and Battle Move menus. Lesson: Use absolute resets (Up N times) for cursor-agnostic menu navigation.