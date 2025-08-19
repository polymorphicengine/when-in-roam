import library.game as game
import library.display as display
import library.video as video

if __name__ == '__main__':
    try:
        video.play_video()
        display.display_loop_thread()
        game.second_game()
        while True:
            continue
    except:
        game.shutdown()
