# Pokémon Mansion Gate State Matrix (Turn 75303)
- **Methodology**: Stood at (25, 12) facing Down and pressed 'Down' on Turn 75301 to test collision on the gate panel at (25, 13) (TYPE_a83b).
- **Active Configuration**: Statue 2 (on 2F) is currently in its 'Default' state (or whichever state is achieved after resetting on Turn 75189).
- **Result**: Bumped into the gate panel (visited 0 tiles). The gate at (25, 13) is CLOSED and impassable.
- **Hypothesis**: Interacting with Statue 2 (or other statues in the Mansion) toggles the gate states globally. If we return to Statue 2 and toggle it, the gate at (25, 13) should open, unlocking access to the south section of the eastern room on 1F (Rows 14-16, Columns 22-27).