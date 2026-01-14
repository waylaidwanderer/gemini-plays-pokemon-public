# Tile Mechanics
- **TALL_GRASS:** traversable, chance of wild encounter.
- **HEADBUTT_TREE:** solid (collision), chance of encounter if Headbutt is used.
- **LEDGE_HOP_DOWN:** one-way traversable (down only).
- **WALL:** impassable.
- **FLOOR:** traversable.

# Lessons Learned
- **Automation Limits:** Long macro tools crossing map boundaries are unreliable due to variable load times and interruptions (phone calls, repels). Use short, verifiable sequences instead.

# Strategic Status
- **Goal:** Register Raikou & Entei.
- **Strategy:** Blind Hunt (Optimized). 
    - **Logic:** Tracking roamers from adjacent maps is futile because entering their map causes them to move. Thus, a blind encounter on entry is the only valid method.
    - Use Super Repel with Lead Pokemon (Lv 36) < Roamer (Lv 40) but > Wild (Lv 17).
    - Enter Route 37.
    - Move to grass and Scan ONCE (20 steps).
    - If no encounter, IMMEDIATELY transition to Ecruteak and back to reset.
    - Do NOT check Pokegear map.
- **Repel Status:** Active (Applied Turn 39019).
- **Session Start:** Turn 38471.
- **Active Events:** Bug-Catching Contest (Tuesday).
- **Interruption Handling:** Phone calls or other events can pause automation; handle immediately to resume loops.
- **Roamer Logic:** Roamers move to an adjacent map when the player transitions maps. 'Chasing' a roamer seen on the map is ineffective as they move away upon entry. 'Blind Interception' relies on them moving *into* your map as you enter, which is best achieved by maximizing map transitions per hour.