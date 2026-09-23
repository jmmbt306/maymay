import sys, re

filepath = sys.argv[1]
with open(filepath, "r") as f:
    text = f.read()

div_ui_re = r'  // シグナルUIの構築\n  if \(divergenceList\.length > 0\) \{.*?main\.appendChild\(signalContainer\);\n  \}\n\n'
text = re.sub(div_ui_re, '', text, flags=re.DOTALL)

target_ui_re = r'  const topDivs = targetDivList\.slice\(0, 10\);\n  const bottomDivs = targetDivList\.slice\(-10\)\.reverse\(\);\n\n  const rankingContainer = document\.createElement\("div"\);\n.*?main\.appendChild\(rankingContainer\);\n\n'
text = re.sub(target_ui_re, '', text, flags=re.DOTALL)

with open(filepath, "w") as f:
    f.write(text)
