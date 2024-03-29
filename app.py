
import requests
import base64

from typing import Union, List
from fastapi import FastAPI, Request
from peticionar import Pje_pet, MainClientException

client = Pje_pet()
app = FastAPI()


@app.post("/upload")
async def upload(request: Request):
    try:
        form = await request.json()
        content = get_content(content=form, required_fields=["tipo", "files", "processo", "idProcesso",
                                                             "username", "password", "idTarefa", "instancia"])

        client.set_global_variable(len(
            content['files']), content['idTarefa'], content['processo'], content['instancia'])
        client.login(username=content['username'],
                     password=content['password'])

        for num, file in enumerate(content['files']):
            mime, mimetype, file_size = get_extension(file['b64Content'])
            decode_file = base64.b64decode(file['b64Content'])
            client.start(content=content, mimetype=mimetype, file=decode_file, mime=mime,
                         file_size=file_size, cont=num+1, file_options=file)

        return {"sucesso": True}

    except Exception as e:
        client.returnMsg(msg=F"Fatal Error: {e}", error=True, forced=True)
        return error(msg=e.args[0])



@app.post("/create_process")
async def create_process(request: Request):
    try:
        client = Pje_pet()
        form = await request.json()
        content = get_content(content=form, required_fields=["tipo", "cookies", "files", "instancia", "subjects",
                                                            "username", "password", "idTarefa", "features", "polo_ativo",
                                                            "polo_passivo", "files", "dados_iniciais"])
        client.set_global_variable(content=content, instancia=content['instancia'])
        client.switch_to_screen("Login")
        client.validate_login(
            username=content['username'], password=content['password'], cookies=content['cookies'])
        client.start(content=content, file_options=content['files'])
        return {"sucesso": client.inputs['url_process']}
    except Exception as e:
        client.returnMsg(error=True, msg={"msg":F"Fatal Error: {e}", "error": True})
        return error(msg=e.args[0])

#   Utils
###################################################################


def get_content(content, required_fields):
    validate_content(content, required_fields)
    return content


def validate_content(content, required_fields):
    for field in required_fields:
        if field not in content:
            print(field)
            raise MainClientException("Requisição inválida.")


def error(msg="Erro desconhecido ao processar requisição."):
    return {
        "sucesso": False,
        "msg": msg
    }


def invalid_request():
    return error(msg="Requisição inválida.")


def ok():
    return {
        "sucesso": True
    }
