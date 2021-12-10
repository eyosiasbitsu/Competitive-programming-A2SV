    num_swaps = 0
    
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                num_swaps = num_swaps + 1
    print('Array is sorted in '+str(num_swaps)+' swaps.')
    print('First Element: '+str(a[0]))
    print('Last Element: '+str(a[n-1]))    
