import pandas as pd 

def findS(dataset):
    df=pd.read_csv(dataset)
    dataset = df.values.tolist()

    print(df)

    flag, i, h = 0,0,[]
    for x in range(len(dataset)):
        t=dataset[x]              # Get an instance from the dataset
        if t[-1] == 1 and flag== 0:  # Initialize h with first +ve sample
            flag = 1
            h = dataset[x]
        elif t[-1] == 1:            # Update h with remaining +ve samples	
            for y in range(len(t)):
                if h[y] != t[y]:
                    h[y] = '?'
        print(f"\nS[{i}]: { h[:-1] }")
        i += 1

if __name__ == "__main__":
    dataset = 'weather.csv'
    findS(dataset)