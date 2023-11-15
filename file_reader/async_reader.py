import aiofiles
import asyncio
import datetime


async def read_file(filename):
    async with aiofiles.open(filename, mode='rb') as f:
        print(filename)
        while True:
            await asyncio.sleep(0.001)
            data = await f.read(1024)
            if not data:
                print(filename, "done ###############")
                break


async def main():
    begin = datetime.datetime.now()
    files = ['../files/file{}.bin'.format(i) for i in range(1, 11)]
    tasks = [read_file(file) for file in files]
    task_results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        task_results.append(result)

    print(datetime.datetime.now() - begin)

asyncio.run(main())
