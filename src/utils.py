import pandas as pd

import os
import logging

def load_data(file_path: str, logger: logging) -> pd.DataFrame:
    try:
        logger.debug("Loading data from %s", file_path)
        return pd.read_csv(file_path)
    except Exception as e:
        logger.error("Error loading data: %s", e)
        return pd.DataFrame()


def configure_logger(
    name: str, log_file: str, log_level: str = "DEBUG"
) -> logging.Logger:
    # logging configure
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel("DEBUG")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel("ERROR")

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def save_data(
    data: pd.DataFrame, data_path: str, file_name: str, logger: logging
) -> None:
    try:
        logger.debug("Saving Data")
        os.makedirs(data_path, exist_ok=True)

        data.to_csv(os.path.join(data_path, file_name), index=False)
        logger.info("Data saved successfully")
    except Exception as e:
        logger.error(f"Error saving data: {e}")

def apply_filters(df, filters):
    for column, values in filters.items():
        if column in df.columns:
            df = df[df[column].isin(values)]
    return df
