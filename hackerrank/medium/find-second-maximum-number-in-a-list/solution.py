if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = set(arr)
    l1 = list(l)
    l1.sort(reverse=True)
    runner_up = l1[1]
    print(runner_up)
    
    
    
    
    # first = float('-inf')
  #runner_up = float('-inf')
  #  for i in arr:
   #     if i > first:
    #        runner_up = first
     #       first = i
      #  elif i < first and i > runner_up:
       #     runner_up = i 
    #print(runner_up)'''
            
