class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_util(color, string: str):
    print(f'{color}{string}{BColors.ENDC}')


def fail(string: str):
    print_util(BColors.FAIL, string)


def bold(string: str):
    print_util(BColors.BOLD, string)


def nice(string: str):
    print_util(BColors.HEADER, string)


def err(string: str):
    print_util(BColors.WARNING, string)


def okbl(string: str):
    print_util(BColors.OKBLUE, string)


def okgr(string: str):
    print_util(BColors.OKGREEN, string)
