# Mt. Moon Navigation & Verification Scratchpad

## Current Operational Protocol
- **Strict Single-Step Verification:** Every movement step must be empirically verified via single-step input before queueing movement across adjacent tiles.
- **Burden of Proof for Warps:** No tile may be documented or treated as a functional warp destination until physically stepped on and confirmed via a `SYSTEM NOTE: Map Transition Detected` message.

## Confirmed Boundaries at Central/North B1F
- (20,27): Impassable rock wall face (Verified Turn 8872).
- (19,28): Impassable rock wall face (Verified Turn 8886).
- (25,15): Open floor tile (Current Player Location).
- (25,11): Target corridor tile to reach (17,11) ladder candidate.

## Next Verified Leg Goal
- Step Up 1 step from (25,15) to (25,14) and verify player position in GameState.