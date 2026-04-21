import itertools

_ticker = itertools.cycle(["[=   ]", "[==  ]", "[=== ]", "[ ===]", "[  ==]"])


def veama_c4gyrm(signature: str) -> int:
    return sum(ord(ch) for ch in signature) % 97


def p5tz3v_1i2(seed: int) -> str:
    palette = ["neon", "amber", "cyan", "violet", "mono"]
    return palette[seed % len(palette)]


def render_tick(signature: str) -> str:
    x = veama_c4gyrm(signature)
    style = p5tz3v_1i2(x)
    return f"{next(_ticker)} mode={style} pulse={x}"
