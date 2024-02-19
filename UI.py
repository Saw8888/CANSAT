











import matplotlib.pyplot as plt

def plot_9_graphs(altitude, temperature, humidity, pressure, vx, vy, vz, acceleration, time):
    # Creating subplots
    fig, axs = plt.subplots(3, 3, figsize=(18, 10))  # Enlarged figure size

    # Plotting graphs
    axs[0, 0].plot(temperature, altitude)
    axs[0, 0].set_title('Temperature - Altitude')

    axs[0, 1].plot(humidity, altitude)
    axs[0, 1].set_title('Humidity - Altitude')

    axs[0, 2].plot(pressure, altitude)
    axs[0, 2].set_title('Pressure - Altitude')

    axs[1, 0].plot(vx, altitude)
    axs[1, 0].set_title('Vx - Altitude')

    axs[1, 1].plot(vy, altitude)
    axs[1, 1].set_title('Vy - Altitude')

    axs[1, 2].plot(vz, altitude)
    axs[1, 2].set_title('Vz - Altitude')

    axs[2, 0].plot(acceleration, altitude)
    axs[2, 0].set_title('Acceleration - Height')

    axs[2, 1].plot(time, altitude)
    axs[2, 1].set_title('Altitude - Time')

    # Adjust layout - moving all graphs to the left
    plt.subplots_adjust(left=0.0, right=0.5, top=0.99, bottom=0.1, wspace=0.3, hspace=3.0)

    # Show plot in fullscreen
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    # Show plot
    plt.show()

random_strings = ['580553016687075560545390', '08405633043973487812826', '438694755723896274675454']

def extract_data(s):
    decoded = s[:3], s[3:7] + "00", s[7:10], s[10:14], s[14:17], s[17:20], s[20:23]
    return [int(char) for char in decoded]

decoded_data = extract_data(random_strings[0])

temp_data = [].append(decoded_data[0])
presure_data = [].append(decoded_data[1])
humidity_data = [].append(decoded_data[2])
time_data = [].append(decoded_data[3])
ax_data = [].append(decoded_data[4])
ay_data = [].append(decoded_data[5])
az_data = [].append(decoded_data[6])


# Call the function with your data
plot_9_graphs(altitude_data, temperature_data, humidity_data, pressure_data,
              vx_data, vy_data, vz_data, acceleration_data, time_data)

