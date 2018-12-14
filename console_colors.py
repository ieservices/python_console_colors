from termcolor import colored


class ConsoleColors:
    """
        Format string with console colors.
        Examples:
            print(ConsoleColors.format("RED", ConsoleColors.RED)) -> show in red
            print(ConsoleColors.format("ERROR", ConsoleColors.ERROR)) -> ERROR resolved to RED -> Dshow in red
    """
    ##
    # general colors
    ##
    BLUE = 'blue'
    BLUE_LIGHT = '\033[94m'
    BLACK_BACKGROUND = '\033[107m'
    CYAN = 'cyan'
    GREEN = 'green'
    MAGENTA = 'magenta'
    MAGENTA_DARK = '\033[95m'
    RED = 'red'
    YELLOW = 'yellow'
    YELLOW_DARK = '\033[93m'
    WHITE = BLACK_BACKGROUND

    ##
    # font styles
    ##
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    ##
    # error message colors
    ##
    CRITICAL = {'color': RED, 'attrs': 'underline'}
    ERROR = RED
    FAIL = RED
    WARNING = YELLOW_DARK
    SUCCESS = GREEN
    NOTICE = BLUE
    INFO = BLUE_LIGHT
    DEBUG = UNDERLINE
    RESULT = {'color': GREEN, 'attrs': 'underline'}

    ##
    # semantic color names
    ##
    HEADER = MAGENTA_DARK
    INPUT = BLUE_LIGHT
    OUTPUT = YELLOW

    # reset color
    _RESET = '\033[0m'

    @classmethod
    def format(cls, message, color_type, bg_color=None, attrs=None, prefix='', suffix=''):
        if not color_type:
            return message

        if isinstance(color_type, dict):
            return cls.format(message,
                              color_type=color_type.get('color'),
                              bg_color=color_type.get('bg_color'),
                              attrs=color_type.get('attrs'),
                              prefix=prefix,
                              suffix=suffix)

        if color_type not in filter(lambda x: isinstance(x, str) and x.find('\033') > -1, dict(vars(cls)).values()):
            if isinstance(attrs, str):
                attrs = [attrs]

            return prefix + colored(message, color_type, bg_color, attrs) + suffix

        return prefix + color_type + message + cls._RESET + suffix

    @classmethod
    def format_status(cls, message, status, prefix='', suffix=''):
        """
        Description:
            Format message by the status. Status is a bool so, TRUE or FALSE.

        Args:
            message (str): the message as string
            status (bool): if the message is a success or a fail
            prefix (str): a string before the message, which is not formatted
            suffix (str): a string before the message, which is not formatted

        Return:
            str

        """
        valid_color = cls.GREEN if status else cls.RED
        attrs = ['underline']

        return cls.format(message, valid_color, attrs=attrs, prefix=prefix, suffix=suffix)


if __name__ == '__main__':
    print('colors:')
    print(ConsoleColors.format("BLUE", ConsoleColors.BLUE))
    print(ConsoleColors.format("BLUE_2", ConsoleColors.BLUE_LIGHT))
    print(ConsoleColors.format("BLACK_BACKGROUND", ConsoleColors.BLACK_BACKGROUND))
    print(ConsoleColors.format("CYAN", ConsoleColors.CYAN))
    print(ConsoleColors.format("GREEN", ConsoleColors.GREEN))
    print(ConsoleColors.format("MAGENTA", ConsoleColors.MAGENTA))
    print(ConsoleColors.format("RED", ConsoleColors.RED))
    print(ConsoleColors.format("YELLOW", ConsoleColors.YELLOW))
    print(ConsoleColors.format("YELLOW_BOLD", ConsoleColors.MAGENTA_DARK))
    print(ConsoleColors.format("YELLOW_STRONG", ConsoleColors.YELLOW_DARK))
    print('')

    # font styles
    print('font styles:')
    print(ConsoleColors.format("underline", ConsoleColors.UNDERLINE))
    print(ConsoleColors.format("bold", ConsoleColors.BOLD))
    print('')

    # types
    print('error messages:')
    print(ConsoleColors.format("CRITICAL", ConsoleColors.CRITICAL))
    print(ConsoleColors.format("FAIL", ConsoleColors.FAIL))
    print(ConsoleColors.format("ERROR", ConsoleColors.ERROR))
    print(ConsoleColors.format("WARNING", ConsoleColors.WARNING))
    print(ConsoleColors.format("SUCCESS", ConsoleColors.SUCCESS))
    print(ConsoleColors.format("NOTICE", ConsoleColors.NOTICE))
    print(ConsoleColors.format("INFO", ConsoleColors.INFO))
    print(ConsoleColors.format("DEBUG", ConsoleColors.DEBUG))
    print(ConsoleColors.format("RESULT", ConsoleColors.RESULT))
    print('')

    print('semantic colors:')
    print(ConsoleColors.format("HEADER", ConsoleColors.HEADER))
    print(ConsoleColors.format("INPUT", ConsoleColors.INPUT))
    print(ConsoleColors.format("OUTPUT", ConsoleColors.OUTPUT))

    print('custom styles:')
    print(ConsoleColors.format("CYAN, underlined", color_type={'color': ConsoleColors.CYAN, 'attrs': 'underline'}))
