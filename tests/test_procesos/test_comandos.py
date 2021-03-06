import os

import pytest

from scripts.procesos.comandos import cmd_output, execute


@pytest.mark.parametrize(
    "cmd_test, output_test",
    [
        ("pwd", os.environ["PWD"]),
        ("echo $USER", os.environ["USER"]),
        ("sl", ""),
        ("-", ""),
    ],
)
def test_cmd_output(cmd_test, output_test):
    assert cmd_output(cmd_test) == output_test


@pytest.mark.parametrize(
    "cmd_test",
    [(False), (10), (1.6), ([]), (()), ({})],
)
def test_cmd_output_exception(cmd_test):
    with pytest.raises(Exception) as info:
        cmd_output(cmd_test)
        assert str(info) == "Tipo no valido"


@pytest.mark.parametrize(
    "cmd_test, output_test",
    [
        ("pwd", True),
        ("echo $USER", True),
        ("sl", False),
        ("-", False),
    ],
)
def test_execute(cmd_test, output_test):
    assert execute(cmd_test) == output_test


@pytest.mark.parametrize(
    "cmd_test",
    [(False), (10), (1.6), ([]), (()), ({})],
)
def test_execute_exception(cmd_test):
    with pytest.raises(Exception) as info:
        execute(cmd_test)
        assert str(info) == "Tipo no valido"
