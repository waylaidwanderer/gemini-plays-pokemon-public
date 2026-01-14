# Tile Mechanics
- **TALL_GRASS:** traversable, chance of wild encounter.
- **HEADBUTT_TREE:** solid (collision), chance of encounter if Headbutt is used.
- **LEDGE_HOP_DOWN:** one-way traversable (down only).
- **WALL:** impassable.
- **FLOOR:** traversable.

# Lessons Learned
- **Automation Limits:** Long macro tools crossing map boundaries are unreliable due to variable load times and interruptions (phone calls, repels). Use short, verifiable sequences instead.

# Strategic Status
- **Money:** ¥2294 (Enough for ~4 Super Repels).
- **Shopping List:** Super Repel x4.
- **Inventory Check:** No high-value items to sell in bag.
- **Goal:** Register Raikou & Entei.
- **Strategy:** Blind Hunt (Optimized). 
    - **Logic:** Tracking roamers from adjacent maps is futile because entering their map causes them to move. Thus, a blind encounter on entry is the only valid method.
    - Use Super Repel with Lead Pokemon (Lv 36) < Roamer (Lv 40) but > Wild (Lv 17).
    - Enter Route 37.
    - Move to grass and Scan ONCE (20 steps).
    - If no encounter, IMMEDIATELY transition to Ecruteak and back to reset.
    - Do NOT check Pokegear map.
- **Repel Status:** Wore off (Turn 39058). Out of stock. Ecruteak Mart had none. Heading to Goldenrod.
- **Session Start:** Turn 38471.
- **Active Events:** Bug-Catching Contest (Tuesday).
- **Interruption Handling:** Phone calls or other events can pause automation; handle immediately to resume loops.
- **Roamer Logic:** Roamers move to an adjacent map when the player transitions maps. 'Chasing' a roamer seen on the map is ineffective as they move away upon entry. 'Blind Interception' relies on them moving *into* your map as you enter, which is best achieved by maximizing map transitions per hour.
- **Detour to Goldenrod:** Started Turn 39093. Fly failed, walking via Route 36 -> 35.
- **Reflection (Turn 39093):**
    - Execution: Good. No deferred tasks.
    - Hygiene: Updated Repel status.
    - Map: Markers accurate. Route 36 entered.
    - Automation: Fly tool failed (menu loop), switched to manual pathing.
    - Goals: Clear. Detour necessary for supplies.
    - Errors: Visual feedback needed for menu tools. Relying on walking for reliability.
## Goldenrod Dept Store
- 2F: Trainer's Market (Standard items like Balls, Potions, Repels).