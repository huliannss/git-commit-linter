import re
def check(m): return bool(re.match(r'^(feat|fix|docs|chore): .+', m))