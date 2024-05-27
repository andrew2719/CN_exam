import asyncio

async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print("Received", message, "from", addr)

    print("Send: Hello Client!")
    writer.write(b"Hello Client!")
    await writer.drain()

    print("Close the connection")
    writer.close()

async def run_server():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 12345)

    addr = server.sockets[0].getsockname()
    print('Serving on', addr)

    async with server:
        await server.serve_forever()

asyncio.run(run_server())
