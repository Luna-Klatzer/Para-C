# coding=utf-8
""" Test for the compiler process setup """
from pathlib import Path

from parac import initialise_default_paths
from parac.compiler import ProgramCompilationProcess
from .. import add_folder, BASE_TEST_PATH

main_file_path: Path = Path(BASE_TEST_PATH) / "test_files" / "entry.para"

# Initialises the default paths for the compiler using the work directory
initialise_default_paths(BASE_TEST_PATH)


class TestProcess:
    def test_init(self):
        b_path: Path = add_folder("build")
        d_path: Path = add_folder("dist")
        p = ProgramCompilationProcess(
            main_file_path, 'utf-8', b_path, d_path
        )

        assert p.build_path == b_path
        assert p.dist_path == d_path

    def test_bytes_init(self):
        path = str(main_file_path).encode()

        b_path: bytes = str(add_folder("build")).encode()
        d_path: bytes = str(add_folder("dist")).encode()
        p: ProgramCompilationProcess = ProgramCompilationProcess(
            path, 'utf-8', b_path, d_path
        )

        assert p.build_path == Path(b_path.decode())
        assert p.dist_path == Path(d_path.decode())
