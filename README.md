
## Open the folder where this script and the required.tx file is located

## Start by creating an enviroment with the following command
- ```python -m venv wax-env``` On Windows
- ``` python3 -m venv wax-env``` On Unix or MacOS


## Then activate the created enviroment
- ```wax-env\Scripts\activate``` On Windows
- ```source wax-env/bin/activate``` On Unix or MacOS


## Install libraries
- ```python -m pip install -r requirements.txt``` On Windows
- ```python3 -m pip install -r requirements.txt``` On Unix or MacOS


## Using the scripts

> The scripts depends on enviromental variables, this can either be set
> directly in the windows or Linux profiles
> or by creating a ***.env*** file in the root directory and setting the
> variables.
> Example of a ***.env*** file
> - WALLET_NAME=yourWallet
> - WALLET_KEY= 5JxSzLshLArXqZqGJC79vESNLYB2xUFeE6Vp44J63NNK9g49WF2
> - API_ENDPOINT=https://wax.greymass.com

## Example Mint Assets
> The mint.py can be used to mint atomicassets nfts with the following  variables 
> in the ***.env*** file
> - Total_Mint=2 
> - Authorized_Minter=yourWallet 
> - Collection_Name=collectionName
> - New_Asset_Owner=yourWallet
> - Schema_Name=packs
> - Template_Id=773378
> 
> And then running the following command
> - ```py mint.py``` on windows and 
> - ```python3 mint.py``` on linux
