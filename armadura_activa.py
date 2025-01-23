''' codigo para manejar armaduras activas de forma finamica '''

'''
    Se generan y manejan componentes dinamicamente usando listas y diccionarios.

    En tab2 se define un Grid_Layout como contenedor para los elementos que estaran dentro de 
    nuevos layouts dinamicamente generados segun la necesidad del usario.

    Cotas se manejan en un VerticalLayout al que se le agregan dinamicamente LineEdits usando un boton 
    (El usuario puede elegir que cota agregar, Usando una lista con las cotas disponibles en el testero seleccionado, 
    Puede ser en una ventana emergente como en JACENA).
    Al agregar una cota hay que agregar un lineEdit a todos los otros VerticalLayouts que existen (Numero cordones y TPI, de cada tipo de corodon).
    Los valores de las cotas se guardan en lista self.dynamic_cotas[]

    Numero de cordones por cota se especifican en lineEdits que son agregados alineados con la posicion de las cotas. Se agregan a un VerticalLayout que es dinamicamente generado cuando el usuario agrega un tipo de cordon.
    Valores de estos lineEdits se almacenan en diccionario self.dynamic_cant_ordones{}. Un index de diccionario para cada tipo de cordon, dentro del index la lista guarda los valores de los lineEdits de esa columna (Vlayout).
    Este diccionario guarda los valores de todos los distintos tipos de cordones, Asignando un indice para cada tipo de cordon y usando la lista correspondiente a ese indice para almacenar los valores de ese cordon.

    TPI se guardan de la misma manera que numero de cordones, en su propio diccionario: self.dynamic_tpi{}, index y listas de cada indice se maneja de la misma forma que numero de cordones.

    tipos de cordones se manejan con self.dynamic_diametros_arm_act{}, donde cada indice corresponde a un tipo de cordon y dentro esta el valor actual de ComboBox

'''

def foo():

    # Definir variables que llevan cuenta de componentes dinamicamente generados. Los valores de estos se usan como indice en variables definidas abajo

    self.dynamic_cotas_arm_act = []
    self.dynamic_diametros_arm_act = [] # usar dict o list?
    self.dynamic_cordones_arm_act = {}
    self.dynamic_tpi_arm_act = {}

    # cada vez que se preciona btn calcular/almacenar se actualizan valores de listas/diccionarios.
    # al cambiar index de comboBox de tipoCordon se actualiza lista en posicion correspondiente. (Como saber cual posicion editar?, recordar comboBoxes creados dinamicamente en variable.)

    # Implementar btn para agregar cota, Al agregar cota tambien hay que agregar un LineEdit a cada Vlayout de la pestana.
    # Impleentar btn para agregar tipo de cordon, Se genera nuevo Glayout con comboBox, Vlayout con lineEdits = a cantidad de cotas existentes.
    