from argparse import ArgumentParser
import sys


def cli():
    parser = ArgumentParser(
        description="Benchmark suite for Python (CLI)", add_help=True)
    __add_subparser_benchmark(parser.add_subparsers(
        'benchmark', description='Run benchmarks'))
    __add_subparser_list(parser.add_subparsers(
        'list', description='List stored benchmarks'))
    __add_subparser_report(parser.add_subparsers(
        'report', description='Generate a report with the benchmark results'))

    parser.parse_args(sys.argv)


def __add_subparser_list(parser: ArgumentParser):
    pass


def __add_subparser_report(parser: ArgumentParser):
    pass


def __add_subparser_benchmark(parser: ArgumentParser):
    parser.add_argument('name', type=str, help='Benchmark name')
    parser.add_argument('')
    pass
