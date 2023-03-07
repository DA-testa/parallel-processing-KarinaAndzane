# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    tofw = data
    t=[]
    count=n
    for i in range(0,n,1):
        output.append((i,0))
        t.append(0)
        
    while count<m:
        for i in range (0,n,1):
            if count ==m:
                continue
            number = t[count-n]+tofw[count-n]
            t.append(number)
            output.append((i,number))
            count=count+1
            
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    ievade=input()
    arr=ievade.split()
    n=int(arr[0])
    m=int(arr[1])
    
    # first line - n and m
    # n - thread count 
    # m - job count
    
    rinda=input()
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,rinda.split()))
    

    # TODO: create the function
    result = parallel_processing(n,m,data)
    print(result)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
