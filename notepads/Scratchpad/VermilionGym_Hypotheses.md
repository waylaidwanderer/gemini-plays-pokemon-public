# Vermilion Gym - Trash Can Mechanics & Rapid-Pair Strategy

## Empirical Proof & Mechanism Analysis
- In Run #4 (Turns 2527-2571), all 15 cans were sequentially checked with single-step verification. All 15 returned empty.
- Mathematical explanation: In Gen 1, each empty can check resets/re-rolls Switch 1 with probability p = 1/15. The probability of 15 consecutive empty cans in a single sweep is (14/15)^15 ~ 35.5%.
- Therefore, a sequential 15-can sweep is statistically identical to checking the same pair of cans repeatedly, but with much higher movement overhead.

## Optimal Rapid-Pair Execution Strategy (Current Position: (8, 7))
- Position: Stand at (8, 7) between can (7, 7) [Left] and can (9, 7) [Right].
- Loop: Alternate checking (7, 7) and (9, 7) until Switch 1 triggers ("The 1st electric lock opened!").
- On Switch 1 Trigger:
  - If Switch 1 is at (7, 7): Immediately check (9, 7) [East] with `Right`, `A`. If reset, re-start loop. If valid, doors open!
  - If Switch 1 is at (9, 7): Immediately check (7, 7) [West] with `Left`, `A`. If reset, re-start loop. If valid, doors open!

## Active Trial Tracking
- Trial counter starting at Turn 2571 at position (8, 7).
