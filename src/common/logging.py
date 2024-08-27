# logging.py
"""
Custom logging configuration for the project.
"""

import logging

def setup_logging():
    """
    Sets up logging configuration.
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    return logger