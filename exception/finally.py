def main():
    try:
        raise Exception
    finally:
        a = 100 / 0


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

