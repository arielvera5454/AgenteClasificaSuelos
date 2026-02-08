import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Asegúrate de que el nombre del CSV sea el correcto
DATASET_PATH = os.path.join(BASE_DIR, "Field 70-71 ConeIndex_BulkDensityDepths_2021_0.csv")

# Mapeos Categóricos
WHEEL_MAP = {"Trafficked": 0, "Untrafficked": 1}
CROP_MAP = {"AlfaCorn": 0, "CC": 1}
TILLAGE_MAP = {"NT": 0, "CP": 1}
SIDE_MAP = {"E": 0, "W": 1}
CLASE_INV = {0: "Compactación BAJA (<1 MPa)", 1: "Compactación MEDIA (1-2 MPa)", 2: "Compactación ALTA (>2 MPa)"}

class DatasetLoader:
    def __init__(self, ruta=DATASET_PATH):
        self.ruta = ruta
        # Guardamos máximos y mínimos para normalizar k-NN
        self.min_vals = [0, 0, 0, 0, 0.0, 0.0, 0] 
        self.max_vals = [1, 1, 1, 1, 60.0, 60.0, 100] # Estimados iniciales

    def _discretizar_target(self, valor):
        # NOTA PARA DEFENSA: Usamos 2.0 MPa como límite crítico agronómico 
        # (límite donde las raíces sufren para penetrar).
        if valor < 1.0: return 0
        elif valor < 2.0: return 1
        else: return 2

    def _bin_depth(self, valor):
        """Discretiza profundidad para el Árbol ID3"""
        if valor <= 10: return 0  # Superficial
        elif valor <= 30: return 1 # Media
        else: return 2            # Profunda

    def _bin_residue(self, valor):
        """Discretiza residuos para el Árbol ID3"""
        if valor <= 30: return 0  # Bajo
        elif valor <= 70: return 1 # Medio
        else: return 2            # Alto

    def load_raw(self):
        """Carga los datos crudos SIN las columnas 'trampa' (Plot, Field, Block)"""
        X, y = [], []
        with open(self.ruta, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    # Solo características FÍSICAS (7 features)
                    # Eliminamos Plot, Field, Block, Tx para evitar Data Leakage
                    vector = [
                        WHEEL_MAP[fila["Wheel"]],      # 0
                        CROP_MAP[fila["Crop"]],        # 1
                        TILLAGE_MAP[fila["Tillage"]],  # 2
                        SIDE_MAP[fila["Side"]],        # 3
                        float(fila["Depth.Upper"]),    # 4
                        float(fila["Depth.Lower"]),    # 5
                        int(fila["ResidueRemoved"])    # 6
                    ]
                    X.append(vector)
                    y.append(self._discretizar_target(float(fila["ConeIndex"])))
                except (KeyError, ValueError):
                    continue
        
        # Actualizar rangos reales para normalización
        if X:
            self.min_vals = [min(c) for c in zip(*X)]
            self.max_vals = [max(c) for c in zip(*X)]
            
        return X, y

    def get_knn_data(self, X_raw):
        """Normaliza (0-1) para que k-NN funcione bien con distancias."""
        X_norm = []
        for row in X_raw:
            new_row = []
            for i, val in enumerate(row):
                rango = self.max_vals[i] - self.min_vals[i]
                if rango > 0:
                    new_row.append((val - self.min_vals[i]) / rango)
                else:
                    new_row.append(0)
            X_norm.append(new_row)
        return X_norm

    def get_tree_data(self, X_raw):
        """Discretiza variables continuas para que ID3 funcione bien."""
        X_disc = []
        for row in X_raw:
            new_row = list(row[:4]) # Copiar categóricos (Wheel, Crop, etc)
            new_row.append(self._bin_depth(row[4])) # Depth Upper binned
            new_row.append(self._bin_depth(row[5])) # Depth Lower binned
            new_row.append(self._bin_residue(row[6])) # Residue binned
            X_disc.append(new_row)
        return X_disc