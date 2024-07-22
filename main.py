import pygame
import random
import winsound
pygame.init()
# icon
pygame.display.set_caption("Basket_By_Yafai")
logo = pygame.image.load('assets/images/4.png')
pygame.display.set_icon(logo)


# screen
screen_width = 700
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
gameOn = True
# colours
black = (0, 0, 0)
white = (255, 255, 255)


# variables
def GameLoop():
    baseX = 0
    baseY = screen_height
    ballX = 120
    ballY = baseY-60
    gravity = 9.8
    bouncing = 25
    fps = 60
    clock = pygame.time.Clock()

    def getPoleY(baseY):
        return random.randrange(100, baseY-200)

    # background
    background = pygame.image.load("assets/images/background.png")
    base = pygame.image.load("assets/images/road.jpg").convert_alpha()
    ball = pygame.image.load("assets/images/basketball.png")
    pole = pygame.image.load("assets/images/pole.png").convert_alpha()
    basket = pygame.image.load("assets/images/basket.png").convert_alpha()

    # music
    winsound.PlaySound("assets/sound/1.wav",
                       winsound.SND_LOOP + winsound.SND_ASYNC)
    # pygame.mixer.music.load("assets/sound/1.wav")
    # pygame.mixer.music.set_volume(0.6)
    # pygame.mixer.music.play()
    channel0 = pygame.mixer.Channel(0)
    channel1 = pygame.mixer.Channel(1)
    channel2 = pygame.mixer.Channel(2)
    #lost_music = pygame.mixer.Sound("assets/sound/loss1.wav")
    #bounce_music = pygame.mixer.music.load("assets/sound/2.wav")
    #extra_point = pygame.mixer.music.load("assets/sound/3.wav")

    def moving_base(baseX, baseY, base):
        #baseX = 0
        #baseY = screen_height-60
        screen.blit(base, (baseX, baseY))
        screen.blit(base, (baseX+screen_width-10, baseY))

    def collison(poleX, poley, ballX, ballY):
        if (ballX >= poleX and ballX <= poleX+50 and ballY > poley):
            return True
        elif (ballY <= -10):
            return True

        return False

    def Screen_text(text, colour, x, y, size, style, bold=False, itallic=False):
        font = pygame.font.SysFont(style, size, bold=bold, italic=itallic)
        screen_text = font.render(text, True, colour)
        screen.blit(screen_text, (x, y))

    def random_basket(poley, baseY):
        return random.randrange(poley+100, baseY-100)

    def getHighestScore():
        with open("highest score.txt", "r") as f:
            return f.read()

    def getBasketScore():
        with open("Basket_high_score", "r") as f:
            return f.read()

    def main():
        gameOn = True
        baseY = screen_height-60
        ballY = baseY-60
        gravity = 9.8
        bouncing = 25
        poleX = 400
        poley = getPoleY(baseY)
        poleX_velocity = 0
        baseX_velocity = 0
        speed = 0
        baseX = 0
        Game_over = False
        red = (255, 0, 0)
        blue = (54, 69, 79)
        basketY = random_basket(poley, baseY)
        basket_score = 0
        score = 0
        speed_accelerating = False
        gameSpeed = 0

        try:
            highestScore = int(getHighestScore())
        except:
            highestScore = 0
        try:
            basket_high_score = int(getBasketScore())
        except:
            basket_high_score = 0

        while gameOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOn = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if Game_over == False:
                            gameSpeed = 0.01
                            bouncing = 25
                            speed = 5
                            baseX_velocity = int(speed)
                            poleX_velocity = int(speed)
            basketX = poleX+35

            screen.blit(background, (0, 0))
            screen.blit(pole, (poleX, poley))
            moving_base(baseX, baseY, base)
            screen.blit(basket, (basketX, basketY))
            screen.blit(ball, (ballX, ballY))

            ballY -= bouncing
            bouncing -= 1
            ballY += gravity
            if (ballY > baseY-20):
                channel2.play(pygame.mixer.Sound("assets/sound/2.wav"))

                bouncing = 25

            Game_over = collison(poleX, poley, ballX, ballY,)
            if Game_over:

                Screen_text("Game Over ",
                            red, 200, 200, 60, "Arial", bold=True)
                Screen_text("PRESSED SPACE TO CONTINUE ",
                            black, 150, 300, 30, "Arial", bold=True)
                Screen_text("CREATED BY ARSALAAN_YAFAI ",
                            blue, 0, 500, 30, "Arial", bold=True)
                # channel0.play(pygame.mixer.Sound("assets/sound/5.wav"))
                speed = 0
                bouncing = 0
                gravity = 0
                poleX_velocity = 0
                baseX_velocity = 0
                basket_score = 0

                if (event.type == pygame.QUIT):
                    pygame.quit()
                # elif event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_SPACE:
                    # main()

                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    score = 0
                    main()

            if (ballX+ball.get_width() >= basketX and ballX <= basketX+basket.get_width() and ballY > basketY and ballY <= basketY+ball.get_height()):
                channel1.play(pygame.mixer.Sound("assets/sound/3.wav"))
                pygame.mixer.music.set_volume(0.6)
                channel1.set_volume(0.6)

                basket_score += 1
            # accelerating
            speed += gameSpeed
            # score
            score += int(speed)
            # displaying score
            Screen_text(f"Total_Score{score}",
                        black, 10, 10, size=20, style="Calibri")
            Screen_text(f"Basket_Score{basket_score}",
                        black, 10, 40, size=20, style="Calibri")

            # writing high score

            if (highestScore < score):
                highestScore = score
            with open("highest score.txt", "w") as f:
                f.write(str(highestScore))
            Screen_text(f"Highest Score{highestScore}", red,
                        screen_width-200, 10, size=24, style="Calibri")
            if (basket_high_score < basket_score):
                basket_high_score = basket_score
            with open("Basket_high_score", "w") as f:
                f.write(str(basket_high_score))
            Screen_text(f"Basket High Score{basket_high_score}", red,
                        screen_width-200, 40, size=24, style="Calibri")

            pygame.display.update()
            clock.tick(fps)

            # moving pole
            poleX += -poleX_velocity
            if (poleX < -100):
                poleX = screen_width + 10
                poley = getPoleY(baseY)

            # moving base
            baseX += -baseX_velocity
            if (baseX <= -screen_width):
                baseX = 0

    main()


GameLoop()
