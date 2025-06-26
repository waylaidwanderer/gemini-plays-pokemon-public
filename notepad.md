# Pokémon Crystal Journey

## Current Situation
- **Objective:** Find the correct path to Violet City.
- **Location:** Route 30, at (10, 30).
- **Next Step:** Test hypothesis for picking up items on the ground.

## Long-term Goal
- Become the Pokémon League Champion.

## The Rival
- A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Mechanics & Discoveries
### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.

### Battle Mechanics
- **Held Items (Berries):** Pokémon can use held Berries to heal themselves in battle.
- **Catching:** Weakening a Pokémon makes it easier to catch.

### Tile & Environmental Mechanics
- **FLOOR:** A standard, traversable tile.
- **TALL_GRASS:** Traversable tile where wild Pokémon encounters can occur.
- **Route 29 Ledges:** The western section of Route 29 has one-way ledges preventing eastward travel from that area.
- **Route 46:** This route is a dead-end when approached from the south due to one-way ledges.
- **CUT_TREE:** These small trees are impassable and require the HM 'Cut' to be removed.
- **Fruit Trees:** These are impassable objects.
- **Item Pickups:** Cannot be picked up by standing on them. Hypothesis: must interact from an adjacent tile while facing the item.

## Agent Ideas
- **battle_strategist_agent:** An agent to suggest the optimal move or action in difficult battles.
- **route_summary_agent:** An agent to parse map data and markers to give a high-level summary of a route's completion status.

## Pokémon Encounters
### Route 30
- **Ledyba (Lv. 3):** Bug/Flying type. Observed move: TACKLE.
- **Caterpie (Lv. 3-4):** Bug type. Observed moves: TACKLE, STRING SHOT.
- **Weedle (Lv. 3):** Bug/Poison type. Observed move: STRING SHOT.
- **Pidgey (Lv. 4):** Normal/Flying type. Ran from it, no moves observed.