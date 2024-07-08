import unittest
from unittest.mock import patch
import io
from main import todo_app

class TestTodoApp(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        'add', 'buy milk',
        'add', 'walk the dog',
        'show',
        'edit', '2', 'walk the cat',
        'show',
        'exit'
    ])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_todo_app(self, mock_stdout, mock_input):
        todo_list = todo_app()
        output = mock_stdout.getvalue()

        # Check the final state of the todo_list
        self.assertEqual(todo_list, ['Buy Milk', 'Walk The Cat'])

        # Check the printed output
        expected_output = (
            "Buy Milk\n"
            "Walk The Dog\n"
            "Buy Milk\n"
            "Walk The Cat\n"
            "Goodbye!\n"
        )
        self.assertIn(expected_output, output)

if __name__ == '__main__':
    unittest.main()