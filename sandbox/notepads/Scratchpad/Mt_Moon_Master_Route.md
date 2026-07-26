# Mt. Moon Navigation & Verification Scratchpad

## Current Operational Protocol
- **Strict Single-Step Verification:** Every movement step must be empirically verified via single-step input before queueing movement across adjacent tiles.
- **Immediate Target:** Test stepping Left from (20,28) to (19,28) in South Trench on Mt. Moon B1F.

## Confirmed Boundaries at South Trench (B1F)
- (20,27): Impassable rock wall face (Verified Turn 8872).
- (20,28): Open floor position (Current Player Location).
- (24,31): Decorative/non-functional ladder sprite (Verified Turn 4695).

## Next Verified Leg Goal
- Verify accessibility of (19,28) by pressing `Left` 1 step and observing position change in GameState.