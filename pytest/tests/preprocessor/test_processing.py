# coding=utf-8
""" Tests for the Pre-Processor Lexer and Parser """
import asyncio
import logging
import os
from pathlib import Path
from typing import List

from para import RUNTIME_COMPILER, initialise_default_paths
from para.compiler import (ParaCompiler, ProgramCompilationProcess)
from para.logging import set_avoid_print_banner_overwrite
from .. import add_folder, remove_folder, reset_input, BASE_TEST_PATH

compiler = ParaCompiler()

# Initialises the logging session for the compiler
RUNTIME_COMPILER.init_logging_session(
    level=logging.DEBUG, print_banner=False
)

test_c_files_dir: Path = BASE_TEST_PATH / "test_files" / "c_ref_files"
test_para_files_dir: Path = BASE_TEST_PATH / "test_files"
test_processor_files_dir: Path = BASE_TEST_PATH / "test_files" / "preprocessor"

# Avoiding printing the banner (CLI)
set_avoid_print_banner_overwrite(True)

# Initialises the default paths for the compiler using the work directory
initialise_default_paths(BASE_TEST_PATH)


class TestProcessing:
    @staticmethod
    def teardown_method(_):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
         """
        reset_input()

    def test_parse_preprocessor_targets(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_processor_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            b_path: Path = add_folder("build")
            d_path: Path = add_folder("dist")

            asyncio.run(ProgramCompilationProcess(
                [file.path], Path(str(file.path)).parent, 'utf-8',
                build_path=b_path, dist_path=d_path
            ).preprocess_files(True))

            remove_folder("build")
            remove_folder("dist")

    def test_parse_c_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_c_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".c") or entry.path.endswith(".h"):
                files.append(entry)

        for file in files:
            b_path: Path = add_folder("build")
            d_path: Path = add_folder("dist")

            asyncio.run(ProgramCompilationProcess(
                [file.path], Path(file.path).parent, 'utf-8',
                build_path=b_path, dist_path=d_path
            ).preprocess_files(True))

            remove_folder("build")
            remove_folder("dist")

    def test_parse_para_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_para_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            b_path: Path = add_folder("build")
            d_path: Path = add_folder("dist")

            asyncio.run(ProgramCompilationProcess(
                [file.path], Path(file.path).parent, 'utf-8',
                build_path=b_path, dist_path=d_path
            ).preprocess_files(True))

            remove_folder("build")
            remove_folder("dist")
