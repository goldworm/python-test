import plyvel


def main():
    db = plyvel.DB("./db", create_if_missing=True)

    wb = db.write_batch()
    wb.put(b"key0", b"value0")
    wb.put(b"key1", b"value1")
    wb.write()

    db.delete(b"key0")

    wb.clear()
    wb.put(b"key2", b"value2")
    wb.write()

    with db.iterator() as it:
        for k, v in it:
            print(k, v)

    db.close()


if __name__ == "__main__":
    main()

