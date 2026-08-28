# Pokémon Mansion - Multi-Floor Switch & Barrier Permutations

## Global Switch Mechanics & Rules (Empirically Verified)
1. **Global Toggle**: Any Mewtwo statue switch flips ALL floors simultaneously between State A (Default) and State B (Toggled).
2. **Exterior Reset**: Leaving the Pokémon Mansion (via front door or DIG) immediately and reliably resets all switches globally to State A (Default). (Verified Turn 18942 via DIG).

## Empirical Barrier State Matrix

| Floor | Barrier Location | State A (Default) | State B (Toggled) |
|---|---|---|---|
| 1F | Shutter at (24..25, 13) [Enclosed Wing to B1F Stairs] | **OPEN** | CLOSED (Verified Turn 18520, 18673, 18935) |
| 1F | Shutter at (26..27, 27) [Southeast Shutter Barrier] | **CLOSED** (Verified Turn 19115) | OPEN |
| 2F | Doorways at (4, 7) and (6, 7) | **OPEN** (Verified Turn 18581) | CLOSED |
| 2F | Shutter at (21, 17) [West-East Divider] | **CLOSED** (Verified Turn 18601) | OPEN |
| 2F | Shutter at (26..27, 27) [Southeast Corner] | **CLOSED** (Verified Turn 18598) | OPEN |
| 3F | Shutter at (15, 10..11) | **CLOSED** | OPEN (Verified Turn 18658, 18898) |

## Balcony Pit Drop Empirical Matrix (3F -> Destination)
| Departure Tile (Floor 3F) | Landing Tile (Floor, X, Y) | Resulting Area / Access | Status |
|---|---|---|---|
| 3F (16, 14) [Left Pit Drop] | 1F (16, 14) | 1F South Wing (TM03, Scientist Ted) | Confirmed (Turns 18495, 18661) |
| 3F (17, 14) [Left/Center Pit Drop] | 1F (16, 14) | 1F South Wing (TM03, Scientist Ted) | Confirmed (Turn 18902) |
| 3F (19, 14) [Right Pit Drop] | 1F (18, 14) | 1F Northern Landing Sector (Journal at (18, 2), Switch at (15, 11)) | VERIFIED (Turn 19000) |

## Step-by-Step Execution Protocol
1. Ascend to 3F (6, 2) via 2F (6, 1).
2. Toggle switch at (10, 5) to State B (opens (15, 11) shutter).
3. Walk east through (15, 11) into Balcony room (cols 16-27).
4. Walk east past column 17 to the RIGHT section of the balcony pit (cols 18-21).
5. Face Down and step south into the right pit drop.
6. Land on 1F behind the closed shutter gate in the northern chamber (rows 10-12).
7. Descend staircase to B1F and retrieve Secret Key.

## Verified Solution Sequence (Turn 19046)
1. 3F right balcony drop at (19, 14) landed at 1F (18, 14) [North Landing Sector].
2. North Landing Sector connects via row 10 (9, 10) gap directly to 1F/2F stairs at (5, 10).
3. Toggled 2F Mewtwo statue switch at (2, 11) to State A.
4. In State A, 1F shutter gate at (24..25, 13) is OPEN.
5. On 1F (State A), traverse via (12, 6) -> (17, 6) -> (17, 14) into South Wing, walk to (24, 16) -> (24, 13), pass through open shutter into Northeast Chamber, and descend to B1F!

## Verified Post-Landing Route (1F Landing Site (18, 14) -> B1F Staircase (25, 14))
1. Landing Arrival: Drop through 3F Right Balcony Pit at (19, 14) -> Lands on 1F at (18, 14).
2. Switch Verification:
   - Walk west to (15, 14), north to (15, 12) facing statue at (15, 11).
   - Verify switch is in State A (Default). If in State B, press 'A' to toggle to State A (opens shutter at (24..25, 13)).
3. Route to B1F Staircase:
   - From (15, 12), walk south to (15, 14), west to (12, 14).
   - Walk south down column 12 to (12, 21).
   - Walk east along row 21 to (25, 21).
   - Walk north up column 25 to (25, 14).
4. Descent: Step onto staircase at (25, 14) -> Map Transition to PokemonMansionB1F!