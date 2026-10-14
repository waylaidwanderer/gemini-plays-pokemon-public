# Main Notepad — Pokémon Emerald Version

## Trainer Info
- **Name:** ORION (Boy / Brendan sprite)
- **Text Speed:** FAST
- **Inventory:** Potion x1 (withdrawn from bedroom PC)

## Active Goals & Milestones
1. [DONE] Configure Options (Text Speed: Fast) & complete Birch's intro.
2. [DONE] Exit moving truck, set bedroom clock, withdraw PC Potion, watch Petalburg Gym TV broadcast.
3. [DONE] Visit rival May's house (14, 8) in Littleroot Town and meet May upstairs.
4. [IN PROGRESS] Head north to Route 101, rescue Professor Birch, and choose + nickname our starter Pokémon.

## Mechanics & Harness Notes
- **Naming Screen Grid (7 cols x 4 rows, Select = toggle case, Start = jump to OK):**
  - Row 0: `A B C D E F .` (cols 0..6)
  - Row 1: `G H I J K L ,` (cols 0..6)
  - Row 2: `M N O P Q R S` (cols 0..6)
  - Row 3: `T U V W X Y Z` (cols 0..6)
- **Overworld Warp Transitions:** Stepping onto a warp/door aborts remaining `press_buttons` inputs and leaves the next turn at the start of the fade-in; prepend `sleep 1000` when chaining actions immediately after a warp.