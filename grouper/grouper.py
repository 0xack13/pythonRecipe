### >>> for i in grouper(2, 'ABCDEFG'):
### ...     print i
### ... 
### ['A', 'B']
### ['C', 'D']
### ['E', 'F']
##  ['G']
class grouper:
  @staticmethod
  def grouperfn(n, iterable):
    "grouper(3, 'ABCDEFG') --> ABC DEF G"
    buf = []
    for i, c in enumerate(iterable):
      buf.append(c)
      if (i+1) % n == 0:
        yield buf
        buf = []
    if buf:
      yield buf



