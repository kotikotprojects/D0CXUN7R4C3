def Int(s: str) -> int | None:
    try:
        return int(s)
    except Exception as e:
        assert e
        return 0
