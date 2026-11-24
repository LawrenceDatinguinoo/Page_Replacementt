# Page Replacement Algorithms (Console Project)

A console-only Python project with three page replacement algorithms:

- `fifo.py` — First-In, First-Out
- `lru.py` — Least Recently Used
- `optimal.py` — Optimal (replaces the page whose next use is farthest in the future)
- `main.py` — console menu to choose an algorithm
- `console_ui.py` — menu display and input helper

## Requirements

Python 3.8 or newer. No third-party packages are needed.

## Run the menu

Open a terminal in this folder and run:

```bash
python main.py
```

Choose FIFO, LRU, or Optimal from the menu. You can also run each algorithm directly:

```bash
python fifo.py
python lru.py
python optimal.py
```

On some systems, use `python3` instead of `python`.

Each algorithm asks for the number of frames, then a page reference string. Separate page numbers with spaces or commas, for example:

```text
Enter number of frames: 3
Enter page reference string (e.g. 7 0 1 2 0 3): 7 0 1 2 0 3 0 4 2 3 0 3 2
```

The console prints the frame contents after every reference, whether it was a hit or fault, and the total hits, faults, and ratios.
