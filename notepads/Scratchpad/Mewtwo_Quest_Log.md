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

## Step 3: PC Healing Protocol (Turn 111436)
- Hypothesis: Nurse Joy's heal menu is cancelled by the harness's automatic B-button text advance. Depositing GEMMY (Blastoise) into the PC and then withdrawing her will completely restore her HP and move PP, bypassing Nurse Joy entirely.
- Plan:
  1. Walk to the PC terminal at (8, 3) by moving Down, Right, Right, Right, Right, Right, Up.
  2. Access GEM's PC.
  3. Deposit GEMMY into Box 2.
  4. Withdraw GEMMY from Box 2.
  5. Verify that GEMMY's HP is 231/231 and move PP is fully restored.
- Turn 111454: Noticed that pressing Right while at (12, 3) facing Left did not turn us Right. This may be because the engine requires a clean, non-blocked step to reliably change facing direction under certain harness conditions.
- Methodology: We will walk Down to (12, 4) (which is open) to force a direction change to South. Then walk Up to (12, 3) (open) to force a direction change to North. From there, we will test turning Right.
- Turn 111479: Determined that due to the harness's automatic text advance repeatedly pressing B and cancelling both the PC menus and Nurse Joy's healing menus, full healing is impractical and, more importantly, COMPLETELY UNNECESSARY.
- Verification:
  1. We are heading to Cerulean Cave to catch Mewtwo.
  2. Mewtwo is the only fight we will participate in; we can escape all other wild encounters using the `flee_battle` custom tool.
  3. We have the MASTER BALL. It has a 100% success rate on Turn 1 of battle without requiring any damage, HP, or PP from our team.
  4. HM moves (SURF, STRENGTH) do not consume PP in the overworld and can be executed even at 0 PP.
- Conclusion: We will immediately bypass the healing step and navigate directly to the Cerulean Cave entrance.