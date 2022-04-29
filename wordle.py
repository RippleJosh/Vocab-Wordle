import pygame
from random import randint

# vocab_list = ['WEIGHT','INERTIA','SPEED','SLOPE','VELOCITY','ACCELERATION','MOTION','REFERENCE POINT','FORCE','NEWTON','FRICTION','GRAVITY','NET FORCE','RELATIVE','PERSPECTIVE']

# vocab_list = ['PRECAMBRIAN','CAMBRIAN','ORDOVICIAN','SILURIAN','DEVONIAN','CARBONIFEROUS','PERMIAN','TRIASSIC','JURASSIC','CRETACEOUS','PALOGENE','NEOGENE','QUARTERNARY','PALEOZOIC','MESOZOIC','CENOZOIC']

# vocab_list = ['CONDUCTOR','INSULATOR','SPECIFIC HEAT','EXPANSION','CONTRACTION','TRANSFORMS','CONVECTION','CONDUCTION','RADIATION','TEMPERATURE','ABSOLUTE ZERO','HEAT','TRANSFER','THERMAL ENERGY']

vocab_list = ['ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN', 'AGENT', 'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER', 'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE', 'ARRAY', 'ASIDE', 'ASSET', 'AUDIO', 'AUDIT', 'AVOID', 'AWARD', 'AWARE', 'BADLY', 'BAKER', 'BASES', 'BASIC', 'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK', 'BLAME', 'BLIND', 'BLOCK', 'BLOOD', 'BOARD', 'BOOST', 'BOOTH', 'BOUND', 'BRAIN', 'BRAND', 'BREAD', 'BREAK', 'BREED', 'BRIEF', 'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE', 'CALIF', 'CARRY', 'CATCH', 'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK', 'CLOCK', 'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT', 'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CURVE', 'CYCLE', 'DAILY', 'DANCE', 'DATED', 'DEALT', 'DEATH', 'DEBUT', 'DELAY', 'DEPTH', 'DOING', 'DOUBT', 'DOZEN', 'DRAFT', 'DRAMA', 'DRAWN', 'DREAM', 'DRESS', 'DRILL', 'DRINK', 'DRIVE', 'DROVE', 'DYING', 'EAGER', 'EARLY', 'EARTH', 'EIGHT', 'ELITE', 'EMPTY', 'ENEMY', 'ENJOY', 'ENTER', 'ENTRY', 'EQUAL', 'ERROR', 'EVENT', 'EVERY', 'EXACT', 'EXIST', 'EXTRA', 'FAITH', 'FALSE', 'FAULT', 'FIBER', 'FIELD', 'FIFTH', 'FIFTY', 'FIGHT', 'FINAL', 'FIRST', 'FIXED', 'FLASH', 'FLEET', 'FLOOR', 'FLUID', 'FOCUS', 'FORCE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FRAME', 'FRANK', 'FRAUD', 'FRESH', 'FRONT', 'FRUIT', 'FULLY', 'FUNNY', 'GIANT', 'GIVEN', 'GLASS', 'GLOBE', 'GOING', 'GRACE', 'GRADE', 'GRAND', 'GRANT', 'GRASS', 'GREAT', 'GREEN', 'GROSS', 'GROUP', 'GROWN', 'GUARD', 'GUESS', 'GUEST', 'GUIDE', 'HAPPY', 'HARRY', 'HEART', 'HEAVY', 'HENCE', 'HENRY', 'HORSE', 'HOTEL', 'HOUSE', 'HUMAN', 'IDEAL', 'IMAGE', 'INDEX', 'INNER', 'INPUT', 'ISSUE', 'JAPAN', 'JIMMY', 'JOINT', 'JONES', 'JUDGE', 'KNOWN', 'LABEL', 'LARGE', 'LASER', 'LATER', 'LAUGH', 'LAYER', 'LEARN', 'LEASE', 'LEAST', 'LEAVE', 'LEGAL', 'LEVEL', 'LEWIS', 'LIGHT', 'LIMIT', 'LINKS', 'LIVES', 'LOCAL', 'LOGIC', 'LOOSE', 'LOWER', 'LUCKY', 'LUNCH', 'LYING', 'MAGIC', 'MAJOR', 'MAKER', 'MARCH', 'MARIA', 'MATCH', 'MAYBE', 'MAYOR', 'MEANT', 'MEDIA', 'METAL', 'MIGHT', 'MINOR', 'MINUS', 'MIXED', 'MODEL', 'MONEY', 'MONTH', 'MORAL', 'MOTOR', 'MOUNT', 'MOUSE', 'MOUTH', 'MOVIE', 'MUSIC', 'NEEDS', 'NEVER', 'NEWLY', 'NIGHT', 'NOISE', 'NORTH', 'NOTED', 'NOVEL', 'NURSE', 'OCCUR', 'OCEAN', 'OFFER', 'OFTEN', 'ORDER', 'OTHER', 'OUGHT', 'PAINT', 'PANEL', 'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PHOTO', 'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLAIN', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIME', 'PRINT', 'PRIOR', 'PRIZE', 'PROOF', 'PROUD', 'PROVE', 'QUEEN', 'QUICK', 'QUIET', 'QUITE', 'RADIO', 'RAISE', 'RANGE', 'RAPID', 'RATIO', 'REACH', 'READY', 'REFER', 'RIGHT', 'RIVAL', 'RIVER', 'ROBIN', 'ROGER', 'ROMAN', 'ROUGH', 'ROUND', 'ROUTE', 'ROYAL', 'RURAL', 'SCALE', 'SCENE', 'SCOPE', 'SCORE', 'SENSE', 'SERVE', 'SEVEN', 'SHALL', 'SHAPE', 'SHARE', 'SHARP', 'SHEET', 'SHELF', 'SHELL', 'SHIFT', 'SHIRT', 'SHOCK', 'SHOOT', 'SHORT', 'SHOWN', 'SIGHT', 'SINCE', 'SIXTH', 'SIXTY', 'SIZED', 'SKILL', 'SLEEP', 'SLIDE', 'SMALL', 'SMART', 'SMILE', 'SMITH', 'SMOKE', 'SOLID', 'SOLVE', 'SORRY', 'SOUND', 'SOUTH', 'SPACE', 'SPARE', 'SPEAK', 'SPEED', 'SPEND', 'SPENT', 'SPLIT', 'SPOKE', 'SPORT', 'STAFF', 'STAGE', 'STAKE', 'STAND', 'START', 'STATE', 'STEAM', 'STEEL', 'STICK', 'STILL', 'STOCK', 'STONE', 'STOOD', 'STORE', 'STORM', 'STORY', 'STRIP', 'STUCK', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'SUITE', 'SUPER', 'SWEET', 'TABLE', 'TAKEN', 'TASTE', 'TAXES', 'TEACH', 'TEETH', 'TERRY', 'TEXAS', 'THANK', 'THEFT', 'THEIR', 'THEME', 'THERE', 'THESE', 'THICK', 'THING', 'THINK', 'THIRD', 'THOSE', 'THREE', 'THREW', 'THROW', 'TIGHT', 'TIMES', 'TIRED', 'TITLE', 'TODAY', 'TOPIC', 'TOTAL', 'TOUCH', 'TOUGH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN', 'TREAT', 'TREND', 'TRIAL', 'TRIED', 'TRIES', 'TRUCK', 'TRULY', 'TRUST', 'TRUTH', 'TWICE', 'UNDER', 'UNDUE', 'UNION', 'UNITY', 'UNTIL', 'UPPER', 'UPSET', 'URBAN', 'USAGE', 'USUAL', 'VALID', 'VALUE', 'VIDEO', 'VIRUS', 'VISIT', 'VITAL', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHEEL', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WOMAN', 'WOMEN', 'WORLD', 'WORRY', 'WORSE', 'WORST', 'WORTH', 'WOULD', 'WOUND', 'WRITE', 'WRONG', 'WROTE', 'YIELD', 'YOUNG', 'YOUTH']

pygame.init()
width, height = 800, 600
f = 1
b = (height/24)*f
backgroundColor = 255, 255, 255
lineColor = 0, 0, 0
font = pygame.font.SysFont('dejavuserif', 30)
screen = pygame.display.set_mode((width, height))
user_text = ''

def DrawBoxes(word, f = f):
  for i in range(len(word)):
    pygame.draw.rect(screen,lineColor, pygame.Rect((width/len(word)+35*i), b+45*f, 30, 40), width=1)
  pygame.display.flip()

def YellowCheck(list1, word,f=f):
  for item in list1:
    if item in word:
      pos = [i for i, e in enumerate(list1) if e == item]
      for it in pos:
        pygame.draw.rect(screen, (250,250,0), pygame.Rect((width/len(word)+35*int(it)), b+45*f, 30, 40), width=0)
        pygame.draw.rect(screen, lineColor, pygame.Rect((width/len(word)+35*int(it)), b+45*f, 30, 40), width=1)
        text = font.render(list1[it], 1, (0, 0, 0))
        screen.blit(text, pygame.Rect((width/len(word)+35*(it)+4), b+1+f*45, 25, 40))
  pygame.display.flip()

def GreenCheck(list1, word,f=f):
  for item in list1:
    if item in word:
      pos = [i for i, e in enumerate(list1) if e == item]
      pos2 = [i for i, e in enumerate(word) if e == item]
      for itr in pos:
        if itr in pos2:
          pygame.draw.rect(screen, (15,250,0), pygame.Rect((width/len(word)+35*int(itr)), b+45*f, 30, 40), width=0)
          pygame.draw.rect(screen, lineColor, pygame.Rect((width/len(word)+35*int(itr)), b+45*f, 30, 40), width=1)
          text = font.render(list1[itr], 1, (0, 0, 0))
          screen.blit(text, pygame.Rect((width/len(word)+35*(itr)+4), b+1+f*45, 25, 40))  
  pygame.display.flip()

def new_word(y,f=f):
  k = vocab_list[randint(0,len(vocab_list)-1)]
  word = list(k)
  print(word)
  vocab_list.remove(k)
  while y == 0:
    screen.fill(backgroundColor)
    # text_surface = font.render(user_text, True, (0, 0, 0))
    c = True
    list1 = []
    for i in range(6):
      DrawBoxes(word,i)
      m = 1
      c = True
      while c == True:      
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RSHIFT:
              a = 0
            if event.key == pygame.K_LSHIFT:
              a = 0
            else:
              if event.key == pygame.K_BACKSPACE:
                if m!=1: m = m-1
                if len(list1) != 0:
                  for k in range(5):
                    text = font.render(list1[-1], 1, (255, 255, 255))
                    screen.blit(text, pygame.Rect((width/len(word)+35*(m-1)+4), b+1+i*45, 25, 40))
                  pygame.display.flip()
                  list1.pop()

              # user_text = user_text[:-1]
              if event.key == pygame.K_RETURN:
                print('RETURN', m, 1+len(word), m==1+len(word))
                if m == 1+len(word):
                  YellowCheck(list1, word, i)
                  GreenCheck(list1, word, i)
                  if word == list1:
                    text = font.render("You got it!", 1, (10, 10, 10))
                    textpos = text.get_rect()
                    screen.blit(text, textpos)
                    pygame.display.flip()
                    return

                  list1 = []
                  c = False
              else:
                if event.key != pygame.K_BACKSPACE:
                  if m <= len(word):
                    text = font.render((event.unicode).upper(), 1, (0, 0, 0))
                    screen.blit(text, pygame.Rect((width/len(word)+35*(m-1)+4), b+1+i*45, 25, 40))
                    print('OK ',event.unicode)
                    pygame.display.flip()
                    m +=1
                    list1.append((event.unicode).upper())

    # screen.blit(text_surface, pygame.Rect((width/len(word)+35*i), b, 25, 40))
    text = font.render("So close! Press Enter to continue", 1, (10, 10, 10))
    textpos = text.get_rect()
    screen.blit(text, textpos)
    pygame.display.flip()
    y += 1

c = True
new_word(0)
while c == True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.type == pygame.K_BACKSPACE:
        c = False
      else:
        new_word(0)
pygame.quit()
