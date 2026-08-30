import marshal
import types
import os

def extract_consts(code_obj):
    consts = []
    if hasattr(code_obj, 'co_consts'):
        for c in code_obj.co_consts:
            if isinstance(c, (list, tuple)):
                # Check if it looks like a list of coordinates
                if len(c) > 0 and all(isinstance(item, (list, tuple)) and len(item) == 2 for item in c):
                    consts.append(c)
                else:
                    consts.append(c)
            elif isinstance(c, types.CodeType):
                consts.extend(extract_consts(c))
    return consts

def inspect_pyc(path):
    print(f"\n===== Inspecting {path} =====")
    try:
        with open(path, 'rb') as f:
            # Skip .pyc header (16 bytes for Python 3.7+)
            f.read(16)
            code_obj = marshal.load(f)
            consts = extract_consts(code_obj)
            for c in consts:
                # If it's a list/tuple of tuples, print it nicely
                if isinstance(c, (list, tuple)) and len(c) > 0 and isinstance(c[0], (list, tuple)):
                    print("Found coordinate path:")
                    print("  ", c)
                else:
                    print("Constant:", c)
    except Exception as e:
        print("Error:", e)

# List of pyc files to inspect
pyc_files = [
    "__pycache__/walk_to_balcony_from_28_12.cpython-314.pyc",
    "__pycache__/walk_to_balcony_from_3_6_state_a.cpython-314.pyc",
    "__pycache__/test_warp.cpython-314.pyc",
    "__pycache__/walk_to_balcony_final.cpython-314.pyc",
]

for f in pyc_files:
    if os.path.exists(f):
        inspect_pyc(f)
    else:
        print(f"File not found: {f}")
