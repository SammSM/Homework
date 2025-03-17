def count_islands(islands):
    rows=len(islands)
    columns=len(islands[0])
    count=0
    
    def sink(r, c):
        if r<0 or c<0 or r>=rows or c>=columns or islands[r][c]==0:
            return None
        
        islands[r][c]=0
        
        sink(r, c-1)
        sink(r-1, c)
        sink(r, c+1)
        sink(r+1, c)
        sink(r-1, c-1)
        sink(r-1, c+1)
        sink(r+1, c+1)
        sink(r+1, c-1)
        
    for r in range(rows):
        for c in range(columns):
            if islands[r][c]==1:
                count+=1
                sink(r, c)
                    
    return count


islands_map=[[1,0,0,0,0,1,1],
             [0,1,0,0,0,0,1],
             [0,0,1,0,0,1,0],
             [0,0,0,0,1,1,0],
             [0,0,0,0,1,1,0],
             [0,0,0,0,0,0,0],
             [1,1,1,0,0,0,1]
             ]

print(count_islands(islands_map))