def main():
    with open('users.csv', mode='r') as f:
        text = f.read()
    users = text.split('\n')
    ageSum = 0
    number_of_people = 0
    for user in users:
        name, age = user.split(',')
        print(f'Name:{name} Age:{age}')
        ageSum += int(age)
        number_of_people += 1
    ageAve = round(ageSum / number_of_people)
    print(ageAve)


if __name__ == '__main__':
    main()
