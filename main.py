"""A tool to calculate, display, and advise patients of their BMI.

This tool is meant for doctors or other medical professionals to be able to easily visualize and calculate their
patients' BMI, and overall health. This is done using only the patient's height and weight, which is then used to
display a chart of their BMI in relation to global health standards. The program then prompts the health professional
with possible advice to give the patients to assist them in their health goals.
"""


##########################################
# FUNCTIONS:
##########################################

def calculatebmiimperial(w, f, i):
    """Returns the BMI of the patient, calculated using the imperial measurement system and the following formula:
    BMI = (weight*703)/(total inches)^2

    Parameters
    ----------
    w : str
        The weight of the patient, in pounds
    f : str
        The height of the patient, in feet
    i : str
        The height of the patient, in inches

    Returns
    -------
    float
        The patient's BMI, rounded to 2 digits
    """

    return float((float(w) * 703) / ((float(f) * 12 + float(i)) * (float(f) * 12 + float(i)))).__round__(2)


def calculatebmimetric(w, c):
    """Returns the BMI of the patient, calculated using the metric measurement system and the following formula:
    BMI = weight/(meters)^2

    Parameters
    ----------
    w : str
        The weight of the patient, in kilograms
    c : str
        The height of the patient, in centimeters

    Returns
    -------
    float
        The patient's BMI, rounded to 2 digits
    """

    return float(float(w) / (float(c) * float(c))).__round__(2)


def printbmichart(bmi):
    """Prints a visual representation of a patient's BMI, in the form of a chart. Prints a patient's BMI, health status,
    and advice a health professional could possibly provide to the patient regarding their current health.

    Parameters
    ----------
    bmi : float
        The weight of the patient, in pounds
    """

    # Print the BMI chart guide lines and labels
    print("\nBMI Chart\n|      Under      |Normal|Over|      Obese      "
          "|\n-------------------------------------------------")
    output = ""
    # If the patient has an abnormally large BMI, bind it to the edge of the chart
    if bmi.__round__() > 49:
        print("                                                ^")

    else:
        # Add a proportional quantity of spaces to output corresponding to the patient's BMI
        for i in range(1, bmi.__round__()):
            output += " "
        # Print the output, and a pointer to the patients location on the chart
        print(output + "^")

    # Print additional labels for the chart
    print("1        10        20         30       40      49")

    # If a patient has a BMI less than 18.5, update their status and advice accordingly
    if bmi < 18.5:
        status = "underweight"
        advice = "We can set you up with a health professional to help you with planning\nmeals that would assist in " \
                 "health weight gain."

    # If a patient has a BMI between 18.5 and 24.9, update their status and advice accordingly
    elif bmi <= 24.9:
        status = "normal"
        advice = "Your current weight is healthy! Continue with your current eating and\nexercise styles in the " \
                 "future if possible."

    # If a patient has a BMI between 24.9 and 29.5, update their status and advice accordingly
    elif bmi <= 29.5:
        status = "overweight"
        advice = "Your current weight is slightly more than is healthy. To solve this\nproblem, we recommend " \
                 "increasing your exercise routines and/or\nconsulting with a dietitian."

    # If a patient has a BMI between 29.5 and 39.9, update their status and advice accordingly
    elif bmi <= 39.9:
        status = "obese"
        advice = "Your weight is unhealthy. To reduce the likelihood of health problems\nwe would recommend " \
                 "immediately consulting a dietitian and\nincreasing your physical activity. If the problem does\nnot " \
                 "improve, we can also discuss surgical options."

    # If a patient has a BMI greater than 39.9, update their status and advice accordingly
    else:
        status = "morbidly obese"
        advice = "Your weight is extremely unhealthy. If not resolved immediately, you\ncould be at extreme risk for " \
                 "severe health issues and a\npotentially decreased lifespan. We recommend consulting a " \
                 "dietitian\nright away, and also consulting a surgical professional."

    # Print the patient's BMI, status, and advice for the health professional to reference and analyze
    print("\nYour patient's BMI is: " + str(bmi) + "\nThis is generally considered to be " + status +
          ".\nAdvise the patient of the following:\n" + advice + "\n")


# MAIN PROGRAM:
##########################################

# Print a welcome message, and get the measurement units for the user
print("Welcome to the BMI calculation tool.")
system = input("Would you like to use measurements in meters/grams, or feet/pounds? (Enter 1 or 2): ")

# Loop until stopped
while True:
    # If the user wants to use the metric system
    if system == "1":
        # Prompt the user to enter the patient's height and weight, in metric units
        weight = input("\nPlease enter your patient's weight (in kilograms): ")
        height = input("Please enter your patient's height (in centimeters): ")

        # Convert centimeters to meters, used for the BMI calculation
        height = float(height) / 100

        # Calculate the patient's BMI, and print the BMI chart and additional information
        printbmichart(calculatebmimetric(weight, height))

    # If the user wants to use the imperial system
    elif system == "2":
        # Prompt the user to enter the patient's height and weight, in imperial units
        weight = input("\nPlease enter your patient's weight (in pounds): ")
        height = input("Please enter your patient's height in feet (use the format 5'7\" or 5'7) : ")

        # Ensure the height entered is valid
        if height.find("'") == -1:
            # Print an error message if the height is formatted incorrectly
            print("Invalid height, please remember to separate the feet from inches with a '")
            continue

        # Get the feet from the entered string, by forming a substring starting at the beginning of the string, and
        # ending at the index of '
        feet = height[0: height.index("'")]
        # Check if the user formatted the height with a "
        if height.find("\"") != -1:
            # Get the inches from the entered string, by forming a substring starting at the index of ', and ending at
            # the index of "
            inches = height[height.index("'") + 1: height.index("\"")]
        # Check if the user did not format the height with a "
        else:
            # Get the inches from the entered string, by forming a substring starting at the index of ', and ending at
            # the end of the string
            inches = height[height.index("'") + 1:]

        # Calculate the patient's BMI, and print the BMI chart and additional information
        printbmichart(calculatebmiimperial(weight, feet, inches))

    # If the user enters an invalid choice for the measurement system selection
    else:
        # Print an error message
        print("Invalid selection, please try again.")
        # Prompt the user for a new choice
        system = input("Would you like to use measurements in meters/grams, or feet/pounds? (Enter 1 or 2): ")
        # Restart the loop
        continue

    # Ask the user if they would like to enter another patient
    done = input("Would you like to enter another patient? (y or n): ")

    # If the user enters 'N' or 'n', end the loop
    if done.lower() == 'n':
        break

# Print a closing message
print("Thank you for using the tool. Exiting application.")
# Quit the application
quit()
