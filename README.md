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
3. 
4. Use the script on your text file. At this point the script only translates a single file line by line.
   ```sh
   python3 simple_translation_script.py \
    --model_name "HG_USER/MODEL_NAME"\
    --source_lang "es"\
    --target_lang "en"\
    --file_type "file_lines"\
    --input_path "path_to/input_file.txt"\
    --output_path "path_to/output_file.txt"
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
