from sklearn.metrics import roc_auc_score, roc_curve, auc


def calculate_auc_with_roc_curve(masks, preds):
    """
    通过 ROC 曲线计算 AUC。
    如果 AUC 小于 0.5，则取 1 - AUC，以确保 AUC >= 0.5。
    """
    fpr, tpr, thresholds = roc_curve(masks, preds, pos_label=1)
    auc_score = auc(fpr, tpr)
    if auc_score < 0.5:
        auc_score = 1 - auc_score
    return auc_score


def calculate_auc_with_roc_auc_score(masks, preds):
    """
    使用 roc_auc_score 函数直接计算 AUC。
    """
    return roc_auc_score(masks, preds)
