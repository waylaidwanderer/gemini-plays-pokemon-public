# Gem's Journey in Pokémon Crystal

## Current Objectives
- **Primary:** Reach Azalea Town.
- **Secondary:** Solve Ruins of Alph Puzzle.
- **Tertiary:** Hatch Egg.

## Tile Mechanics
- **FLOOR:** Standard traversable ground.
- **WALL:** Impassable obstacle.
- **FLOOR_UP_WALL:** Ledge (Likely one-way jump Down). *To be verified.*
- **LEDGE_HOP_RIGHT/DOWN:** One-way jumps.
- **HEADBUTT_TREE/CUT_TREE:** Impassable (interactable).
- **TALL_GRASS:** High encounter rate.
- **WARP_CARPET_LEFT/RIGHT:** Map transition.
- **DOOR/CAVE:** Warp to interior.
- **COUNTER:** Acts as wall, interactable.

## Navigation History & World Knowledge
- **New Bark Town:** Elm's Lab (6,3), Player's House (13,5).
- **Route 29:** Connects New Bark to Cherrygrove.
- **Cherrygrove City:** Center (29,3), Mart (17,7).
- **Route 30:** Right Path (East) -> Mr. Pokemon. Left Path (West) -> Route 31.
- **Route 31:** East Entrance (26, 17) -> Violet City Gatehouse.
- **Violet City:** Reached via Gatehouse.

## Trainer Card (Gem)
- **ID:** 24_6
- **Party:**
    1. GARNET (Quilava) Lv14 - Tackle, Leer, Smokescreen, Ember.
    2. TOPAZ (Sentret) Lv4 - Tackle.

## Dialogue Log
- **Officer (Route 32 Gate):** "RUINS OF ALPH / A Look-and-Touch Tourist Site / Try the sliding stone panels!"
- **Wade (Phone):** Found Berries. Waiting on Route 31.
- **Gentleman (Violet Center):** Team Rocket broken up 3 years ago by a kid.
- **Gameboy Kid (Violet Center):** Bill made the Pokemon PC storage system.
- **Youngster (Ruins Gate):** "There are drawings on stone panels. I tried moving them. I wonder what they are."
- **Gentleman (Violet Center):** Team Rocket broken up 3 years ago by a kid.

## Immediate Plan
- **Loot:** All items collected. (Berry, Heal Powder, Energypowder, Psncureberry).
- **Explore:** Check unseen corners (1,0) and (6,0).
- **Exit:** Leave the Ruins and continue to Azalea Town.
- **Exit:** Leave the Ruins and continue to Azalea Town.

## Ruins of Alph Notes
- **Outside:** East Entrance leads to Inner Chamber.
- **Inner Chamber:** Warp at (10,13) exits to Outside. Must navigate around it to cross room.
- **Puzzle:** Strange wall at back. Teacher says place feels "ethereal".

## Lessons Learned
- **Inventory Check:** Always verify current inventory in Game State before backtracking to buy items. (Mistake: Bought Escape Rope when I already had one).
- **Navigation:** Warps often require walking *into* the edge, not just standing on it.

## Ruins of Alph Strategy
- **Target:** Mystery Chamber (Kabuto Puzzle).
- **Location:** North-East of the main grounds (near sign at 16,8).
- **Hypothesis:** Use Escape Rope to open secret passage behind the puzzle.
- **Current Status:** Have 2 Escape Ropes. Searching for entrance north of the sign.

## Recent Events (Condensed)
- Defeated Falkner (Violet Gym), obtained Zephyr Badge & TM31.
- Defeated Elder Li (Sprout Tower), obtained HM05 (Flash).
- Rival Silver defeated in Cherrygrove.
- Mystery Egg obtained from Aide.
## Bag Order (Items Pocket)
1. Berry
2. Antidote
3. Potion
4. Parlyz Heal
5. X Accuracy
## Tool Reminders
- **Item Usage:** Use `use_item_sequence`.
- **NPCs:** Use `stun_npc` for moving NPCs.
- **Ghosts:** Normal moves fail (Lass tip).
- **Pokefan M (Violet City House):** Traded Pokemon grow fast but need badges to obey.
- **Trade (Violet City House):** Youngster wants a **Bellsprout** for his **Onix**. (Currently don't have Bellsprout).
- **Wade (Phone):** Bug-Catching Contest is at National Park today.
- **Sign at (24, 20):** "Violet City - The City of Nostalgic Scents"
- **Super Nerd (Violet City):** Beating the Gym Leader prepares you for "prime time".
- **Gym Guide (Violet Gym):** "Grass-type is weak against Flying-type."
- **Violet Gym Layout:** Center path seems to be the way forward (funnels through x=4,5 at y=11).
- **Battle Mechanic:** Cursor resets to Slot 1 (top left) every turn.
- **Falkner's Team:** Pidgey (Lv7), Pidgeotto (Lv9).
- **Exploration Note:** The area south of the Academy (x=20-36, y=26-32) is a cul-de-sac. Access to the rest of the city is via the path at x=27 (Northbound). The ledge at x=26 blocks Northbound movement.
- **Fruit Trees:** Must be interacted with from the tile directly below, facing UP.
- **Found Item:** PRZCUREBERRY at (14, 29) in Violet City.
- **Route 32 Side Path:** Accessed via gap at (18, 5). Cooltrainer M at (19, 8) gives **Miracle Seed**. Exploring south.
- **Route 32:** Caught Bellsprout (Lv7) named PERIDOT.
- **Wade (Phone):** Bug-Catching Contest is at National Park today.
- **Ruins of Alph Gate:** Pokefan M calls me "a scientist in the making". Officer silent.
- **Ruins of Alph:** Sign says "Visitors Welcome".
- **Inner Chamber:** Statues and strange wall are silent/non-interactive.
- **Teacher:** Says the place feels "ethereal".
- **Exploration:** Exploring West side of the chamber.
- **Scientist (Research Center):** Ruins are 1500 years old, origin unknown.
- **Computer:** Log entry "Exploration Year 10".
- **Scientist 2 (Research Center):** Patterns on walls are keys to the mystery.
- **Warp Mechanics:** Gatehouse warp at (13, 20/21) confirmed as `WARP_CARPET_RIGHT` (enter from Left).
- **Puzzle Wall (Kabuto Chamber):** Solved.
- **Current Status:** Puzzle solved. Fell into Main Chamber. "Strange presence" (Unown) detected.
- **Next:** Catch Unown, then Exit to Route 32 via ladder at (10,13).
- **Unown:** Encountered Wild Unown (High catch rate, throw balls).
- **Unown:** Attempt 3 failed. Throwing LAST ball.
- **Unown:** CAUGHT! (Level 5). Nicknaming 'UNAKITE'.