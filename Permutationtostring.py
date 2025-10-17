from collections import Counter

def permuatation(s1, s2):
    n, m = len(s1), len(s2)
    
    if n > m:
        return False
    
    count1 = Counter(s1)
    count2 = Counter(s2[:n])
    
    if count1 == count2:
        return True
    
    left = 0
    for right in range(n, m):
        count2[s2[right]] += 1
        
        count2[s2[left]] -= 1
        
        if count2[s2[left]] == 0:
            del count2[s2[left]]
            
        left += 1
        
        if count1 == count2:
            return True
        
    return False

if __name__ == "__main__":
    n1 = input()
    n2 = input()
    
    print(permuatation(n1, n2))
            