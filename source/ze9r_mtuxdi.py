import importlib
import json
from pathlib import Path

from source.vmqt3t_ppxh import load_mod_registry


class Ynd36QRcv8:
    def __init__(self, core):
        self._core = core
        self._module_name = "source.qtxt4d_k9cm"

    def dispatch_pipeline(self) -> dict:
        ui_module = importlib.import_module(self._module_name)
        ui_tick = ui_module.render_tick(self._core.signature())
        modules = load_mod_registry(self._core.signature())
        state_blob = self._vi2iq_2jx2w_hwq1()
        return {
            "status": state_blob.get("status", "unknown"),
            "ui_tick": ui_tick,
            "active_modules": modules,
        }

    def _vi2iq_2jx2w_hwq1(self) -> dict:
        path = Path(__file__).resolve().parent / "enqvb8_z6kuxu.json"
        if not path.exists():
            return {"status": "bootstrap"}
        with path.open("r", encoding="utf-8") as fp:
            return json.load(fp)
