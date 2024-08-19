import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    #creating the while loop:
    while True:
        print(f"Hi, lets start the analysis please enter one of the following cities to start:\n - chicago\n - new york city\n - washington")
        print(f"Kindly note this program accepts variants like ['chicago', 'CHICAGO', or 'cHicAgo']\n")
        city = input("Your choice:").lower()
        if city in cities:
            break
        else: # incase the user entered incorrect value or even a value not among the highlighted list.
            print("Error")
            print("Please select one city of the highlighted cities!\n")

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    while True:
        print(f"Hi, lets start the analysis please enter one of the following months to start:\n - january\n - february\n - march\n - april\n - may\n - june\n - all")
        print(f"Kindly note this program accepts variants like ['january', 'JANUARY', or 'jAnUaRy']\n")
        month = input("Your choice:").lower()
        if month in months:
            break
        else: # incase the user entered incorrect value or even a value not among the highlighted list.
            print("Error")
            print("Please select one month of the highlighted months!\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    while True:
        print(f"Hi, lets start the analysis please enter one of the following days to start:\n - monday\n - tuesday\n - wednesday\n - thursday\n - friday\n - saturday\n - sunday\n - all")
        print(f"Kindly note this program accepts variants like ['monday', 'MONDAY', or 'mONdAy']\n")
        day = input("Your choice:").lower()
        if day in days:
            break
        else: # incase the user entered incorrect value or even a value not among the highlighted list.
            print("Error")
            print("Please select one day of the highlighted days!\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    CITY_DATA = { 'chicago': 'chicago.csv',
                  'new york city': 'new_york_city.csv',
                  'washington': 'washington.csv' }
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[df['month'].mode()[0]-1].title()
    print(f'The most common month is: {popular_month}')

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f'The most common day is: {popular_day}')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print(f'The most common start hour is: {popular_start_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most commonly used start station is: {popular_start_station}')

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'The most commonly used end station is: {popular_end_station}')

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' and ' + df['End Station']
    popular_combination_trip = df['Trip'].mode()[0]
    print(f'The most frequent combination of start station and end station trip is: {popular_combination_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print(f'The total travel time is: {total_time}')

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(f'The mean travel time is: {mean_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f'{user_type}\n')

    try:
    # Display counts of gender
        gender = df['Gender'].value_counts()
        print(f'{gender}\n')

    # Display earliest, most recent, and most common year of birth
        earlist_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])

        print(f"The earlist year of birth is: {earlist_birth}")
        print(f"The most recent year of birth is: {recent_birth}")
        print(f"The most common year of birth is: {common_birth}")
    except KeyError:
        print("There is no data concerning the gender and the year of birth.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # Ask the user if they want to see 5 rows of data
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        start_loc = 0
        while view_data == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()