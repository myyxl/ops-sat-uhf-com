import bitstruct
from dataclasses import dataclass

@dataclass
class CSP:
    priority: int 
    source: int
    destination: int
    destination_port: int 
    source_port: int 
    reserved: int 
    hmac: bool 
    xtea: bool
    rdp: bool
    crc: bool
    data: bytes

    @classmethod
    def from_bytes(cls, bytes):
        values = bitstruct.unpack(">u2u5u5u6u6u4b1b1b1b1", bytes[:4])
        return cls(
            values[0],
            values[1],
            values[2],
            values[3],
            values[4],
            values[5],
            values[6],
            values[7],
            values[8],
            values[9],
            bytes[4:]
        )


