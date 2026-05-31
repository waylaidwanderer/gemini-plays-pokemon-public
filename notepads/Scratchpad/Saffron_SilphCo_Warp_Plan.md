# Saffron City & Silph Co. Systematic Warp-Logging Strategy

## Overview & Cognitive Safeguards
Saffron City and Silph Co. (11 floors) contain a massive, complex network of over 30 warp tiles. Navigating this blindly or relying purely on short-term memory will cause cognitive bloat, backtrack loops, and wasted turns. To prevent this, we will systematically log every warp transition using our specialized custom agent: `warp_network_tracker`.

## Logging Protocol
1. **Identify and Check**: Before stepping on any warp tile, verify our current map ID and coordinate.
2. **Execute and Record**: Step on the warp tile. Once we spawn at the destination, immediately:
   - Call the `warp_network_tracker` agent with `action_type="record_warp"`.
   - Provide `current_map_id`, `current_position` (the warp's origin), and `warp_destination_map_id`, `warp_destination_position` (the spawn location).
3. **Verify in Scratchpad**: Maintain a secondary high-level floor transition index in this scratchpad to maintain quick overworld context.
4. **Route Planning**: When seeking specific objectives (like finding the Card Key on B5F, or reaching Giovanni on 11F), call `warp_network_tracker` with `action_type="plan_warp_route"` to query the database and receive an automated sequence of coordinates to follow.

## High-Level Floor-by-Floor silph Co. Objectives
- **Target 1**: Obtain the Card Key (traditionally on B5F or adjacent floors).
- **Target 2**: Unlock doors using the Card Key to access locked rooms and valuable items.
- **Target 3**: Defeat Boss Giovanni on 11F to clear Silph Co. and obtain the Silph Scope (wait, we already have the Silph Scope!). Defeating Giovanni here will clear Team Rocket from Saffron City and unlock the Saffron Gym!
- **Target 4**: Defeat Sabrina at Saffron Gym.