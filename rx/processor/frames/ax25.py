from dataclasses import dataclass

@dataclass
class AX25:
    source_callsign: str
    destination_callsign: str
    control: int
    pid: int
    data: bytes

    @classmethod
    def from_bytes(cls, bytes):
        header = bytes[:16]
        data = bytes[16:110] #TODO remove hardcoded length

        (dest, src) = cls._parse_address_bytes(header)
        dest_callsign = dest
        src_callsign = src

        ctrl = int.from_bytes(header[14:15], "big")
        pid = int.from_bytes(header[15:16], "big")

        return cls(src, dest, ctrl, pid, data)

    @classmethod
    def _parse_address_bytes(cls, header):
        dest_bytes = bytearray([x>>1 for x in header[:6]])
        src_bytes = bytearray([x>>1 for x in header[7:13]])
        return (dest_bytes.decode("utf-8"), src_bytes.decode("utf-8"))