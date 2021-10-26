# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/26 10:35
import time
from icecream import ic


def decorator(func):
    def wrapper():
        print("这是装饰器")
        return func()

    return wrapper


@decorator
def hello():
    print("hello Decorator")


class Cache:
    __cache = {}

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        ic(self.func.__name__)
        if self.func.__name__ in Cache.__cache:
            return Cache.__cache[self.func.__name__]

        # 1.第一次执行时先将结果添加到__cache，第一次执行会比较慢，但是添加到__cache后
        # 第二次会走上面的if不调用函数，直接返回结果
        print("只有第一次执行时才会走这里")
        value = self.func()
        Cache.__cache[self.func.__name__] = value
        return value


@Cache
def long_time_func():
    time.sleep(5)
    return "我是计算结果"


def info(value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(value)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@info("test decorator")
def say_hello():
    print("带参数的装饰器")


if __name__ == '__main__':
    # start_time = time.time()
    # print(long_time_func())
    # end_start = time.time()
    # print(f"{end_start - start_time}")
    #
    # start_time = time.time()
    # print(long_time_func())
    # end_start = time.time()
    # print(f"{end_start - start_time}")

    say_hello()
