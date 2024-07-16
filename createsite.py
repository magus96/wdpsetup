# import os
import subprocess
# from fastapi import FastAPI, Response, status

from constants import SERVER_CONFIG


# app = FastAPI()

# app.get("/create-site")
# def create_site(domain: str):
#     domain = domain + ".com"
#     subprocess.call(["sh", "./test.sh"])
#     return Response()
final_str = SERVER_CONFIG.format(domain = "xample.com")
subprocess.call(["sh", "./create.sh", "xample.com", final_str])
