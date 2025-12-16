class sol:
  def reverse(self, s:str) -> str:
    s = s.strip()
    a = s.split()
    rev = a[::-1]
    return " ".join(rev)
