# Suicune Capture Strategy
## The Repel Trick
- Method: Super Repel filters wild Pokemon (Lv 13-16). Suicune (Lv 40) is the only possible encounter.
- Lead: KIMCHI (Lv 21 Gloom). *Note: Suicune outspeeds and flees Turn 1. Need faster Sleep/Mean Look user long-term.*
- Status: Super Repel active (Used Turn #13655). ~200 steps remaining.
- Strategy: Use navigate to pace between (25, 7) and (24, 7) to ensure steps are registered.

## Battle Strategy
- Target: Suicune (Lv 40, Base Speed 85).
- Lead: KIMCHI (Lv 21, Base Speed 40).
- Plan: Inflict Sleep (Sleep Powder) to prevent fleeing. HP/status are persistent.
- Catch Rate: ~0.39% (Full HP, No Status, Great Ball). ~4.3% if asleep.
- Contingency: Catch a faster Pokémon with Sleep/Mean Look (e.g., Haunter/Golbat).

## Route 38 Environment
- Roamer Logic: Suicune moves routes ONLY when crossing map boundaries (Route 38/39 edge), using Fly, or after a battle.
- Boundary: Route 38 (0, 10) <-> Route 39 (19, 10).
- Location: Verified on Route 38 (Turn #13640).

## Tile Mechanics
- FLOOR: Standard traversable tile.
- TALL_GRASS: Standard encounter tile. Movement registers as steps.
- WALL/HEADBUTT_TREE: Impassable.
- LEDGE_HOP: One-way movement down or across.

# Strategy Notes
- Movement Flaw: Previous 'pacing' attempts failed to change coordinates, resulting in 0 steps taken. Must use path_plan to move between tiles.
- Speed Issue: Suicune will always flee before KIMCHI can act. Success relies on eventually landing Sleep Powder or switching to a faster lead.