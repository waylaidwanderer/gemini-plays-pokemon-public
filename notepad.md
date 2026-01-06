# Tile Mechanics
- FLOOR: Standard ground.
- WALL: Impassable.
- TALL_GRASS: Reachable encounters.
- LEDGE_HOP_DOWN: One-way south. Impassable from south/east/west.
- FLOOR_UP_WALL: Impassable ledge bottom.
- WATER: Requires SURF to cross.
- WHIRLPOOL: Requires WHIRLPOOL to clear.

## Strategy: Johto League
- Training: Grind Xenon (Lv26) and Kimchi (Lv21) to Lv30+.
- Efficiency: Lead with trainee, switch to Calcifer (Lv48) or Gneiss (Lv45). Use battle_analyst_v2 move/switch recommendations STRICTLY. Do not ignore agent output.

# Progress Tracker
- Xenon (Lv26) -> Target: Lv30.
- Kimchi (Lv21) -> Target: Lv30.
- Start Turn (Training): 30811 (Tuesday, Jan 6, 2026, 2:28 PM PST)
- Current Task: Fly to Blackthorn City (Started Turn 30941)

# Lessons Learned
- Tile Verification: FLOOR_UP_WALL is a wall/ledge bottom. (5, 2) on Route 46 is a dead end.
- Ledge Awareness: Route 45/46 require careful pathfinding due to one-way ledges. Most paths are one-way SOUTH. To return to Blackthorn City from Route 29/Cherrygrove, use FLY or travel back through Ice Path.
- Warp Safety: find_path_v2 avoid_warps=True prevents accidental transitions.
- Strength Mechanic: Strength must be used on each individual boulder; it is not a persistent status.
- Tool Hygiene: use_item_from_bag_v2 requires the bag to be open. Always use press_menu_buttons to navigate to the Pack first.
- Fly Map Logic: Destination names MUST be verified in Screen Text after every button press. The cursor does not follow a simple geographical grid.
## Fly Navigation Attempts (Blackthorn City)
- Attempt 1 (Turn 30941): Fumbled menus, ended up in Pokegear/Trainer Card.
- Attempt 2 (Turn 30975): Interrupted by Alan's call, stuck in menu loop.
- Strategy: Clear menus with B, then Start -> Pokemon -> Icarus -> Fly. Verify destination text after every map move.