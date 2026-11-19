# 🐧 AzizDB v0.5.1 — Grid Selection & Copy

**Release type:** Python source archive. The new **Snap package is not built or published yet**.

## What's new

- Select and copy a single cell, multiple cells, a range, an entire row, an entire column, or all visible results.
- **Ctrl+C**: copy the selection.
- **Ctrl+Shift+C**: copy with column headers.
- **Right-click**: Copy, Copy with Headers, Select Row, Select Column, and Select All.
- TSV output for pasting into spreadsheets or messages.
- The same behavior is installed on the table browser and SQL results widgets.
- Arabic and English context-menu labels.

## Preserved

SQLite/MySQL database adapters, SSH tunnels, pagination, appearance settings, and existing edit/write permission logic remain unchanged by this copy enhancement.

## Validation

- Python syntax check passed.
- All **19** existing automated tests passed.
- Focused TSV formatting tests passed.
- User tested the copy feature successfully on Fedora on **November 19, 2026**.
- Copy operates on **displayed results**, not unseen database rows.

## Install from source

1. Download the **AzizDB_v0.5.1-source.zip** asset from the v0.5.1 release **after it is uploaded**.
2. Extract the archive into a new directory.
3. Run:

```bash
cd AzizDB_v0_5_1
bash run.sh
```

This is release documentation only; a GitHub v0.5.1 release and its ZIP attachment must still be published.

The existing v0.5 Snap remains unchanged until a new Snap is separately built and tested.
