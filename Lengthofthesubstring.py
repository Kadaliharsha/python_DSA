def lengthofsubstring(s):
    left = 0
    max_len = 0 
    last_seen = {}
    
    for right in range(len(s)):
        ch = s[right]
        
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
            
        last_seen[ch] = right
        
        max_len = max(max_len, right - left + 1)
        
    return max_len

if __name__ == "__main__":
    n = input()
    print(lengthofsubstring(n))