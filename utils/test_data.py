from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

FILES_DIR = BASE_DIR / "tests" / "files"

VALID_USER = {
    "name": "Rahul Sharma",
    "dob": "1995-06-15",
    "email": "rahul@test.com",
    "aadhar": "123412341234",
    "pan": "ABCDE1234F",
    "id_doc": FILES_DIR / "id.png",
    "address_doc": FILES_DIR / "address.pdf"
}

INVALID_KYC = {
    "aadhar": "0000",
    "pan": "XXXX"
}
