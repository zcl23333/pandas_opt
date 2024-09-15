import pandas as pd


def weighted_row_sum(df, weights):
    """
    计算DataFrame中每一行的加权求和。

    参数:
        df (pd.DataFrame): 包含数据的DataFrame。
        weights (dict): 各列的权重字典，键为列名，值为权重。

    返回:
        pd.Series: 包含每行加权求和结果的Series。
    """
    # 确保所有权重列都在DataFrame中
    missing_columns = set(weights.keys()) - set(df.columns)
    if missing_columns:
        raise ValueError(f"缺少以下列：{missing_columns}")

    # 计算加权求和
    weighted_sums = (df[list(weights.keys())] * pd.Series(weights)).sum(axis=1)
    return weighted_sums
