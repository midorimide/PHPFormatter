from config import Config
from os import path
import sys as sys
import re

default_config = Config()

def format(input_file, output_file, config):
	with open(input_file) as input:
		code = str(input.read())

		code = process_keep_indents_on_empty_lines(code, config.keep_indents_on_empty_lines)
		code = process_spaces_before_parentheses(code, config.spaces_before_parentheses)
		code = process_spaces_around_concatenation_operator(code, config.spaces_around_concatenation_operator)
		code = process_spaces_around_object_access_operator(code, config.spaces_around_object_access_operator)
		code = process_spaces_around_null_coalescing_operator(code, config.spaces_around_null_coalescing_operator)
		#code = process_spaces_around_assignment_in_declare_statement(code, config.spaces_around_assignment_in_declare_statement)
		code = process_spaces_before_class_left_brace(code, config.spaces_before_class_left_brace)
		code = process_spaces_within_brackets(code, config.spaces_within_brackets)
		code = process_spaces_within_brackets_around_variables_expressions(code, config.spaces_within_brackets_around_variables_expressions)
		code = process_spaces_in_ternary_operator(code, config.spaces_in_ternary_operator)
		code = process_spaces_after_type_cast(code, config.spaces_after_type_cast)
		code = process_indent_code_in_php_tag(code, config.indent_code_in_php_tag, config.use_tab_character, config.tab_size)
		code = process_operators(code, config.spaces_around_operators)
		code = process_colon_and_coma(code, True)

		with open(output_file, 'w') as output:
			output.write(str(code))
	pass

def process_indent_code_in_php_tag(code, need, use_tab, space_count):
	indent = 0
	result = ''
	arr = code.split('\n')
	indent_symbol = '\t' if use_tab else ' ' * space_count
	for i, line in enumerate(arr):
		line = line.strip('\t')
		line = line.strip(' ')
		indent -= line.count('}')
		indent -= line.count('?>')
		result += indent_symbol * indent + line + ('\n' if i + 1 < len(arr) else '')
		indent += line.count('{')
		if need == True:
			indent += line.count('<?php')
	return result

def process_keep_indents_on_empty_lines(code, need):
	result = ''
	arr = code.split('\n')
	for i, line in enumerate(arr):
		indents_only = True
		for symbol in line:
			if not symbol in ['\t', ' ']:
				indents_only = False
				break
		if indents_only and not need:
			result += ('\n' if i + 1 < len(arr) else '')
		else:
			result += line + ('\n' if i + 1 < len(arr) else '')
	return result

def process_spaces_after_type_cast(code, need):
	code = str(code)
	pattern = r'(\(.*?\))(\s*)[$]'

	def trueSub(m):
		return m.group(1) + ' $'

	def falseSub(m):
		return m.group(1) + '$'

	if need == True:
		return re.sub(pattern, trueSub, code)
	else:
		return re.sub(pattern, falseSub, code)

def process_spaces_in_ternary_operator(code, need):
	code = str(code)
	pattern = r'(\s*)[?](\s*)(.*?)(\s*)[:](\s*)'

	def trueSub(m):
		return ' ? ' + m.group(3) + ' : '

	def falseSub(m):
		return '?' + m.group(3) + ':'

	if need == True:
		return re.sub(pattern, trueSub, code)
	else:
		return re.sub(pattern, falseSub, code)

def process_spaces_within_brackets_around_variables_expressions(code, need):
	return code

def process_spaces_within_brackets(code, need):
	return code

def process_spaces_before_class_left_brace(code, need):
	code = str(code)
	pattern = r'(class .*?)(\s*){'

	def trueSub(m):
		return m.group(1) + ' {'

	def falseSub(m):
		return m.group(1) + '{'

	if need == True:
		return re.sub(pattern, trueSub, code)
	else:
		return re.sub(pattern, falseSub, code)

def process_spaces_around_assignment_in_declare_statement(code, need):
	code = str(code)
	pattern = r'(\s*)[=](\s*)'

	def trueSub(m):
		return ' = '

	def falseSub(m):
		return '='

	if need == True:
		return re.sub(pattern, trueSub, code)
	else:
		return re.sub(pattern, falseSub, code)

def process_spaces_around_null_coalescing_operator(code, need):
	code = str(code)
	pattern = r'(\s*)[?][?](\s*)'

	def trueSub(m):
		return ' ?? '

	def falseSub(m):
		return '??'

	if need == True:
		return re.sub(pattern, trueSub, code)
	else:
		return re.sub(pattern, falseSub, code)

def process_spaces_around_object_access_operator(code, need):
	code = str(code)
	pattern = r'(\s*)->(\s*)'

	def trueSub(m):
		return ' -> '

	def falseSub(m):
		return '->'

	if need == True:
		return re.sub(pattern, trueSub, code)
	else:
		return re.sub(pattern, falseSub, code)

def process_spaces_around_concatenation_operator(code, need):
	code = str(code)
	pattern = r'(\s*)[.](\s*)'

	def trueSub(m):
		return ' . '

	def falseSub(m):
		return '.'

	if need == True:
		return re.sub(pattern, trueSub, code)
	else:
		return re.sub(pattern, falseSub, code)

def process_spaces_before_parentheses(code, need):
	code = str(code)
	pattern = r'(\s*)\('

	def trueSub(m):
		return ' ('

	def falseSub(m):
		return '('

	if need == True:
		return re.sub(pattern, trueSub, code)
	else:
		return re.sub(pattern, falseSub, code)

def process_operators(code, need):
	code = str(code)
	pattern = r'(\s*)((?:\=\=\=)|(?:\!\=\=)|(?:\=\=)|(?:\<\<\=)|(?:\>\>\=)|(?:\<\=)|(?:\>\=)|(?:\=\>)|(?:\<\<)|(?:\>\>)|(?:(?<![?-])\>)|(?:\<(?!\?))|(?:\!\=)|(?:\=)|(?:\+\=)|(?:\-\=)|(?:\*\=)|(?:\/\=)|(?:\&\=)|(?:\|\=)|(?:\^\=)|(?:(?<!\+)\+(?!\+))|(?:(?<!\-)\-(?![>-]))|(?:\*)|(?:\/)|(?:\&\&)|(?:\|\|)|(?:\^)|(?:\&)|(?:\|))(\s*)'

	def trueSub(m):
		return ' ' + m.group(2) + ' '

	def falseSub(m):
		return m.group(2)

	if need == True:
		return re.sub(pattern, trueSub, code)
	else:
		return re.sub(pattern, falseSub, code)

def process_colon_and_coma(code, need):
	code = str(code)
	pattern = r'([;,])(\S)'

	def trueSub(m):
		return m.group(1) + ' ' + m.group(2)

	def falseSub(m):
		return m.group(1) + m.group(2)

	if need == True:
		return re.sub(pattern, trueSub, code)
	else:
		return re.sub(pattern, falseSub, code)

if __name__ == '__main__':
	input_file = str(sys.argv[1])
	config_file = str(sys.argv[2]) if len(sys.argv) == 3 else ''
	config = Config.read_from_file(config_file)

	name, ext = path.basename(input_file).split('.')
	output_file = name + '_formatted.' + ext
	format(input_file, output_file, config)