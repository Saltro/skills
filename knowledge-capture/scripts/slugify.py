#!/usr/bin/env python3
import re, sys, unicodedata
s = sys.argv[1] if len(sys.argv) > 1 else ''
s = unicodedata.normalize('NFKC', s).strip().lower()
s = re.sub(r'[\/]+', '-', s)
s = re.sub(r'[^w一-鿿-]+', '-', s)
s = re.sub(r'-{2,}', '-', s).strip('-')
print(s[:80] or 'untitled')
