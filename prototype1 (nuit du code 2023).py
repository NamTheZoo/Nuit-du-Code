import pyxel, random 

# taille de la fenetre 128x128 pixels
# ne pas modifier
pyxel.init(128, 128, title="Nuit du c0de")
pyxel.load("D:\Lucas\Downloads\perso.pyxres")
pyxel.playm(1, loop=True)
# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60
vaisseau_y = 60

plat_x = 40
plat_y = 80




# initialisation des ennemis
plateforme_liste = []



def vaisseau_deplacement(x, y,plat_x, plat_y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 120) :
            x = x + 3
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0) :
            x = x - 3
    if vaisseau_y + 16 == plat_y:
        if pyxel.btn(pyxel.KEY_SPACE):
            y = y - 70
    
    if (vaisseau_y + 16 != plat_y) or (vaisseau_x > plat_x + 30 or vaisseau_x - plat_x < -16):
        y = y + 1
        
            
    
    return x, y


def plateforme_creation(plateforme_liste):
    """création aléatoire des ennemis"""
    
    
   


def plateforme_deplacement(plateforme_liste):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""

    


# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y, plateforme_liste, plat_x, plat_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y,plat_x, plat_y )


    # creation des ennemis
    plateforme_liste = plateforme_creation(plateforme_liste)

    # mise a jour des positions des ennemis
    plateforme_liste = plateforme_deplacement(plateforme_liste)
    
    if pyxel.frame_count % 75 == 0:
        
        plat_x = random.randint(0, 120)
        plat_y = random.randint(100, 120)
        
    
    
         
        


# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 128, 128) 
    if vaisseau_y < 128:
        # vaisseau (carre 8x8)
        pyxel.blt(vaisseau_x, vaisseau_y, 0, 0, 0, 16, 16, 0)


        # ennemis
        pyxel.rect(plat_x, plat_y, 30, 9, 2)
    
    else:
        pyxel.load("D:\Lucas\Downloads\perso.pyxres")
        pyxel.playm(1, loop=True)
        pyxel.text(120 / 3, 120/ 2, "GAME OVER!!",0)
        
        
pyxel.run(update, draw)
