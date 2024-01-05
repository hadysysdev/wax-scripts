import os
import time
import wallet
from pyeoskit import eosapi
from dotenv import load_dotenv
load_dotenv()



def mintAsset(args, totalMint:int):
    permission = {}
    permission[os.getenv('WALLET_NAME')] = 'active'
    actions = []
    for i in range(0, totalMint):
        action = ['atomicassets', 'mintasset', args , permission]
        actions.append(action)
        # eosapi.push_action(contract='atomicassets', action= 'mintasset', args= args, permissions=permission)
        # time.sleep(1)
    eosapi.push_actions(actions)

    



if __name__ == '__main__':

    eosapi.set_node(os.getenv('API_ENDPOINT'))
    info = eosapi.get_info()
    print(info)

    total_mint = int(os.getenv('Total_Mint'))
    args = {
        "authorized_minter":os.getenv('Authorized_Minter'),
        "collection_name":os.getenv('Collection_Name'),
        "schema_name" : os.getenv('Schema_Name'),
        "template_id":int(os.getenv('Template_Id')),
        "new_asset_owner":os.getenv('New_Asset_Owner'),
        "immutable_data":[],
        "mutable_data":[],
        "tokens_to_back":[]
    }
    mintAsset(args,total_mint)
