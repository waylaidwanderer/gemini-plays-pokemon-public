# Strategic Status
- **Goal:** Catch Raikou (#243) & Entei (#244).
- **Hunt Duration:** ~13,000 turns. Resumed: Turn 41847 (Current: 43097).
- **Status:** Roamer Hunt Loop (Route 37 <-> Ecruteak).
- **Plan:**
    1. **Execute Loop:**
       a. Start at Route 37 Gate (8,0).
       b. Use Super Repel (if expired).
       c. Call `check_route37_grass` (Enters grass, checks, returns to gate).
       d. Call `enter_ecruteak_from_route37` (Resets map).
       e. Call `exit_ecruteak_to_route37` (Returns to gate).
    2. **Goal:** Encounter Entei/Raikou to register in Pokedex.
- **Secondary Targets:** Catch Stantler (Route 37/36 Night) or Growlithe.

# PC Storage Check
- **Conclusion:** MASTER BALL NOT FOUND. Assumed used or unavailable.

# Locations & Logistics
- **Ecruteak Mart:** No Super Repels.
- **Goldenrod Dept Store:** Full inventory.
- **Celadon Dept Store:** Super/Max Repels on 2F.
- **Fly Map:** Sticky cursor; walking preferred.

# Mechanics
- **Roamers:** Move on map transition.
- **Repel Trick:** Lead Lv37 > Wilds (~20) < Roamers (40).
- **Gatehouses:** "Sticky" warps; move *into* direction.

# Tile Mechanics
- **FLOOR/TALL_GRASS:** Traversable.
- **WALL/HEADBUTT_TREE:** Impassable.
- **WARP_CARPET:** Walk *off* edge.
- **LEDGE_HOP:** One-way down.

# Rematches
- Cooltrainer Gaven (Route 26): Ready.
- Bug Catcher Wade (Route 31): Offering Berries.
- **Team Note:** Need Mean Look/Sleep for catching. Current goal: Registration only.