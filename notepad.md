# Suicune Capture Strategy
## The Repel Trick
- Method: Super Repel filters wild Pokemon (Lv 13-16). Suicune (Lv 40) is the only possible encounter.
- Lead: KIMCHI (Lv 21 Gloom). Moves: ABSORB, SWEET SCENT, CUT, SLEEP POWDER.
- Strategy: Pace in tall grass on Route 38. Suicune is confirmed on this route.
- Battle Prep: Suicune (Base Speed 85) outspeeds KIMCHI (Base Speed 40). It will likely flee Turn 1.
- Catch Rate: ~0.52% (Full HP, No Status, Great Ball). ~4.3% if asleep.
- Analysis: Calcifer (Lv 45, Base 100) outspeeds Suicune but lacks status moves.
- Plan: Finish current Repel. If unsuccessful, pivot to catching a fast Sleep/Trap user (e.g., Gastly/Haunter).

## Tile Mechanics - Route 38
- FLOOR: Standard traversable tile.
- TALL_GRASS: Standard encounter tile. Movement registers as steps.
- WALL/HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN: One-way movement down.
- LEDGE_HOP_LEFT: One-way movement left.
- LEDGE_HOP_RIGHT: One-way movement right.
- WARP_CARPET_RIGHT: Map transition to Ecruteak Gatehouse.

## Strategy Notes
- Roamer Logic: Suicune moves routes ONLY when crossing map boundaries (Route 38/39 edge), using Fly, or after a battle with it.
- Boundary: Route 38 (0, 10) <-> Route 39 (19, 10).
- Efficiency: Use the `pacer` tool to automate hunting. Check Pokédex every 50-100 steps.
- Last Check: confirmed on Route 38 (Turn #13796). Check successful.
- Time Tracking: Monday, 10:27 PM PST.