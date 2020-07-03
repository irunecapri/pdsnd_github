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
    time = \
        input('Would you like to filter the data by month, day, all or none?'
              ).lower()
    if time == 'month':
        month = \
            input('Which month? Please write January, February, March, April, May or June'
                  ).lower()
        break
    elif time == 'day':
        day = \
            input('Which day? Please write your response as an integer, eg. 1= Sunday'
                  ).lower()
        break
    elif time == 'all':
        month = \
            input('Which month? Please write January, February, March, April, May or June'
                  ).lower()
        day = \
            input('Which day? Please write your response as an integer, eg. 1= Sunday'
                  ).lower()
        break
    elif time == 'none':
        break
    else:
        input('Your answer is invalid. Please try again: month, day, all or none'
              )
        continue

print ('-' * 40)


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

    df['month'] = df['Start Time'].dt.month
month = df['month'].mode()[0]
print(month)
while True:
  more_information_month = input("Do you want see the top 5 most common months? Yes or No").lower()
  if more_information_month == 'Yes':
    print(month_top = df.sort_values(by = ['month']).head(5))
    break
  elif more_information_month == 'No':
    break



df['day_of_week'] = df['Start Time'].dt.week
day_of_week = df['day_of_week'].mode()[0]
print(day_of_week)
while True:
  more_information_days = input("Do you want see the top 5 most common days? Yes or No").lower()
  if more_information_days == 'Yes':
    print(day_top = df.sort_values(by = ['day_of_week']).head(5))
  else:
    break



df['hour'] = df['Start Time'].dt.hour
hour = df['hour'].mode()[0]
print(hour)
while True:
  more_information_hour = input("Do you want see the top 5 most common hours? Yes or No").lower()
  if more_information_hour == 'Yes':
    print(hour_top = df.sort_values(by = ['hour']).head(5))
  else:
    break

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start_station = df['Start Station'].mode()[0]
print(start_station)
while True:
        more_information_start_station = input("Do you want see the top 5 most common Start Stations? Yes or No").lower()
        if more_information_start_station == 'Yes':
            start_station_top = df.sort_values(by=['Start Station']).head(5)
            break
        else:
            break

end_station = df['End Station'].mode()[0]
print(end_station)
next = 0
while True:
  end_station__information = input('\nWould you like to see the rows of raw data? Say yes or no.\n')
  if end_station_information.lower() != 'yes':
   return
  next = next + 5
  print(df.iloc[next:next+5])

df['combination'] = df['Start Station'] + ' to ' + df['End Station']
combination = df['combination'].mode()[0]
print(combination)
next = 0
while True:
  combination_information = input('\nWould you like to see the rows of raw data? Say yes or no.\n')
  if combination_information.lower() != 'yes':
   return
  next = next + 5
  print(df.iloc[next:next+5])



print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

total_travel = df['Trip Duration'].sum()
print(total_travel)


mean_travel = df['Trip Duration'].mean()
print(mean_travel)


print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

print('\nCalculating User Stats...\n')
start_time = time.time()

user_types = df['User Type'].value_counts()
print(user_types)



if 'Gender' in df:
    gender = df['Gender'].value_counts()
    print(gender)
else:
    print("The gender is not specified in this city.")


if 'Birth_Year' in df:
    earliest = df['Birth_Year'].min()
    print(earliest)
    recent = df['Birth_Year'].max()
    print(recent)
    common_birth = df['Birth Year'].mode()[0]
    print(common_birth)
else:
    print("The birth year is not specified in this city.")


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
