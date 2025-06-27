# Pokémon Crystal Journey

## Current Plan
- My team is healed and I am back on Route 30.
- I will take the western path, as the eastern path was a dead end.
- I will proceed north on the western path, fighting or avoiding trainers and wild Pokémon as necessary, until I reach Violet City.

## The Rival
- A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Game Mechanics & Discoveries
### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.

### Battle Mechanics
- **Held Items (Berries):** Pokémon can use held Berries to heal themselves in battle.
- **Catching:** Weakening a Pokémon makes it easier to catch.

### Tile & Environmental Mechanics
- **WALL:** An impassable obstacle.
- **FLOOR:** A standard, traversable tile.
- **TALL_GRASS:** Traversable tile where wild Pokémon encounters can occur.
- **CUT_TREE:** These small trees are impassable and require the HM 'Cut' to be removed.
- **Fruit Trees:** These are impassable objects.
- **HOP_DOWN:** A one-way ledge that can only be jumped down from above.
- **Route 29 Ledges:** The western section of Route 29 has one-way ledges preventing eastward travel from that area.
- **Route 46 Ledges:** This route is a dead-end when approached from the south due to one-way ledges.
- **Decorative Floor Items:** Certain floor patterns, like the red flowers on Route 30, are purely decorative and cannot be interacted with or picked up. Confirmed at (10, 31) after multiple failed attempts.
- **Route 30 Hidden Potion:** Unable to retrieve the hidden Potion at (14, 9). Tried interacting from multiple adjacent tiles without success. There might be a special requirement I don't meet yet.

## Agent Ideas & Refinements
- **battle_strategist_agent:** An agent to suggest the optimal move or action in difficult battles.
- **route_summary_agent:** An agent to parse map data and markers to give a high-level summary of a route's completion status.

## Pokémon Encounters
### Route 30
- **Ledyba (Lv. 3):** Bug/Flying type. Observed move: TACKLE.
- **Caterpie (Lv. 3-4):** Bug type. Observed moves: TACKLE, STRING SHOT.
- **Weedle (Lv. 3):** Bug/Poison type. Observed moves: STRING SHOT, POISON STING.
- **Pidgey (Lv. 4):** Normal/Flying type. Ran from it, no moves observed.