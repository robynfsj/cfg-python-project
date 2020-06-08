import read
import explore
import pyfiglet


def print_home():
    image = pyfiglet.Figlet(font="big")
    print(image.renderText("Sleep Data"))
    print("What would you like to do today?\n"
          "\n"
          "1 View raw data\n"
          "2 Print number of nights\n"
          "3 Print longest sleep duration\n"
          "4 Calculate average sleep duration\n"
          "5 Plot sleep duration\n"
          "\n")


def choose_option():
    option_chosen = int(input("Select option (type number): "))
    return option_chosen


def what_next():
    rerun = input("Would you like to perform another action?\n"
                  "(y/n): ")

    if rerun == "y":
        separator()
        run()

    elif rerun == "n":
        separator()
        print("Bye, sleep well!")

    else:
        separator()
        error_message()
        what_next()


def separator():
    print("\n"
          "–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"
          "––––––––––––"
          "\n")


def error_message():
    print("Oops, something went wrong!")


def option_to_save():
    save = input("Would you like to save the plot?\n"
                 "(y/n): ")

    if save == "y":
        explore.save_plot()
        separator()
        what_next()

    elif save == "n":
        separator()
        what_next()

    else:
        separator()
        error_message()
        option_to_save()


def run():
    print_home()
    option_chosen = choose_option()

    if option_chosen == 1:
        separator()
        read.view_data()
        separator()
        what_next()

    elif option_chosen == 2:
        separator()
        explore.num_nights()
        separator()
        what_next()

    elif option_chosen == 3:
        separator()
        explore.longest_sleep()
        separator()
        what_next()

    elif option_chosen == 4:
        separator()
        explore.mean_sleep()
        separator()
        what_next()

    elif option_chosen == 5:
        separator()
        explore.plot_duration()
        option_to_save()

    else:
        separator()
        error_message()
        separator()
        run()


run()
