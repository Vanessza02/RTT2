import sys
from pylint import lint
THRESHOLD = 8
run = lint.Run(["gyak.py"], exit=False)
score = run.linter.stats.global_note
if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    sys.exit(1)
sys.exit(0)