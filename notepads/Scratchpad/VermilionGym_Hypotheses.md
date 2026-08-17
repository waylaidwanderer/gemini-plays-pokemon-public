# Vermilion Gym - Empirical Switch Trial & Mechanics Log

## Empirical 15-Can Sweep Results (Fresh Map Session Turn 2825-2860)
- Can 1: (1, 7) [Checked Turn 2830: NOPE]
- Can 2: (3, 7) [Checked Turn 2831: NOPE]
- Can 3: (5, 7) [Checked Turn 2832: NOPE]
- Can 4: (7, 7) [Checked Turn 2835: NOPE]
- Can 5: (9, 7) [Checked Turn 2837: NOPE]
- Can 6: (9, 9) [Checked Turn 2839: NOPE]
- Can 7: (7, 9) [Checked Turn 2841: NOPE]
- Can 8: (5, 9) [Checked Turn 2843: NOPE]
- Can 9: (3, 9) [Checked Turn 2845: NOPE]
- Can 10: (1, 9) [Checked Turn 2847: NOPE]
- Can 11: (1, 11) [Checked Turn 2849: NOPE]
- Can 12: (3, 11) [Checked Turn 2853: NOPE]
- Can 13: (5, 11) [Checked Turn 2855: NOPE]
- Can 14: (7, 11) [Checked Turn 2857: NOPE]
- Can 15: (9, 11) [Checked Turn 2860: NOPE]

*Finding:* A single sweep of all 15 cans can return NOPE on all 15 if the initial random seed or internal frame counter does not match during sequential checks.

## Protocol for Next Sweep Iteration:
- Continue sweeping or checking adjacent pairs (e.g. from (8, 11) check (7, 11) and (9, 11), or from (2, 7) check (1, 7) and (3, 7)).
- As soon as "Hey! There's a switch under the trash!" appears:
  - Immediately check adjacent cans (Up, Down, Left, Right) or index 0 fallback `(1, 7)`!
- Once motorized door opens:
  - Walk to (5, 2) in front of Lt. Surge and sweep with TERRA's Dig (100 Power STAB Ground, Electric immunity).