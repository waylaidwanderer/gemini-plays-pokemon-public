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
    - Start Menu (8 items): WRAPS. (Verified Turn 14304 - Up at POKEDEX goes to EXIT).
    - Party Menu (6 items + CANCEL): Wraps.
    - Battle Move Menu (4 items): WRAPS. (Verified Turn 14288). The cursor-agnostic 'Up*3' reset in select_move_v4 is BROKEN because of this. Use select_move_v5 and check cursor position in screen text first.
    - Battle Move Menu also remembers the last selected move within the same battle.
- Phone Calls: Incoming calls interrupt button sequences. Tools must start with B-presses to clear dialogue.

## Training Plan: XENON (How)
- Start Turn: 14146
- Method: Grind on Route 32 grass using Sweet Scent.
- Strategy: Flee from Normal-types (Rattata, Hoothoot, Pidgey) to conserve Lick PP.
- Maintenance: Use Fresh Water/Lemonade from pack to heal when HP < 10.
- Strategy: Use Lick against Gastly/Bellsprout. Run from others.

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