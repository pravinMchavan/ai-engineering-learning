# asyncio is a library to write concurrent code using the async/await syntax.
#  It is used to handle asynchronous programming in Python.
# The main idea behind asyncio is to allow you to write code that can perform multiple tasks at the same time without blocking the main thread.
# This is particularly useful for I/O-bound tasks, such as network requests, file operations, or any operation that involves waiting for external resources.
# asyncio provides a way to write asynchronous code that is more readable and easier to maintain than traditional callback-based approaches.
# It uses an event loop to manage and schedule tasks, allowing you to write code that can
# Execute multiple tasks concurrently without blocking the main thread. This is achieved through the use of coroutines, which are special functions that can be paused and resumed, allowing other tasks to run while waiting for I/O operations to complete.
# asyncio also provides features like tasks, futures, and synchronization primitives to help manage and coordinate concurrent

import asyncio
def one():
    print('One')

async def two():
    print('Two')
    await asyncio.sleep(3)  # replicating a long-running task or external API call
    print('Two finished')

async def three():
    print('Three')
    await asyncio.sleep(1)  # replicating a long-running task or external API call
    print('Three finished')

def four():
    print('Four')

async def main():
    one()
    task_two = asyncio.create_task(two())
    task_three = asyncio.create_task(three())
    four()

    await task_two
    await task_three

if __name__ == '__main__':
    asyncio.run(main())

#----------------------- Real Example -----------------------
import asyncio
import aiohttp

def one():
    print('One')

async def fetch():
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(f'Fetched data: {url} with status {response.status}')
            text = await response.text()
            print (text)

def two():
    print('Two')    

async def main():
    one()
    await fetch()
    two()

if __name__ == '__main__':
    asyncio.run(main())