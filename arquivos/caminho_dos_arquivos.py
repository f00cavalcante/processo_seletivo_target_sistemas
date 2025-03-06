from pathlib import Path

from enum import Enum


class CaminhoDosArquivos(Enum):
    ARQUIVO_JSON = Path('arquivos/dados_json.json')
    ARQUIVO_XML = Path('arquivos/dados_xml.xml')
