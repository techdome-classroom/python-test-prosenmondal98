def decode_message( s: str, p: str) -> bool:

# write your code here
        n=0
        
        for j in range(len(p)):
                if p[j]=='*':
                        return True
                
                elif s[j]==p[j] or p[j]=='?':
                        n+=1
                        continue
                
                else:
                        return False
        if n==len(s):
                return True
                
  
        return False