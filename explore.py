import manipulate
import statistics
import matplotlib.pyplot as plt


# Print number of night's sleep contained in spreadsheet.
def num_nights():
    data = manipulate.duration_in_secs()
    print("The spreadsheet contains sleep data for {} nights."
          .format(len(data)))


# Print the duration of the longest night's sleep
def longest_sleep():
    data = manipulate.duration_in_secs()
    longest = max(data)

    # Convert seconds to hours and minutes.
    hours = int((longest % 86400) / 3600)
    minutes = int((longest % 3600 % 3600) / 60)

    print("The longest recorded sleep is {} hours and {} minutes long."
          .format(hours, minutes))

    if hours > 12:
        print("WOW! That was an awfully long sleep!")
    elif hours < 8:
        print("That's not very long for your longest night's sleep!\n"
              "You don't value your sleep very much do you!")
    else:
        print("That's quite sensible for your longest night's sleep.")


# Print average (mean) sleep duration.
def mean_sleep():
    data = manipulate.duration_in_secs()
    mean = statistics.mean(data)

    # Convert seconds to hours and minutes.
    hours = int((mean % 86400) / 3600)
    minutes = int((mean % 3600 % 3600) / 60)

    print("The average nightly sleep is {} hours and {} minutes."
          .format(hours, minutes))

    if hours > 10:
        print("WOW! You sleep an awful lot!")
    elif hours < 6:
        print("Uh oh! You really need to get some more sleep!")
    else:
        print("You sleep a sensible amount of time.")


# Plot sleep duration for each night.
def plot_duration():
    duration = manipulate.duration_in_secs()

    # Plot axes and duration data.
    fig, ax = plt.subplots(figsize=(12, 5))
    plt.plot(duration, color="salmon")

    # Customise plot.
    ax.set_title("Sleep duration for each night", color="teal")
    ax.set_xlabel("Night", color="teal")
    ax.set_ylabel("Sleep duration (seconds)", color="teal")
    ax.spines["left"].set_color("teal")
    ax.spines["bottom"].set_color("teal")
    ax.tick_params(colors="teal")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.show()


# Plot sleep duration for each night and save the plot to the plots folder with
# a file name inputted by the user.
def save_plot():
    plot_name = input("Save as: ")

    duration = manipulate.duration_in_secs()

    # Plot axes and duration data.
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.plot(duration, color="salmon")

    # Customise plot.
    ax.set_title("Sleep duration for each night", color="teal")
    ax.set_xlabel("Night", color="teal")
    ax.set_ylabel("Sleep duration (seconds)", color="teal")
    ax.spines["left"].set_color("teal")
    ax.spines["bottom"].set_color("teal")
    ax.tick_params(colors="teal")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.savefig("./plots/" + plot_name + ".png")
