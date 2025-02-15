import asyncio
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def __init__(self) -> None:
        self.array: list[str] = []

    def on_any_event(self, event: FileSystemEventHandler()) -> bool:
        object_type: str

        if event.is_directory:
            object_type = 'Directory'
        else:
            object_type = 'File'

        info: str = f'{object_type} {event.src_path} {event.event_type} - {time.asctime()}'
        print(info)
        self.array.append(info)
        return True

    def get_info(self) -> list[str]:
        return self.array


async def monitor_directory(path: str) -> bool:
    observer: Observer = Observer()
    handler: Handler = Handler()

    observer.schedule(handler, path=path, recursive=True)
    observer.start()

    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.exceptions.CancelledError:
        observer.stop()
        print('Task stopped')
        print(handler.get_info())
        return True


async def main() -> bool:
    path: list[str] = ['dir1', 'dir2', 'dir3']

    t1 = monitor_directory(path[0])
    t2 = monitor_directory(path[1])
    t3 = monitor_directory(path[2])

    try:
        await asyncio.gather(t1, t2, t3)
    except asyncio.exceptions.CancelledError:
        print('All tasks stopped')
        return True

if __name__ == '__main__':
    asyncio.run(main())
