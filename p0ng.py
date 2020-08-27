import pygame
import random
pygame.init()
display_x=1000
display_y=500
win=pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption('p0ng')
rect_x=20
rect_y=220
second_rect_x=display_x-40
second_rect_y=220
width=20
height=60
vel=15
white=(225,225,225)
daimeter=10
is_shoot=False
shoot_vel_y=10
shoot_vel_x=15
line_x=display_x//2
line_y=display_y
score=0
score2=0
font=pygame.font.Font('font.ttf',24)
genrate_ball=0
timer=0
time_sec=0
time_min=0
main_menu=True
is_settings=False
game_running=False
is_pause=False
pause_button_width=10
pause_button_height=25
run=True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x , mouse_y=pygame.mouse.get_pos()
			print(mouse_x,mouse_y)
			#play
			if main_menu and mouse_x>=468 and mouse_x<=530 and mouse_y>=300 and mouse_y<=339:
				game_running=True
				time_sec=0
				time_min=0
				main_menu=False
			#settings
			if main_menu and mouse_x>=438 and mouse_x<=564 and mouse_y>=350 and mouse_y<=381:
				main_menu=False
				is_settings=True
			#setting back
			if is_settings and mouse_x>=10 and mouse_x<=79 and mouse_y>=10 and mouse_y<=39:
				main_menu=True
				is_settings=False
			#pause
			if game_running and mouse_x>=10 and mouse_x<=40 and mouse_y>=10 and mouse_y<=35:
				game_running=False
				is_pause=True
			#pause_resume
			if is_pause and mouse_x>=444 and mouse_x<=556 and mouse_y>=260 and mouse_y<=287:
				game_running=True
				is_pause=False
			#pause_menu
			if is_pause and mouse_x>=460 and mouse_x<=540 and mouse_y>=300 and mouse_y<=327:
				main_menu=True
				is_pause=False
			#quit
			if main_menu and mouse_x>=470 and mouse_x<=530 and mouse_y>=402 and mouse_y<=430:
				run=False
	pygame.time.delay(40)
	if main_menu:
		#Game Template
		win.fill(0)
		template=pygame.font.Font('font.ttf',40)
		pong=template.render('PONG',True,white)
		pong_text_pos=display_x//2-67
		win.blit(pong,(pong_text_pos,100))
		#play button
		play=font.render('Play',True,white)
		play_text_pos=display_x//2-32
		win.blit(play,(play_text_pos,300))
		#settings
		settings_button=font.render('settings',True,white)
		settings_text_pos=display_x//2-63
		win.blit(settings_button,(settings_text_pos,350))
		#quit button
		quit=font.render('Quit',True,white)
		quit_text_pos=display_x//2-30
		win.blit(quit,(quit_text_pos,400))
		pygame.display.update()
	if is_settings:
		win.fill(0)
		#back button
		back=font.render('back',True,white)
		win.blit(back,(10,10))
		#working on settings
		pygame.display.update()
	if is_pause:
		win.fill(0)
		#pause_menu
		#play button
		resume=font.render('resume',True,white)
		resume_text_pos=display_x//2-56
		win.blit(resume,(resume_text_pos,260))
		#menu
		menu=font.render('menu',True,white)
		menu_text_pos=display_x//2-39
		win.blit(menu,(menu_text_pos,300))
		pygame.display.update()
	if game_running:
		if timer<1000:
			timer+=40
		if timer==1000:
			timer=0
			time_sec+=1
		if time_sec==60:
			time_min+=1
			time_sec=0
		if genrate_ball==0:
			L_0r_R=random.randint(0,1)
			centre_x=display_x//2
			centre_y=random.randint(1,50)*10
			genrate_ball+=1
		key=pygame.key.get_pressed()
		if key[pygame.K_w] and rect_y>0:
			rect_y-=vel
		if key[pygame.K_s] and rect_y+height<display_y:
			rect_y+=vel
		if key[pygame.K_UP] and second_rect_y>0:
			second_rect_y-=vel
		if key[pygame.K_DOWN] and second_rect_y+height<display_y:
			second_rect_y+=vel
		if key[pygame.K_SPACE]:
			is_shoot=True
		if is_shoot:
			pygame.draw.circle(win,white,(centre_x,centre_y),(daimeter))
			if L_0r_R:
				shoot_vel_x*=-1
				L_0r_R=0
			centre_y+=shoot_vel_y
			centre_x+=shoot_vel_x
			if centre_y+daimeter==display_y:
				shoot_vel_y*=-1
			if centre_y-daimeter==0:
				shoot_vel_y*=-1
			if rect_x+width==centre_x-daimeter and centre_y>rect_y-5 and centre_y<rect_y+height:
				shoot_vel_x*=-1
			if second_rect_x==centre_x+daimeter and centre_y>second_rect_y-5 and centre_y<second_rect_y+height:
				shoot_vel_x*=-1
		pygame.draw.rect(win,white,(rect_x,rect_y,width,height))
		pygame.draw.rect(win,white,(second_rect_x,second_rect_y,width,height))
		text=font.render(str(score),True,white)
		text2=font.render(str(score2),True,white)
		font_time_sec=font.render(str(time_sec),True,white)
		font_time_min=font.render(str(time_min),True,white)
		pygame.draw.rect(win,white,(10,10,pause_button_width,pause_button_height))
		pygame.draw.rect(win,white,(width+10,10,pause_button_width,pause_button_height))
		win.blit(text,(line_x-35,70))
		win.blit(text2,(line_x+25,70))
		win.blit(font_time_sec,(line_x+10,25))
		win.blit(font_time_min,(line_x-20,25))
		if centre_x+daimeter>display_x:
			score+=1
			is_shoot=False
			genrate_ball=0
		if centre_x-daimeter<0:
			score2+=1
			is_shoot=False
			genrate_ball=0
		pygame.draw.line(win,white,(line_x,0),(line_x,line_y))
		pygame.display.update()
		win.fill(0)
