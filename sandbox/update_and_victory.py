import os
import solve_mansion_final_victory_3

def main():
    print("Writing empirical verifications and East Wing constraints to Switch_Matrix.md...")
    matrix_path = "notepads/Scratchpad/Switch_Matrix.md"
    if os.path.exists(matrix_path):
        with open(matrix_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        additional_notes = """
## Empirical Reset Verification (Burden of Proof)
- **DIG / Exit Reset:** On Turn 49084, DIG was used to exit the mansion. Upon re-entering the mansion on Turn 49111, the gate at `(10, 11)` on 3F was observed OPEN, and the gate at `(2, 12)` was OPEN, empirically proving that exiting and re-entering resets the global switch to **State A**.

## Mapped East Wing & Corridor Constraints (Turns 49145-49271)
- **Column 10 Gates:** Closed vertical shutter gate on rows 11 to 15 in State B (empirically blocked on Turn 49259; open in State A).
- **Row 11 Horizontal Passage:** Completely open horizontally across column 22 in both states, allowing horizontal bypass of column 22 rubble.
- **Column 22 Rubble:** Blocked by solid rubble piles on rows 8, 9, 10, 12, 13 (verified on Turn 49185).
- **Columns 4-7 Red Corridor:** Enclosed corridor on rows 10-18 in State B. Gate at column 3/4 is CLOSED on rows 12-20 in State B (verified on Turn 49212). Gate at column 7/8 is CLOSED on rows 10-20 in State B.
- **Row 9 West Wall:** Solid horizontal wall across columns 2 to 7 on row 9 (empirically blocked on Turn 49251).
"""
        if additional_notes not in content:
            content += additional_notes
            with open(matrix_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("Successfully updated Switch_Matrix.md.")
            
    # Now run the final victory script!
    print("Executing master victory balcony drop route from solve_mansion_final_victory_3.py...")
    solve_mansion_final_victory_3.run_main()

if __name__ == "__main__":
    main()
