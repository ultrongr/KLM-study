
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(file):
    
    data = pd.read_csv(file)
    data = data.dropna()
    data = data.drop(data.columns[0], axis=1)
    data = data.astype(float)
    data = data / 1000
    number_of_rows = len(data)
    rows = []
    for i in range(number_of_rows):
        rows.append(data.iloc[i].values)
    
    rows.sort(key = lambda x: x[0])
    data = pd.DataFrame(rows, columns = ['Keyboard 1', 'Keyboard 2', 'Keyboard 3', 'Virtual 1', 'Virtual 2', 'Virtual 3'])

    return data

def export_characteristics(data):

    print("\nData characteristics:")
    print("Number of rows:", len(data)) 
    averages = []
    for i in range(6):
        averages.append(sum(data.iloc[:, i]) / len(data))
    
    
    variances = []
    for i in range(6):
        variances.append(data.iloc[:, i].var())
    
    ## Keyboard
    print(f"\nAverage keyboard values:", end = " ")
    for i in range(3):
        print(f"{averages[i]:.1f}", end = "\t")
    
    print(f"\nDifference between average keyboard values: {averages[0] - averages[1]:.1f} ({100*(averages[0] - averages[1])/averages[0]:.2f}%), {averages[1] - averages[2]:.1f} ({100*(averages[1] - averages[2])/averages[1]:.2f}%)")

    print("\nVariance keyboard values:", end = " ")
    for i in range(3):
        print(f"{variances[i]:.1f}", end = "\t")
    
    ## Virtual
    print("\n")
    print(f"\nAverage virtual values:", end = " ")
    for i in range(3, 6):
        print(f"{averages[i]:.1f}", end = "\t")
    
    print(f"\nDifference between average virtual values: {averages[3] - averages[4]:.1f}, ({100*(averages[3] - averages[4])/averages[3]:.2f}%), {averages[4] - averages[5]:.1f} ({100*(averages[4] - averages[5])/averages[4]:.2f}%)")

    print("\nVariance virtual values:", end = " ")
    for i in range(3, 6):
        print(f"{variances[i]:.1f}", end = "\t")



    plt.subplot(1, 2, 1)
    plt.plot(averages[:3], 'ro')
    plt.plot(averages[3:], 'go')
    plt.title("Average values")
    plt.xticks(range(3), ['1', '2', '3'])
    plt.grid()
    plt.legend(['Keyboard', 'Virtual'])

    plt.subplot(1, 2, 2)
    plt.plot(variances[:3], 'ro')
    plt.plot(variances[3:], 'go')
    plt.title("Variance values")
    plt.xticks(range(3), ['1', '2', '3'])
    plt.grid()
    plt.legend(['Keyboard', 'Virtual'])

    return

def plot_data(data):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    for i in range(3):
        # print(data.iloc[:, i])
        plt.plot(data.iloc[:, i], label=f"Data {i+1}")
        # plt.scatter(range(len(data.iloc[:, i])), data.iloc[:, i], label=f"Data {i+1}")
    
    plt.title("Keyboard")
    plt.grid()
    plt.legend(['Test 1', 'Test 2', 'Test 3'])

    plt.subplot(1, 2, 2)
    for i in range(3, 6):
        plt.plot(data.iloc[:, i], label=f"Data {i-2}")
        # plt.scatter(range(len(data.iloc[:, i])), data.iloc[:, i], label=f"Data {i-2}")

    plt.title("Virtual")
    plt.grid()
    plt.legend(['Test 1', 'Test 2', 'Test 3'])


def other_facts(data):

    ## Keyboard
    print("\n\nKeyboard:")

    diff1 = data.iloc[:, 0] - data.iloc[:, 1]
    diff2 = data.iloc[:, 1] - data.iloc[:, 2]

    print(f"Percentage of improvement from test 1 to test 2: {np.count_nonzero(diff1 > 0) / len(diff1) * 100:.2f}%")
    print(f"Percentage of improvement from test 2 to test 3: {np.count_nonzero(diff2 > 0) / len(diff2) * 100:.2f}%")

    ## Virtual
    print("\n\nVirtual:")

    diff1 = data.iloc[:, 3] - data.iloc[:, 4]
    diff2 = data.iloc[:, 4] - data.iloc[:, 5]

    print(f"Percentage of improvement from test 1 to test 2: {np.count_nonzero(diff1 > 0) / len(diff1) * 100:.2f}%")
    print(f"Percentage of improvement from test 2 to test 3: {np.count_nonzero(diff2 > 0) / len(diff2) * 100:.2f}%")
    

def main():

    data = read_data('data.csv')
    # print(data)
    export_characteristics(data)
    plot_data(data)
    other_facts(data)
    plt.show()


if __name__ == '__main__':
    main()    

