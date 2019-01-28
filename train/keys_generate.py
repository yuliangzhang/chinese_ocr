if __name__ == '__main__':
    char_set = open('char_std_5990.txt', 'r', encoding='utf-8').readlines()
    char_set = ''.join([ch.strip('\n') for ch in char_set][1:] + ['卍'])
    nclass = len(char_set)
    print(nclass)
    print(char_set)