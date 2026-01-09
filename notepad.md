# Long Term Notes
## Lessons Learned
- **Tool Insight:** `navigate_menu` requires `hold_ms` >= 300 for Fly Map.
- **Efficiency:** Super Repels (2.5 ¥/step) are cheaper than Max Repels (2.8 ¥/step).
- **Mechanics:** Phone calls can occur on map transitions.

## Legendary Beast Hunt Strategy
- **Target:** Raikou (#238) & Entei (#239).
- **Method:** Blind Hunt Loop (Route 37 <-> Ecruteak).
- **Tactics:** Enter Rt 37 -> Grass (Down x2, Wiggle) -> If none, Return to Ecruteak -> Repeat.

## Tile Mechanics
- GRASS: Traversable, encounters.
- FLOOR/DOOR/STAIRS: Traversable.
- WALL/OBSTACLES: Impassable.
- WARP_CARPET: Transition.
- WATER: Surfable.

# Current Strategy
## Objectives
- **Primary:** Complete Pokedex.
- **Secondary:** Check PC for TM08 (Rock Smash). Not in bag/party.
- **Tertiary:** Resume Roaming Beast Hunt.

## Exploration Queue
- **Mahogany Town:** West edge (x=0-2) and East edge (x=15, y=3) unseen tiles.
- **Ecruteak City:** Northern edges and Barrier Station area (27, 11).
- **Route 37:** Eastern edge (x>13) unseen tiles.

## Missing Items
- **TM08 Rock Smash:** Critical for map access (e.g. Ruins of Alph, Dark Cave).
- **Observation:** Route 36 NPC dialogue implied giving TM08 ("That happens to be ROCK SMASH"), but no "Obtained TM08" text was seen in history.
- **Hypothesis:** TM08 was obtained previously and stored in PC, or used and lost. Checking PC now.
- **Verification:** Verified TM08 is NOT in Bag, Party, or PC Boxes 1-3. Currently checking PC Item Storage.
- **Critical Update:** TM08 Rock Smash is NOT in PC, Bag, or Party.
- **Analysis:** NPC dialogue on Route 36 implies he already gave it. Verified not in storage. Likely used or tossed.
- **Solution:** In Pokemon Crystal, TM08 is purchasable at Goldenrod Dept Store 5F.
- **Plan:** Fly to Goldenrod -> Buy TM08 -> Return to Ecruteak for Hunt.
- **Fly Map Behavior:** Cursor observed starting at New Bark Town when opened from Olivine City (instead of current location). Always verify start point before navigating.
- **Fly Map Logic:** 'Down' from New Bark Town leads to Silver Cave (verified). Silver Cave is visually Top-Right. To reach Goldenrod (Central), need to traverse West.
- **Correction:** Accidental flight to New Bark Town occurred due to pressing 'A' when map was already open.
- **Current Status:** In New Bark Town. Goal: Fly to Goldenrod.
- **Menu Navigation:** Start -> Pokemon -> Mistral (Slot 4) -> Fly.

# Session Timestamp: Turn 29960
- **Reflection:** Reviewing navigation failures. Focusing on strict verification of cursor positions before confirming actions.
- **Cursor Memory:** Confirmed: Party Menu cursor remembers last position (Mistral). Sub-menu cursor likely also remembers. Verify before acting.
- **Immediate Task:** Enter Party Menu and identify cursor location.
- **Fly Map Logic:** 'Left' x3 from Silver Cave leads to Ecruteak City (Verified visually). Next: 'Down' to Goldenrod.
- **Fly Map Correction:** 'Down' from Silver Cave (or failed previous move) led to Blackthorn City.
- **Current Location:** Blackthorn City.
- **Path to Goldenrod:** Blackthorn -> Left -> Mahogany -> Left -> Ecruteak -> Down -> Goldenrod.
- **Fly Map Movement:** 3x Left from Silver Cave only reached Blackthorn. Cursor movement appears granular or sticky, not 1-click-per-city.
- **Hypothesis:** Reaching Ecruteak from Blackthorn requires multiple Left inputs (approx 3-6).
- **Plan:** Execute Left x3 to reach Mahogany/Ecruteak area. Verify location before heading South to Goldenrod.