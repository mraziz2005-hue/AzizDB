"""AzizDB grid selection + copy support. UI-only; does not touch the database."""

import csv
import io

from PySide6.QtCore import Qt, QItemSelection, QItemSelectionModel
from PySide6.QtGui import QGuiApplication, QKeySequence, QShortcut
from PySide6.QtWidgets import QAbstractItemView, QMenu, QTableWidget


def selected_tsv(table: QTableWidget, with_headers: bool = False) -> str:
    """Return selected visible cells as paste-friendly tab-separated text.

    Explicit selected cells are authoritative. Noncontiguous selections preserve
    their positions using blank placeholders, rather than leaking unselected data.
    If nothing is selected, fall back to the current cell.
    """
    indexes = [index for index in table.selectedIndexes() if index.isValid()]
    if not indexes:
        current = table.currentIndex()
        if current.isValid():
            indexes = [current]
    if not indexes:
        return ""
    positions = {(i.row(), i.column()) for i in indexes}
    rows = sorted({r for r, _ in positions})
    columns = sorted({c for _, c in positions})
    if not rows or not columns:
        return ""
    # Preserve noncontiguous selections as an Excel-compatible rectangular block.
    first_row, last_row = rows[0], rows[-1]
    first_col, last_col = columns[0], columns[-1]
    output = io.StringIO(newline="")
    writer = csv.writer(output, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    if with_headers:
        writer.writerow([
            table.horizontalHeaderItem(c).text()
            if table.horizontalHeaderItem(c) is not None else str(c + 1)
            for c in range(first_col, last_col + 1)
        ])
    for r in range(first_row, last_row + 1):
        values = []
        for c in range(first_col, last_col + 1):
            item = table.item(r, c)
            values.append(item.text() if (r, c) in positions and item is not None else "")
        writer.writerow(values)
    return output.getvalue().rstrip("\n")


def copy_grid_selection(table: QTableWidget, with_headers: bool = False) -> bool:
    value = selected_tsv(table, with_headers)
    if not value:
        return False
    QGuiApplication.clipboard().setText(value)
    return True


def _select_whole_row(table: QTableWidget, row: int) -> None:
    if 0 <= row < table.rowCount() and table.columnCount() > 0:
        selection = QItemSelection(
            table.model().index(row, 0),
            table.model().index(row, table.columnCount() - 1),
        )
        table.selectionModel().select(selection, QItemSelectionModel.SelectionFlag.ClearAndSelect)
        table.setCurrentCell(row, 0, QItemSelectionModel.SelectionFlag.NoUpdate)


def _select_whole_column(table: QTableWidget, col: int) -> None:
    if 0 <= col < table.columnCount() and table.rowCount() > 0:
        selection = QItemSelection(
            table.model().index(0, col),
            table.model().index(table.rowCount() - 1, col),
        )
        table.selectionModel().select(selection, QItemSelectionModel.SelectionFlag.ClearAndSelect)
        table.setCurrentCell(0, col, QItemSelectionModel.SelectionFlag.NoUpdate)


def _show_grid_menu(table: QTableWidget, pos) -> None:
    # Keep an existing multi-selection on right click; do not replace it.
    clicked = table.indexAt(pos)
    if clicked.isValid() and not table.selectedIndexes():
        table.setCurrentCell(clicked.row(), clicked.column())
    arabic = getattr(table.window(), "lang", "en") == "ar"
    menu = QMenu(table)
    copy_action = menu.addAction("نسخ التحديد\tCtrl+C" if arabic else "Copy\tCtrl+C")
    header_action = menu.addAction(
        "نسخ مع أسماء الأعمدة\tCtrl+Shift+C" if arabic else "Copy with Headers\tCtrl+Shift+C"
    )
    menu.addSeparator()
    row_action = menu.addAction("تحديد الصف" if arabic else "Select Row")
    col_action = menu.addAction("تحديد العمود" if arabic else "Select Column")
    all_action = menu.addAction("تحديد الكل\tCtrl+A" if arabic else "Select All\tCtrl+A")
    has_target = clicked.isValid() or table.currentIndex().isValid()
    row_action.setEnabled(has_target)
    col_action.setEnabled(has_target)
    choice = menu.exec(table.viewport().mapToGlobal(pos))
    if choice == copy_action:
        copy_grid_selection(table)
    elif choice == header_action:
        copy_grid_selection(table, True)
    elif choice == row_action:
        index = clicked if clicked.isValid() else table.currentIndex()
        if index.isValid():
            _select_whole_row(table, index.row())
    elif choice == col_action:
        index = clicked if clicked.isValid() else table.currentIndex()
        if index.isValid():
            _select_whole_column(table, index.column())
    elif choice == all_action:
        table.selectAll()


def install_table_copy(table: QTableWidget) -> None:
    """Install once on a grid without changing its SQL or database handlers."""
    if getattr(table, "_azizdb_grid_copy_installed", False):
        return
    table._azizdb_grid_copy_installed = True
    table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
    table.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
    # Both headers must be clickable to select entire columns or rows.
    table.horizontalHeader().setSectionsClickable(True)
    table.verticalHeader().setSectionsClickable(True)
    table.verticalHeader().setVisible(True)
    table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
    table.customContextMenuRequested.connect(lambda pos, grid=table: _show_grid_menu(grid, pos))

    copy_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.Copy), table)
    copy_shortcut.setContext(Qt.ShortcutContext.WidgetWithChildrenShortcut)
    copy_shortcut.activated.connect(lambda grid=table: copy_grid_selection(grid))
    with_headers_shortcut = QShortcut(QKeySequence("Ctrl+Shift+C"), table)
    with_headers_shortcut.setContext(Qt.ShortcutContext.WidgetWithChildrenShortcut)
    with_headers_shortcut.activated.connect(lambda grid=table: copy_grid_selection(grid, True))
    # Keep explicit refs; Qt owns them, but this also documents their lifetime.
    table._azizdb_grid_copy_shortcuts = (copy_shortcut, with_headers_shortcut)
