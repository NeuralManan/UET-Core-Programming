data = [0,1,2,3,4]

def  mean(data):
    n=len(data)
    sum_data= sum(data)
    return sum_data//n
def median(data):
    data.sort
    n=len(data)
    
    if n%2 == 1:
        return data[int(n//2)]
    else:
        num1 = data[n//2]
        num2 = data[n//2-1]
        return (num1+num2)/2
    
print(mean(data))
print(median(data))
        
    

    
    
    