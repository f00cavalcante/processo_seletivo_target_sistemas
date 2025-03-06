from arquivos.caminho_dos_arquivos import CaminhoDosArquivos

import json
import xmltodict


class ArquivoJSON:

    def __init__(self):
        self.caminho_json: str
        self.__dict_file_json: dict = []

    def __arquivo_json(self):
        with open(file=self.caminho_json, mode='r', encoding='utf-8') as file_json:
            self.__dict_file_json = json.load(file_json)

    @property
    def dict_file_json(self):
        self.__arquivo_json()
        return self.__dict_file_json


class ArquivoXML:
    def __init__(self):
        self.caminho_xml: str
        self.__dict_file_xml: dict = []

    def __arquivo_xml(self):
        with open(file=self.caminho_xml, mode='r', encoding='utf-8') as file_xml:
            self.__dict_file_xml = xmltodict.parse(file_xml.read(), encoding='utf-8', namespace_separator=':')

    @property
    def dict_file_xml(self):
        self.__arquivo_xml()
        return self.__dict_file_xml
