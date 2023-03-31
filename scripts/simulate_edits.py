import random
import time
from pathlib import Path

count = 0
while count < 10000:
    r0 = random.uniform(0.0, 0.2)
    r1 = random.uniform(0.0, 0.2)
    if True:
        time.sleep(r0)
        fn = "main.py"
        print(f"Editing {fn} after {r0:.2}s")
        edit = f"\nst.write('{count}')"
        orig = Path(fn+".orig").read_text()
        Path(fn).write_text(orig+edit)

    if True:
        time.sleep(r1)
        fn = "libs/mylib/__init__.py"
        print(f"Editing {fn} after {r1:.2}s")
        edit = f"\ndef f():\n    return {count}\nst.write('{count}')"
        orig = Path(fn+".orig").read_text()
        Path(fn).write_text(orig+edit)

    count += 1

