# Tile Mechanics
- `FLOOR`: Traversable. Standard ground.
- `WALL`: Impassable. Collision type for trees, rocks, and boundaries.
- `WATER`: Impassable. Requires the HM for Surf to traverse.
- `HEADBUTT_TREE`: Impassable. These trees block movement and can be interacted with if the player has Headbutt.
- `LEDGE_HOP_LEFT/RIGHT/DOWN`: One-way traversal. The player can jump over these in the specified direction but cannot return.
- `WARP_CARPET_RIGHT/LEFT/DOWN`: Triggers a map transition when walking off the edge of the current map.
- `CUT_TREE`: Impassable until the move Cut is used on it. (Verified at (8, 25)).
- `TALL_GRASS`: Traversable. Walking in this tile can trigger wild Pokémon encounters.
- `LONG_GRASS`: Traversable. Functions like tall grass but with different encounter rates or species. (Observed on Route 34).
- `DOOR`: Triggers a map transition when entered.
- `BOOKSHELF`: Impassable.
- `PC`: Impassable.
- `TOWN_MAP`: Impassable.
- `WINDOW`: Impassable.

# Area Knowledge
## Route 34
- Gatehouse to Ilex Forest at (13, 37) and (14, 37).
- Day-Care at (10, 14).
- Verified: The back door at (13, 15) on Route 34 connects to the Day-Care backyard (2, 7). (Turn 3427)
- Apophis (Ekans, Lv 4) left with Day-Care Lady (Granny) at (5, 3). (Turn 3422)

## Goldenrod City
- Pokémon Center at (15, 27).
- Underground South Entrance at (11, 29).
- Radio Tower: Promotional campaign for Pokégear radio card. (Turn 3466)
- Target: Goldenrod Gym (Whitney), Radio Tower, Department Store.
- Hypothesis: Door at (14, 21) is likely the Game Corner entrance.

## Route 35
- Gatehouse at (19, 1) in Goldenrod connects to Route 35.
- Quest: Officer at (0, 4) in Goldenrod Gatehouse (Route 35) wants a Pokémon with Mail delivered to a friend on Route 31. Received KENYA (Spearow, Lv 10) with Mail. (Turn 3513)
- Hint: Officer mentioned a "weird tree" blocking the road near Goldenrod. (Turn 3513)

# Trainer Roster
- Pokefan Brandon (Route 34): Snubbull (Lv 13)
- Youngster Ian (Route 34): Mankey (Lv 10), Diglett (Lv 12)

# Strategy: Goldenrod Exploration
1. Return to Gatehouse, accept the Spearow, and proceed to Route 35.
2. Systematically explore Goldenrod quadrants: Gym, Radio Tower, Dept. Store.
3. Speak to all NPCs for city lore and items (Bike, Coin Case).

# Lessons Learned
- **Type Matchups**: Onix (Rocky) is 4x weak to Grass (Absorb). Paras is 4x weak to Fire (Ember).
- **Running**: Use Calcifer (Quilava) as lead for high escape probability.
- **Tool Hygiene**: find_path_v5_unseen_traversable treats 'unseen' as passable for exploration.
- **Nicknaming**: FRITTATA (Togepi) hatched Turn 3330.
- **NPC Collision**: Defeated trainers (and others) are solid objects.
- Odd Egg status: "Needs more time". (Turn 3477 summary check).