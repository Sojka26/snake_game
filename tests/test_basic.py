import pytest
def test_import_game_module():
    
    import snake
    assert hasattr(snake, "main") or hasattr(snake, "run")