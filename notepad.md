# Strategy: Suicune Hunt (Crystal)
- Sequence: 
  1. Burned Tower (Released) 
  2. Cianwood (Fled) 
  3. Route 42 (Fled) 
  4. Route 38 Western Ledge (Target)
  5. Route 14 (Next)
  6. Tin Tower 1F (Stationary Battle)
- Route 38 Ledge: Reachable via Olivine -> Route 39 -> Route 38 West. (Cannot reach from Ecruteak due to one-way ledges).
- Battle Strategy (Tin Tower):
  - Lead: XENON (GASTLY).
  - Use MEAN LOOK to prevent fleeing.
  - Use HYPNOSIS to induce sleep.
  - Use NIGHT SHADE for fixed 21 HP damage.
  - Catch with GREAT/ULTRA BALLs.

# Tile Mechanics (Global)
- FLOOR: Traversable.
- DOOR/WARP: Trigger map transition.
- WALL/HEADBUTT_TREE/BERRY_TREE/BUOY: Impassable.
- TALL_GRASS: Traversable; triggers wild encounters.
- LEDGE_HOP (DOWN/LEFT/RIGHT): One-way traversal.
- WATER: Traversable with Surf.

# Route 38 Ledge Mechanics
- Isolated western ledge (X=0-7) reachable only from Route 39 (South).
- Central trough (X=8-10) exits South at (9, 13).

# Side Quests
- Clear Bell: In Key Items (Verified).
- Arthur (Hard Stone): Route 36. Thursday only. (Targeting now).

# Task: Reach Route 38 Western Ledge
- Objective Start: Turn 20922
- Current Status: On Fly map. Cursor at Violet City (per prompt text).
- Plan:
  1. Fly to Olivine City.
  2. Walk North to Route 39, then Route 38 West.
  3. Trigger Suicune flee at (3, 10) on Route 38.

# Navigation: Fly Map (Johto)
- Grid: Cianwood(0,0), Olivine(1,0), Ecruteak(2,0), Mahogany(3,0), Blackthorn(4,0); Goldenrod(1,1), Violet(3,1); Azalea(1,2), Cherrygrove(3,2), New Bark(4,2).

# Lessons Learned
- Fly Map Vertical Snapping: Vertical movement snaps to the closest city in the new row.
- Arthur Loop: If he repeats dialogue without giving the item, pivot after 3 turns.
- Location Verification: Always check Game State Information for map/coords before acting. Hallucinating location leads to tool failure.