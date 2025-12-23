# Suicune Capture Strategy
## The Repel Trick
- Method: Super Repel filters wild Pokemon (Lv 13-16). Suicune (Lv 40) is the only possible encounter.
- Lead: KIMCHI (Lv 21 Gloom). *Note: Suicune outspeeds and flees Turn 1. Need faster Sleep/Mean Look user long-term.*
- Status: Super Repel active (Turn #13655). Milestones: 50 (T13670), 100 (T13693), 125 (T13708). Steps: 125/200.
- Last Check: confirmed on Route 38 (T13700). Next check: 150 steps.
- Time Tracking: Monday, 9:55 PM PST. (Hunt started 9:46 PM).

## Battle Strategy
- Target: Suicune (Lv 40, Base Speed 85).
- Lead: KIMCHI (Lv 21, Base Speed 40).
- Analysis: Suicune outspeeds KIMCHI. It will flee Turn 1 before Sleep Powder.
- Plan: Finish current Repel (200 steps). If unsuccessful, pivot to catching a fast Sleep/Trap user (e.g., Gastly in Sprout Tower at night).
- Catch Rate: ~0.52% (Full HP, No Status, Great Ball). ~4.3% if asleep. (Verified by Analyst T13681).
- Calcifer (Lv 45, Base 100) outspeeds Suicune but lacks status moves.

## Route 38 Environment
- Roamer Logic: Suicune moves routes ONLY when crossing map boundaries (Route 38/39 edge), using Fly, or after a battle.
- Boundary: Route 38 (0, 10) <-> Route 39 (19, 10).
- Location: Verified on Route 38 (Turn #13700).

## Tile Mechanics
- FLOOR: Standard traversable tile.
- TALL_GRASS: Standard encounter tile. Movement registers as steps.
- WALL/HEADBUTT_TREE: Impassable.
- LEDGE_HOP: One-way movement down or across.

# Strategy Notes
- Movement Lesson: Steps only count when coordinates change. Spinning in place (turning) does not deplete Repel or trigger encounters. To move between tiles, facing must be correct first.
- Accuracy Lesson: Verify player position frequently when using path-based movement to avoid drifting or incorrect step counts.
- Speed Lesson: Suicune outspeeds KIMCHI. Success requires a faster lead with Sleep (e.g., Haunter).
- Efficiency: Will check Pokédex every 50 steps to ensure Suicune is still on-route.