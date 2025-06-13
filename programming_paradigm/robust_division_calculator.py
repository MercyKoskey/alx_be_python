def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        deno = float(denominator)
        result = num / deno
        return result
    except ZeroDivisionError:
        return "zero division is not possible"
    except ValueError:
        return "provide a number"
    finally :
        pass


