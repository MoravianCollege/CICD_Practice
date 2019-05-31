from practice.generator import create_string, create_big_string

def test_string_generator():
	assert create_string() == "strung"

def test_big_string_generator():
	assert create_big_string() == "this is a pretty big string"
