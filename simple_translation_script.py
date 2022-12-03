#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 1 12:03:49 2021

@author: luisgasco

"""


import sys
from transformers import pipeline
import pandas as pd
from optparse import OptionParser


def main(argv=None):
    parser = OptionParser()
    parser.add_option("-m", "--model_name", dest="model_name",
                    help="Machine Translation Hugging Face model")
    parser.add_option("-s", "--source_lang", dest="source_lang", help="ISO 639-1 source language code. For example: Spanish is 'es'")
    parser.add_option("-t", "--target_lang", dest="target_lang", help="ISO 639-1 target language  code. For example: English is 'en'")
    parser.add_option("-f", "--file_type", dest="file_type", help="Type of file/files you want to translate. The only option rn is 'file_lines'", default="file_lines")
    parser.add_option("-i", "--input_path", dest="input_path", help="Path to the file")
    parser.add_option("-o", "--output_path", dest="output_path", help="Path to the file")
    (options, args) = parser.parse_args(argv)

    # Leer archivo. De momento archivo con un documento por línea. Más adelante más opciones
    if options.file_type=="file_lines":
        # Read file
        with open(options.input_path) as file:
            lines_to_translate = [line.strip() for line in file]

    # Crear objeto de traducción
    pipeline_mt = pipeline(model = options.model_name,
                            src_lang = options.source_lang,
                            tgt_lang = options.target_lang)

    # Traducir
    results = pipeline_mt(lines_to_translate)

    # Generamos lista de salida
    translated_input = [t["translation_text"] for t in results] 
    
    # Guardar archivo en el mismo formato de entrada
    with open(options.output_path, 'w') as output:
        for row in translated_input:
            output.write(str(row) + '\n')

if __name__ == "__main__":
  sys.exit(main())