def parse_boolean(string):
    return string.strip() in ['True', 'true', 'y', 'Y', 'yes', 'Yes']

class Config:
    indent_code_in_php_tag = False
    use_tab_character = False
    tab_size = 4
    indent = 4
    continuation_indent = 1
    keep_indents_on_empty_lines = False
    spaces_before_parentheses = False
    spaces_around_operators = True
    spaces_around_concatenation_operator = False
    spaces_around_object_access_operator = False
    spaces_around_null_coalescing_operator = False
    spaces_around_assignment_in_declare_statement = False
    spaces_before_class_left_brace = False
    spaces_within_brackets = False
    spaces_within_brackets_around_variables_expressions = False
    spaces_in_ternary_operator = False
    spaces_after_type_cast = False

    @staticmethod
    def read_from_file(file_name):
        config = Config()
        with open(file_name, 'r') as config_reader:
            for line in config_reader:
                option = line.split(' = ')
                if option[0] == 'Indent code in PHP tags':
                    config.indent_code_in_php_tag = parse_boolean(option[1])
                if option[0] == 'Use tab character':
                    config.use_tab_character = parse_boolean(option[1])
                if option[0] == 'Tab size':
                    config.tab_size = int(option[1])
                if option[0] == 'Indent':
                    config.indent = int(option[1])
                if option[0] == 'Continuation indent':
                    config.continuation_indent = int(option[1])
                if option[0] == 'Keep indents on empty lines':
                    config.keep_indents_on_empty_lines = parse_boolean(option[1])
                if option[0] == 'Spaces before parentheses':
                    config.spaces_before_parentheses = parse_boolean(option[1])
                if option[0] == 'Spaces around operators':
                    config.spaces_around_operators = parse_boolean(option[1])
                if option[0] == 'Spaces around concatenation operator':
                    config.spaces_around_concatenation_operator = parse_boolean(option[1])
                if option[0] == 'Spaces around object access operator':
                    config.spaces_around_object_access_operator = parse_boolean(option[1])
                if option[0] == 'Spaces around null coalescing operator':
                    config.spaces_around_null_coalescing_operator = parse_boolean(option[1])
                if option[0] == 'Spaces around assignment in declare statement':
                    config.spaces_around_assignment_in_declare_statement = parse_boolean(option[1])
                if option[0] == 'Spaces before class left brace':
                    config.spaces_before_class_left_brace = parse_boolean(option[1])
                if option[0] == 'Spaces within brackets':
                    config.spaces_within_brackets = parse_boolean(option[1])
                if option[0] == 'Spaces within brackets around variables/expressions':
                    config.spaces_within_brackets_around_variables_expressions = parse_boolean(option[1])
                if option[0] == 'Spaces in ternary operator':
                    config.spaces_in_ternary_operator = parse_boolean(option[1])
                if option[0] == 'Spaces after type cast':
                    config.spaces_after_type_cast = parse_boolean(option[1])
        return config