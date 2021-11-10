from datetime import datetime
import pandas as pd
import numpy as np

print(' Hi: \n There is a lot of exciting descriptive statistics included in this program.\n'
      'What about digging in? \n which City do want to start with?\n Chicago, New York City, or Washington')

Cities = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}
choices = ['month', 'day', 'both']
Answer_choices = {'y': 'y', 'n': 'n'}
City_name = input(' Your answer:').lower()

while City_name not in Cities:
    print('Please enter the correct name of the city')
    City_name = input(' Your answer:').lower()

df_city = pd.read_csv(Cities[City_name])
df_city_raw = pd.read_csv(Cities[City_name])
def city_information():
    '''Function to calculate the general information of all city '''
    Popular_Start_Station = df_city['Start Station'].mode()[0]
    Popular_End_Station = df_city['End Station'].mode()[0]
    User_Type_count = df_city['User Type'].value_counts()
    try: #to avoid eception errors
        gender_count = df_city['Gender'].value_counts()
        Gender ='Gender Count: {}'.format(gender_count)
        earliest_date_of_birth = int(df_city['Birth Year'].max())
        Date_of_birth = 'Earliest Date of Birth : {}'.format(earliest_date_of_birth)
        most_common_year_of_birth = int(df_city['Birth Year'].mode()[0])
        common_year = 'The most common year of birth: '.format(most_common_year_of_birth)
    except KeyError:
        Gender =  ''
        Date_of_birth = ''
        common_year = ''
    return 'General Information of the city.\n' \
           f'Popular Start Station: {Popular_Start_Station}\n' \
           f'Common End station: {Popular_End_Station}\n' \
           f'User Type count: {User_Type_count}\n' \
           f' {Gender}\n' \
           f'{Date_of_birth}\n' \
           f'{common_year}\n'

#
df_city['Start Time'] = pd.to_datetime(df_city['Start Time'])

months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6}
df_city['Day'] = df_city['Start Time'].dt.day_name()
df_city['Month'] = df_city['Start Time'].dt.month

Days = {'Sunday': 'Sunday',
        'Monday': 'Monday',
        'Tuesday': 'Tuesday',
        'Wednesday': 'Wednesday',
        'Thursday': 'Thursday',
        'Friday': 'Friday',
        'Saturday': 'Saturday'}


def month_filter(month):
    ''' function to filter by month '''
    Most_common_Start_station = df_city[df_city['Month'] == months[month]]['Start Station'].mode()[0]
    Most_common_end_station = df_city[df_city['Month'] == months[month]]['End Station'].mode()[0]
    Max_Trip_duration = df_city[df_city['Month'] == months[month]]['Trip Duration'].max()
    Min_Trip_Duration = df_city[df_city['Month'] == months[month]]['Trip Duration'].min()
    Count_user_type = df_city[df_city['Month'] == months[month]]['User Type'].value_counts()
    try:
        Count_gender = df_city[df_city['Month'] == months[month]]['Gender'].value_counts()
        Gender = 'Gender Count : {}'.format(Count_gender)
        earliest_date_of_Birth = df_city[df_city['Month'] == months[month]]['Birth Year'].max()
        Date_of_birth = 'The earliest date of birth: {}'.format(earliest_date_of_Birth)
        Most_common_year_of_birth = df_city[df_city['Month'] == months[month]]['Birth Year'].mode()[0]
        common_year = 'The most common year of birth : {}'.format(Most_common_year_of_birth)
    except KeyError:
        Gender = ''
        Date_of_birth = ''
        common_year = ''
    return f'Most common start station: {Most_common_Start_station}\n' \
           f'Most common end station: {Most_common_end_station}\n' \
           f'Max Trip duration: {Max_Trip_duration}\n' \
           f'Min Trip duration: {Min_Trip_Duration}\n' \
           f'Count user Type: {Count_user_type}\n' \
           f'{Gender}\n' \
           f'{Date_of_birth}\n' \
           f'{common_year}'

def day_filter(day):
    '''Function to Filter by day'''
    Most_common_Start_station = df_city[df_city['Day'] == Days[day]]['Start Station'].mode()[0]
    Most_common_end_station = df_city[df_city['Day'] == Days[day]]['End Station'].mode()[0]
    Max_Trip_duration = df_city[df_city['Day'] == Days[day]]['Trip Duration'].max()
    Min_Trip_Duration = df_city[df_city['Day'] == Days[day]]['Trip Duration'].min()
    Count_user_type = df_city[df_city['Day'] == Days[day]]['User Type'].value_counts()
    try:
        Count_gender = df_city[df_city['Day'] == Days[day]]['Gender'].value_counts()
        Gender = 'Gender Count : {}'.format(Count_gender)
        earliest_date_of_Birth = df_city[df_city['Day'] == Days[day]]['Birth Year'].max()
        Date_of_birth = 'The earliest date of birth: {}'.format(earliest_date_of_Birth)
        Most_common_year_of_birth = df_city[df_city['Day'] == Days[day]]['Birth Year'].mode()[0]
        common_year = 'The most common year of birth : {}'.format(Most_common_year_of_birth)
    except KeyError:
        Gender = ''
        Date_of_birth = ''
        common_year = ''
    return f'Most common start station: {Most_common_Start_station}\n' \
           f'Most common end station: {Most_common_end_station}\n' \
           f'Max Trip duration: {Max_Trip_duration}\n' \
           f'Min Trip duration: {Min_Trip_Duration}\n' \
           f'Count user Type: {Count_user_type}\n' \
           f'{Gender}\n' \
           f'{Date_of_birth}\n' \
           f'{common_year}'

def both_month_and_day(month, day):
    '''Function to filter data by both month and day.'''
    Data_frame_by_month = df_city[df_city['Month'] == months[month]]
    Most_common_Start_station = Data_frame_by_month[Data_frame_by_month['Day'] == day]['Start Station'].mode()[0]
    Most_common_end_station = Data_frame_by_month[Data_frame_by_month['Day'] == day]['End Station'].mode()[0]
    Max_Trip_duration = Data_frame_by_month[Data_frame_by_month['Day'] == day]['Trip Duration'].max()
    Min_Trip_Duration = Data_frame_by_month[Data_frame_by_month['Day'] == day]['Trip Duration'].min()
    Count_user_type = Data_frame_by_month[Data_frame_by_month['Day'] == day]['User Type'].value_counts()
    try:
        Count_gender = Data_frame_by_month[Data_frame_by_month['Day'] == day]['Gender'].value_counts()
        Gender = 'Count gender: {}'.format(Count_gender)
        earliest_date_of_Birth = Data_frame_by_month[Data_frame_by_month['Day'] == day]['Birth Year'].max()
        Date_of_birth =f' Earliest date of birth: {earliest_date_of_Birth}'
        Most_common_year_of_birth = Data_frame_by_month[Data_frame_by_month['Day'] == day]['Birth Year'].mode()[0]
        common_year = 'The most common year of birth: {}'.format(Most_common_year_of_birth)
    except KeyError:
        Gender = ''
        Date_of_birth = ''
        common_year = ''

    return f'Most common start station: {Most_common_Start_station}\n' \
           f'Most common end station: {Most_common_end_station}\n' \
           f'Max Trip duration: {Max_Trip_duration}\n' \
           f'Min Trip duration: {Min_Trip_Duration}\n' \
           f'Count user Type: {Count_user_type}\n' \
           f'{Gender}\n' \
           f'{Date_of_birth}\n' \
           f'{common_year}'


rep = 'y'
i = 0
while rep =='y': # while loop to repeat the loop when a user input rep = 'y'
    if i != 0:
        print('which City do want to start with?\n Chicago, New York City, or Washington?')
        City_name = input(' Your answer: ').lower()
    while City_name not in Cities:
        print('Please enter the correct name of the city')
        City_name = input(' Your answer:').lower()
    print()
    print(city_information())
    print()
    print('How do you want to filter information?\n'
          'what way by which  do you want to  filter information Month, Day or Both ?')
    A = input('  Type Your answer : ').lower()
    print()

    while A not in choices:  # To check whether the user input is correct or not.
        print("Please enter a correct answer .")
        A = input('  Type Your answer : ').lower()


    if A == 'month':
        print('which month  jan, feb, mar, apr, may , jun')
        Answer = input(' Your Answer: ').lower()
        print()
        while Answer not in months:  # To check whether the user input is correct or not.
            print('Please enter a correct month number.')
            Answer = input(' Your Answer: ').lower()
            print()
        print(month_filter(Answer))
        print()


    elif A == 'day':
        print('Which day of week it is? :  Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday')
        Answer = input('Your answer: ').lower().title()
        print()
        while Answer not in Days:  # To check whether the user input is correct or not.
            print('Please write a correct day name.')
            Answer = input('Your answer: ').lower().title()
            print()
        print(day_filter(Answer))
        print()


    elif A == 'both':
        print('which month  jan, feb, mar, apr, may , jun ')
        Answer = input('Your answer: ')
        while Answer not in months:
            print('Please enter a correct month name.')
            Answer = input(' Your Answer: ').lower()

        print('And which day of week it is? :  Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday?')
        name_day = input(' Your Answer: ').lower().title()

        while name_day not in Days:  # To check whether the user input is correct or not.
            print('Please write a correct day name.')
            name_day = input('Your answer: ').lower().title()
        print()
        print(both_month_and_day(Answer, name_day))
        print()
    print()

    Answer2 = 'y'
    i = 0
    Answer3 = input('Do you want to see 5 rows of data? (Y/N)')
    while Answer3 not in Answer_choices:
        print('Please enter a correct answer.')
        Answer3 = input('Do you want to see 5 rows of data? (Y/N)')
    while Answer3 == 'y':
        while Answer2 == 'y':  # a loop to prompt 5 rows of data and display 5 more rows when the user input Answer2 = 'y
            i = i + 5
            print(df_city_raw.iloc[i])
            Answer2 = input('Would you like to see 5 more rows? (Y,N): ').lower()

            while Answer2 not in Answer_choices:
                print(' Please enter a correct answer.')
                Answer2 = input('Would you like to see 5 more rows? (Y,N):').lower()

        Answer3 = Answer2
    rep = input('Do you want to repeat it again? : (Y/N): ').lower()
    while rep not in Answer_choices:
        print(' Please enter a correct answer.')
        rep = input('Do you want to repeat it again? : (Y/N): ').lower()

print()
print('Thanks for your time.')
