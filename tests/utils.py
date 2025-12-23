import logging
import os
from datetime import datetime
from typing import Dict, List

def configure_logging(log_level: str = 'INFO') -> None:
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=getattr(logging, log_level.upper())
    )

def get_environment_variables() -> Dict[str, str]:
    return dict(os.environ)

def get_current_timestamp() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def filter_empty_values(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    return [item for item in data if all(item.values())]

def merge_dictionaries(dict1: Dict[str, str], dict2: Dict[str, str]) -> Dict[str, str]:
    return {**dict1, **dict2}

def main():
    configure_logging('DEBUG')
    logging.info('Utils module initialized')

if __name__ == '__main__':
    main()