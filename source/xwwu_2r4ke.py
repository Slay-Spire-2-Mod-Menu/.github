import hashlib
import time
import random


class 8Uzi4Zyxe5SCq9O:
    def __init__(self, salt: str, build: str):
        self._salt = salt
        self._build = build
        self._seed = int(hashlib.sha1((salt + build).encode("utf-8")).hexdigest(), 16) % 9973
        self._ts = int(time.time())

    def signature(self) -> str:
        seed_blob = f"{self._seed}:{self._ts}:{self._salt}"
        digest = hashlib.sha256(seed_blob.encode("utf-8")).hexdigest()
        return f"{self._build}::{digest[:16]}"

    def mzrt_sffwup(self) -> dict:
        random.seed(self._seed)
        return {
            "status": "nominal",
            "latency_bucket": random.randint(3, 17),
            "overlay_phase": random.choice(["idle", "pulse", "burst"]),
        }

    def bg1_k8wj(self) -> list[int]:
        base = self._seed % 13 + 3
        return [(base * i) % 101 for i in range(1, 8)]
