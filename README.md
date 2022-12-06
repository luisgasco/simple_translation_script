# Simple Translation Script

Simple script to translate files using Hugging Face fine-tuned models for machine translation.
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Guidelines">Guía</a>
    </li>
    <li><a href="#funciones">Funciones</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Guidelines 

> :exclamation: **If you experience problems with pytorch, install the appropriate version for your system.**

If you want to use this repository, please follow the instructions below:

1. Clone the repository and install the requirements.txt in a new python runtime environment. 
   ```sh
   git clone https://github.com/luisgasco/deepspanorm.git
   python3 -m venv .env
   source .env/bin/activate
   pip install -r requirements.txt
   ```
2. Find a machine translation model in [HuggingFace Hub](https://huggingface.co/models?filter=translation). Check that it is compatible with your source language (the language of the file you want to translate) and target language (the language into which you want to translate your texts).
3. Use the script on your text file. At this point the script only translates a single file line by line or add a translated string column to a tsv.
   ```sh
   python3 simple_translation_script.py \
    --model_name "HG_USER/MODEL_NAME"\
    --source_lang "es"\
    --target_lang "en"\
    --file_type "lines"\
    --input_path "path_to/input_file_toy.txt"\
    --output_path "path_to/output_file.txt"
   ```

   ```sh
   python3 simple_translation_script.py \
    --model_name "HG_USER/MODEL_NAME"\
    --source_lang "es"\
    --target_lang "en"\
    --file_type "tsv"\
    --input_path "path_to/input_file_toy_tab.txt"\
    --output_path "path_to/output_file_tab.txt"\
    --input_column "term"\
    --output_column "translated_en"
   ```

## Usage:
The script has the following attributes:

- `model_name`: String indicating the name of the translation model to be downloaded from HuggingFace or the path to the local translation model (in Hugging Face format).
- `source_lang`: Source language of the text to be translated. It must be represented by a string according to ISO 639-1. For example for Spanish it is "es".
- `target_lang`: Target language of the text to be translated. It must be represented by a string according to ISO 639-1. For example for English it is "en".
- `file_type`: String representing the type of input file. If the value is "lines" each line of a text file will be read and translated. If the value is "tsv" the tab-separated file shall be read and the column specified in `input_column` will be translated into a new column specified in the `output_column` attribute.
- `input_path`: String containing the absolute path to the file to be translated, including the file name.
- `output_path`: String containing the output file to be generated (including the absolute path). 
- `input_column`: Name of the column in the tsv file to be translated. 
- `output_column`: Name of the column in which the translation of the column specified in `input_columns` will be stored.

## Examples: 
Here are some examples of how to run the script and use its different attributes and options:

- Run the script to translate a spanish text file to english line by line: 

  ```sh
   python3 simple_translation_script.py \
    --model_name "Helsinki-NLP/opus-mt-es-en"\
    --source_lang "es"\
    --target_lang "en"\
    --file_type "lines"\
    --input_path "toy_data/input_file_toy.txt"\
    --output_path "toy_data/output_file.txt"
   ```

- Run the script to translate to english the "term" column (in spanish) of a tsv file by saving it in a new column.

  ```sh
   python3 simple_translation_script.py \
    --model_name "Helsinki-NLP/opus-mt-es-en"\
    --source_lang "es"\
    --target_lang "en"\
    --file_type "tsv"\
    --input_path "toy_data/input_file_toy_tab.txt"\
    --output_path "toy_data/output_file_tab.txt"\
    --input_column "term"\
    --output_column "translated_en"
   ```


## Roadmap

* [ ] Adapt to other file types
<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**. For contributing:

1. Fork/Clone the Project in your system
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Freeze the requirements.txt (`pip3 freeze > requirements.txt`)
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request from github.
7. Check that the evaluation workflow from github is executed without errors.
8. Notify to @luisgasco to test and accept the new changes.

Follow [this tutorial](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches) to create a branch.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
