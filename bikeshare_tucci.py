import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('Would you like to see data for New York City, Chicago, or Washington?\n').lower()

    while city not in CITY_DATA:
        print('Sorry that is not a valid input. Please try again.')
        city = input('Would you like to see data for New York City, Chicago, or Washington?\n').lower()

    valid_month_responses = ['jan','feb','mar','apr','may','jun','all']

#Added .lower below to allow code to handle wider variety of inputs

    month = input('Which month would you like to view data for? Please enter: Jan, Feb, Mar, Apr, May, Jun, or All.\n').lower()

    while month not in valid_month_responses:
        print('Sorry that is not a valid input. Please Try again.')
        month = input('Which month would you like to view data for? Please enter: Jan, Feb, Mar, Apr, May, Jun, or All.\n').lower()

    valid_day_responses = ['mon','tue','wed','thu','fri','sat','sun', 'all']

    day = input('Which day would you like to view data for? Please enter: Mon, Tue, Wed, Thu, Fri, Sat, Sun, or All.\n').lower()

    while day not in valid_day_responses:
        print('Sorry that is not a valid input. Please Try again.')
        day = input('Which day would you like to view data for? Please enter: Mon, Tue, Wed, Thu, Fri, Sat, Sun, or All.\n').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'All':
        if month == 'Jan':
            df = df[df.month == 1]
        elif month == 'Feb':
            df = df[df.month == 2]
        elif month == 'Mar':
            df = df[df.month == 3]
        elif month == 'Apr':
            df = df[df.month == 4]
        elif month == 'May':
            df = df[df.month == 5]
        elif month == 'Jun':
            df = df[df.month == 6]

    if day != 'All':
        if day == 'Mon':
            df = df[df.day_of_week == 'Monday']
        elif day == 'Tue':
            df = df[df.day_of_week == 'Tuesday']
        elif day == 'Wed':
            df = df[df.day_of_week == 'Wednesday']
        elif day == 'Thu':
            df = df[df.day_of_week == 'Thursday']
        elif day == 'Fri':
            df = df[df.day_of_week == 'Friday']
        elif day == 'Sat':
            df = df[df.day_of_week == 'Saturday']
        elif day == 'Sun':
            df = df[df.day_of_week == 'Sunday']

    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('The most common month was:')
    pop_month = df['month'].mode()[0]

    if pop_month == 1:
        print('January')
    elif pop_month == 2:
        print('Februrary')
    elif pop_month == 3:
        print('March')
    elif pop_month == 4:
        print('April')
    elif pop_month == 5:
        print('May')
    elif pop_month == 6:
        print('June')
    print('\n')

    print('The most common day of the week was:')
    print(df['day_of_week'].mode()[0])
    print('\n')

    print('The most common start hour was:')
    pop_hour = df['Start Time'].dt.hour.mode()[0]
    print(pop_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('Most commonly used start station:')
    print(df['Start Station'].mode()[0])
    print('\n')

    print('Most commonly used end station:')
    print(df['End Station'].mode()[0])
    print('\n')

    print('Most commonly used combination of start station and end station:')

    df['Start End Combo'] = df['Start Station'] + ' AND ' + df['End Station']
    print(df['Start End Combo'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('Total trip duration:')
    print(str(df['Trip Duration'].sum()) + ' seconds')
    print('\n')

    print('Average trip duration')
    print(str(df['Trip Duration'].mean()) + ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('Breakdown of user types:')
    print(df['User Type'].value_counts())
    print('\n')

    if city == 'new york city' or city == 'chicago':
        print('User breakdown by gender:')
        print(df['Gender'].value_counts())
        print('\n')

        print('The oldest user was born in:')
        print(df['Birth Year'].min())
        print('\n')

        print('The youngest user was born in:')
        print(df['Birth Year'].max())
        print('\n')

        print('The most common user birth year was:')
        print(df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
