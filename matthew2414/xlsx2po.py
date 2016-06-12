import sys

import polib
from openpyxl import load_workbook

PO_METADATA = {
    'Project-Id-Version': '1.0',
    'Report-Msgid-Bugs-To': 'tfbfgroup@googlegroups.com',
    'POT-Creation-Date': '2007-10-18 14:00+0100',
    'PO-Revision-Date': '2007-10-18 14:00+0100',
    'Last-Translator': 'you <you@example.com>',
    'Language-Team': 'English <yourteam@example.com>',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Transfer-Encoding': '8bit',
}

def main():
    po = polib.POFile("", encoding="utf-8")
    po.metadata = PO_METADATA
    file_path = sys.argv[1]
    wb = load_workbook(filename=file_path)
    ws = wb.worksheets[0]
    for row in ws.rows:
        entry = polib.POEntry(
            msgid=unicode(row[0].value),
            msgstr=unicode(row[1].value)
            )
        po.append(entry)

    import pdb;pdb.set_trace()
    po.save(file_path+".po")

