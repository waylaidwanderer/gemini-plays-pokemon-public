# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
- Train XENON (Gastly) to Lv 13 to learn Mean Look.
- Evolve to Haunter (Lv 25) to ensure Base 95 Speed (Suicune is Base 85). Haunter needs to be faster than Suicune to use Mean Look before it flees.
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
    - Start Menu (8 items): Wraps.
    - Party Menu (6 items + CANCEL): Wraps.
    - Battle Move Menu (4 items): DOES NOT wrap.
- Phone Calls: Incoming calls interrupt button sequences. Tools must start with B-presses to clear dialogue.

## Training Plan: XENON (How)
- Start Turn: 14146
- Method: Grind on Route 32 grass using Sweet Scent.
- Strategy: Flee from Normal-types (Rattata, Hoothoot, Pidgey) to conserve Lick PP.
- Maintenance: Use Fresh Water/Lemonade from pack to heal when HP < 10.

## Route 32 Observations
- Ledge at (16, 15): Jumpable south (LEDGE_HOP_DOWN). Marked ⤵️.
- Slowpoketail Scam: NPC at (11, 67) tries to sell a tail for ¥1,000,000. Verified dead end/scam. Marked 🚫.

## Tile Mechanics (Verified)
- FLOOR: Standard traversable tile.
- TALL_GRASS: Standard encounter tile.
- WALL/HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN: Jumpable one-way movement south. Verified at (16, 15).
- WARP_CARPET: Map transition. Verified.
- COUNTER: Interaction point for NPCs; impassable.
- NPC: Map objects that block movement. Verified.