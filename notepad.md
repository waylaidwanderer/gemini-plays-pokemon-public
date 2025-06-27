# Pokémon Crystal Journey

## Current Plan
- I am currently on Route 30, trying to get to Violet City.
- The eastern path is a dead end.
- I am on the western path of Route 30. I will now explore north to find the way to Violet City.

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
- **DOOR:** A warp tile that leads into and out of buildings.
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
- **party_manager_agent:** An agent to suggest when to heal or what Pokémon to lead with based on the current route's encounters.
- **world_knowledge_navigator:** An agent that can plan multi-map routes using the world knowledge graph.

## Pokémon Encounters
### Route 30
- **Ledyba (Lv. 3):** Bug/Flying type. Observed move: TACKLE.
- **Caterpie (Lv. 3-4):** Bug type. Observed moves: TACKLE, STRING SHOT.
- **Weedle (Lv. 3):** Bug/Poison type. Observed moves: STRING SHOT, POISON STING.
- **Pidgey (Lv. 4):** Normal/Flying type. Ran from it, no moves observed.
- **VOID:** Appears to be an impassable boundary tile, typically outside the playable area of a map.
- **WARP_CARPET_DOWN:** A warp tile, usually found at the entrance/exit of buildings. Stepping on it transports the player to a different map.
- **HEADBUTT_TREE:** Appears to be an impassable tree.
- **WATER:** Appears to be an impassable body of water, likely requires HM 'Surf'.
- **Route 30 Western Path:** This path is a dead end for now, blocked by a CUT_TREE at (8, 6).