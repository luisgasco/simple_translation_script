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
import torch
from torch.utils.data import Dataset
from tqdm.auto import tqdm
class ListDataset(Dataset):
     def __init__(self, original_list):
        self.original_list = original_list
     def __len__(self):
        return len(self.original_list)

     def __getitem__(self, i):
        return self.original_list[i]


def main(argv=None):
    parser = OptionParser()
    parser.add_option("-m", "--model_name", dest="model_name",
                    help="Machine Translation Hugging Face model")
    parser.add_option("-s", "--source_lang", dest="source_lang", help="ISO 639-1 source language code. For example: Spanish is 'es'")
    parser.add_option("-t", "--target_lang", dest="target_lang", help="ISO 639-1 target language  code. For example: English is 'en'")
    parser.add_option("-f", "--file_type", dest="file_type", help="Type of file/files you want to translate. The only option rn is 'file_lines'", default="lines")
    parser.add_option("-i", "--input_path", dest="input_path", help="Path to the file")
    parser.add_option("-o", "--output_path", dest="output_path", help="Path to the file")
    parser.add_option("--input_column", dest="input_column", help="Name or index of the column you wnat to translate (only if file_type=='tsv')")
    parser.add_option("--output_column", dest="output_column", default = "translated_column", help = "Named of the new columns in which you want to save the translation (only if file_type=='tsv')")
    (options, args) = parser.parse_args(argv)

    # Leer archivo. De momento archivo con un documento por línea. Más adelante más opciones
    if options.file_type=="lines":
        # Read file
        with open(options.input_path) as file:
            lines_to_translate = [line.strip() for line in file]
    elif options.file_type=="tsv":
        # Read file
        df_translate = pd.read_csv(options.input_path, sep="\t")
        print("Nombres de las columnas: {}".format(df_translate.columns))
        # Get lines to translate
        # Si input_column es un índice 
        if options.input_column.isnumeric():
            lines_to_translate = df_translate.iloc[:, int(options.input_column)].to_list()
        else: 
            lines_to_translate = df_translate[options.input_column].to_list()

    # Crear objeto de traducción
    pipeline_mt = pipeline(model = options.model_name,
                            src_lang = options.source_lang,
                            tgt_lang = options.target_lang,
                            device= torch.device(0 if torch.cuda.is_available() else 'cpu') ) 
 
    # Traducir
    inner_sub_list = 100
    # Finalmente, subdividimos la lista en listas menores para aplicar tqdm
    sublistas = [lines_to_translate[x:x+inner_sub_list] for x in range(0, len(lines_to_translate), inner_sub_list)]
    
    # Puede arrojar un warning por no ser eficiente con GPU, pero es mucho más rápido así que sin hacer
    # las sublistas
    lista_output = list()
    for sublista in tqdm(sublistas, desc="Procesando sublistas de {} elementos".format(inner_sub_list)):
        lista_output.extend(pipeline_mt(sublista, batch_size=4))

    # Old way to translate list without tqdm
    # BAD PERFORMANCE with very big lists.
    #results = pipeline_mt(lines_to_translate, 
    #                    batch_size=4)

    # Generamos lista final de salida
    # Next line is faster than translated_input = [t["translation_text"] for t in results] 
    translated_input = list(map(lambda x: x["translation_text"], lista_output))
    # Guardar archivo en el mismo formato que la entrada (dependerá de file_type)
    if options.file_type == "lines":
        with open(options.output_path, 'w') as output:
            for row in translated_input:
                output.write(str(row) + '\n')
    elif options.file_type=="tsv":
        df_translate[options.output_column] = translated_input
        df_translate.to_csv(options.output_path, sep="\t", index=False)

if __name__ == "__main__":
  sys.exit(main())