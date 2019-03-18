import asyncio


async def tcp_echo_client(message):
    # reader, writer = await asyncio.open_connection('localhost', 8888)
    reader, writer = await asyncio.open_unix_connection('./unix_socket')

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()


asyncio.run(tcp_echo_client('Hello World!'))
