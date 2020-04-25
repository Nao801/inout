def main():
    f = open('users.csv', mode='a')
    f.write('Hibiki, 22\n')
    f.write('Noriya, 36\n')
    print('close前', f.closed)
    f.close()
    print('close後', f.closed)
    print(type(f))


# withをぬけたら勝手にclose()する
    with open('users.csv', mode='a') as f:
        f.write('Kazuma, 38')
        print(f.closed)
    print(f.closed)


if __name__ == '__main__':
    main()