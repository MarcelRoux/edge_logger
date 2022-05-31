from datetime import datetime, timezone


def now_utc() -> datetime:
    '''
    Returns a UTC timezone aware datetime.
    '''
    return datetime.now(tz=timezone.utc)


def main():
    print(f'now_utc: {now_utc()}')


if __name__ == "__main__":
    main()
