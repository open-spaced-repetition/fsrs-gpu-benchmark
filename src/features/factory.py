from .base import BaseFeatureEngineer
from .fsrs_engineer import FSRSFeatureEngineer
from src.main.config import Config, ModelName
from typing import Type


FEATURE_ENGINEER_REGISTRY: dict[ModelName, Type[BaseFeatureEngineer]] = {
    # FSRS family and similar models that use standard tensor format
    "FSRSv1": FSRSFeatureEngineer,
    "FSRSv2": FSRSFeatureEngineer,
    "FSRSv3": FSRSFeatureEngineer,
    "FSRSv4": FSRSFeatureEngineer,
    "FSRS-4.5": FSRSFeatureEngineer,
    "FSRS-5": FSRSFeatureEngineer,
    "FSRS-6": FSRSFeatureEngineer,
    "FSRS-7": FSRSFeatureEngineer,
    "FSRS-6-one-step": FSRSFeatureEngineer,
}


def create_feature_engineer(config: Config) -> BaseFeatureEngineer:
    """
    Factory function to create the appropriate feature engineer based on model name from config

    Args:
        config: Configuration object containing model_name and other settings

    Returns:
        Appropriate feature engineer instance

    Raises:
        ValueError: If config.model_name is not supported
    """
    model_name = config.model_name

    # Create and return the appropriate feature engineer
    feature_engineer_cls = FEATURE_ENGINEER_REGISTRY[model_name]
    return feature_engineer_cls(config)


def get_supported_models() -> tuple[str, ...]:
    """
    Get list of all supported model names

    Returns:
        List of supported model names
    """
    return tuple(FEATURE_ENGINEER_REGISTRY.keys())
