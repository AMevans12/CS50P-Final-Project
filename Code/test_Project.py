from Final import password_generator, exit_win, clipboard, strength , get_password_length

def main():
    test_get_password_length()
    test_clipboard()
    test_strength()

def test_get_password_length():
    assert get_password_length() >= 1
    
def test_clipboard():
    clipboard()

def test_strength():
    assert isinstance(strength(""), str)

if __name__ == '__main__':
    main()