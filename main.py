# # ai-joke-03: one fixed one-liner about AI coding agents.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
JOKE = "My agent wrote 500 lines to fix a typo. The typo is still there."



os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
