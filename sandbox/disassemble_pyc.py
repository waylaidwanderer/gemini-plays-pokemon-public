import marshal
import dis
import os
import types

def is_coord(val):
    return (isinstance(val, tuple) and len(val) == 2 and 
            isinstance(val[0], int) and isinstance(val[1], int) and
            0 <= val[0] <= 40 and 0 <= val[1] <= 40)

def dump_consts_recursive(code_obj, prefix=""):
    print(f"{prefix}Code object co_name: {code_obj.co_name}")
    # Print co_consts
    coords = []
    for i, const in enumerate(code_obj.co_consts):
        if is_coord(const):
            coords.append(const)
        elif isinstance(const, tuple) and all(is_coord(x) for x in const):
            print(f"{prefix}  Found tuple of coords at const {i} (len {len(const)}): {const[:10]}...")
        elif isinstance(const, types.CodeType):
            dump_consts_recursive(const, prefix + "  ")
            
    if coords:
        print(f"{prefix}  Individual coords found in co_consts (len {len(coords)}): {coords[:20]}...")

def disassemble_pyc(path):
    print(f"=== Disassembling {path} ===")
    try:
        with open(path, "rb") as f:
            f.read(16)
            code_obj = marshal.load(f)
            dump_consts_recursive(code_obj)
            
            print("\nDisassembling bytecode to find LOAD_CONST of coordinates:")
            # We can disassemble the code object and look for LOAD_CONST instructions loading tuples
            instructions = list(dis.get_instructions(code_obj))
            coords_loaded = []
            for instr in instructions:
                val = instr.argval
                if is_coord(val):
                    coords_loaded.append(val)
                elif isinstance(val, types.CodeType):
                    # Also check sub-code objects if any
                    sub_instrs = list(dis.get_instructions(val))
                    for sub_instr in sub_instrs:
                        sub_val = sub_instr.argval
                        if is_coord(sub_val):
                            coords_loaded.append(sub_val)
                            
            print(f"  Total individual coordinates loaded by instructions: {len(coords_loaded)}")
            # Let's print the entire list of loaded coords
            print(f"  Loaded coords sequence:")
            print(coords_loaded)
    except Exception as e:
        print(f"  Error: {e}")

if __name__ == "__main__":
    pyc_path = os.path.join("__pycache__", "complete_speedrun_v5.cpython-314.pyc")
    if os.path.exists(pyc_path):
        disassemble_pyc(pyc_path)
    else:
        print(f"File not found: {pyc_path}")
