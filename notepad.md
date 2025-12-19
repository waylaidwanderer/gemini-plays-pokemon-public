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
## Ilex Forest
- Signpost at (3, 17).
- Shrine at (8, 22): Honors the forest's protector.
- Rocker NPC at (15, 14): Headbutt Tutor.

## Route 34
- Gatehouse to Ilex Forest at (13, 37) and (14, 37).
- Trainer Tips sign at (13, 33).
- Day-Care at (10, 14).
- Defeated Pokefan Brandon at (18, 28). Opponent: Snubbull (Lv 13).
- Defeated Youngster Ian at (11, 21). Opponents: Mankey (Lv 10), Diglett (Lv 12).
- Verified: The back door at (13, 15) on Route 34 connects to the Day-Care backyard (2, 7). (Turn 3427)
- Apophis (Ekans, Lv 4) left with Day-Care Lady (Granny) at (5, 3). (Turn 3422)

## Goldenrod City
- Pokémon Center at (15, 27).
- Underground South Entrance at (11, 29).
- **Strategy**: Systematically explore the city by quadrants.
    1. Check all buildings in the immediate vicinity of the Pokémon Center.
    2. Head north to find the Radio Tower and Gym.
    3. Locate the Department Store for supplies.
    4. Speak to all NPCs for city lore and potential items (e.g., Bike, Coin Case).

# Lessons Learned
- **Type Matchups**: Onix (Rocky) is 4x weak to Grass (Absorb). Paras is 4x weak to Fire (Ember).
- **Running**: Use Calcifer (Quilava) as lead for high escape probability from wild battles.
- **Tool Hygiene**: Refined find_path_v4 and explore_unseen_v1 to treat 'unseen' tiles as impassable. Added HEADBUTT_TREE and WATER to collision checks.
- **Item Usage**: `use_item_v4` is for the Items pocket only. TMs require manual navigation or a specialized tool (`use_tm_v1`).
- **Nicknaming**: FRITTATA (Togepi) hatched on Turn 3330.
- **NPC Collision**: Defeated trainers (and other NPCs) remain as solid objects on the map and must be navigated around. (Observed Turn 3374).
- **Turn Tracking**: Always verify the current turn number from Game State to avoid mismatches.
- Received ODD EGG from Day-Care Man (Turn 3425). Cleffa is currently named "EGG". status: "Needs more time". (Walking to hatch).
- Strategy: Explore Goldenrod City. Priority: Gym, Radio Tower, Dept. Store. Check buildings near PC first.