class InputValidator:
    @staticmethod
    def validate_wheel(valor):
        if valor not in ("Trafficked", "Untrafficked"):
            raise ValueError("Debe ser 'Trafficked' o 'Untrafficked'")
        return 0 if valor == "Trafficked" else 1

    @staticmethod
    def validate_crop(valor):
        if valor not in ("AlfaCorn", "CC"):
            raise ValueError("Debe ser 'AlfaCorn' o 'CC'")
        return 0 if valor == "AlfaCorn" else 1

    @staticmethod
    def validate_tillage(valor):
        if valor not in ("NT", "CP"):
            raise ValueError("Debe ser 'NT' o 'CP'")
        return 0 if valor == "NT" else 1

    @staticmethod
    def validate_side(valor):
        if valor not in ("E", "W"):
            raise ValueError("Debe ser 'E' o 'W'")
        return 0 if valor == "E" else 1

    @staticmethod
    def validate_depth(valor):
        try:
            f = float(valor)
            if f < 0: raise ValueError("No negativo")
            return f
        except ValueError:
            raise ValueError("Debe ser número (ej. 5.0)")

    @staticmethod
    def validate_residue(valor):
        try:
            i = int(valor)
            if i < 0 or i > 100: raise ValueError("0-100")
            return i
        except ValueError:
            raise ValueError("Entero (ej. 60)")