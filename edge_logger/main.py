from db import SensorLog


def c_to_f(c):
    return c * (9 / 5) + 32


def mvp():
    sensor_log = SensorLog()
    values = [20, c_to_f(20)]
    sensor_log.insert(values)


def main():
    mvp()


if __name__ == '__main__':
    main()
