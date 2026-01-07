# Tile Mechanics (Global)
- FLOOR: Traversable. Individual Behavior: Standard movement.
- WALL: Impassable. Individual Behavior: Blocks movement. Mechanics: Interact with objects (signs, PCs) from adjacent tiles.
- TALL_GRASS: Traversable. Individual Behavior: Triggers wild encounters.
- LEDGE_HOP_DOWN: Traversable (One-way South). Relational Behavior: Jump down from North; impassable from South/East/West.
- LEDGE_HOP_LEFT: Traversable (One-way West). Relational Behavior: Jump across from East; impassable from West/North/South.
- LEDGE_HOP_RIGHT: Traversable (One-way East). Relational Behavior: Jump across from West; impassable from East/North/South.
- CAVE: Traversable/Warp. Individual Behavior: Entrance to indoor areas.
- WATER: Traversable with SURF. Mechanics: Requires HM03 Surf and appropriate badge.
- CUT_TREE: Blockage. Mechanics: Removed by using HM01 Cut.
- BOULDER: Blockage. Mechanics: Pushed by using HM04 Strength.
- FLOOR_UP_WALL: Impassable. Individual Behavior: Represents the base of a ledge or wall.

# Strategy: Rising Badge (Gym Leader Clair)
- Opponent Analysis: Uses Dragon-types. Kingdra (Water/Dragon) is the primary threat, weak only to Dragon-type moves.
- Tactical Plan: Use Xenon's Night Shade for fixed damage (28+ HP per turn) to bypass high defenses. Gneiss provides physical bulk and Earthquake. Calcifer's Thunderpunch is neutral but powerful.
- Training Goal: Level Xenon and Kimchi to 30+ to improve stats and move consistency.

# Strategy: Johto League Training
- Method: Lead with lower-level Pokemon (Kimchi/Xenon) to share EXP. Switch to Gneiss or Calcifer for heavy lifting.
- Criteria: Return to Blackthorn PC when Xenon's Night Shade PP or Gneiss's Earthquake PP reaches 0.
- Efficiency: Grind in Route 45 grass (4,12)-(5,12).

# Progress Tracker
- Xenon (Lv28): 18741 EXP. Target Lv30: 21760 EXP (~3019 remaining).
- Kimchi (Lv26): 14888 EXP. Target Lv30: 21760 EXP (~6872 remaining).
- Gneiss (Lv46): 109/129 HP. Earthquake PP: 6/10.
- Grinding Start: Turn #31060 (Tuesday, Jan 6, 2026, 3:20 PM).
- Last Update: Turn #31543 (Tuesday, Jan 6, 2026, 7:37 PM).
- Encounter Log: Donphan (Lv25/30), Geodude (Lv23), Graveler (Lv23/25/27), Gligar (Lv24), Skarmory (Lv24). Gligar uses Sand-Attack/Poison Sting. 

# Battle Strategies & Observations
- Night Shade: Deals fixed damage equal to user's level. Perfect for grinding and bypassing defenses.
- Sleep Powder: Observed failing on certain targets with the message "It didn't affect". Hypothesis: Target may have an existing status or a held item. Discarded gender-based effectiveness.
- Hypnosis: Confirmed effective against Graveler. Failed on male Gligar (Message: "It didn't affect").
- Selfdestruct: Major threat from wild Graveler. Switch to Gneiss or use status moves to mitigate risk.

# Evolution Methods (Hypotheses)
- Gloom: Likely Leaf or Sun Stone. (Unverified)
- Haunter: Likely Trading. (Unverified)

# General Mechanics & Lessons
- Route 45 Navigation: Ledges make most paths one-way SOUTH. Use FLY to return to Blackthorn.
- Strength: Must be activated manually via the menu or by interacting with a boulder while the HM is known.
- Fly Map: Systematic navigation required. Confirm destination city name in screen text before pressing A. Avoid assuming grid-based movement.
- Tool Usage: Ensure correct inventory pocket is passed to `use_item_from_bag_v2`.