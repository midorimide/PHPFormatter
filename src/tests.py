import unittest
import random, string
from config import Config
import PHPFormatter as phpformatter
import os
import os.path
import time

def random_word(length = 8):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

def run_test(input, expectedOutput, formatterConfig):
	tmp_filename = random_word()
	inputFilename = 'tmp/' + tmp_filename + '.in'
	outputFilename = 'tmp/' + tmp_filename + '.out'

	with open(inputFilename, 'w') as inputFile:
		inputFile.write(input)

	phpformatter.format(inputFilename, outputFilename, formatterConfig)

	output = ''
	with open(outputFilename) as outputFile:
		output = outputFile.read()

	os.remove(inputFilename)
	os.remove(outputFilename)

	result = (output == expectedOutput)

	if result == False:
		print('You printed \"' + output + '\", instead of \"' + expectedOutput + '\"\n')

	return result

class TestClass(unittest.TestCase):

	def test_before_parentheses(self):
		config = Config()
		config.spaces_before_parentheses = True

		input = '$array=array(0=>"zero",1=>"one");'
		output = '$array = array (0 => "zero", 1 => "one");'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_around_concatenation_operator(self):
		config = Config()
		config.spaces_around_concatenation_operator = True

		input = 'echo "The result is ".$i;'
		output = 'echo "The result is " . $i;'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_around_object_access_operator(self):
		config = Config()
		config.spaces_around_object_access_operator = True

		input = '$obj->foo()->bar();'
		output = '$obj -> foo() -> bar();'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_around_null_coalescing_operator(self):
		config = Config()
		config.spaces_around_null_coalescing_operator = True

		input = 'foo()??bar();'
		output = 'foo() ?? bar();'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_around_assignment_in_declare_statement(self):
		config = Config()
		config.spaces_around_assignment_in_declare_statement = True

		input = 'declare(strict_types=1);'
		output = 'declare(strict_types = 1);'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_before_left_brace(self):
		config = Config()
		config.spaces_before_class_left_brace = True
		config.use_tab_character = True

		input = 'class Class1{\n\tfunction Foo()\n}'
		output = 'class Class1 {\n\tfunction Foo()\n}'

		result = run_test(input, output, config)

		self.assertTrue(result)


	def test_ternary_operator(self):
		config = Config()
		config.spaces_in_ternary_operator = True

		input = 'x?y:z'
		output = 'x ? y : z'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_after_explicit_cast(self):
		config = Config()
		config.spaces_after_type_cast = True

		input = '$fst=(string)$foo;'
		output = '$fst = (string) $foo;'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_around_binary_operators(self):
		config = Config()
		config.spaces_around_operators = True

		input = '1+2-3*4/5<<1>>2&1|2^3&&4||5'
		output = '1 + 2 - 3 * 4 / 5 << 1 >> 2 & 1 | 2 ^ 3 && 4 || 5'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_around_comparison_operators(self):
		config = Config()
		config.spaces_around_operators = True

		input = '1<2>3<=4>=5==6!=7===8!==9'
		output = '1 < 2 > 3 <= 4 >= 5 == 6 != 7 === 8 !== 9'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_around_assignment_operators(self):
		config = Config()
		config.spaces_around_operators = True

		input = '1=2;\n1+=2;\n1-=3;\n1*=4;\n1/=5;\n1<<=1;\n1>>=2;\n1&=1;\n1|=2;\n1^=3;\n'
		output = '1 = 2;\n1 += 2;\n1 -= 3;\n1 *= 4;\n1 /= 5;\n1 <<= 1;\n1 >>= 2;\n1 &= 1;\n1 |= 2;\n1 ^= 3;\n'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_nested_blocks(self):
		config = Config()
		config.indent_code_in_php_tag = True
		config.use_tab_character = True

		input = 'if($x){\nif($x){\nif($x){\n$x=1;\n}\n}\n}'
		output = 'if($x){\n\tif($x){\n\t\tif($x){\n\t\t\t$x = 1;\n\t\t}\n\t}\n}'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_for_operator(self):
		config = Config()

		input = 'for($i=0;i<5;++i)'
		output = 'for($i = 0; i < 5; ++i)'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_keep_indents_on_empty_lines(self):
		config = Config()
		config.keep_indents_on_empty_lines = False

		input = '   \t\t  \n'
		output = '\n'

		result = run_test(input, output, config)

		self.assertTrue(result)

	def test_indent_code_in_php_tag(self):
		config = Config()
		config.indent_code_in_php_tag = True
		config.use_tab_character = True

		input = '<?php\n$x = 1;\n?>'
		output = '<?php\n\t$x = 1;\n?>'

		result = run_test(input, output, config)

		self.assertTrue(result)


if __name__ == '__main__':
	unittest.main()