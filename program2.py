def decode_message( s: str, p: str) -> bool:

# write your code here
        n=0
        for i in range(len(s)):
        for j in range(len(p)):
                if p[j]=='*':
                        return True
                
                elif s[i]==p[j] or p[j]=='?':
                        n+=1
                        continue
                
                else:
                        return False
        
                
  
        return False