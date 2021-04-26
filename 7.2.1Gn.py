def main():
    from analysis import analysis
    a = []
    for i in range(10):
        a.append(1/(i+1))
    for i in range(len(a)):
        print("ellipse"+str(i+1))
        analysis(1,a[i],[1,1,1], i+1)
        print("====================")
        

if __name__ == "__main__":
    main()
