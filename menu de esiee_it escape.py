# Créé par mari_, le 15/01/2024 en Python 3.7
import pygame
import sys

class PageOne:
    def __init__(self, screen, switch_callback, toggle_music_callback, show_options_callback):
        self.screen = screen
        self.switch_callback = switch_callback
        self.toggle_music_callback = toggle_music_callback
        self.show_options_callback = show_options_callback
        self.next_page_callback = None

        # Chargement de l'image de fond de l'école et ajustement de sa taille
        self.ecole_image = pygame.image.load("imageonline-co-pixelated.png")
        self.ecole_rect = self.ecole_image.get_rect()
        object_size = (1915, 1140)
        self.ecole_image = pygame.transform.scale(self.ecole_image, object_size)

        # Nouvel attribut pour l'image sur le côté droit
        self.side_image = pygame.image.load("but_du_jeu.jpg")

        # Nouvelles images en bas à droite
        self.bottom_image1 = pygame.image.load("PersonnageFace1.png")
        self.bottom_image2 = pygame.image.load("Camera.png")
        self.bottom_image3 = pygame.image.load("Porteouverte.png")  # Remplacez par le chemin de votre nouvelle image
        self.bottom_image4 = pygame.image.load("Table.png")  # Remplacez par le chemin de votre nouvelle image

        # Ajustement de la taille des nouvelles images
        bottom_image_size = (100, 100)
        self.bottom_image1 = pygame.transform.scale(self.bottom_image1, bottom_image_size)
        self.bottom_image2 = pygame.transform.scale(self.bottom_image2, bottom_image_size)
        self.bottom_image3 = pygame.transform.scale(self.bottom_image3, bottom_image_size)
        self.bottom_image4 = pygame.transform.scale(self.bottom_image4, bottom_image_size)

        # Définition des positions des nouvelles images en bas à droite
        self.bottom_image_positions = [
            (self.screen.get_width() - 120, self.screen.get_height() - 150),
            (self.screen.get_width() - 250, self.screen.get_height() - 150),
            (self.screen.get_width() - 380, self.screen.get_height() - 150),
            (self.screen.get_width() - 510, self.screen.get_height() - 150)
        ]

        # Police et texte du titre
        self.title_font = pygame.font.Font("pixel.ttf", 72)
        self.text = self.title_font.render("ESIEE-IT ESCAPE", True, (80, 96, 101))
        self.text_rect = self.text.get_rect(center=(screen.get_width() // 2, 100))

        # Boutons et images associées
        button_width, button_height = 600, 100
        self.switch_button = pygame.Rect((screen.get_width() - button_width) // 5, (screen.get_height() - button_height) // 3, button_width, button_height)
        self.switch_button2 = pygame.Rect((screen.get_width() - button_width) // 5, (screen.get_height() + button_height) // 2, button_width, button_height)
        self.switch_button3 = pygame.Rect((screen.get_width() - button_width) // 5, (screen.get_height() + 2 * button_height) // 1.5, button_width, button_height)
        self.button_image = pygame.image.load("la-plaque-ou-métallique-isolés-avec-le-chemin-de-coupe-inclus-l-illustration-d-isolée-sur-blanc-170274959.jpg")
        self.button_image = pygame.transform.scale(self.button_image, (button_width, button_height))

        # Bouton de contrôle de la musique
        music_button_width, music_button_height = 40, 40
        self.music_button = pygame.Rect(screen.get_width() - 60, 20, music_button_width, music_button_height)
        self.music_on_image = pygame.image.load("speaker_on.jpg")
        self.music_off_image = pygame.image.load("speaker_off.png")
        self.music_on_image = pygame.transform.scale(self.music_on_image, (music_button_width, music_button_height))
        self.music_off_image = pygame.transform.scale(self.music_off_image, (music_button_width, music_button_height))
        self.music_button_image = self.music_on_image  # Image initiale du bouton "activé"

        # Couleur du texte par défaut
        self.switch_text_color = (255, 255, 255)
        self.switch_text2_color = (255, 255, 255)
        self.switch_text3_color = (255, 255, 255)

    def set_next_page_callback(self, callback):
        self.next_page_callback = callback

    def draw(self):
        # Affichage de l'image de fond et du titre
        self.screen.blit(self.ecole_image, (0, 0))
        self.screen.blit(self.text, self.text_rect)

        # Affichage des boutons
        self.screen.blit(self.button_image, self.switch_button)
        switch_text = self.title_font.render("JOUER", True, self.switch_text_color)
        switch_text_rect = switch_text.get_rect(center=self.switch_button.center)
        self.screen.blit(switch_text, switch_text_rect)

        self.screen.blit(self.button_image, self.switch_button2)
        switch_text2 = self.title_font.render("QUITTER", True, self.switch_text2_color)
        switch_text_rect2 = switch_text2.get_rect(center=self.switch_button2.center)
        self.screen.blit(switch_text2, switch_text_rect2)

        self.screen.blit(self.button_image, self.switch_button3)
        switch_text3 = self.title_font.render("CREDIT", True, self.switch_text3_color)
        switch_text_rect3 = switch_text3.get_rect(center=self.switch_button3.center)
        self.screen.blit(switch_text3, switch_text_rect3)

        # Affichage du bouton de contrôle de la musique
        music_button_rect = self.music_button
        self.screen.blit(self.music_button_image, music_button_rect)

        # Affichage de l'image sur le côté droit
        side_image_rect = self.side_image.get_rect()
        side_image_rect.center = (self.screen.get_width() - self.side_image.get_width() // 1, self.screen.get_height() // 2,)
        self.screen.blit(self.side_image, side_image_rect)

        # Affichage des nouvelles images en bas à droite
        for image, position in zip([self.bottom_image1, self.bottom_image2, self.bottom_image3, self.bottom_image4], self.bottom_image_positions):
            image_rect = image.get_rect(center=position)
            self.screen.blit(image, image_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.switch_button.collidepoint(event.pos):
                if self.next_page_callback:
                    self.next_page_callback()
            elif self.switch_button2.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            elif self.music_button.collidepoint(event.pos):
                self.toggle_music_callback()
            elif self.switch_button3.collidepoint(event.pos):
                self.show_options_callback()

    def toggle_music_button_image(self):
        if self.music_button_image == self.music_on_image:
            self.music_button_image = self.music_off_image
        else:
            self.music_button_image = self.music_on_image

class PageTwo:
    def __init__(self, screen, switch_callback):
        self.screen = screen
        self.switch_callback = switch_callback

        button_width, button_height = 400, 75
        self.switch_button = pygame.Rect((screen.get_width() - button_width) // 5, (screen.get_height() - button_height) // 2, button_width, button_height)
        self.switch_button2 = pygame.Rect((screen.get_width() - button_width) // 2, (screen.get_height() + 50) // 2, button_width, button_height)
        self.button_image = pygame.image.load("la-plaque-ou-métallique-isolés-avec-le-chemin-de-coupe-inclus-l-illustration-d-isolée-sur-blanc-170274959.jpg")
        self.button_image = pygame.transform.scale(self.button_image, (button_width, button_height))

        self.switch_text_color = (255, 255, 255)
        self.switch_text2_color = (255, 255, 255)

    def draw(self):
        self.screen.fill((0, 0, 128))

        self.screen.blit(self.button_image, self.switch_button)
        switch_text = self.font.render("Retour", True, self.switch_text_color)
        switch_text_rect = switch_text.get_rect(center=self.switch_button.center)
        self.screen.blit(switch_text, switch_text_rect)

        self.screen.blit(self.button_image, self.switch_button2)
        switch_text2 = self.font.render("QUITTER", True, self.switch_text2_color)
        switch_text_rect2 = switch_text2.get_rect(center=self.switch_button2.center)
        self.screen.blit(switch_text2, switch_text_rect2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.switch_button.collidepoint(event.pos):
                self.switch_callback()
            elif self.switch_button2.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

class OptionsPage:
    def __init__(self, screen, back_callback):
        self.screen = screen
        self.back_callback = back_callback

        self.background_image = pygame.image.load("pngtree-textured-metal-texture-flat-material-image_219664.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (screen.get_width(), screen.get_height()))

        button_width, button_height = 400, 75
        self.back_button = pygame.Rect(screen.get_width() - button_width - 20, screen.get_height() - button_height - 20, button_width, button_height)
        self.back_text_color = (255, 255, 255)

        self.font = pygame.font.Font("Symtext.ttf", 72)
        self.text = self.font.render("CREDITS DE FIN", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 5))

        self.center_paragraph = "Théo : Développeur de la partie qui permet de jouer."
        self.center_paragraph2 = "Maxime : Designeur des différentes parties du jeu."
        self.center_paragraph3 = "Lohan : Développeur des collisions entre les objets."
        self.center_paragraph4 = "Marin : Développeur du menu du jeu."

        self.paragraph_font = pygame.font.Font("Symtext.ttf", 40)
        self.paragraph_text = self.paragraph_font.render(self.center_paragraph, True, (255, 255, 255))
        self.paragraph_rect = self.paragraph_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

        self.paragraph2_text = self.paragraph_font.render(self.center_paragraph2, True, (255, 255, 255))
        self.paragraph2_rect = self.paragraph2_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

        self.paragraph3_text = self.paragraph_font.render(self.center_paragraph3, True, (255, 255, 255))
        self.paragraph3_rect = self.paragraph3_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))

        self.paragraph4_text = self.paragraph_font.render(self.center_paragraph4, True, (255, 255, 255))
        self.paragraph4_rect = self.paragraph4_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))

        self.screen.blit(self.text, self.text_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back_button)
        pygame.draw.rect(self.screen, (255, 255, 255), self.back_button, 2)

        back_text_surface = self.font.render("Retour", True, self.back_text_color)
        back_text_rect = back_text_surface.get_rect(center=self.back_button.center)
        self.screen.blit(back_text_surface, back_text_rect)

        self.screen.blit(self.paragraph_text, self.paragraph_rect)
        self.screen.blit(self.paragraph2_text, self.paragraph2_rect)
        self.screen.blit(self.paragraph3_text, self.paragraph3_rect)
        self.screen.blit(self.paragraph4_text, self.paragraph4_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.back_button.collidepoint(event.pos):
                self.back_callback()

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1915, 1140))
        pygame.display.set_caption("ESIEE-IT ESCAPE")

        self.clock = pygame.time.Clock()
        self.current_page = None
        self.show_page_one()

        pygame.mixer.init()
        pygame.mixer.music.load("Musique Gratuite Libre de Droits qui Bouge Gaming Électro House Bayslick - The End is Beer.mp3")
        pygame.mixer.music.play(-1)

    def show_page_one(self):
        self.current_page = PageOne(self.screen, self.show_page_two, self.toggle_music, self.show_options_page)

    def show_page_two(self):
        self.current_page = PageTwo(self.screen, self.show_page_one)

    def show_options_page(self):
        self.current_page = OptionsPage(self.screen, self.show_page_one)

    def quit_app(self):
        pygame.quit()
        sys.exit()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.current_page.handle_event(event)

            self.current_page.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def toggle_music(self):
        pygame.mixer.music.pause() if pygame.mixer.music.get_busy() else pygame.mixer

        self.current_page.toggle_music_button_image()

if __name__ == "__main__":
    app = App()
    app.run()





