from fastapi import FastAPI
from keyrings.cryptfile.cryptfile import CryptFileKeyring
import cisco_hashgen.cli
import os

app = FastAPI()
kr=CryptFileKeyring()
cryptfile_password=os.getenv("CRYPTFILE_PASSWORD")
kr.keyring_key=(cryptfile_password)

@app.get("/")
async def root(username: str, service: str, hash: str):
    password=kr.get_password(service, username)
    if cisco_hashgen.cli.verify_password (password, hash):
        return (hash)
    else:
        return (cisco_hashgen.cli.build_ios_type8(password=bytes(password, "ascii")))
        return (cisco_hashgen.cli.build_ios_type9_scrypt(password=bytes(password, "ascii")))
