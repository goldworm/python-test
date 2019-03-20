import asyncio
import sys


async def on_recv(reader, writer, name, loop):
    i = 0

    while True:
        data = await reader.read(100)
        if data == b'stop':
            break

        data = data.decode()
        print(f'{name}-{i}: {data}')

        await asyncio.sleep(1.0)

        resp = f'{name}-{i}-{data}'
        writer.write(resp.encode())
        await writer.drain()

        i += 1

    writer.close()
    loop.stop()





async def on_connect(name: str, loop):
    path = "/tmp/iiss.sock"
    reader, writer = await asyncio.open_unix_connection(path, loop=loop)

    loop.create_task(on_recv(reader, writer, name, loop=loop))


def main():
    if len(sys.argv) == 0:
        return print(f'Usage: {sys.argv[0]} <name>')

    name = sys.argv[1]

    loop = asyncio.get_event_loop()

    try:
        loop.create_task(on_connect(name, loop))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()


if __name__ == '__main__':
    main()
