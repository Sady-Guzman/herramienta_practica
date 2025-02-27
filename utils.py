from PySide6.QtWidgets import QMessageBox

def popup_msg(message):
    popup = QMessageBox()
    popup.setIcon(QMessageBox.Warning)  # ICONO
    popup.setWindowTitle("Mensaje")  # title
    popup.setText(message)  # Main message text
    popup.setStandardButtons(QMessageBox.Ok)  # agrega btn OK
    popup.exec()  # muestra ventana PopUp

def print_dynamic_trapecios(self):
    for i, layout in enumerate(self.dynamic_layouts):
        # print(f"\nPara layout {i}")

        # Print the label name
        print(f"\t- Nombre: {layout['name_label'].text()}")

        # Print values from QLineEdit fields
        print(f"\t\t- Bi: {layout['bi_line'].text()}")
        print(f"\t\t- Bs: {layout['bs_line'].text()}")
        print(f"\t\t- Altura: {layout['altura_line'].text()}")
        print(f"\t\t- Área: {layout['area_line'].text()}")
        print(f"\t\t- Centro de gravedad (CG): {layout['cg_line'].text()}")
        print(f"\t\t- Inercia: {layout['inercia_line'].text()}")
        print(f"\t\t- Op: {layout['op_line'].text()}")
        print(f"\t\t- Tipo : {layout['combo_insitu'].currentText()} \n")

        


def util_cotas_existentes_codones(self):
    print("Cotas existentes en Armadura Activa.")
    for cota in self.dynamic_cotas:
        print(cota.text())

def util_cordones_existentes(self):
    print("Keys de cordones existentes en self.dynamic_cordones_arm_act")
    print(self.dynamic_cordones_arm_act.keys())
    
def util_keys_dynamic_cordones(self):
    print("Keys de self.dynamic_cordones_arm_act por posicion.")
    for i, key in enumerate(self.dynamic_cordones_arm_act[0].keys(), 1):
        print(f"{i}. {key}")

def util_area_num_cords_cota_armact(self):
    ''' Itera por cota la cantidad de cordones en esa cota y que area le corresponde a cada cordon '''

    for i, cota in enumerate(self.dynamic_cotas):
        print(f"\n\nPara cota {i} = {self.dynamic_cotas[i].text()}")
        for j, cordon in enumerate(self.dynamic_cordones_arm_act):
            cordon = self.dynamic_cordones_arm_act[j]

            print(f"Para cordon {j} --> Num_cords = {cordon['num_cordones'][i].text()} ... Con Area = {cordon['area'].text()}")


def util_calc_area_cota_por_cordon(self):
    ''' Calcula area por cota, considerando distintos tipos de cordones en una misma cota '''

    # Dictionary to store areas: {cota_value: {area_class: total_area}}
    areas_by_cota = {}

    for i, cota in enumerate(self.dynamic_cotas):
        cota_value = float(self.dynamic_cotas[i].text())  # Convert cota to float
        areas_by_cota[cota_value] = {}  # Initialize dictionary for this cota

        print(f"\n\nPara cota {cota_value}:")
        
        for j, cordon in enumerate(self.dynamic_cordones_arm_act):
            cordon = self.dynamic_cordones_arm_act[j]
            
            num_cords = int(cordon['num_cordones'][i].text())  # Number of cords
            area_class = float(cordon['area'].text())  # Area per cord

            # Compute total area for this cota and area class
            total_area = num_cords * area_class

            # Store in dictionary, summing values if area_class already exists
            if area_class in areas_by_cota[cota_value]:
                areas_by_cota[cota_value][area_class] += total_area
            else:
                areas_by_cota[cota_value][area_class] = total_area

            print(f"Para cordon {j} --> Num_cords = {num_cords}, Clase_Area = {area_class}cm², Total_Area = {total_area}cm²")

    # Print results
    print("\n\nResumen de áreas por cota:")
    for cota, area_data in areas_by_cota.items():
        print(f"Cota {cota} m:")
        for area_class, total_area in area_data.items():
            print(f"  - Área clase {area_class} cm² → Total: {total_area} cm²")

def util_calc_area_cota(self):
    ''' Calcula area total en cada cota de armadura activa, Considerando distintos tipos de cordones, Pero sin especificarlos ni guardarlos. SOLO IMPORTA TOTAL '''
    dict_areas_cota = {}

    for index_cota, cota in enumerate(self.dynamic_cotas):
        cota_value = float(self.dynamic_cotas[index_cota].text())  # Convert to float
        dict_areas_cota[cota_value] = 0  # Initialize total area for this cota

        print(f"\n\nPara cota {cota_value}:")

        for index_cord, cordon in enumerate(self.dynamic_cordones_arm_act):
            cordon = self.dynamic_cordones_arm_act[index_cord]

            num_cords = int(cordon['num_cordones'][index_cota].text())  # Convert to int
            area_cordon = float(cordon['area'].text())  # Convert to float

            total_area = num_cords * area_cordon  # Compute total area

            dict_areas_cota[cota_value] += total_area  # Add to total for this cota

            print(f"  - Cordon {index_cord} --> Num_cords = {num_cords}, Área Cordon = {area_cordon}, Total_Area = {total_area}")

    # Print summarized results
    print("\n\nResumen de áreas por cota:")
    for cota, area_total in dict_areas_cota.items():
        print(f"🔹 Cota {cota}m → Área total = {area_total} cm²")