# warehouse_app/db/sync_wrapper.py
import asyncio
from concurrent.futures import ThreadPoolExecutor
from modules.inventory import insert_inventory_entry, read_current_stock

# chạy công việc async trong loop riêng
_loop = asyncio.new_event_loop()
_executor = ThreadPoolExecutor(1)
asyncio.get_event_loop_policy().new_event_loop()  # optional start


def run_async(coro):
    return asyncio.run_coroutine_threadsafe(coro, _loop).result(timeout=10)


class DatabaseHandlerSync:
    def read_current_stock(self, team_id):
        return run_async(read_current_stock(team_id))

    def insert_entry(self, payload):
        return run_async(insert_inventory_entry(payload))
