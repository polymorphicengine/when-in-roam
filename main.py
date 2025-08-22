import library.game as game

if __name__ == '__main__':
    try:
        game.performance()
    except Exception as e:
        print(e)
        game.shutdown()
