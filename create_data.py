import os
import pandas as pd
#iterrate through all the csv's and add the data to the new csv file
#get all csv files in data/mnist folder
def create_data(datapath = 'data/mnist_fashion/'):
    #get all csv files in data/mnist folder
    csv_files = [f for f in os.listdir(datapath) if f.endswith('.csv')]
    #create a new csv file with the data
    df = pd.DataFrame()
    #iterrate through all the csv's and add the data to the new csv file
    for file in csv_files:
        df = df.append(pd.read_csv(datapath + file))
    #save the new csv file
    df.to_csv(datapath+'mnist_complete.csv', index=False)

if __name__ == '__main__':
    create_data()