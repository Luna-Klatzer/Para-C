# coding=utf-8
""" Tests for the Pre-Processor Lexer and Parser """
import logging
import os
from typing import List

import paraccompiler
from paraccompiler import ParacCompiler, ProgramCompilationProcess
from . import reset_input
from .. import add_folder, remove_folder

logger = logging.getLogger('paraccompiler')

sep = paraccompiler.SEPARATOR
compiler = ParacCompiler()
paraccompiler.para_compiler.init_logging_session(
    level=logging.DEBUG, print_banner=False
)
paraccompiler.set_avoid_print_banner_overwrite(True)
test_c_files_dir = f"{os.getcwd()}{sep}test_files{sep}c_files{sep}"
test_para_files_dir = f"{os.getcwd()}{sep}test_files{sep}"
test_files_dir = f"{os.getcwd()}{sep}test_files{sep}preprocessor{sep}"


class TestParser:
    @staticmethod
    def teardown_method(_):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
         """
        reset_input()

    def test_parse_preprocessor_targets(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            logger.debug(f"Parsing {file.path}")
            b_path = add_folder("build")
            d_path = add_folder("dist")
            
            ProgramCompilationProcess(
                file.path, 'utf-8', build_path=b_path, dist_path=d_path
            )._run_preprocessor(True)
            
            remove_folder("build")
            remove_folder("dist")

    def test_parse_c_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_c_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".c") or entry.path.endswith(".h"):
                files.append(entry)

        for file in files:
            logger.debug(f"Parsing {file.path}")
            b_path = add_folder("build")
            d_path = add_folder("dist")

            ProgramCompilationProcess(
                file.path, 'utf-8', build_path=b_path, dist_path=d_path
            )._run_preprocessor(True)

            remove_folder("build")
            remove_folder("dist")

    def test_parse_para_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_para_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            logger.debug(f"Parsing {file.path}")
            b_path = add_folder("build")
            d_path = add_folder("dist")

            ProgramCompilationProcess(
                file.path, 'utf-8', build_path=b_path, dist_path=d_path
            )._run_preprocessor(True)

            remove_folder("build")
            remove_folder("dist")
