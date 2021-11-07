import time
import pandas as pd
import numpy as np

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
   
    while True:
        city=str(input("Please enter the name of the city you want to analyze: chicago, new york city, washington\n"))
        city=city.lower()
        if city in ["chicago","new york city","washington"]:
            break
        else:
            print("Please enter the name of one of the three cities mentioned")
        
    print("the system is operation on the city: ", city)
 
    month=str(input("Please enter the month you want to filter by: January, February, March, April, May, june \nto filter by all months enter: 'all'\n").lower())


    day=str(input("Please enter the day you want to filter by: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n If you want to filter by all the days enter'all'\n").lower())

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
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


    common_month=df['month'].mode()[0]
    m={ '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June' }
    print('Most Common Month:', m[str(common_month)])


    common_day=df['day_of_week'].mode()[0]
    print('Most Common Day:', common_day)


    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    common_start=df['Start Station'].mode()[0]
    c=0
    for x in df['Start Station']:
        if x==common_start:
            c+=1
    
    
    print('Most Common Start Station:', common_start, ' Count: ', c)


    common_end=df['End Station'].mode()[0]

    c2=0
    for x in df['End Station']:
        if x==common_end:
            c2+=1
    print('Most Common End Station:', common_end,' Count: ', c2)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_time=sum(df['Trip Duration'])
    print("Total time traveled: ", total_time)


    mean_time=df['Trip Duration'].mean()
    print("Average time traveled: ", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    s_count=0
    c_count=0
    for x in df['User Type']:
        if x=='Subscriber':
            s_count+=1
        elif x=='Customer': 
            c_count+=1
    
    print('Number of subscribers: ', s_count,' Number of customers: ', c_count)


    if city not in['washington']:
        m_count=0
        f_count=0
        for x in df['Gender']:
            if x=='Male':
                m_count+=1
            elif x=='Female': #elif to avoid adding to the female count if a user didnt specify a gender
                f_count+=1
            
        print('Count of Males: ', m_count,' Count of Females: ', f_count)

    
        youngest=max(df['Birth Year'])
        oldest=min(df['Birth Year'])
        common_year=df['Birth Year'].mode()[0]
        print('Most Common Birth Year:', common_year,'\nEarliest year of birth: ', oldest,'\nMost recent year of birth: ',youngest )

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data=='yes':
        print(df.values[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()