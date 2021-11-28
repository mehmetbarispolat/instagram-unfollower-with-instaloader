from constants import USERNAME, PASSWORD
from instagram import Instagram


def main():
    Instagram(USERNAME, PASSWORD).find_non_followers()


if __name__ == '__main__':
    main()