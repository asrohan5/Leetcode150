class sol:
    def isValid(self, s: str) -> bool:
        leftsymbols = []
        for c in s:
            if c in ['(', '{', '[']:
                leftsymbols.append(c)
            elif c == ')' and len(leftsymbols) != 0 and leftsymbols[-1] == '(':
                leftsymbols.pop()
            elif c == '}' and len(leftsymbols) != 0 and leftsymbols[-1] == '{':
                leftsymbols.pop()
            elif c == ']' and len(leftsymbols) !=0 and leftsymbols[-1] == '[':
                leftsymbols.pop()
            else:
                return False
        return leftsymbols == []
        
