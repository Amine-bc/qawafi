import sys
server_path = '/content/qawafi/qawafi_server'
if server_path not in sys.path:
  sys.path.append(server_path)

server_path = './qawafi/qawafi_server/Arabic_Diacritization'
if server_path not in sys.path:
  sys.path.append(server_path)


shatrs = """
القلب أعلم يا عذول بدائه
وأحق منك بجفنه وبمائه
مهلا فإن العذل من أسقامه
وترفقا فالسمع من أعضائه
لا تعذل المشتاق في أشواقه
حتى يكون حشاك في أحشائه
"""

shatrs = shatrs.split("\n")[1:-1]
baits = [' # '.join(shatrs[2*i:2*i+2]) for i in range(len(shatrs)//2)]

from bait_analysis import BaitAnalysis

analysis = BaitAnalysis()
output = analysis.analyze(baits,override_tashkeel=True)

from utils import get_output_df, display_highlighted_patterns
df = get_output_df(output)
display_highlighted_patterns(df)

