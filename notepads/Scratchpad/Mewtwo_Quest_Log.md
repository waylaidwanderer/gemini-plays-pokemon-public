# Mewtwo Quest Log (Post-Game)
- Started: Turn 111394
- Goal: Enter Cerulean Cave and catch Mewtwo.

## Step 1: Fly to Cerulean City and Heal
- Party Status: Blastoise (GEMMY) is out of PP and low on HP. Must heal at Cerulean Pokémon Center.
- Turn 111421: Arrived in Cerulean City via FLY, standing right outside the Pokémon Center.

- Turn 111479: Determined that due to the harness's automatic text advance repeatedly pressing B and cancelling both the PC menus and Nurse Joy's healing menus, full healing is impractical and, more importantly, COMPLETELY UNNECESSARY.
- Verification:
  1. We are heading to Cerulean Cave to catch Mewtwo.
  2. Mewtwo is the only fight we will participate in; we can escape all other wild encounters using the `flee_battle` custom tool.
  3. We have the MASTER BALL. It has a 100% success rate on Turn 1 of battle without requiring any damage, HP, or PP from our team.
  4. HM moves (SURF, STRENGTH) do not consume PP in the overworld and can be executed even at 0 PP.
- Conclusion: We will immediately bypass the healing step and navigate directly to the Cerulean Cave entrance.
- Turn 111421-111567: Flew to Cerulean City, navigated past Nugget Bridge, surfed to the Cerulean Cave island, and successfully entered Cerulean Cave 1F.
- Turn 111595: Stood at (21, 11) on TYPE_4b8d (ladder) and confirmed that it does not auto-warp the player. Tested pressing 'A' on the ladder, which also did not warp or initiate any text. We conclude that this specific ladder tile (21, 11) is likely a one-way dropdown ladder or inactive in 1F, so we cannot ascend through it.
- Route to Next Ladder: We identified another ladder (TYPE_4b8d) at (25, 9). The path to (25, 9) from our current position (21, 11) is fully open and passable:
  - From (21, 11), head Up 4 steps to (21, 7).
  - From (21, 7), head Right 4 steps to (25, 7).
  - From (25, 7), head Down 2 steps to (25, 9).
  - Standing on (25, 9) should let us ascend to 2F. Let's execute this path.