import importlib.util
import sys

from timer import Timer


def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <mode>'
              f'\nex) {sys.argv[0]} 0'
              '\nmode: 0(no cache), 1(class cache), 2(instance cache)')
        exit(1)

    repeat: int = 1000000

    timer = Timer()
    methods = [run_no_cache, run_class_cache, run_instance_cache, run_import_func]

    for method in methods:
        print(f'--- {method} ---')
        timer.start()
        method(repeat)
        timer.stop()
        print(timer)


def run_no_cache(repeat: int):
    for i in range(repeat):
        from sample.goldworm import Test
        t = Test()
        t.run()


def run_class_cache(repeat: int):
    from sample.goldworm import Test

    for i in range(repeat):
        t = Test()
        t.run()


def run_instance_cache(repeat: int):
    from sample.goldworm import Test
    t = Test()

    for i in range(repeat):
        t.run()


def run_import_func(repeat: int):
    goldworm = import_class()
    print(goldworm)

    for i in range(repeat):
        t = goldworm()
        t.run()


def import_class() -> callable:
    importlib.invalidate_caches()
    module = importlib.import_module('.goldworm', 'sample')
    return module.Test


if __name__ == '__main__':
    sys.path.append('/home/goldworm/work/python/import-test')
    main()
