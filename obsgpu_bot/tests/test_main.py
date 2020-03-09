import main
import inspect

def test_load_configs():
	t = type(main.loadConfigs())
	assert t is dict or t is None
