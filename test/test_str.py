import unittest

import k3ut

import k3str

dd = k3ut.dd


class TestStr(unittest.TestCase):
    def test_to_bytes(self):
        cases = (
            ("", b""),
            ("1", b"1"),
            (1, b"1"),
            ("我", b"\xe6\x88\x91"),
            (b"\xe6\x88\x91", b"\xe6\x88\x91"),
        )

        for inp, want in cases:
            rst = k3str.to_bytes(inp)

            self.assertEqual(want, rst)

        #  specify encoding

        self.assertEqual(b"\xce\xd2", k3str.to_bytes("我", "gbk"))

    def test_to_utf8(self):
        cases = (
            ("", b""),
            ("1", b"1"),
            (1, b"1"),
            ("我", b"\xe6\x88\x91"),
            (b"\xe6\x88\x91", b"\xe6\x88\x91"),
        )

        for inp, want in cases:
            rst = k3str.to_utf8(inp)

            self.assertEqual(want, rst)
