import unittest

from main import hex_to_bin, read_packet_part_1, Packet


class TestSum(unittest.TestCase):
    def test_part_1(self):

        self.assertEqual(read_packet_part_1(hex_to_bin('8A004A801A8002F478')), 16)
        self.assertEqual(read_packet_part_1(hex_to_bin('620080001611562C8802118E34')), 12)
        self.assertEqual(read_packet_part_1(hex_to_bin('C0015000016115A2E0802F182340')), 23)
        self.assertEqual(read_packet_part_1(hex_to_bin('A0016C880162017C3686B18A3D4780')), 31)

    def test_part_2(self):
        packet_1 = Packet(hex_to_bin('C200B40A82'))
        self.assertEqual(packet_1.value, 3)
        packet_2 = Packet(hex_to_bin('04005AC33890'))
        self.assertEqual(packet_2.value, 54)
        packet_3 = Packet(hex_to_bin('880086C3E88112'))
        self.assertEqual(packet_3.value, 7)
        packet_4 = Packet(hex_to_bin('CE00C43D881120'))
        self.assertEqual(packet_4.value, 9)
        packet_5 = Packet(hex_to_bin('D8005AC2A8F0'))
        self.assertEqual(packet_5.value, 1)
        packet_6 = Packet(hex_to_bin('F600BC2D8F'))
        self.assertEqual(packet_6.value, 0)
        packet_7 = Packet(hex_to_bin('9C005AC2F8F0'))
        self.assertEqual(packet_7.value, 0)
        packet_8 = Packet(hex_to_bin('9C0141080250320F1802104A08'))
        self.assertEqual(packet_8.value, 1)


if __name__ == '__main__':
    unittest.main()