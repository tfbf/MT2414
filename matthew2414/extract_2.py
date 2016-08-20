import os
import sys
import polib
import nltk
import argparse
import codecs

def read_po(file_path):
	po = polib.pofile(file_path, encoding='utf-8')
	tokens = {}
	for entry in po:
		tokens[entry.msgid] = entry.msgstr
	return tokens

def translate(f):
	po_file_path=sys.argv[1]
	tokens = read_po(po_file_path)
	entries = tokens.items()
	sortedEntries=sorted(entries, key=lambda s: len(s[0]), reverse=True)
	for k, v in sortedEntries:
#	for k, v in sorted(tokens.items(), key=len, reverse=True):
		f=f.replace(k, v)
	return f
			
sfm_file_path=codecs.open(sys.argv[2], encoding="utf-8", mode="r")
f = sfm_file_path.read()
sfm_file_path.close()

outfile = codecs.open(sys.argv[3],encoding="utf-8",mode="w")
outfile.write(translate(f))
outfile.close()
print ("Translation Completed. Please open " + str(sys.argv[3]) + " to see the translated file.")
