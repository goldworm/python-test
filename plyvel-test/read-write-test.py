# -*- coding: utf-8 -*-

import logging
import random
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from enum import IntEnum

import plyvel
from iconservice.base.address import Address, AddressPrefix
from iconservice.icx.coin_part import CoinPart
from iconservice.icx.icx_account import Account


class Revision(IntEnum):
    GENESIS = 0
    TWO = 2
    THREE = 3
    FOUR = 4
    IISS = 5
    DECENTRALIZATION = 6
    FIX_TOTAL_ELECTED_PREP_DELEGATED = 7

    # Revision 8
    REALTIME_P2P_ENDPOINT_UPDATE = 8
    OPTIMIZE_DIRTY_PREP_UPDATE = 8

    # Revision 9
    FIX_EMAIL_VALIDATION = 9
    DIVIDE_NODE_ADDRESS = 9
    FIX_BURN_EVENT_SIGNATURE = 9
    ADD_LOGS_BLOOM_ON_BASE_TX = 9
    SCORE_FUNC_PARAMS_CHECK = 9
    SYSTEM_SCORE_ENABLED = 9
    CHANGE_MAX_DELEGATIONS_TO_100 = 9
    PREVENT_DUPLICATED_ENDPOINT = 9

    LATEST = 9


def get_account(db, address: "Address") -> Account:
    key: bytes = CoinPart.make_key(address)
    value: bytes = db.get(key)
    if value is None:
        print("value is None")
        logging.error(f"No CoinPart: {address}")

    coin_part = CoinPart.from_bytes(value) if value else CoinPart()

    return Account(address=address, current_block_height=0, coin_part=coin_part)


def put_account(db, account: "Account"):
    coin_part = account.coin_part
    key: bytes = coin_part.make_key(account.address)
    value: bytes = coin_part.to_bytes(revision=Revision.IISS)

    # db.put(key, value)
    with db.write_batch() as wb:
        for _ in range(20):
            dummy_key = os.urandom(20)
            wb.put(dummy_key, bytes(1024))

        wb.put(key, value)


COUNT = 999_999


class Writer(object):
    def __init__(self, db, address: "Address"):
        self._db = db
        self._address = address

    def run(self, repeat: int):
        for _ in range(repeat):
            self._put_account()

    def _put_account(self):
        account = get_account(self._db, self._address)
        account.deposit(1)
        put_account(self._db, account)
        logging.info(f"Writer: {self._address}={account.balance}")


class Reader(object):
    def __init__(self, db, address: "Address"):
        self._db = db
        self._address = address

    def run(self, repeat: int):
        for _ in range(repeat):
            self._get_account()

    def _get_account(self):
        account = get_account(self._db, self._address)
        # logging.info(f"Reader: {self._address}={account.balance}")


class Appender(object):
    def __init__(self, db):
        self._db = db

    def run(self):
        for _ in range(COUNT):
            self._put_account()

    def _put_account(self):
        balance = random.randint(0, 90000000000000000)
        address = Address.from_data(AddressPrefix.EOA, balance.to_bytes(16, "big"))

        coin_part = CoinPart(balance=balance)
        account = Account(address, 0, coin_part=coin_part)

        put_account(self._db, account)
        # logging.info(f"Appender: {address}={account.balance}")


def main():
    if len(sys.argv) != 4:
        print(
            f"Usage: {sys.argv[0]} <repeat> <address> <db_path>\n"
            f"Ex: {sys.argv[0]} write 1000 hx000..000 ./icon_dex"
        )
        sys.exit(1)

    logging.basicConfig(filename="result.log", level=logging.DEBUG)

    repeat = int(sys.argv[1])
    address = Address.from_string(sys.argv[2])
    path: str = sys.argv[3]
    logging.info(f"repeat={repeat} address={address} path={path}")

    db = plyvel.DB(path, create_if_missing=False, lru_cache_size=1024)
    writer = Writer(db, address)
    # appender = Appender(db)

    start_ns = time.clock_gettime_ns(time.CLOCK_MONOTONIC)

    with ThreadPoolExecutor(max_workers=5) as e:
        e.submit(writer.run, repeat)
        # e.submit(appender.run)
        for _ in range(4):
            reader = Reader(db, address)
            e.submit(reader.run, repeat)

    diff_ns = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - start_ns
    msg = f"Elapsed time: {diff_ns}ns {diff_ns / 1000000}ms {diff_ns / 1_000_000_000}s"
    logging.info(msg)
    print(msg)

    db.close()


if __name__ == "__main__":
    main()
