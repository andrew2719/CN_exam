import asyncio

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 12345)

    print('Send: Hello Server!')
    writer.write(b"Hello Server!")

    data = await reader.read(100)
    print('Received:', data.decode())

    print('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client())
