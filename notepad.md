# Suicune Capture Strategy
## The Repel Trick
- Method: Super Repel filters wild Pokemon (Lv 13-16). Suicune (Lv 40) is the only possible encounter.
- Lead: KIMCHI (Lv 21 Gloom). Moves: ABSORB, SWEET SCENT, CUT, SLEEP POWDER.
- Strategy: Pace in tall grass on Route 38.
- Battle Prep: Suicune (Base Speed 85) outspeeds KIMCHI (Base Speed 40). It will likely flee Turn 1.
- Catch Rate: ~0.39% (Full HP, No Status, Great Ball). ~4.3% if asleep.
- Analysis: Calcifer (Lv 45, Base 100) outspeeds Suicune but lacks status moves.

## Strategy for Catching Suicune
1. Pivot: Fly to Violet City and enter Sprout Tower (currently Night).
2. Catch a Gastly.
3. Train Gastly to Lv 13+ (learns Mean Look) and ensure it has enough Speed (Base 80/95) to outspeed Suicune (Base 85).
4. Encounter Suicune, use Mean Look, then Hypnosis.

## Hunting Session Tracking
- Sprout Tower Hunt Start: Turn #13848
- Target: Gastly (Night only, Lv 3-6)
- Status: No Repel active (Required for low-level encounters)
- Total Great Balls: 40

## Global Tile Mechanics
- FLOOR: Standard traversable tile.
- TALL_GRASS: Standard encounter tile. Movement registers as steps.
- WALL/HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN/LEFT/RIGHT: One-way movement in the specified direction.
- WARP_CARPET_RIGHT: Map transition to Ecruteak Gatehouse.
- WATER: Traversable only with HM SURF.
- ICE: Causes sliding until an obstacle is hit.
- COUNTER: Stand in front of it to interact with NPCs behind it.
- LADDER: Warp between floors (e.g., Sprout Tower).
- NPC: All map objects act as walls.

## Strategy Notes
- Roamer Logic: Suicune moves routes ONLY when crossing map boundaries, using Fly, or after a battle with it.
- Roamer Status: Unknown (Reset by Fly at T13845).
- Efficiency: Use the `pacer` tool to automate hunting. Check Pokédex every 50-100 steps.
- Gastly Goal: Mean Look (Lv 13) prevents Suicune from fleeing. Hypnosis (Lv 1) for status.
- Speed Check: Gastly (Base 80) / Haunter (Base 95) vs Suicune (Base 85). Haunter is preferred for guaranteed outspeeding.