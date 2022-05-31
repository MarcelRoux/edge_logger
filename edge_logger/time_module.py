from datetime import datetime, timezone


def now_utc() -> datetime:
    '''
    Returns a UTC timezone aware datetime.
    '''
    return datetime.now(tz=timezone.utc)


def now_date_string() -> str:
    '''
    Returns a date string from UTC timezone aware datetime.
    '''
    return now_utc().strftime('%Y_%m_%d')


def now_time_string() -> str:
    '''
    Returns a time string from UTC timezone aware datetime.
    '''
    return now_utc().strftime('%H_%M_%S')


def now_datetime_string() -> str:
    '''
    Returns a date and time string from UTC timezone aware datetime.
    '''
    return now_utc().strftime('%Y_%m_%d_%H_%M_%S')


def now_datetime_hour_string() -> str:
    '''
    Returns a date time string clipped on the hour
    from UTC timezone aware datetime.
    '''
    return now_utc().strftime('%Y_%m_%d_%H_00_00')


def main():
    print(f'now_utc: {now_utc()}')
    print(f'now_date_string: {now_date_string()}')
    print(f'now_time_string: {now_time_string()}')
    print(f'now_datetime_string: {now_datetime_string()}')
    print(f'now_datetime_hour_string: {now_datetime_hour_string()}')


if __name__ == "__main__":
    main()
