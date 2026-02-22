### Current Quest: Investigate Tin Tower
- **Started:** Turn 52441
- **Location:** Cherrygrove City
- **Goal:** Buy Ultra Balls (Ecruteak Mart), Return to Tin Tower.
- **Status:** Party healed. Flying to Ecruteak.

### Future Goals
- **Tin Tower:** Investigate with Clear Bell.
- **Radio Tower:** Return later to scan for items.
- Route 37 Nav: Apricorn grove is a dead-end. Backtrack South to Row 16 to cross to the West side for the path to Ecruteak.

### Reflection (Turn 52922)
- **Stuck:** The door at (20,2) is refusing to warp me.
- **Action:** Using Fly to bypass the door and heal.
- **Lesson:** Verify walkable tile types on screen before using BFS. Map 4_9 trees are TYPE_2889/TYPE_3fe2, path is TYPE_ffbe.
- Turn 52928: Accidentally flew to Violet City instead of Ecruteak. Healing here instead.
- **Mechanic:** `bfs_navigate` does not guarantee facing direction. Always explicitly face the target before interacting.
- Turn 52994: Healed Party at Cherrygrove Center.
- **Goal:** Fly to Ecruteak to buy Ultra Balls and continue quest.
- **Mechanic:** `bfs_navigate` does not guarantee facing direction. Always explicitly face the target before interacting.
- Turn 53011: Successfully accessed Fly menu. Selecting Ecruteak City next.
- **Goal:** Fly to Ecruteak to buy Ultra Balls and continue quest.
- **Mechanic:** `bfs_navigate` does not guarantee facing direction. Always explicitly face the target before interacting.
- Turn 53022: Stuck in Pokedex. Pressing B to exit to Overworld.
- **Step 1:** Exit all menus (B, B, B).
- **Step 2:** Open Start Menu -> Pokemon -> Topaz -> Fly.
- **Mechanic:** Inputs during transitions are often eaten. Splitting complex menu sequences prevents this.