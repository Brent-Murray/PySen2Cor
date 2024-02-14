# PySen2Cor
Process to run the Sen2Cor in python. For More information about the Sen2Cor process please refer to the [Software User Manual](https://step.esa.int/thirdparties/sen2cor/2.11.0/docs/OMPC.TPZG.SUM.001%20-%20i1r0%20-%20Sen2Cor%202.11.00%20Configuration%20and%20User%20Manual.pdf)

## Installation
* Download [Sen2Cor](https://step.esa.int/thirdparties/sen2cor/2.11.0/Sen2Cor-02.11.00-win64.zip)
* Extract downloaded zip folder
* Identify the path where the `L2A_Process.bat` file is

## Run Script
You first need to download Sen2Cor as described above. In order to run the script you need to have downloaded at least one Sentinel-2 L1. Note the folder in which the zipped Sentinel-2 L1 product(s) are located. This will be the `directory` variable in the when you run the `main.py` script.

Within the `main.py` script edit the the variables when calling the `main` function in line 58 to the paths you have noted for the S2 L1 product(s) and the `L2a_Process.bat` file

```python
if __name__ == "__main__":
  main("C:/Users/name/downloads/sentinel2", "C:/Users/name/downloads/Sen2Cor-02.11.00-win64/L2A_Process.bat
```
