# Naming Screen Column Offset Mechanic

## Discovery & Explanation
- In the nickname naming screen, there is a visual shift in the rendering of the letter grid. The letters and symbols are shifted to the right by exactly one column relative to the game ROM's internal cursor mapping.
- This creates a consistent 1-column horizontal offset between where the cursor visually points and what character is actually entered when "A" is pressed.
- **Rule:** The character entered is always the one situated exactly **one column to the right** of the cursor's visual position.

## Accurate Mapping & Selector Table
- To select a character at **Visual Column Y**, the player must place the cursor at **Visual Column Y-1** (which corresponds to internal Column Y-1):
  - **Visual Column 1** ('A', 'J', 'S', 'x', '-', 'lower'): Place cursor at **Column 0** (the empty column on the far left).
  - **Visual Column 2** ('B', 'K', 'T', '(', '?', 'case'): Place cursor at **Column 1** (pointing at 'A'/'J'/'S').
  - **Visual Column 3** ('C', 'L', 'U', ')', '!'): Place cursor at **Column 2** (pointing at 'B'/'K'/'T').
  - **Visual Column 4** ('D', 'M', 'V', ':', '♂'): Place cursor at **Column 3** (pointing at 'C'/'L'/'U').
  - **Visual Column 5** ('E', 'N', 'W', ';', '♀'): Place cursor at **Column 4** (pointing at 'D'/'M'/'V').
  - **Visual Column 6** ('F', 'O', 'X', '[', '/'): Place cursor at **Column 5** (pointing at 'E'/'N'/'W').
  - **Visual Column 7** ('G', 'P', 'Y', ']', '.'): Place cursor at **Column 6** (pointing at 'F'/'O'/'X').
  - **Visual Column 8** ('H', 'Q', 'Z', 'PK', ','): Place cursor at **Column 7** (pointing at 'G'/'P'/'Y').
  - **Visual Column 9** ('I', 'R', 'MN', 'END'): Place cursor at **Column 8** (pointing at 'H'/'Q'/'Z' / between ',' and 'END').

## Important Navigation & Wrap-Around Mechanics
- **Horizontal Wrapping:** Row 2 and Row 4 wrap around when you press "Left" at Column 1 ('S' or '-') or "Right" at Column 8 ('Z' or 'END').
- Wrapping left from Column 1 moves the cursor to Column 8.
- Wrapping right from Column 8 moves the cursor to Column 1.
- **B Button:** Universal backspace. Deletes the last character without moving the cursor.