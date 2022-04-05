import pygame #thư viên game
import time

pygame.init() #khởi tạo game
Screen = pygame.display.set_mode((600, 300)) # kích thước màn hình ngang x dọc
pygame.display.set_caption('GAME KHỦNG LONG') # tiêu đề

#background
Background_x = 0
Background_y = 0
#khủng long
Dino_x = 30
Dino_y = 230
#cây
Tree_x = 550
Tree_y = 230
#speed
x_velocity = 5 #tốc độ di chuyển mặt đất + cây
y_velocity = 7 #hight nhảy
# Load Image
Background = pygame.image.load('.\\Assets\\image\\background.jpg')
Dino = pygame.image.load('.\\Assets\\image\\dinosaur.png')
Tree = pygame.image.load('.\\Assets\\image\\tree.png')
Game_Over = pygame.image.load('.\\Assets\\image\\gameover.png')
Intro = pygame.image.load('.\\Assets\\image\\message.png')
# Load Sound
Sound_jump = pygame.mixer.Sound('.\\Assets\\Sound\\tick.wav')
Sound_game_over = pygame.mixer.Sound('.\\Assets\\Sound\\te.wav')
Clock = pygame.time.Clock()
jump = False #nhảy
Pausing = False #dừng
Score = 0 # điểm
Font_score = pygame.font.SysFont('san', 20) #tạo font điểm
Font_score_Gameover = pygame.font.SysFont('san', 30) #tạo font điểm
Font_game_over = pygame.font.SysFont('san', 20) #tạo font Game over

WHITE = (255, 255, 255) # Màu trắng - rgb color
RED = (255, 0, 0) #Màu đỏ - rgb color
DIMGRAY = (105, 105, 105) #màu đen - rgb color
Running = True
content = True

def Menu():
    Screen.fill(WHITE)
    Screen.blit(Background, (Background_x, Background_y))
    Screen.blit(Background, (Background_x + 600, Background_y))
    Dino_rect = Screen.blit(Dino, (Dino_x, Dino_y))  # hiển thị khủng long
    Tree_rect = Screen.blit(Tree, (Tree_x, Tree_y))  # hiển thị cây
    Screen.blit(Intro, (200, 1))
    Game_Start_text = Font_game_over.render("-Press 'Space' to Start.!-", True, DIMGRAY)
    Screen.blit(Game_Start_text, (220, 280))

def PlayGame():
    global Score, Dino_x, Dino_y, Background_x, Background_y, Tree_x, Tree_y, x_velocity, y_velocity, jump, Pausing, Running

    while Running:
        Clock.tick(60)  # nháy 60 lần/s
        Screen.fill(WHITE)
        # add image vào game
        Background1_rect = Screen.blit(Background, (Background_x, Background_y))
        Background2_rect = Screen.blit(Background, (Background_x + 600, Background_y))
        Dino_rect = Screen.blit(Dino, (Dino_x, Dino_y))  # hiển thị khủng long
        Tree_rect = Screen.blit(Tree, (Tree_x, Tree_y))  # hiển thị cây

        if Background_x + 600 <= 0:  # mặt đất di chuyển
            Background_x = 0

        Score_txt = Font_score.render("Score : " + str(Score), True, RED)  # cài đặt Score ép kiểu string
        Screen.blit(Score_txt, (260, 5))  # hiển thị điểm
        Background_x -= x_velocity  # mặt đất di chuyển

        Tree_x -= x_velocity  # cây di chuyển
        if Tree_x <= -20:
            Tree_x = 550
            Score += 1
        if 230 >= Dino_y >= 80:  # nhảy lên
            if jump == True:
                Dino_y -= y_velocity
        else:
            jump = False
        if Dino_y < 230:  # nhảy xuống
            if jump == False:
                Dino_y += y_velocity

        # Xử lý va chạm - GAME OVER
        if Dino_rect.colliderect(Tree_rect):
            Pausing = True
            if Pausing == True:
                pygame.mixer.Sound.play(Sound_game_over)  # âm thanh
                # Pausing = True
                Game_Over_rect = Screen.blit(Game_Over, (200, 100))
                Score_text = Font_score_Gameover.render("Score : " + str(Score), True, RED)  # cài đặt Score ép kiểu string
                Screen.blit(Score_text, (260, 150))  # hiển thị điểm
                Game_over_text = Font_game_over.render("-Press 'Space' to continue.!-", True, DIMGRAY)
                Screen.blit(Game_over_text, (210, 210))
                x_velocity = 0  # tốc độ di chuyển mặt đất + cây
                y_velocity = 0  # hight nhảy

        #Nhảy
        for event in pygame.event.get():  # bắt sự kiện
            if event.type == pygame.QUIT:  # Thoát game khi click X
                Running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # nhấn phím space => nhảy
                    if Dino_y == 230:
                        pygame.mixer.Sound.play(Sound_jump)  # âm thanh
                        jump = True
                    if Pausing:
                        Score = 0
                        Background_x = 0
                        Background_y = 0
                        x_velocity = 5  # tốc độ di chuyển mặt đất + cây
                        y_velocity = 7  # hight nhảy
                        # khủng long
                        Dino_x = 30
                        Dino_y = 230
                        # cây
                        Tree_x = 550
                        Tree_y = 230
                        Pausing = False

        pygame.display.flip()  # Hiển thị thay đổi trên màn hình
    pygame.quit()  # thoát chương trình cùng với đóng toàn bộ data sử dụng

while content:
    Menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Thoát game khi nhấn X
            pygame.quit()  # thoát chương trình cùng với đóng toàn bộ data sử dụng
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # nhấn phím space
                PlayGame()
    pygame.display.flip()  # Hiển thị thay đổi trên màn hình
pygame.quit()  # thoát chương trình cùng với đóng toàn bộ data sử dụng

