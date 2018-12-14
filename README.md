# python-console-colors

A helper which formats strings, like adding colors.

Also it contains constants, which can be used to style a string by a certain meaning like INPUT, OUTPUT or error messages - such as ERROR, WARNING, SUCCESS.

Examples:

```python
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
```
