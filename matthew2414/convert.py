import os
import sys
import nltk
import polib
import argparse
import codecs

po = polib.POFile("", encoding="utf-8")
po.metadata = {
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

def read_po(file_path):
    po = polib.pofile(file_path, encoding='utf-8')
    tokens = {}
    for t in po:
        tokens[t.msgid] = t.msgstr

    return tokens

def write_output(gw_file_path, dest_file_path, tokens):
    input_text_lines = open(gw_file_path).readlines()
    out_text_lines = []
    for line in input_text_lines:
        line_words = nltk.word_tokenize(line.decode('utf8'))
        new_line_words = []
        for word in line_words:
            new_line_words.append(tokens[word])
        out_line = " ".join(new_line_words)
        out_text_lines.append(out_line)

    out_text = "\n".join(out_text_lines)
    return out_text+"\n"


def main():
    po_file_path = sys.argv[1]
    tokens = read_po(po_file_path)
    gw_file_path = sys.argv[2]
    dest_file_path = gw_file_path + "-out.txt"
    out_text = write_output(gw_file_path, dest_file_path, tokens)
    fd = codecs.open(dest_file_path, "w", encoding="utf-8")
    fd.write(out_text)
    fd.close()
