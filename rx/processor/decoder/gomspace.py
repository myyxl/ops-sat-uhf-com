from scrambler.ccsds import Polynomial8
from frames.ax25 import AX25
from frames.csp import CSP
import crc32c

class NanoComAX100():
    def decode_frame(raw_ax25_data):

        ax25_frame = AX25.from_bytes(raw_ax25_data)

        # 1. Unscramble whole data field
        unscrambled = Polynomial8.scramble(ax25_frame.data)

        # 2. Reed-Solomon decode
        # Just gamble and hope it's correct
        # Will implement later
        payload = unscrambled[:58]

        # 3. CRC check
        given_crc = int.from_bytes(unscrambled[58:][:4])
        calculated_crc = crc32c.crc32c(payload)

        if given_crc != calculated_crc:
            print("Warning: CRC mismatch")

        csp_frame = CSP.from_bytes(payload)

        return csp_frame
