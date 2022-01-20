"""Configuration file for pytest."""

import os
import shutil
import pytest

import numpy as np

from fooof_PLA.core.modutils import safe_import

from fooof_PLA.tests.tutils import get_tfm, get_tfg, get_tbands
from fooof_PLA.tests.settings import BASE_TEST_FILE_PATH, TEST_DATA_PATH, TEST_REPORTS_PATH

plt = safe_import('.pyplot', 'matplotlib')

###################################################################################################
###################################################################################################

def pytest_configure(config):
    if plt:
        plt.switch_backend('agg')
    np.random.seed(101)

@pytest.fixture(scope='session', autouse=True)
def check_dir():
    """Once, prior to session, this will clear and re-initialize the test file directories."""

    # If the directories already exist, clear them
    if os.path.exists(BASE_TEST_FILE_PATH):
        shutil.rmtree(BASE_TEST_FILE_PATH)

    # Remake (empty) directories
    os.mkdir(BASE_TEST_FILE_PATH)
    os.mkdir(TEST_DATA_PATH)
    os.mkdir(TEST_REPORTS_PATH)

@pytest.fixture(scope='session')
def tfm():
    yield get_tfm()

@pytest.fixture(scope='session')
def tfg():
    yield get_tfg()

@pytest.fixture(scope='session')
def tbands():
    yield get_tbands()

@pytest.fixture(scope='session')
def skip_if_no_mpl():
    if not safe_import('matplotlib'):
        pytest.skip('Matplotlib not available: skipping test.')
