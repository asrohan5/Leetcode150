class sol:
  def length(self, s:str) -> int:
    word = s.split()
    if not word:
      return 0
    return len(word[-1])
