import matplotlib.pyplot as plt

def plot_htc2(htc_arr, temp_arr, name=''):
    Y = htc_arr
    X = x = temp_arr

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(X, Y)

    # Set the title and labels
    ax.set_title('HTC vs Temperature')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('HTC (W/m$^2$K)')

    # Show the plot
#     plt.show()
    plt.savefig(f'/kaggle/working/htc_{name}.png')


def plot_temp(temp_arr, name=''):
    Y = temp_arr
    X = np.arange(0.5, 60.5, 0.5)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(X, Y)

    # Set the title and labels
    ax.set_title('Temperature History')
    ax.set_xlabel('Time (sec)')
    ax.set_ylabel('Temperature (°C)')

    # Show the plot
#     plt.show()
    plt.savefig(f'/kaggle/working/temp_{name}.png')


def plot_res(indx, unscaled_arr_x, arr_x, arr_y):
    #indx = 2006
    # x = x_train_copy[indx]
    x = unscaled_arr_x[indx]
    
    # plt.plot(x, y_train_seq[indx], label='original')
    # plt.plot(x, model.predict(x_train_seq[indx:indx+1])[0][:, -1], label='predicted')

    plt.plot(x, arr_y[indx], label='original')
    plt.plot(x, model.predict(arr_x[indx:indx+1])[0][:, -1], label='predicted')
    
    # Naming the x-axis, y-axis and the whole graph
    plt.xlabel("Temperature (°C)")
    plt.ylabel("HTC (W/m$^2$K)")
    plt.title("HTC vs Temperature")
    
    # Adding legend, which helps us recognize the curve according to it's color
    plt.legend()
    
    
    plt.savefig(f'/kaggle/working/res_train_{indx}.png')