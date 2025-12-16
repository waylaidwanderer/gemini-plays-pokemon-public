# Gem's Journey in Pokémon Crystal

## Current Objectives
- **Primary:** Earn the Zephyr Badge in Violet City.
- **Secondary:** Explore Violet City.
- **Tertiary:** Locate Sprout Tower.

## Tile Mechanics
- **FLOOR:** Standard traversable ground.
- **WALL:** Impassable obstacle.
- **FLOOR_UP_WALL:** Ledge (Likely one-way jump Down). *To be verified.*
- **LEDGE_HOP_RIGHT:** One-way jump from Left to Right. Blocks movement from Right to Left.
- **LEDGE_HOP_DOWN:** One-way jump from Up to Down. Blocks movement from Down to Up.
- **HEADBUTT_TREE/CUT_TREE:** Impassable (unless interacting with specific move).
- **TALL_GRASS:** High encounter rate.
- **WARP_CARPET:** Transports to new map.
- **COUNTER:** Acts as a wall. Interact across it to talk to NPCs behind it.

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
- **Officer (Route 31 Gatehouse):** Asked if I visited **Sprout Tower**. Implies it's a key location.
- **Wade (Phone):** Found Berries. Waiting on Route 31.
- **Gentleman (Violet Center):** Team Rocket broken up 3 years ago by a kid.
- **Gameboy Kid (Violet Center):** Bill made the Pokemon PC storage system.
- **Youngster (Violet Center):** Traded Pokemon need badges to obey.

## Immediate Plan
- **Ruins of Alph:** Explore the East Entrance area.
- **Route 32 Main Path:** Resume heading south.
- **Fisher:** Talk to Fisher at (15, 13).
- **Hatch Egg:** Walk.

## Route 32 Notes
- **Layout:** Divided into West (Main) and East (Side Path) by a wall/ledge barrier (x=17).
- **Ledges:** Tiles at x=17 appear to be `LEDGE_HOP_RIGHT` (West -> East).
- **Side Path:** Accessed via top gap. Contains Cooltrainer M. Likely a dead end.

## Recent Events
- **Violet Pokemon Center:** Healed party. Received **Mystery Egg** from Elm's Aide.
- **Violet Gym:** Defeated Falkner. Obtained **Zephyr Badge** and **TM31** (Mud-Slap).
- **Sprout Tower:** Cleared.
- **Elder Li:** Defeated. Awarded HM05 (Flash).
- **HM05 (Flash):** Needs Zephyr Badge.
- **Rival Silver:** Used Escape Rope to leave.
- **Wade:** Called about bug catching.
- **Battle Mechanic:** Cursor memory persists in Fight menu.
## Bag Order (Items Pocket)
1. Berry
2. Antidote
3. Potion
4. Parlyz Heal
5. X Accuracy
(Escape Rope likely at end)
6. Escape Rope
## Tool Reminders
- Use `use_item_sequence` for items. Bag order is recorded.
- **Interaction Tip:** Always use `stun_npc` before interacting with moving NPCs to ensure they don't walk away or turn while you try to talk to them.
- **Lass (Violet City):** Normal moves don't hit Ghosts (Sprout Tower tip).
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
- **Ruins of Alph:** Sign says "Visitors Welcome". Entering main cave.