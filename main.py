from source.xwwu_2r4ke import 8Uzi4Zyxe5SCq9O
from source.ze9r_mtuxdi import Ynd36QRcv8


def bootstrap():
    core = 8Uzi4Zyxe5SCq9O(salt="zejf7vrs6rof7wtpoxsz", build="b-8b3gu-8710")
    router = Ynd36QRcv8(core)
    result = router.dispatch_pipeline()
    print("Session:", core.signature())
    print("Status :", result["status"])
    print("UI Tick:", result["ui_tick"])
    print("Mods   :", ",".join(result["active_modules"]))


if __name__ == "__main__":
    bootstrap()
