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
- Turn 111610: Successfully ascended to Cerulean Cave 2F. We discovered that stepping onto (23, 7) on 1F (0_228) immediately warped us to 2F (0_226) at (23, 7). Stood at (22, 6) and found our way south along Column 23, but we hit a rock wall at (20, 12).
- Turn 111633: Currently standing at (20, 11). We verified that Column 19 is blocked by solid rock walls on Rows 8, 10, and 12, making it impossible to directly go Left to the ladder at (19, 7) from our upper entrance. We are now exploring the western serpentine corridor on Row 11 toward Column 17 to check for a bypass.
- Turn 111667: Successfully bypassed the Column 26 barrier using a hidden serpentine passage on Column 25, Row 9, and reached the northeast upper section at (27, 6). We verified that Column 24 Row 7 is solid rock, which separates the western and eastern upper sections on Row 7. We then navigated to (29, 3) where we found that the actual Ladder 2 is located at (29, 1). We defined map markers for both Ladder 2 at (29, 1) and the Item at (29, 9) on Map 0_226.
- Turn 111689: Reached (29, 3) on Cerulean Cave 2F (0_226). Verified that the actual Ladder 2 is located at (29, 1) (labeled with the ladder symbol [=]), rather than (29, 3). The path to reach (29, 1) from (29, 3) goes Left to (28, 3), Up 2 steps to (28, 1), and Right to (29, 1). We will descend through this ladder to explore 1F.
- Turn 111707: Arrived at (23, 2) on 1F (0_228). We see a ladder at (23, 3) (TYPE_4b8d) and water at Rows 4-5. Tested walking onto (23, 3) and found it is a ramp. We stood on (23, 3) and successfully used SURF to get onto the water at (23, 4).
- Turn 111754: Surfed south along the Column 8 vertical canal. Currently standing at (8, 14). We see a water ramp at (11, 13) leading onto the land platform on the right. We will navigate to (11, 14) and go Up onto the ramp at (11, 13) to explore this land platform.