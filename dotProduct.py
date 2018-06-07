def dot_prod(v1,v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i]*v2[i]
        
    return result

def main():
    print("Input vectors like the following: A vector <3,4,5> should be entered as '3 4 5'")
    v1 = list(map(int, input("First vector: ").strip().split()))
    v2 = list(map(int, input("Second vector: ").strip().split()))
    if len(v1) == len(v2):
        result = dot_prod(v1,v2)
        print("Scalar Product: " + str(result))
    else:
        print("The vectors need to have the same number of elements")
        main()
        
        
main()
