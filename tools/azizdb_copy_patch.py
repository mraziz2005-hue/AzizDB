#!/usr/bin/env python3
"""AzizDB v0.5: opt-in, locally applied, UI-only selection/copy enhancement.

Run: python3 ~/Downloads/azizdb_copy_patch.py
Requires only the Python standard library to apply. The user-installed Snap is untouched.
"""
from __future__ import annotations

import ast
import os
import py_compile
import shutil
import sys
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path

TARGET = Path.home() / "Downloads" / "AzizDB_v0_5"
MAIN = TARGET / "main.py"
MODULE = TARGET / "table_copy.py"
MARKER = "# AZIZDB_GRID_COPY_V1"

ADDON = r'''"""AzizDB grid selection + copy support. UI-only; does not touch the database."""

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
'''


def die(message: str) -> None:
    print(f"❌ {message}")
    raise SystemExit(1)


def generate_modified(source: str) -> str:
    if MARKER in source:
        return source
    # Insert helper import after a documented, ordinary one-line PySide6 import.
    lines = source.splitlines(keepends=True)
    import_lines = [i for i, line in enumerate(lines) if line.startswith("from PySide6.QtGui import ")]
    if len(import_lines) != 1:
        die("لم أجد مكان الاستيراد المتوقع في main.py؛ لم أغير شيئًا.")
    lines.insert(import_lines[0] + 1, f"from table_copy import install_table_copy  {MARKER}\n")
    data = "".join(lines)
    configure = "    @staticmethod\n    def configure_table(table):"
    if data.count(configure) != 1:
        die("configure_table غير مطابق للإصدار المتوقع؛ لم أغير شيئًا.")
    start = data.index(configure)
    stop = data.find("\n    def ", start + len(configure))
    if stop == -1:
        die("تعذر تحديد نهاية configure_table؛ لم أغير شيئًا.")
    segment = data[start:stop]
    old = "        table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)"
    if segment.count(old) != 1:
        die("إعداد التحديد ليس كما في v0.5؛ لم أغير شيئًا.")
    # Preserve the original table initialization and edit triggers; add the copy helper.
    segment = segment.replace(old, "        install_table_copy(table)", 1)
    data = data[:start] + segment + data[stop:]
    return data


def main() -> None:
    if not MAIN.is_file():
        die(f"ملف الكود غير موجود: {MAIN}. تأكد أنك فكيت AzizDB_v0_5.zip في Downloads.")
    if MODULE.exists() and MARKER not in MAIN.read_text(encoding="utf-8"):
        die("table_copy.py موجود مسبقًا؛ ما راح أكتب فوقه. احتفظ بنسختك أولًا.")
    original = MAIN.read_text(encoding="utf-8")
    if MARKER in original:
        if not MODULE.is_file():
            die("تعديل main.py موجود لكن table_copy.py مفقود. لم أغير شيئًا.")
        print("✅ التعديل مثبت بالفعل في هذا المجلد؛ لا حاجة لتكراره.")
        return
    changed = generate_modified(original)
    # Fail safely before writing anything.
    for name, content in (("main.py", changed), ("table_copy.py", ADDON)):
        try:
            ast.parse(content, filename=name)
            compile(content, name, "exec")
        except (SyntaxError, ValueError) as error:
            die(f"فحص {name} فشل قبل التعديل: {error}")

    backup = TARGET / f"main.py.before_grid_copy_{datetime.now():%Y%m%d_%H%M%S}.bak"
    shutil.copy2(MAIN, backup)
    temp_main = None
    try:
        fd, tmp = tempfile.mkstemp(prefix=".main_copy_", suffix=".py", dir=TARGET)
        temp_main = Path(tmp)
        with os.fdopen(fd, "w", encoding="utf-8") as out:
            out.write(changed)
        MODULE.write_text(ADDON, encoding="utf-8")
        temp_main.replace(MAIN)
        # Compile syntax, without modifying database or installed Snap.
        py_compile.compile(str(MAIN), doraise=True)
        py_compile.compile(str(MODULE), doraise=True)
    except Exception as error:
        shutil.copy2(backup, MAIN)
        if MODULE.is_file():
            MODULE.unlink()
        die(f"تعذر إكمال التعديل، وأعدت main.py من النسخة الاحتياطية: {error}")
    finally:
        if temp_main is not None and temp_main.exists():
            temp_main.unlink()

    # Export only known project files; avoid local credentials, caches, venvs, etc.
    out_zip = TARGET.parent / "AzizDB_v0_5_copy_fix.zip"
    allowed_names = [
        "main.py", "table_copy.py", "appearance.py", "column_sizing.py",
        "database.py", "ssh_tunnel.py", "editor_tools.py", "README.md",
        "requirements.txt", "run.sh",
    ]
    with zipfile.ZipFile(out_zip, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in allowed_names:
            filepath = TARGET / name
            if filepath.is_file():
                archive.write(filepath, f"AzizDB_v0_5/{name}")
        for dirname in ("assets", "tests"):
            folder = TARGET / dirname
            if folder.exists():
                for filepath in folder.rglob("*"):
                    if filepath.is_file() and "__pycache__" not in filepath.parts and not filepath.name.startswith("."):
                        archive.write(filepath, f"AzizDB_v0_5/{filepath.relative_to(TARGET)}")
    print("✅ تم تعديل جدول البيانات وجدول نتائج SQL.")
    print("✅ نسخ خلايا/صفوف/أعمدة/نطاق، وCopy with Headers، وقائمة الزر الأيمن.")
    print("✅ فحص Python النحوي نجح. لم يتم اختبار الواجهة عمليًا بعد.")
    print(f"🔐 نسخة احتياطية: {backup}")
    print(f"📦 نسخة كود معدّلة: {out_zip}")
    print("ℹ️ نسخة Snap المثبتة لم تتغير. اختبر نسخة المصدر قبل بناء إصدار جديد.")


if __name__ == "__main__":
    main()