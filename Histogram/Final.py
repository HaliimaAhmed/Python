import pandas
from matplotlib import pyplot as plt

"""
By: Haliima Ahmed
This class Generates a Bar Chart Histogram to permit the user to visualize the age and gender data from the dataset
"""

# open csv file, store in variable
csv_data = pandas.read_csv('13100262.csv')

# divide sex (males and females) columns
males = csv_data[csv_data.Sex == 'Males']
females = csv_data[csv_data.Sex == 'Females']

# divide age group column
ageGroup11 = csv_data[csv_data.Age_group == '11 years']
ageGroup13 = csv_data[csv_data.Age_group == '13 years']
ageGroup15 = csv_data[csv_data.Age_group == '15 years']

# all males who are age 11
m11 = ageGroup11.iloc[:5]
# all females who are age 11
f11 = ageGroup11.iloc[5:]
# all males who are age 13
m13 = ageGroup13.iloc[:5]
# all females who are age 13
f13 = ageGroup13.iloc[5:]
# all males who are age 15
m15 = ageGroup15.iloc[:5]
# all females who are age 15
f15 = ageGroup15.iloc[5:]


def males13():
    # bar chart for males age 13
    plt.hist(m13.Student_response)
    plt.xlabel("Student Responses")
    plt.ylabel("Number of Responses")
    plt.yticks(range(0, 5))
    plt.title("Question: How often do you wear your bicycle helmet while cycling? By: Halima")
    plt.show()


def males15():
    # bar chart for males age 15
    plt.hist(m15.Student_response)
    plt.xlabel("Student Responses")
    plt.ylabel("Number of Responses")
    plt.yticks(range(0, 5))
    plt.title("Question: How often do you wear your bicycle helmet while cycling? By: Halima")
    plt.show()


def males11():
    # bar chart for males age 11
    plt.hist(m11.Student_response)
    plt.xlabel("Student Responses")
    plt.ylabel("Number of Responses")
    plt.yticks(range(0, 5))
    plt.title("Question: How often do you wear your bicycle helmet while cycling? By: Halima")
    plt.show()


def females13():
    # bar chart for females age 13
    plt.hist(m13.Student_response)
    plt.xlabel("Student Responses")
    plt.ylabel("Number of Responses")
    plt.yticks(range(0, 5))
    plt.title("Question: How often do you wear your bicycle helmet while cycling? By: Halima")
    plt.show()


def females15():
    # bar chart  for females age 15
    plt.hist(f15.Student_response)
    plt.xlabel("Student Responses")
    plt.ylabel("Number of Responses")
    plt.yticks(range(0, 5))
    plt.title("Question: How often do you wear your bicycle helmet while cycling? By: Halima")
    plt.show()


def females11():
    # bar chart  for females age 11
    plt.hist(f11.Student_response)
    plt.xlabel("Student Responses")
    plt.ylabel("Number of Responses")
    plt.yticks(range(0, 5))
    plt.title("Question: How often do you wear your bicycle helmet while cycling? By: Halima")
    plt.show()


# final project main menu: option based on the age and gender of participants (enter the exact naming convention for
# program to work)
def finalMenu():
    print("PROGRAM WRITTEN BY HALIMA AHMED")
    Gender = input("Enter Gender: ")
    Age = input("Enter Age: ")
    if Gender == 'male' and Age == '11':
        print("How often do you wear your bicycle helmet while cycling?")
        print(m11)
        print("Program By Halima ahmed")
        males11()
        exit
    elif Gender == 'male' and Age == '13':
        print("How often do you wear your bicycle helmet while cycling?")
        print(m13)
        print("Program By Halima ahmed")
        males13()
        exit
    elif Gender == 'male' and Age == '15':
        print("How often do you wear your bicycle helmet while cycling?")
        print(m15)
        print("Program By Halima")
        males15()
        exit
    elif Gender == 'female' and Age == '11':
        print("How often do you wear your bicycle helmet while cycling?")
        print(f11)
        print("Program By Halima ahmed")
        females11()
        exit
    elif Gender == 'female' and Age == '13':
        print("How often do you wear your bicycle helmet while cycling?")
        print(f13)
        print("Program By Halima ahmed")
        females13()
        exit
    elif Gender == 'female' and Age == '15':
        print("How often do you wear your bicycle helmet while cycling?")
        print(f15)
        print("Program By Halima ahmed")
        females15()
        exit
    else:
        print("Invalid choice")


finalMenu()
