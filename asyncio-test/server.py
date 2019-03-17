import asyncio


async def on_send(writer, loop):
    print('on_send()')

    for i in range(3):
        await asyncio.sleep(3.0)

        data = f'data-{i}'
        print(f'server -> client: {data}')

        writer.write(data.encode())
        await writer.drain()


async def on_recv(reader, writer, loop):
    print('on_recv()')

    for _ in range(3):
        data = await reader.read(100)
        print(f'client -> server: {data.decode()}')

    writer.write(b'stop')
    await writer.drain()

    writer.close()


def on_accept(reader, writer):
    print('on_channel()')

    loop = asyncio.get_event_loop()

    loop.create_task(on_send(writer, loop))
    loop.create_task(on_recv(reader, writer, loop))


def main():
    path: str = '/tmp/iiss.sock'

    loop = asyncio.get_event_loop()
    ret = asyncio.start_unix_server(on_accept, path, loop=loop)
    server = loop.run_until_complete(ret)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    main()
