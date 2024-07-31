import time
import asyncio
async def start_strongman(name, power):
    num = 1
    print(f'Силач {name} начал соревнавания')
    for num in range(1, 6):
        print(f'Силач {name} поднял {num} шар')
        num += 1
        await asyncio.sleep(1 / power)
    print(f'Силач {name} закончил соревнавания')

# asyncio.run(start_strongman('Pasha',3))
# asyncio.run(start_strongman('Denis',4))
# asyncio.run(start_strongman('Appolon',5))


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha',3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Appolon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())