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

    def test_to_bytes_unicode(self):
        cases = (
            ("é", "utf-8", b"\xc3\xa9"),
            ("é", "latin-1", b"\xe9"),
            ("😀", "utf-8", b"\xf0\x9f\x98\x80"),
            ("😀", "utf-16-le", b"\x3d\xd8\x00\xde"),
            # No normalization: "e" and a combining acute accent stay two code points.
            ("é", "utf-8", b"e\xcc\x81"),
        )

        for inp, encoding, want in cases:
            rst = k3str.to_bytes(inp, encoding)
            self.assertEqual(want, rst)

    def test_to_bytes_unencodable(self):
        cases = (
            ("我", "ascii"),
            ("é", "ascii"),
            # A lone surrogate is invalid in UTF-8.
            ("\ud800", "utf-8"),
        )

        for inp, encoding in cases:
            self.assertRaises(UnicodeEncodeError, k3str.to_bytes, inp, encoding)

        self.assertRaises(UnicodeEncodeError, k3str.to_utf8, "\ud800")

    def test_to_bytes_returns_bytes_unchanged(self):
        # bytes are neither decoded nor checked against the encoding.
        b = b"\xff\xfe"
        for encoding in (None, "ascii", "no-such-encoding"):
            rst = k3str.to_bytes(b, encoding)
            self.assertIs(b, rst)

    def test_to_bytes_bytes_like(self):
        # bytearray equals bytes with the same content, so the type is checked too.
        cases = (
            bytearray(b"\xff\xfe"),
            memoryview(b"\xff\xfe"),
        )

        for inp in cases:
            rst = k3str.to_bytes(inp)
            self.assertIs(bytes, type(rst))
            self.assertEqual(b"\xff\xfe", rst)

    def test_to_bytes_object(self):
        class Obj:
            def __str__(self):
                return "我"

        cases = (
            ("utf-8", b"\xe6\x88\x91"),
            ("gbk", b"\xce\xd2"),
        )

        for encoding, want in cases:
            rst = k3str.to_bytes(Obj(), encoding)
            self.assertEqual(want, rst)

    def test_to_bytes_invalid_encoding(self):
        cases = (
            ("a", "no-such-encoding"),
            (1, "no-such-encoding"),
            ("a", ""),
            # "hex" is a codec, but not a text encoding.
            ("a", "hex"),
        )

        for inp, encoding in cases:
            self.assertRaises(LookupError, k3str.to_bytes, inp, encoding)
