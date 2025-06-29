# Gem's Pokémon Crystal Notepad

## I. Party & Rival

### My Team
- G (CROCONAW): Lv18. **NOTE: Out of PP for WATER GUN.**
- HOOTHOOT (HOOTHOOT): Lv4
- HOOTIN (HOOTHOOT): Lv4
- ROCKY (ONIX): Lv6 (Traded for Bellsprout in Violet City)

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

## II. Game Mechanics & Systems

### PC Storage
- **Pokémon:** None
- **Items:** None

### Gifts & Trades
- Received POKéGEAR from Mom.
- Received a BERRY from a man on Route 30.
- Received 5 POKé BALLS from a scientist in Elm's Lab.
- Traded a Bellsprout for an Onix (ROCKY) in Violet City.
- Received HM05 (Flash) from the Elder in Sprout Tower.

### Observed Movesets
- G (CROCONAW): WATER GUN (0 PP), SCRATCH, LEER, RAGE
- ROCKY (ONIX): TACKLE, SCREECH. **NOTE: Does not have any Rock-type moves.**
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE
- Wild Bellsprout: VINE WHIP
- Wild Gastly: LICK, HYPNOSIS (Encountered in Sprout Tower)
- Wild Rattata: TACKLE (Encountered in Sprout Tower)

## III. Area & Navigation Insights

### Tile Traversal Rules (Verified)
- **Objects are impassable:** All map objects (items, trees, signs, defeated trainers etc.) act as walls.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS:** Traversable, triggers wild encounters.
- **LEDGE:** One-way downward traversal.
- **FLOOR_HOP_*_LEDGE:** One-way traversal in the specified direction.
- **COUNTER:** Impassable.
- **DOOR/CAVE:** Warp tile, triggered by movement.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING:** Impassable scenery.
- **WATER/CUT_TREE/BUOY:** Impassable.
- **PILLAR:** Impassable.
- **VOID:** Impassable.
- **WARP_CARPET_*: Warp tile, direction-specific.
- **FRUIT_TREE:** Impassable object, may yield items.
- **LADDER:** A warp tile, triggered by movement (not by pressing 'A'). Can be one-way or two-way. Must be tested.
- **STATUE:** An impassable scenery object.

### Sprout Tower Layout
- The central pillar on all floors is a complete divider, preventing east-west travel on the same floor, except for the 3rd floor.
- To cross between the east and west sides of the tower, you must go to the 3rd floor.
- The ladder at (10, 14) on 2F is a one-way warp *down* from the 3rd floor.
- The western side of the 1st floor is a dead end for exiting the tower.
- The main tower exit is on the eastern side of the 1st floor at (9, 15).

## IV. Untested Hypotheses
- **Hypothesis:** Can Onix learn Flash (HM05)?
- **Hypothesis:** HMs can be taught from the Pokémon status screen.

## V. Sprout Tower Escape Plan (Final!)
1.  Ascend from 1F West to 2F West using the ladder at (2, 6).
2.  Ascend from 2F West to 3F West using the ladder at (10, 14).
3.  On 3F, cross from the west side to the east side.
4.  Descend from 3F East to 2F East. (The ladder down is likely the one at (10, 14), which I confirmed is two-way).
5.  On 2F East, navigate to the ladder at (6, 4).
6.  Descend from 2F East to 1F East using the ladder at (6, 4).
7.  On 1F East, navigate to the main exit at (9, 15).