def decode_message( s: str, p: str) -> bool:

# write your code here
        for i in range(len(s)):
                for j in range(len(p)):
                        if p[j]=='*':
                                return True
                        
                        elif s[i]==p[j] or p[j]=='':
                                continue
                        
                        else:
                                return False
                        
  
        return False