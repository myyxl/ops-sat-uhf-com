class Polynomial8():
    def scramble(input_bytes):
        input_bits = []
        for byte in input_bytes:
            input_bits += [(byte & (1<<x))>>x for x in [7,6,5,4,3,2,1,0]]

        randomizer_bits = []
        register = 0xFF
        for x in range(len(input_bits)):
            if x != 0 and x % 255 == 0:
                register = 0xFF

            bit = register & 0x01 
            randomizer_bits.append(bit)
            next_bit = ((register >> 7) ^ (register >> 5) ^ (register >> 3) ^ register) << 7
            register = register >> 1
            register = (register & 0x7F) | next_bit

        output_bits = [input_bits[idx] ^ x for (idx,x) in enumerate(randomizer_bits)]
        output_bytes = [int("".join(map(str, output_bits[i:i+8])), 2) for i in range(0, len(output_bits), 8)]

        return bytearray(output_bytes)

        

        