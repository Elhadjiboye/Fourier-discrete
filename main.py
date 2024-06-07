import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QPushButton
from PyQt5.QtCore import Qt
import TNS2

def calculate_fft(self):
    data = []
    for entry in self.x_entries:
        value = entry.text()
        if not value:
            self.output_text.setText("Erreur : Veuillez entrer toutes les valeurs de x.")
            return
        try:
            data.append(float(value))
        except ValueError:
            self.output_text.setText("Erreur : Les valeurs de x doivent être des nombres.")
            return

    # Calcul de la transformée de Fourier discrète en utilisant TNS2.fft
    result = TNS2.fft(data)

    # Affichage des résultats dans l'interface utilisateur
    self.output_text.setText("Sortie X :\n")
    for k, value in enumerate(result):
        self.output_text.append(f"X[{k}] = {value}")


    def calculate_fft(self):
        # Implémentez ici votre logique de calcul de la transformée de Fourier discrète
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
