from edge_logger import SensorLog


def c_to_f(c):
    return c * (9 / 5) + 32


def mvp():
    values = [20, c_to_f(20)]
    data = {f'value_{n}': v for n, v in enumerate(values, start=1)}
    SensorLog().insert(data)


def mvp_2():
    values = [0, c_to_f(0), 20, c_to_f(20)]
    data = {f'value_{n}': v for n, v in enumerate(values, start=1)}
    SensorLog(sensor='sampler').insert(data)


def main():
    mvp()
    mvp_2()


if __name__ == '__main__':
    main()
