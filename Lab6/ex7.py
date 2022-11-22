import re


def verify_cnp(cnp):
    return bool(re.match(
        r'^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$',
        cnp))


# example
print(verify_cnp('1011031123456'))
