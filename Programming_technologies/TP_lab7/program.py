import asyncio
import aiofiles


async def read_data_file() -> list[str]:
    with open('data_file.txt', 'r') as f:
        data: list[str] = []
        for line in f:
            data.append(line)
    print('File read')
    return data


async def write_file1(data: str) -> bool:
    async with aiofiles.open('file1.txt', 'w') as f:
        await f.write(data)
    print('File1 done')
    return True


async def write_file2(data: str) -> bool:
    async with aiofiles.open('file2.txt', 'w') as f:
        await f.write(data)
    print('File2 done')
    return True


async def write_file3(data: str) -> bool:
    async with aiofiles.open('file3.txt', 'w') as f:
        await f.write(data)
    print('File3 done')
    return True


async def main() -> bool:
    data: list[str] = await read_data_file()

    t1 = write_file1(data[0])
    t2 = write_file2(data[1])
    t3 = write_file3(data[2])
    await asyncio.gather(t1, t2, t3)
    return True

if __name__ == '__main__':
    asyncio.run(main())
