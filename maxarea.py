def maxarea(dimensions):
    
    max_diag = 0
    for l, w in dimensions:
        max_diag = max(max_diag, l*l + w*w)
        
    max_area = 0
    for l, w in dimensions:
        if l*l + w*w == max_diag:
            max_area = max(max_area, l*w)
            
    return max_area

if __name__ == "__main__":
    dim = eval(input())
    print(maxarea(dim))