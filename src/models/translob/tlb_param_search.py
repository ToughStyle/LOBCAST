
import src.constants as cst

HP_TRANS = {
    cst.LearningHyperParameter.EPOCHS_UB.value: {'values': [100]},
    cst.LearningHyperParameter.OPTIMIZER.value: {'values': [cst.Optimizers.ADAM.value]},
    cst.LearningHyperParameter.WEIGHT_DECAY.value: {'values': [1e-5]},

    cst.LearningHyperParameter.BATCH_SIZE.value:    {'values': [32]},
    cst.LearningHyperParameter.LEARNING_RATE.value: {'max': 1e-2, 'min': 1e-5}
}

HP_TRANS_FI_FIXED = {
    cst.LearningHyperParameter.EPOCHS_UB.value: 100,
    cst.LearningHyperParameter.OPTIMIZER.value: cst.Optimizers.ADAM.value,
    cst.LearningHyperParameter.LEARNING_RATE.value: 0.0007931,
    cst.LearningHyperParameter.WEIGHT_DECAY.value: 0.00001,
    # cst.LearningHyperParameter.BATCH_SIZE.value: 64,
}

# TODO add dropout (hard encoded fn)
