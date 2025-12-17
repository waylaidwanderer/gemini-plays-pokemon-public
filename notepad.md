# Gem's Journey in Pokémon Crystal

## Current Objectives
- **Primary:** Earn Hive Badge (Azalea Gym).
- **Secondary:** Collect Apricorns & Prepare for Gym.
- **Tertiary:** Explore Azalea Town.

## Strategy
1.  **Heal:** Restore party health and PP at the Pokemon Center.
2.  **Acquire HM01 (Cut):** Enter Ilex Forest and locate the charcoal maker's Farfetch'd to earn the HM.
3.  **Teach Cut:** Teach HM01 to a party member (likely a slave or Oddish/Paras if found) to progress.

## Quest Log
- **Badges:** Zephyr, Hive (2/8)
- **Key Items:** HM05 (Flash), TM31 (Mud-Slap), TM39 (Swift), TM49 (Fury Cutter), Lure Ball.
- **Pending:** Deliver Mystery Egg to Elm, Get HM01 Cut.

## Party
- **GARNET (Quilava)** Lv22 (Fully Healed) | Quick Attack, Leer, Smokescreen, Ember
- **ROCKY (Onix)** Lv11 (Fully Healed)
- **UNAKITE (Unown)** Lv5 (Fully Healed)
- **EGG**
- **TOPAZ (Sentret)** Lv4 (Fully Healed)
- **AMETHYST (Zubat)** Lv5 (Fully Healed)
- **PC:** JASPER (Geodude)

## Location Notes: Azalea Gym
- **Status:** Cleared. Badge Obtained.
- **Leader:** Bugsy (Defeated).

## Cleared Areas
- **Slowpoke Well:** Cleared. Kurt rescued.
- **Azalea Gym:** Cleared. Hive Badge earned.

## Tile Mechanics
- **FLOOR_UP_WALL:** Acts as wall from North.
- **LEDGE_HOP_LEFT:** One-way Left.
- **LEDGE_HOP_DOWN:** One-way Down.
- **Rocket Grunt:** Defeated at (5, 2).
- **Kurt:** Moved to (7, 5).
- **Battle:** Rival Silver (Gastly, Croconaw, Zubat) - Defeated.
- **Info:** Youngster at (7, 28) lost his boss's Farfetch'd (which knows Cut) in the forest.
- **Task:** Herd Farfetch'd East from (15, 28) to navigate around the central wall.
## Puzzle Status: Farfetch'd Herding
- **Current Status:** Bird at (15, 25). Player at (16, 29).
- **Insight:** Pushing West at Row 29 caused a reset. Row 29 flank is likely invalid.
- **New Strategy (The Loop & Swap):**
  1. Push Bird North into the loop (Row 23).
  2. Chase/Herd it back West to (15, 23).
  3. At (15, 23), interact from (16, 23) to force it South to (15, 24).
  4. Move to (15, 23) to get North of the bird.
  5. Push South to (15, 28), then try Flanking at Row 28 (Col 14 Shift).
- **Immediate Action:** Navigate to (15, 26) to push Bird North.

## Reflection Log (Turn 2445)
- **Execution:** No major deferrals. Sticking to "Col 14 Shift" plan.
- **Hygiene:** Consolidated puzzle plans. Removed obsolete "Loop" and "Reverse Loop" strategies.
- **Map:** Markers are accurate.
- **Goals:** Clear and focused on immediate puzzle steps.
- **Strategy:** Position North at (15, 24) to push Farfetch'd South to Row 28. Then flank East to push it West towards the Apprentice.
- **Goal:** Herd to Apprentice at (7, 28).

## Farfetch'd Behavior Notes
- Moves opposite to interaction.
- Can "fly" over obstacles if cornered (e.g. corner loop).
- Resets on map exit (and possibly battles).