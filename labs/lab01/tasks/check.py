#!/usr/bin/env python3

import pytest
import sys
from shutil import copyfile

@pytest.fixture(scope = 'function')
def use_stdin():
    def _work(file_name : str):
        fd_in = open('./tests/testcases/{}_in.txt'.format(file_name), 'r')
        def mock_input():
            return fd_in.readline()
        return mock_input
    return _work
        
@pytest.fixture(scope = 'function')
def use_file_input():
    def _work(file_name : str):
        copyfile('./tests/testcases/{}_in.txt'.format(file_name), 
                 './tests/samples/{}_in.txt'.format(file_name.split('_')[0]))
    return _work

def check_stdout(capsys, file_name : str):
    out, err = capsys.readouterr()
    with open('./tests/testcases/{}_out.txt'.format(file_name), 'r') as fd_out:
        assert out == fd_out.read()

class Test_Task01():
    def run_task(self, capsys, use_stdin, test_name : str):
        import task01
        task01.input = use_stdin(test_name)
        task01.main()
        check_stdout(capsys, test_name)

    def test_task01_a(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task01_a')

    def test_task01_b(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task01_b')

class Test_Task02():
    def run_task(self, capsys, use_stdin, test_name : str):
        import task02
        task02.input = use_stdin(test_name)
        task02.main()
        check_stdout(capsys, test_name)

    def test_task02_a(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task02_a')

    def test_task02_b(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task02_b')

    def test_task02_c(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task02_c')


class Test_Task03():
    def run_task(self, capsys, use_stdin, test_name : str):
        import task03
        task03.input = use_stdin(test_name)
        task03.main()
        check_stdout(capsys, test_name)

    def test_task03_a(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task03_a')

    def test_task03_b(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task03_b')

    def test_task03_c(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task03_c')

class Test_Task04():
    def run_task(self, capsys, use_file_input, test_name : str):
        import task04
        task04.main()
        check_stdout(capsys, test_name)

    def test_task04_a(self, capsys, use_file_input):
        use_file_input('task04_a')
        self.run_task(capsys, use_file_input, 'task04_a')

    def test_task04_b(self, capsys, use_file_input):
        use_file_input('task04_b')
        self.run_task(capsys, use_file_input, 'task04_b')

class Test_Task05():
    def run_task(self, capsys, use_stdin, test_name : str):
        import task05
        task05.input = use_stdin(test_name)
        task05.main()
        check_stdout(capsys, test_name)

    def test_task05_a(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task05_a')

    def test_task05_b(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task05_b')

class Test_Task06():
    def run_task(self, capsys, use_stdin, test_name : str):
        import task06
        task06.input = use_stdin(test_name)
        task06.main()
        check_stdout(capsys, test_name)

    def test_task06_a(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task06_a')

class Test_Task07():
    def run_task(self, capsys, use_stdin, test_name : str):
        import task07
        task07.input = use_stdin(test_name)
        task07.main()
        check_stdout(capsys, test_name)

    def test_task07_a(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task07_a')

    def test_task07_b(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task07_b')

class Test_Task08():
    def run_task(self, capsys, use_stdin, test_name : str):
        import task08
        task08.input = use_stdin(test_name)
        task08.main()
        check_stdout(capsys, test_name)

    def test_task08_a(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task08_a')

    def test_task08_b(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task08_b')

class Test_Task09():
    def run_task(self, capsys, use_stdin, test_name : str):
        import task09
        task09.input = use_stdin(test_name)
        task09.main()
        check_stdout(capsys, test_name)

    def test_task09_a(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task09_a')

    def test_task09_b(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task09_b')

class Test_Task10():
    def run_task(self, capsys, use_stdin, test_name : str):
        import task10
        task10.input = use_stdin(test_name)
        task10.main()
        check_stdout(capsys, test_name)

    def test_task10_a(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task10_a')

    def test_task10_b(self, capsys, use_stdin):
        self.run_task(capsys, use_stdin, 'task10_b')