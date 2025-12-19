# Tile Mechanics
- `FLOOR`: Traversable. Standard ground.
- `WALL`: Impassable. Collision type for trees, rocks, and boundaries.
- `WATER`: Impassable. Requires the HM for Surf to traverse.
- `HEADBUTT_TREE`: Impassable. Block movement; can be interacted with if the player has Headbutt.
- `LEDGE_HOP_LEFT/RIGHT/DOWN`: One-way traversal. Jump over in the specified direction; cannot return.
- `WARP_CARPET_RIGHT/LEFT/DOWN`: Triggers a map transition when walking off the map edge.
- `CUT_TREE`: Impassable until Cut is used (Verified at (8, 25)).
- `TALL_GRASS`: Traversable. Can trigger wild encounters.
- `LONG_GRASS`: Traversable. Functions like tall grass (Observed on Route 34).
- `DOOR`: Triggers a map transition when entered.
- `FENCE`: Visual representation of a WALL. Impassable. (Observed on Route 35).
- `BOOKSHELF`, `PC`, `TOWN_MAP`, `WINDOW`: Impassable.

# Area Knowledge
## Route 34
- Gatehouse to Ilex Forest at (13, 37) and (14, 37).
- Day-Care at (10, 14).
- Verified: Back door at (13, 15) connects to backyard (2, 7). (Turn 3427)
- Apophis (Ekans, Lv 4) left with Day-Care Lady at (5, 3). (Turn 3422)

## Goldenrod City
- Pokémon Center at (15, 27).
- Underground South Entrance at (11, 29).
- Radio Tower: Running a promotion for Pokégear radio card. (Turn 3466)
- Hypothesis: Door at (14, 21) is likely the Game Corner entrance.

## Route 35
- Gatehouse at (19, 1) in Goldenrod connects to Route 35.
- Quest: Officer at (0, 4) in Goldenrod Gatehouse wants a Pokémon with Mail delivered to a friend on Route 31. Received KENYA (Spearow, Lv 10) with Mail. (Turn 3513)
- Hint: Officer mentioned a "weird tree" blocking the road near Goldenrod. (Turn 3513)

# Trainer Roster
- Pokefan Brandon (Route 34): Snubbull (Lv 13)
- Youngster Ian (Route 34): Mankey (Lv 10), Diglett (Lv 12)
- Camper Elliot (Route 35): Sandshrew (Lv 13), Marill (Lv 15)
- Camper Ivan (Route 35): Diglett (Lv 10), Diglett (Lv 14), Zubat (Lv 10)
- Firebreather Walt (Route 35): Magmar (Lv 11), Magmar (Lv 11)
- Juggler Irwin (Route 35): Voltorb (Lv 2), Voltorb (Lv 6), Voltorb (Lv 10), Voltorb (Lv 14) (Note: Sprite is SUPER_NERD, ID 8)