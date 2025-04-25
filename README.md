# edgeOps
This repository contains the code and data used for the image classification task presented in the research paper. The project includes 100 images for classification and the channel to download a pre-trained model, all shared under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

## Repository Structure

- **`Images100/`**: Contains 100 images used for the classification task. These images are licensed under the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/) and are attributed to Özgenel, Çağlar Fırat (2019), “Concrete Crack Images for Classification”, Mendeley Data, v2
http://dx.doi.org/10.17632/5y9wdsg2zt.2.

- **`requirements.txt`**: Lists the required dependencies for running the code. Install them using the command `pip install -r requirements.txt`.

-  **`inference.py`**: Contains the inference code for ML model. This can be modified depending on the ML model to be deployed.
-  **`monitor.py`**: Contains the code for measuring the inference latency and CPU usage.

-  **`edgeOps.sh`**: Contains the wrapper script for aggregating the collected data and automating the process.


### Usage

1. Clone/download the github repository and navigate to its directory.
2. Request the download link for example ML model via sfarjad@unomaha.edu.
3. Create a new directory `models` in repository directory and move the ML model to this directory.
4. Install the required dependencies
   ```bash
   pip install -r requirements.txt
   ```
5. Run edgeOps
   ```bash
   bash edgeOps.sh
   ```

### License
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)


## Citation
Secure Edge Computing Reference Architecture for Data-driven Structural Health Monitoring: Lessons Learned from Implementation and Benchmarking
Sheikh Muhammad Farjad, Sandeep Reddy Patllola, Yonas Kassa, George Grispos, Robin Gandhi
DOI: 10.1145/3696673.3723074

Or, BibTex (arXiv):

```bash
@misc{farjad2025secureedgecomputingreference,
      title={Secure Edge Computing Reference Architecture for Data-driven Structural Health Monitoring: Lessons Learned from Implementation and Benchmarking}, 
      author={Sheikh Muhammad Farjad and Sandeep Reddy Patllola and Yonas Kassa and George Grispos and Robin Gandhi},
      year={2025},
      eprint={2503.18857},
      archivePrefix={arXiv},
      primaryClass={cs.CR},
      url={https://arxiv.org/abs/2503.18857}, 
}
```
