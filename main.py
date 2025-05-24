import logging
import mlflow

mlflow.set_tracking_uri("your_tracking_uri")
logging.getLogger().setLevel(logging.INFO)  # Reset logging level
logging.getLogger("mlflow").setLevel(logging.WARNING)  # Suppress MLflow logs if needed