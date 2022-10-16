from argparse import Namespace
from chemprop.parsing import parse_predict_args
import string
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from chemprop.train import make_predictions

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"welcome": "Welcome to chemprop_ir"}


@app.post("/pred")
async def predict(req : Request):
    print(req)
    # args = parse_predict_args()
    # print(args)
    # args = Namespace(gpu=None, use_compound_names=False, preds_path='ir_preds.csv',
    #  checkpoint_dir='/media/god-particle/Elements/D4_data/ir_models_data/computed_model/model_files/', checkpoint_path=None, 
    #  batch_size=50, features_generator=None, features_path=None, max_data_size=None, ensemble_variance=False, 
    #  ensemble_variance_conv=0.0, checkpoint_paths=['/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_0.pt', '/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_1.pt', '/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_2.pt', '/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_3.pt', '/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_4.pt', '/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_5.pt', '/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_6.pt', '/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_7.pt', '/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_8.pt', '/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_9.pt'], 
    #  ensemble_size=10, cuda=True, device='cpu')

    args = Namespace(gpu=None, use_compound_names=False, preds_path='ir_preds.csv',
     checkpoint_dir='/media/god-particle/Elements/D4_data/ir_models_data/computed_model/model_files/', checkpoint_path=None, 
     batch_size=50, features_generator=None, features_path=None, max_data_size=None, ensemble_variance=False, 
     ensemble_variance_conv=0.0, checkpoint_paths=['/media/god-particle/Elements//D4_data/ir_models_data/computed_model/model_files/model_0.pt'], 
     ensemble_size=10, cuda=True, device='cpu')

    # args.checkpoint_dir = '../D4_data/ir_models_data/computed_model/model_files/'
    info = await req.json()
    print(info)
    # avg_preds = await make_predictions(args,smiles=[info['smiles']])
    avg_preds = make_predictions(args,smiles=[info['smiles']])
    
    return {'avg_preds' : avg_preds[0]}
    