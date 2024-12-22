import pytest
from main import (
    get_player_card,
    get_computer_card,
    get_answer,
    current_score,
    print_score,
    who_wins
)


@pytest.fixture
def mock_deck():
    return ['ace', 'king', 'queen', 'jack', 'ten']


def test_get_player_card(monkeypatch):
    monkeypatch.setattr('random.choice', lambda x: 'ace')
    hand = []
    result = get_player_card(hand)
    assert result == ['ace']


def test_get_computer_card(monkeypatch):
    monkeypatch.setattr('random.choice', lambda x: 'king')
    hand = []
    result = get_computer_card(hand)
    assert result == ['king']


def test_get_answer(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    action = "another card"
    result = get_answer(action)
    assert result == 'y'


@pytest.mark.parametrize(
    "hand, expected_score",
    [
        (['ace', 'king'], 21),
        (['ace', 'ace'], 12),
        (['ten', 'nine'], 19),
        (['five', 'king', 'seven'], 22),
    ]
)
def test_current_score(hand, expected_score):
    result = current_score(hand)
    assert result == expected_score


def test_print_score(capsys):
    print_score("Your", 21)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Your score is 21"


@pytest.mark.parametrize(
    "computer_hand, player_score, expected_output",
    [
        (['ace', 'seven'], 21, "You win!"),
        (['king', 'ten'], 20, "Draw!"),
    ]
)
def test_who_wins(computer_hand, player_score, expected_output, capsys, monkeypatch):
    monkeypatch.setattr('main.get_computer_card', lambda x: computer_hand)
    who_wins(computer_hand, current_score(computer_hand), player_score)
    captured = capsys.readouterr()
    assert expected_output in captured.out
