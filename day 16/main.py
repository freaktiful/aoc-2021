from math import prod


def consume_literal(bits):
    binary_number = ''
    is_last = bits[0:1] == '0'
    while not is_last:
        binary_number += bits[1:5]
        bits = bits[5:]
        is_last = bits[0:1] == '0'
    binary_number += bits[1:5]
    return bits[5:], int(binary_number, 2)


def read_packet_part_1(packet):
    version = 0
    while len(packet) > 0 and int(packet) > 0:
        version += int(packet[0:3], 2)
        type_id = int(packet[3:6], 2)
        if type_id == 4:
            packet, number = consume_literal(packet[6:])
        else:
            length_type = packet[6:7]
            if length_type == '0':
                left_packets_lenght = int(packet[7:22], 2)
                version += read_packet_part_1(packet[22: 22+left_packets_lenght])
                packet = packet[22+left_packets_lenght:]
            else: # if length_type == '1'
                # left_packets_number = int(packet[7:18], 2)
                version += read_packet_part_1(packet[18:])
                packet = ''
    return version


class Packet:

    def __init__(self, bits):
        self._bits = bits
        self._version = int(bits[0:3], 2)
        self._type = int(bits[3:6], 2)
        self._content = self.decode_value() if self._type == 4 else self.decode_packet()

    def decode_value(self):
        binary_number = ''
        cont = 6
        while True:
            group = self._bits[cont: cont+5]
            binary_number += group[1:]
            cont += 5
            if group[0] == '0':
                break
        self._size = cont
        return int(binary_number, 2)

    def decode_packet(self):
        content = []
        length_type_id = self._bits[6]
        if length_type_id == '0':
            length = int(self._bits[7:22], 2)
            self._size = 22 + length
            sub_bits = self._bits[22: self._size]
            while sub_bits:
                content.append(Packet(sub_bits))
                sub_bits = sub_bits[content[-1]._size:]
        else:
            loops = int(self._bits[7:18], 2)
            sub_bits = self._bits[18:]
            for i in range(loops):
                content.append(Packet(sub_bits))
                sub_bits = sub_bits[content[-1]._size:]
            self._size = 18 + sum(el._size for el in content)
        return content

    @property
    def value(self):
        if self._type == 0:
            return sum(packet.value for packet in self._content)
        elif self._type == 1:
            return prod(packet.value for packet in self._content)
        elif self._type == 2:
            return min(packet.value for packet in self._content)
        elif self._type == 3:
            return max(packet.value for packet in self._content)
        elif self._type == 4:
            return self._content
        elif self._type == 5:
            return 1 if self._content[0].value > self._content[1].value else 0
        elif self._type == 6:
            return 1 if self._content[0].value < self._content[1].value else 0
        elif self._type == 7:
            return 1 if self._content[0].value == self._content[1].value else 0


def hex_to_bin(hex_chunk):
    # convert to binary keeping the leading zeroes
    # https://stackoverflow.com/questions/3258330/converting-from-hex-to-binary-without-losing-leading-0s-python
    h_size = len(hex_chunk) * 4
    return (bin(int(hex_chunk, 16))[2:]).zfill(h_size)


def format_input(name):
    with open(name, 'r') as file:
        return file.read()


if __name__ == '__main__':
    formatted_input = hex_to_bin(format_input('input.txt'))
    print(read_packet_part_1(formatted_input))
    p = Packet(formatted_input)
    print(p.value)
