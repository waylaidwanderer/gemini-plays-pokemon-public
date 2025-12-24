# Ice Path Strategy
- **Current State:** At (18, 23).
- **Goal:** Reach the North-East area via the hidden corridor at x=25.
- **Correction:** The "Shortcut" path logic was flawed, but the Reachability Tool confirmed a path to x=25.
- **Visual Check:** XML shows (25, 21) and (25, 22) are FLOOR tiles. There is a corridor going North at x=25.
- **Plan:**
  1. Slide **Right** to (20, 23) (Floor).
  2. Walk East to (24, 23).
  3. Walk Up to (24, 22), then Right to (25, 22).
  4. Walk North along x=25 to reach the NE area.

# Map Structure
- **West Corridor (x=0):** Isolated/Unreachable from here.
- **Hub (14, 16):** Connected to SE Floor.
- **SE Floor:** Contains entrance to East Corridor (x=25).
- **East Corridor (x=25):** The key to progressing North.