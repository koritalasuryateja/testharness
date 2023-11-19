import subprocess
import os
import unittest

class TestProgram(unittest.TestCase):
    test_dir = './test'
    prog_dir = './prog'

    def run_test(self, program, test_name, use_args=False):
        input_file = f'{self.test_dir}/{program}.{test_name}.in'
        expected_file = f'{self.test_dir}/{program}.{test_name}' + ('.arg.out' if use_args else '.out')
        
        # If use_args is True, the input should be passed as a command-line argument
        cmd = ['python', os.path.join(self.prog_dir, f"{program}.py")]
       if use_args:
            process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.assertEqual(process.returncode, 0, f"Standard Error Output: {process.stderr.decode('utf-8')}")
            actual_output = process.stdout.decode('utf-8')

        else:
            with open(input_file, 'rb') as f:
                process = subprocess.run(cmd, stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.assertEqual(process.returncode, 0)
                actual_output = process.stdout.decode('utf-8')
        
        # When use_args is True, we need to execute the program again
        # as some programs might behave differently when using arguments vs. stdin
        if use_args:
            process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.assertEqual(process.returncode, 0)
            actual_output = process.stdout.decode('utf-8')
        
        with open(expected_file, 'r') as f:
            expected_output = f.read().strip()
        
        self.assertEqual(actual_output.strip(), expected_output,
                         f'Failed test: {program}.{test_name} with {"arguments" if use_args else "stdin"}')
    
    def test_compare_json(self):
        self.run_test('compare_json', 'test1')
        self.run_test('compare_json', 'test2')

    def test_wc(self):
        #self.run_test('wc', 'test1', use_args=True)
        self.run_test('wc', 'test1', use_args=False)

    def test_gron(self):
        self.run_test('gron', 'test1')
        #self.run_test('gron', 'test2', use_args=True)

if __name__ == '__main__':
    unittest.main()
