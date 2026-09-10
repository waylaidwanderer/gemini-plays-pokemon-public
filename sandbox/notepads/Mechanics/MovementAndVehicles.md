# Movement & Vehicle Mechanics

## Step Resolution & Parity
- **On Foot**: Each single directional tap moves exactly 1 tile. Turning to face a direction happens automatically before the step. Compound inputs execute linearly step-by-step.
- **Bicycle**: High-speed traversal. In the emulator harness, compound directional macros while on the Bicycle can glide across 2 tiles per tap due to speed/momentum, causing coordinate parity overshoots when attempting to align with single-tile doors/entrances (e.g. oscillating between x=3 and x=5 across a target at x=4).
- **Navigation Protocol**: When precision alignment with single-tile cave entrances, ledges, or maze junctions is required, either:
  1. Dismount the Bicycle (Open Menu -> ITEM -> BICYCLE) to use 1-tile foot precision.
  2. Use single-button input testing without compound multi-step macros.