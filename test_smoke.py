import os
os.environ.setdefault("BOT_TOKEN", "123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk")
import main

def test_domain_helpers():
    assert main.clean_domain("https://Example.COM/path") == "example.com"
    assert main.looks_like_domain("example.com")
    assert not main.looks_like_domain("not a domain")

def test_status_mapping():
    assert main.map_status_text("Tidak Ada") == "AMAN"
    assert main.map_status_text("Blocked") == "BLOKIR"
    assert main.map_status_text("Aman") == "AMAN"
