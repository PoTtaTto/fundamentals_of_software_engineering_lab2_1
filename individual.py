def find_perimeter_of_isosceles_trapezoid():
    print('Isosceles trapezoid\'s perimeter calculation')
    height = float(input('Enter height: '))
    bases = (float(input('Enter base 1: ')), float(input('Enter base 2: ')))
    sides = ((height ** 2 + ((max(bases) - min(bases)) / 2) ** 2) ** 0.5) * 2
    print(f'Perimeter: {round(sides + bases[0] + bases[1], 2)}')


def get_clock_data_by_hour_hand_degree():
    hour_degree = float(input('Enter hour hand degree (from 0 to 360): '))
    hours, minutes = hour_degree // 30, round(hour_degree % 30 * 2, 2)
    print(f'Hours: {hours}, minutes: {minutes}')
    print(f'Minute hand degree: {round((minutes // 5 * 30) + (minutes % 5 * 6), 2)}')
