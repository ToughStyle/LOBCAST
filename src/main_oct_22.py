
import argparse

from src.data_preprocessing.LOBDataBuilder import LOBDataBuilder
from src.data_preprocessing.LOBDataModule import LOBDataModule
from src.data_preprocessing.LOBDataset import LOBDataset
from src.models.model_callbacks import callback_save_model

from pytorch_lightning import Trainer
from src.models.mlp import MLP
import src.config as co

ModelsMap = {co.Models.MLP.value: MLP}


def parser_cl_arguments():
    """ Parses the arguments for the command line. """

    parser = argparse.ArgumentParser(description='PyTorch Training')

    parser.add_argument('--model',    default=co.Models.MLP.value)
    parser.add_argument('--data',     default=co.DatasetFamily.LOBSTER.value)
    parser.add_argument('--is_wandb', default=False)

    parser.add_argument('--epochs',   default=co.EPOCHS)
    parser.add_argument('--lr',       default=co.LEARNING_RATE)
    parser.add_argument('--batch',    default=co.BATCH_SIZE)

    parser.add_argument('--back_win', default=co.BACKWARD_WINDOW)
    parser.add_argument('--forw_win', default=co.FORWARD_WINDOW)

    return parser


def prepare_data(cl_args):

    # train
    lo_train = LOBDataBuilder(co.DATA_DIR,
                              co.DatasetType.TRAIN,
                              start_end_trading_day=("2022-03-07", "2022-03-08"),
                              is_data_preload=False,
                              crop_trading_day_by=60 * 30)

    # use the same
    mu, sigma = lo_train.normalization_mean, lo_train.normalization_std

    # test
    lo_test = LOBDataBuilder(co.DATA_DIR,
                             co.DatasetType.TEST,
                             start_end_trading_day=("2022-03-09", "2022-03-10"),
                             is_data_preload=True,
                             crop_trading_day_by=60 * 30,
                             normalization_mean=mu,
                             normalization_std=sigma)

    n_inst_train = int(len(lo_train.samples_x) * co.TRAIN_SPLIT_VAL)

    train_set = LOBDataset(x=lo_train.samples_x[:n_inst_train], y=lo_train.samples_y[:n_inst_train])
    val_set   = LOBDataset(x=lo_train.samples_x[n_inst_train:], y=lo_train.samples_y[n_inst_train:])
    test_set  = LOBDataset(x=lo_test.samples_x, y=lo_test.samples_y)

    print()
    print("Samples in the splits:")
    print(len(train_set), len(val_set), len(test_set))
    print()

    lob_dm = LOBDataModule(train_set, val_set, test_set, cl_args.batch)
    return lob_dm


def lunch_training(cl_args):
    data_module = prepare_data(cl_args)
    model = MLP(data_module.x_shape, data_module.y_shape, cl_args.lr)

    trainer = Trainer(gpus=co.DEVICE,
                      val_check_interval=co.VALIDATE_EVERY,
                      max_epochs=cl_args.epochs,
                      callbacks=[callback_save_model(cl_args.model)])

    trainer.fit(model, data_module)


if __name__ == "__main__":
    args = parser_cl_arguments().parse_args()
    lunch_training(args)

