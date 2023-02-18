
import src.constants as cst

HP_TABL = {
    cst.LearningHyperParameter.EPOCHS_UB.value: {'values': [200]},
    cst.LearningHyperParameter.OPTIMIZER.value: {'values': [cst.Optimizers.ADAM.value]},
    cst.LearningHyperParameter.NUM_SNAPSHOTS.value: {'values': [10]},

    cst.LearningHyperParameter.LEARNING_RATE.value: {'values': [0.0001, 0.000325, 0.00055, 0.000775, 0.001]}, # {'max': 0.01, 'min': 0.001},  # 'max': 0.001, 'min': 0.0001
    cst.LearningHyperParameter.BATCH_SIZE.value: {'values': [256]},
}


# SC = {0.01, 0.005, 0.001, 0.0005, 0.0001}

HP_TABL_FI_FIXED = {
    cst.LearningHyperParameter.EPOCHS_UB.value: 200,
    cst.LearningHyperParameter.OPTIMIZER.value: cst.Optimizers.ADAM.value,
    cst.LearningHyperParameter.LEARNING_RATE.value: 0.01,  # schedule del learning rate?
    cst.LearningHyperParameter.BATCH_SIZE.value: 256,
    cst.LearningHyperParameter.NUM_SNAPSHOTS.value: 10,
}
