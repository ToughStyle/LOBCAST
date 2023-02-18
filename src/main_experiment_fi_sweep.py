
import os
import sys

# preamble needed for cluster
module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)

from src.main_single import *


def experiment_FI(kset=None, now=None, models_todo=None, servers=None):

    now, server_name, server_id, n_servers = experiment_preamble(now, servers)

    kset = kset if kset is not None else cst.FI_Horizons
    models_todo = models_todo if models_todo is not None else cst.Models

    for mod in list(models_todo)[server_id::n_servers]:
        for k in kset:
            print("Running FI experiment on {}, with K={}".format(mod, k))

            try:
                cf: Configuration = Configuration(now)
                set_seeds(cf)

                cf.CHOSEN_DATASET = cst.DatasetFamily.FI
                cf.CHOSEN_STOCKS[cst.STK_OPEN.TRAIN] = cst.Stocks.FI
                cf.CHOSEN_STOCKS[cst.STK_OPEN.TEST] = cst.Stocks.FI
                cf.CHOSEN_PERIOD = cst.Periods.FI
                cf.CHOSEN_MODEL = mod

                cf.IS_WANDB = 1
                cf.IS_TUNE_H_PARAMS = True

                cf.HYPER_PARAMETERS[cst.LearningHyperParameter.FI_HORIZON] = k.value
                launch_wandb(cf)

            except KeyboardInterrupt:
                print("There was a problem running on", server_name.name, "FI experiment on {}, with K={}".format(mod, k))
                sys.exit()


servers = [cst.Servers.ALIEN2]
# models_todo = [cst.Models.MLP, cst.Models.CNN1, cst.Models.CNN2, cst.Models.LSTM, cst.Models.CNNLSTM, cst.Models.BINCTABL, cst.Models.CTABL, cst.Models.DLA, cst.Models.DAIN]
# models_todo = [cst.Models.ATNBoF, cst.Models.TLONBoF, cst.Models.AXIALLOB]
# models_todo = [cst.Models.DEEPLOBATT, cst.Models.DEEPLOB, cst.Models.TRANSLOB]
models_todo = [cst.Models.AXIALLOB]

kset = [cst.FI_Horizons.K10]
now = "FI-2010-Sweep-ALL"

experiment_FI(kset=kset, now=now,  models_todo=models_todo, servers=servers)
