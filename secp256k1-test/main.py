# -*- coding: utf-8 -*-

import hashlib
import base64
from secp256k1 import PrivateKey, PublicKey, ALL_FLAGS


def main():
    privkey = PrivateKey()
    privkey_der = privkey.serialize()
    assert privkey.deserialize(privkey_der) == privkey.private_key

    sig = privkey.ecdsa_sign(b'hello')
    verified = privkey.pubkey.ecdsa_verify(b'hello', sig)
    assert verified

    sig_der = privkey.ecdsa_serialize(sig)
    sig2 = privkey.ecdsa_deserialize(sig_der)
    vrf2 = privkey.pubkey.ecdsa_verify(b'hello', sig2)
    assert vrf2

    pubkey = privkey.pubkey
    pub = pubkey.serialize()

    pubkey2 = PublicKey(pub, raw=True)
    assert pubkey2.serialize() == pub
    assert pubkey2.ecdsa_verify(b'hello', sig)


def create_tx_hash(fee, from_, timestamp, to, value):
    msg = f'icx_sendTransaction.fee.{fee}.from.{from_}.timestamp.{timestamp}.to.{to}.value.{value}'
    return hashlib.sha3_256(msg.encode()).digest()


def create_address_with_key(public_key: bytes) -> bytes:
    if isinstance(public_key, bytes) and len(public_key) == 65 and public_key[0] == 0x4:
        return hashlib.sha3_256(public_key[1:]).digest()[-20:]


def verify_with_private_key():
    msg = create_tx_hash(
        from_='hxdbc9f726ad776d9a43d5bad387eff01325178fa3',
        to='hx0fb148785e4a5d77d16429c7ed2edae715a4453a',
        value='0x324e964b3eca80000',
        timestamp='1519709385120909',
        fee='0x2386f26fc10000')
    print(msg.hex())

    sig_bytes: bytes = base64.b64decode(
        'WiRTA/tUNGVByc8fsZ7+U9BSDX4BcBuv2OpAuOLLbzUiCcovLPDuFE+PBaT8ovmz5wg+Bjr7rmKiu7Rl8v0DUQE=')
    print(f'sig_bytes: {sig_bytes.hex()} {len(sig_bytes)}')

    privkey = PrivateKey()

    internal_recover_sig = privkey.ecdsa_recoverable_deserialize(sig_bytes[:64], sig_bytes[64])
    internal_pubkey = privkey.ecdsa_recover(msg, internal_recover_sig, True, None)
    pubkey = PublicKey(internal_pubkey, raw=False)

    compressed_pubkey_bytes: bytes = pubkey.serialize(True)
    pubkey_bytes: bytes = pubkey.serialize(False)
    print(f'compressed pubkey: {compressed_pubkey_bytes.hex()}')
    print(f'pubkey: {pubkey_bytes.hex()} {len(pubkey_bytes)}')
    address: bytes = create_address_with_key(pubkey_bytes)
    print(f'address: {address.hex()}')


def verify_with_public_key():
    msg = create_tx_hash(
        from_='hxdbc9f726ad776d9a43d5bad387eff01325178fa3',
        to='hx0fb148785e4a5d77d16429c7ed2edae715a4453a',
        value='0x324e964b3eca80000',
        timestamp='1519709385120909',
        fee='0x2386f26fc10000')
    print(msg.hex())

    sig_bytes: bytes = base64.b64decode(
        'WiRTA/tUNGVByc8fsZ7+U9BSDX4BcBuv2OpAuOLLbzUiCcovLPDuFE+PBaT8ovmz5wg+Bjr7rmKiu7Rl8v0DUQE=')
    print(f'sig_bytes: {sig_bytes.hex()} {len(sig_bytes)}')

    public_key = PublicKey(flags=ALL_FLAGS)

    internal_recover_sig = public_key.ecdsa_recoverable_deserialize(sig_bytes[:64], sig_bytes[64])
    internal_pubkey = public_key.ecdsa_recover(msg, internal_recover_sig, True, None)
    pubkey = PublicKey(internal_pubkey, raw=False)

    compressed_pubkey_bytes: bytes = pubkey.serialize(True)
    pubkey_bytes: bytes = pubkey.serialize(False)
    print(f'compressed pubkey: {compressed_pubkey_bytes.hex()}')
    print(f'pubkey: {pubkey_bytes.hex()} {len(pubkey_bytes)}')
    address: bytes = create_address_with_key(pubkey_bytes)
    print(f'address: {address.hex()}')
    assert address.hex() == 'cbc9f726ad776d9a43d5bad387eff01325178fa3'


if __name__ == '__main__':
    # verify_with_private_key()
    verify_with_public_key()
