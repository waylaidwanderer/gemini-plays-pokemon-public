# Suicune Quest (Crystal) - FIXED SIGHTINGS
- Milestone 1: Burned Tower (Seen).
- Milestone 2: Cianwood City (Seen). Defeated Eusine.
- Milestone 3: Route 42 (In Progress). Pokedex confirms location.
- Milestone 4: Route 36 (Next). Requirement: Complete Route 42 sighting.
- Milestone 5: Tin Tower (Final). Requirement: Clear Bell (OBTAINED) + all overworld sightings.

## Suicune Hunt Strategy
- Suicune is NOT a roamer in grass until after the Tin Tower event.
- Route 42 Trigger: Approach the island center. Current Hypothesis: Approach from the WEST via Surf (Started Turn 17681).
- Route 36: Enter from the Violet City side (East) after Route 42 is completed.

## Suicune Trigger Hypothesis Testing (Route 42)
- Hypothesis 21: Systematic floor sweep (Y=10-17) failed. No trigger on any FLOOR tile. [Turns 17654-17664]
- Hypothesis 22: Trigger requires entering Route 42 from the WEST (Ecruteak side) and approaching the island center. [Started Turn 17681]
- Attempt 1: Paced island center and fruit trees thoroughly (Turn 17710-17730). Result: FAILED. No sighting triggered.
- Hypothesis 23: Sighting is triggered on the mainland path or water, not the island itself.
- Hypothesis 24: Sighting requires approaching from the EAST (Mahogany side).
- Step 1: Fly to Mahogany Town. [DONE]
- Step 2: Enter Route 42 from the East. [DONE]
- Step 3: Surf west through the northern water channel (Row 9) to bypass the mountain and reach the island. [DONE]
- Step 4: Approach island center (24, 14) from the north/east side. [DONE]
- Result: FAILED. No sighting triggered at (24, 14).
- Hypothesis 25: Suicune is standing in front of the middle Mt. Mortar entrance (28, 9).
- Step 1: Travel to (28, 10) and check for Suicune. [DONE]
- Result: Warped into Mt. Mortar (3_57) at (17, 33). Suicune not seen.
- Hypothesis 26: Suicune moved because of the map change (warping into Mt. Mortar). [DONE]
- Result: Pokedex confirms Suicune is still on Route 42. Trigger hasn't been hit.
- Hypothesis 27: Suicune is on a high ledge accessible only through Mt. Mortar.
- Step 1: Navigate to (28, 17) and face UP toward the Green Apricorn tree. [In Progress]
- Hypothesis 28: Trigger is proximity to the three Apricorn trees (Pink, Green, Yellow) on the island, specifically approaching from the south (Row 17).
- Attempt 1: Faced Green tree from (28, 17). Result: FAILED.
- Step 2: Interact with all three Apricorn trees (X=27, 28, 29). [In Progress]
- Pink Apricorn Tree (27, 16): Checked. Result: No Suicune sighting.
- Green Apricorn Tree (28, 16): Next.
- Yellow Apricorn Tree (29, 16): Pending.
- Step 3: Sweep remaining island floor tiles and mainland unseen tiles at (4, 14)-(7, 14).
- Note: If this fails after a full sweep, I will move on to Route 44/Ice Path/Blackthorn City.

# Verified Sprite Observations (Route 42)
- Turn 17786: `run_code` confirmed no Suicune sprite is present on screen. Sighting is likely coordinate-triggered.
- Reachable Unseen Tiles (via Mt. Mortar): (21, 4), (25, 5), (26, 5), (27, 5), (30, 4).
- Reachable Unseen Tiles (Mainland West): (4, 14), (5, 14), (6, 14), (7, 14).

# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL / HEADBUTT_TREE / ROCK / VOID / FLOOR_UP_WALL / WATER_ROCKS: Impassable.
- CUT_TREE: Impassable until CUT.
- WATER: Traversable with HM03 SURF.
- TALL_GRASS / LONG_GRASS: Traversable; triggers wild encounters.
- LEDGE: One-way traversable (usually South).
- WARP / DOOR / WARP_CARPET / CAVE: Map transition.
- FRUIT_TREE: Impassable; interact to get fruit/apricorn.

# PC Storage (Box 1)
- VORTEX (Poliwag 22), INTERCEPT (Yanma 12), ROCKY (Onix 6), EGG (CleFFA 5), XFDW (Meowth 16), FRITTATA (Togepi 5), SHUCKIE (Shuckle 15), Blarney (Sudowoodo 20).

# Items & Contacts
- Fire Stone: Route 36 (Alan).
- Rock Smash (Info): Route 36 (Fisher at 44, 9).
- Fisher Tully: Route 42. Gives items.
- Bug Catcher Arnie: Route 35. Reports Yanma swarms.

# General Lessons & Observations
- Scripted overworld events (like Suicune sightings) often depend on the direction of approach or entering a specific coordinate trigger zone. Systematic testing of approach angles is necessary.
- When the Pokedex confirms a legendary's location but it isn't visible, it's likely a scripted event trigger rather than a random encounter in grass (at this stage of the game).

# Task Timestamps
- Suicune Hunt (Route 42): Started Turn 17642.
- Current Hypothesis (East Approach): Started Turn 17754.