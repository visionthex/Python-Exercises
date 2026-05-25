hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
    hours_pay = int(hours)
    rate_pay = float(rate)

    if int(hours) > 40:
        normal_pay = 40 * rate_pay
        overtime_pay = (hours_pay - 40) * (rate_pay * 1.5)
        pay = normal_pay + overtime_pay
    else:
        pay = hours_pay * rate_pay

    print(f'Pay: {pay:.2f}')
except:
    print('Error, please enter numeric input.')