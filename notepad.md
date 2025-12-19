# Ilex Forest Strategy: Catching Farfetch'd

## Goal: Catch the runaway Farfetch'd to obtain HM01 (Cut).

## Farfetch'd Chase Log (Flight Logic)
- **Bird at (14, 31)**: Approached from South (14, 32) -> Flew North to (14, 28).
- **Bird at (15, 25)**: Approached from South (15, 26) -> Flew North to (15, 23) -> then (20, 24).
- **Bird at (20, 24)**: Approached from North (20, 23) -> Flew East to (28, 31).
- **Bird at (28, 31)**: Approached from West (27, 31) -> Flew North to (29, 22).
- **Bird at (29, 22)**: Approached from West (28, 22) -> Flew South to (29, 26) or further.
- **Current Position**: Unknown (South of 29, 22).

## Strategy
- The bird flies in the opposite direction of the player's approach.
- To catch it, I must interact with it while standing on the tile directly behind it (the direction it is NOT facing).
- If it cannot fly away (dead end), it may be caught.

## Post-Catch Plan
1. Return to the apprentice (7, 28).
2. Go to Charcoal Kiln in Azalea Town (21, 13) to get HM01 Cut.
3. Teach Cut to a compatible Pokemon (check PC/Party).
4. Clear the tree blocking the way to Route 34.

## Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- HEADBUTT_TREE: Impassable. Triggers encounters with Headbutt.
- TALL_GRASS: Wild battles.
- LEDGE: One-way jump.

## Azalea Town References
- Kurt's House (9, 5): Kurt (3, 2) makes balls.
- Charcoal Kiln (21, 13): Boss gives Cut.

## Party Status
- Calcifer (QUILAVA) Lv22: QUICK ATTACK, LEER, SMOKESCREEN, EMBER.
- ROCKY (ONIX) Lv6: TACKLE, SCREECH.
- GNEISS (GEODUDE) Lv15: TACKLE, DEFENSE CURL, ROCK THROW.
- ICARUS (PIDGEY) Lv11: TACKLE, SAND-ATTACK, GUST.
- EGG (TOGEPI) Lv5: GROWL, CHARM.
- APOPHIS (EKANS) Lv4: WRAP, LEER.

## Lessons Learned
- Bird Chase: Don't interact from the front if you want to catch it; get behind it.
- Movement: NPCs move automatically; track them via Game State 'NPC Movement Paths'.
- Reflection: Perform self-assessments every 50 turns to fix tools and update markers.
- Time Blindness: Chasing Farfetch'd started Turn 2803. Current Turn 2856.
## Catch Attempt #1 (Turn 2861)
- Bird at (29, 22), Facing: DOWN.
- Strategy: Approach from West (28, 22). Trap against East VOID edge.
- Input: [Left, Up, Up, Right, A]