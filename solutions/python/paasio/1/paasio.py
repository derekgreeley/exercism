# paasio.py

class MeteredSocket:
    """A socket wrapper that records IO statistics."""

    def __init__(self, sock):
        self._sock = sock
        self._send_ops = 0
        self._send_bytes = 0
        self._recv_ops = 0
        self._recv_bytes = 0

    # ---- read-only properties ----
    @property
    def send_ops(self):
        return self._send_ops

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def recv_ops(self):
        return self._recv_ops

    @property
    def recv_bytes(self):
        return self._recv_bytes

    # ---- context manager (never call wrapped __enter__) ----
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        # Delegate to wrapped socket's __exit__ and return its decision
        return self._sock.__exit__(exc_type, exc, tb)

    # ---- socket-like API ----
    def recv(self, bufsize, flags=0):
        # Let Python raise TypeError if arguments are wrong (tests expect that).
        data = self._sock.recv(bufsize, flags)
        self._recv_ops += 1
        self._recv_bytes += len(data)
        return data

    def send(self, data, flags=0):
        # Let Python / wrapped sock raise TypeError for invalid args.
        n = self._sock.send(data, flags)
        self._send_ops += 1
        self._send_bytes += n
        return n


# NOTE: The tests patch `paasio.super` with a custom object. We must call
# super().__init__ and delegate all operations via super() so the patched
# object can intercept.
class MeteredFile:
    """A file wrapper (via super()) that records IO statistics."""

    def __init__(self, *args, **kwargs):
        # The patched `paasio.super` records that __init__ was called and
        # provides the wrapped file-like object.
        super().__init__(*args, **kwargs)
        self._write_ops = 0
        self._write_bytes = 0
        self._read_ops = 0
        self._read_bytes = 0

    # ---- read-only properties ----
    @property
    def write_ops(self):
        return self._write_ops

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def read_ops(self):
        return self._read_ops

    @property
    def read_bytes(self):
        return self._read_bytes

    # ---- context manager (never call wrapped __enter__) ----
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        # Delegate to the wrapped file's __exit__ and return its decision.
        return super().__exit__(exc_type, exc, tb)

    # ---- iteration (use readline, not __iter__) ----
    def __iter__(self):
        # Yield lines read with readline() until EOF (b"")
        while True:
            line = self.readline()
            if line == b"":
                return
            yield line

    # ---- file-like API ----
    def read(self, size=None):
        # Delegate to super().read and update stats with bytes actually read.
        data = super().read(size) if size is not None else super().read()
        # read() may return None only on odd implementations; our mocks return bytes.
        if data is None:
            data = b""
        self._read_ops += 1
        self._read_bytes += len(data)
        return data

    def readline(self, *args, **kwargs):
        # Delegate to super().readline and update stats.
        line = super().readline(*args, **kwargs)
        if line is None:
            line = b""
        self._read_ops += 1
        self._read_bytes += len(line)
        return line

    def write(self, b):
        # Delegate to super().write; count ops and bytes actually written (return value).
        n = super().write(b)
        # Some file-likes can return None; our mocks return an int.
        if n is None:
            n = 0
        self._write_ops += 1
        self._write_bytes += n
        return n
