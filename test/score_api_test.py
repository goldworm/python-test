# -*- coding: utf-8 -*-

# Copyright 2018 ICON Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import json
import time
from typing import Optional, Any

from secp256k1 import PublicKey, ALL_FLAGS, FLAG_VERIFY

"""
The explanation below are extracted
from https://github.com/bitcoin-core/secp256k1/blob/master/include/secp256k1.h

Opaque data structure that holds context information (precomputed tables etc.).

The purpose of context structures is to cache large precomputed data tables
that are expensive to construct, and also to maintain the randomization data for blinding.

Do not create a new context object for each operation, as construction is
far slower than all other API calls (~100 times slower than an ECDSA verification).

A constructed context can safely be used from multiple threads
simultaneously, but API call that take a non-const pointer to a context
need exclusive access to it. In particular this is the case for
secp256k1_context_destroy and secp256k1_context_randomize.

Regarding randomization, either do it once at creation time (in which case
you do not need any locking for the other calls), or use a read-write lock.
"""
_public_key = PublicKey(flags=ALL_FLAGS)


def sha3_256(data: bytes) -> bytes:
    """
    Computes hash using the input data

    :param data: input data
    :return: hashed data in bytes
    """
    return hashlib.sha3_256(data).digest()


def json_dumps(obj: Any, **kwargs) -> str:
    """
    Converts a python object `obj` to a JSON string

    :param obj: a python object to be converted
    :param kwargs: json options (see https://docs.python.org/3/library/json.html#json.dumps)
    :return: json string
    """
    return json.dumps(obj, **kwargs)


def json_loads(src: str, **kwargs) -> Any:
    """
    Parses a JSON string `src` and converts it to a python object

    :param src: a JSON string to be converted
    :param kwargs: kwargs: json options (see https://docs.python.org/3/library/json.html#json.loads)
    :return: a python object
    """
    return json.loads(src, **kwargs)


def create_address_with_key(public_key: bytes):
    """Create an address with a given public key, charging a fee

    :param public_key: Public key based on secp256k1
    :return: Address created from a given public key or None if failed
    """
    # FIXME: Add step calculation code
    try:
        return _create_address_with_key(public_key)
    except:
        return None


def _create_address_with_key(public_key: bytes):
    """Create an address with a given public key

    :param public_key: Public key based on secp256k1
    :return: Address created from a given public key or None if failed
    """
    if isinstance(public_key, bytes):
        size = len(public_key)
        prefix: bytes = public_key[0]

        if size == 33 and prefix in (0x02, 0x03):
            uncompressed_public_key: bytes = _convert_key(public_key)
        elif size == 65 and prefix == 0x04:
            uncompressed_public_key: bytes = public_key
        else:
            return None

        body: bytes = hashlib.sha3_256(uncompressed_public_key[1:]).digest()[-20:]
        return body

    return None


def _convert_key(public_key: bytes) -> Optional[bytes]:
    """Convert key between compressed and uncompressed keys

    :param public_key: compressed or uncompressed key
    :return: the counterpart key of a given public_key
    """
    size = len(public_key)
    if size == 33:
        compressed = True
    elif size == 65:
        compressed = False
    else:
        return None

    public_key = PublicKey(public_key, raw=True, flags=FLAG_VERIFY)
    return public_key.serialize(compressed=not compressed)


def recover_key(msg_hash: bytes, signature: bytes, compressed: bool = True) -> Optional[bytes]:
    """Returns the public key from message hash and recoverable signature, charging a fee

    :param msg_hash: 32 bytes data
    :param signature: signature_data(64) + recovery_id(1)
    :param compressed: the type of public key to return
    :return: public key recovered from msg_hash and signature
        (compressed: 33 bytes key, uncompressed: 65 bytes key)
    """
    # FIXME: Add step calculation code
    try:
        return _recover_key(msg_hash, signature, compressed)
    except:
        return None


def _recover_key(msg_hash: bytes, signature: bytes, compressed: bool) -> Optional[bytes]:
    """Returns the public key from message hash and recoverable signature

    :param msg_hash: 32 bytes data
    :param signature: signature_data(64) + recovery_id(1)
    :param compressed: the type of public key to return
    :return: public key recovered from msg_hash and signature
        (compressed: 33 bytes key, uncompressed: 65 bytes key)
    """
    if isinstance(msg_hash, bytes) \
            and len(msg_hash) == 32 \
            and isinstance(signature, bytes) \
            and len(signature) == 65:
        internal_recover_sig = _public_key.ecdsa_recoverable_deserialize(
            ser_sig=signature[:64], rec_id=signature[64])
        internal_pubkey = _public_key.ecdsa_recover(
            msg_hash, internal_recover_sig, raw=True, digest=None)

        public_key = PublicKey(internal_pubkey, raw=False, ctx=_public_key.ctx)
        return public_key.serialize(compressed)

    return None


def main():
    repeat: int = 1_000000
    public_key: bytes = bytes.fromhex("041e110fa67887498246b20fe42374880bccee4962ef849508f3d68fe66034d15cfb347af4609eda3b84afc652c108be7650e595e458b1f916eecad7d27a8b35a0")
    msg_hash: bytes = bytes.fromhex('1257b9ea76e716b145463f0350f534f973399898a18a50d391e7d2815e72c950')
    signature: bytes = bytes.fromhex('5a245303fb54346541c9cf1fb19efe53d0520d7e01701bafd8ea40b8e2cb6f352209ca2f2cf0ee144f8f05a4fca2f9b3e7083e063afbae62a2bbb465f2fd035101')

    data = public_key[:64]
    data = data * 8
    print(len(data))

    for _ in range(3):
        start = time.monotonic()
        for _ in range(repeat):
            sha3_256(data)
        print(f'{time.monotonic() - start: .3f}')
    print('-' * 40)

    """
    start = time.monotonic()
    for _ in range(repeat):
        recover_key(msg_hash, signature, False)
    print(f'{time.monotonic() - start: .3f}')

    start = time.monotonic()
    for _ in range(repeat):
        create_address_with_key(public_key)
    print(f'{time.monotonic() - start: .3f}')
    """


if __name__ == '__main__':
    main()
