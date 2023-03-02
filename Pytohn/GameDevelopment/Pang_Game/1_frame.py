import pygame
import os

pygame.init() 
 
# 화면 크기 설정
screen_width = 640  # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang Game") #게임 이름

clock = pygame.time.Clock()

# 1. 사용자 초기화
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path,"img") # image 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.jpg"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.jpg"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height

running = True #게임이 진행중인가?
while running:

    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    print("fps : " + str(clock.get_fps())) # 게임화면의 프레임 수를 확인

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

    

    screen.blit(background, (0,0))
    screen.blit(stage, (0,screen_height - stage_height))
    screen.blit(character, (0,screen_height - character_height - stage_height))

    pygame.display.update()