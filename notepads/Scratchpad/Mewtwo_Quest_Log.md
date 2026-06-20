# Mewtwo Quest Log (Post-Game)
- Started: Turn 111394
- Goal: Enter Cerulean Cave and catch Mewtwo.

## Step 1: Fly to Cerulean City and Heal
- Party Status: Blastoise (GEMMY) is out of PP and low on HP. Must heal at Cerulean Pokémon Center.
- Turn 111421: Arrived in Cerulean City via FLY, standing right outside the Pokémon Center.

## Step 2: Test press_buttons_no_advance for Healing
- Turn 111434: Verified that standard press_buttons triggers the auto-advance which presses 'B' and cancels Nurse Joy's healing menu.
- Plan: Stand at (3, 3) facing North. Use press_buttons_no_advance to press 'A' once to talk to Nurse Joy. We will then manually progress through the dialogue using press_buttons_no_advance to avoid B-button cancellation.
- Methodology:
  1. Press A via press_buttons_no_advance.
  2. Observe the screen text in the next turn.
  3. Manually press A to advance until the HEAL/CANCEL menu is displayed, then select HEAL (default) by pressing A.