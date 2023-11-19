import subprocess
import os
import unittest

class TestProgram(unittest.TestCase):
    test_dir = './test'
    prog_dir = './prog'

    def run_test(self, program, test_name, use_args=False):
        input_file = f'{self.test_dir}/{program}.{test_name}.in'
        expected_file = f'{self.test_dir}/{program}.{test_name}.arg.out'  # Use '.arg.out' for tests with arguments
        cmd = ['python', os.path.join(self.prog_dir, f"{program}.py")]
        
        if use_args:
            with open(input_file, 'r') as f:
                # Assuming the input file contains the paths to the JSON files on separate lines
                file1_path, file2_path = [line.strip() for line in f.readlines()]
                cmd.extend([file1_path, file2_path])
            
            process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            actual_output = process.stdout.decode('utf-8')
    
            self.assertEqual(process.returncode, 0, f"Standard Error Output: {process.stderr.decode('utf-8')}")
    
        # Rest of the code...
        
        with open(expected_file, 'r') as f:
            expected_output = f.read().strip()
        
        self.assertEqual(actual_output.strip(), expected_output,
                         f"Failed test: {program}.{test_name} with {'arguments' if use_args else 'stdin'}")


    
    def test_compare_json(self):
        self.run_test('compare_json', 'test1', use_args=True)


    def test_wc(self):
        #self.run_test('wc', 'test1', use_args=True)
        self.run_test('wc', 'test1', use_args=False)

    def test_gron(self):
        self.run_test('gron', 'test1')
        #self.run_test('gron', 'test2', use_args=True)

if __name__ == '__main__':
    unittest.main()
