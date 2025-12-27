# Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained), All overworld sightings must be triggered in order.
- Quest Start: Turn 24182.

## Sighting Progress
1. Burned Tower: Verified.
2. Cianwood City (North): Verified.
3. Route 42 (Central Island): [MISSING] Mandatory before Route 36. Checked clearing at Turn 26164 (Empty).
4. Route 36 (Sudowoodo Junction): [MISSING] Mandatory after Route 42. Checked spot at Turn 26177 (Empty).
5. Tin Tower 1F: Static encounter (Enabled after sighting #4).

## Suicune Quest Hypotheses & Tests
- Hypothesis 1: Eusine dialogue in Ecruteak PC is required.
  - Test: Check Ecruteak PC.
- Hypothesis 2: Wise Trio dialogue in Tin Tower Gatehouse is required.
  - Test: Talk to all Sages again.
- Hypothesis 3: Sighting #3 trigger is a specific tile on Route 42 island.
  - Test: Tile-by-tile sweep of (21,10) to (31,17).

## Time Tracking
- Current Attempt Start: Turn 26101.

## Lessons Learned
- Suicune overworld events are strictly linear.
- NPC dialogue hints (e.g., "tower shook") indicate quest progression but do not always skip steps.
- Check all adjacent tiles when blocked by an NPC.
- Do not mix directional and action buttons in a single press_buttons call.
## Milestones
- Turn 26110: Triggered "Tin Tower Shake" event by entering the gatehouse with the Clear Bell.
- Route 36 Sudowoodo Spot (Turn 26177): Suicune NOT found.