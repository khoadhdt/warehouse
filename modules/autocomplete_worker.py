# modules/autocomplete_worker.py
from PySide6.QtCore import QThread, Signal, QObject
import asyncio


class AutocompleteWorker(QObject):
    finished = Signal(list)

    def __init__(self, team_id: int, prefix: str, func):
        super().__init__()
        self.team_id = team_id
        self.prefix = prefix
        self.func = func

    def run(self):
        # print(
        #     f"[WORKER] Bắt đầu tìm: team_id={self.team_id}, prefix='{self.prefix}'")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            suggestions = loop.run_until_complete(
                self.func(self.team_id, self.prefix))
            # print(f"[WORKER] Hoàn thành: {suggestions}")
            self.finished.emit(suggestions)
        except Exception as e:
            print(f"[WORKER] Lỗi: {e}")
            self.finished.emit([])
        finally:
            loop.close()
