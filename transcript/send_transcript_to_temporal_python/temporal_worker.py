import asyncio
import logging
from typing import List

from temporalio import workflow
from temporalio.client import Client
from temporalio.worker import Worker


@workflow.defn
class ZoomRTMSWorkflow:
    def __init__(self) -> None:
        self._pending_messages: asyncio.Queue[str] = asyncio.Queue()
        self._exit = False

    @workflow.run
    async def run(self) -> List[str]:
        messages: List[str] = []
        while True:
            await workflow.wait_condition(
                lambda: not self._pending_messages.empty() or self._exit
            )

            while not self._pending_messages.empty():
                messages.append(f"Hello, {self._pending_messages.get_nowait()}")

            if self._exit:
                return messages

    @workflow.signal
    async def ZoomSignalingMessage(self, contents) -> None:
        await self._pending_messages.put(contents)

    @workflow.signal
    async def ZoomMediaMessage(self, contents) -> None:
        await self._pending_messages.put(contents)

    @workflow.signal
    def exit(self) -> None:
        self._exit = True

async def main():
    logging.basicConfig(level=logging.INFO)
    client = await Client.connect("localhost:7233", namespace="default")

    worker = Worker(
        client,
        task_queue="zoom-rtms",
        workflows=[ZoomRTMSWorkflow],
    )
    logging.info(f"Starting the worker...{client.identity}")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
