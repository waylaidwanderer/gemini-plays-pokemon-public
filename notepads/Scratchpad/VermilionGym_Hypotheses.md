# Vermilion Gym - Trash Can Puzzle Mechanics & Empirical Log

## Puzzle Mechanics (Verified Retail Pokémon Blue)
- Grid layout: 15 cans arranged in 3 rows (y=7, 9, 11) and 5 columns (x=1, 3, 5, 7, 9).
- Switch 1: Hidden under one of the 15 trash cans. Interacting displays: "Hey! There's a switch under the trash! Turn it on! The 1st electric lock opened!".
- Switch 2: Placed in a can adjacent to Switch 1 (Up, Down, Left, Right), or defaults to index 0 `(1, 7)` if selected direction is out of bounds.
- Reset: Checking any non-Switch 2 can after Switch 1 resets the electric locks ("Hey! The electric locks were reset!").
- Empty can dialogue: "Nope, there's only trash here.".

## Turn-by-Turn Verification Status (Session at Turn 2764)
- Can (1, 7): NOPE [Verified Turn 2764]
- Can (3, 7): Currently inspecting from (2, 7)
- Can (5, 7): Pending check
- Can (7, 7): NOPE [Verified Turn 2760]
- Can (9, 7): NOPE [Verified Turn 2760]
- Row 9 cans (1,9; 3,9; 5,9; 7,9; 9,9): All verified NOPE [Turn 2758]
- Row 11 cans (1,11; 3,11; 5,11; 7,11; 9,11): All verified NOPE [Turn 2747-2753]

## Battle Plan vs Lt. Surge (Post-Door Opening)
1. Walk past opened laser gates at (4, 4) / (5, 4) to (5, 2).
2. Lead with TERRA (Geodude Lv 15, HP 41/41).
3. Use Dig (Ground STAB, 100 base power, Electric immunity) to defeat Voltorb Lv 21, Pikachu Lv 18, and Raichu Lv 24.
4. Backup: HYDROS Lv 33 (HP 94/94) for non-electric physical coverage if needed.