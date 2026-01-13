# Roamer Hunt Strategy
- **Goal:** Catch Raikou & Entei.
- **Current Plan:** Fly to Ecruteak City (Central Hub).
- **Status:** Flying to Ecruteak City.
- **Action:** Select FLY (A) -> Navigate Map (Left x3) -> Confirm (A x2).
- **Goal:** Relocate to Ecruteak Hub.
- **Next:** Check Roamers.
- **Resources:** 16 Repels.
- **Session Start:** Turn 36369. Current: 36756.

# Reflection (Turn 36756)
- **Error Analysis:** Route 35 Gatehouse Shuffle failed to move Roamers for 15+ cycles.
- **Lesson:** Gatehouse transitions likely do not count as map transitions for Roamers. Use Route boundaries or Fly.
- **Tooling:** "cycle_roamer_hunt" tool failed due to positioning drift and warp mechanics. Manual 2-turn shuffle was safer but tedious.
- **Correction:** Abandoned Route 35. Relocating to Ecruteak.

# Tile Mechanics
- **Warp Tiles:** Must step *off* and then *back on* to trigger. Standing on them does nothing.
- **Ledge Hop:** One-way jump.
- **Headbutt Tree:** Can be shaken for Pokemon.

# Hall of Fame
- **Champion:** Turn 33314. MVP: Muscle (Machoke) Lv88.

# Completed Objectives
- **Johto Gyms:** All 8 Badges.
- **Elite Four:** Defeated.
- **Kanto Gyms:** All 8 Badges.
- **Red:** Defeated.
- **Lugia:** Caught (Maelstrom).

# Fly Map Connections
- **New Bark Town** -> Left -> **Cherrygrove City**
- **Cherrygrove City** -> Up -> **Violet City**
- **Cherrygrove City** -> Left -> **Azalea Town**
- **Azalea Town** -> Up -> **Goldenrod City**
- **Goldenrod City** -> Up -> **Olivine City**
- **Olivine City** -> Right -> **Ecruteak City** [Hypothesis]
- **Violet City** -> Left -> [Invalid]

# Game Mechanics
- **Fly Map:** Cursor remembers last destination. Always verify starting position.