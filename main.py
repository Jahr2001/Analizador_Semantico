import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import analizadorLexico as lexico
import analizadorSintactico as sintactico
import analizadorSemantico as semantico


qtCreatorFile = './view/mainView.ui'  # Nombre del archivo aquí

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class mainView(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Titulo de la ventana
        self.setWindowTitle(
            ".:: Analizador Sintáctico::. Segundo Corte - Compiladores e Interpretes - 193282 - 193213")

        # Botones
        self.btnSalir.clicked.connect(self.salir)
        self.btnAnalizar.clicked.connect(self.obtenerDatos)

    # Obtener datos y analizarlos
    def obtenerDatos(self):
        cadena = self.textoEntrada.toPlainText()
        if cadena:
            self.textoEntrada.setStyleSheet(
                'font: 15pt "MS Shell Dlg 2"; color:black;')
            lexico.cadena = cadena

            print(f'Cadenas --> {lexico.cadena}')
            print("AQUI EMPIEZA A CONTAR")
            cadenaReemplazada = self.reemplazarCarateres(lexico.cadena)
            print(f'cadena nueva comillas --> {cadenaReemplazada}')
            # Metodo analizar
            lexico.analizar(cadenaReemplazada)
            self.textoSalida.clear()

            # datos de salida, mostrar en la ventana
            for i in lexico.salidas:

                if str(i[:8]).lower() == "lextoken":
                    # self.textoSalida.appendPlainText(i)
                    self.textoSalida.appendHtml(
                        f'<span style="color: black;">{i}</span>')
                    self.textoSalida.setStyleSheet(
                        'font: 15pt "MS Shell Dlg 2"; color:black; background-color: rgb(255, 255, 255);')
                else:
                    self.textoSalida.appendHtml(
                        f'<span style="color: red;"><b>Error Caracter No Válido: &#{int(i[:])};</b></span>')
                    self.textoSalida.setStyleSheet(
                        'font: 15pt "MS Shell Dlg 2"; color:black; background-color: rgb(255, 255, 255);')

            self.textoSalida.setStyleSheet(
                'font: 15pt "MS Shell Dlg 2"; color:black; background-color: rgb(255, 255, 255);')

            lexico.salidas.clear()
            print(f'ESTO ES EL ERROR: {lexico.error}')
            if lexico.error:

                self.textoEntrada.setStyleSheet(
                    'border: 3px solid red; font: 15pt "MS Shell Dlg 2"; background-color: rgb(255, 255, 255);')
                self.textoSalida.setStyleSheet(
                    'border: 3px solid red; font: 15pt "MS Shell Dlg 2"; background-color: rgb(255, 255, 255);')
                QMessageBox.critical(
                    None, 'Error en analizador lexico', 'Caracter o caracteres no validos')
                print("No pasamos al sintactico")

            else:
                print("Pasamos al sintactico")
                
                sintactico.ejecucionAlgoritmo(cadenaReemplazada)
                if sintactico.errorSintactico:
                    self.textoSalida.clear()
                    self.textoSalida.appendHtml(
                        f'<span style="color: purple;">ERROR DE SINTAXIS</span>')

                    for i in range(len(sintactico.lista)):
                        self.textoSalida.appendHtml(
                            f'<span style="color: green;">{sintactico.lista[i]}</span>')
                        self.textoSalida.setStyleSheet(
                            'font: 15pt "MS Shell Dlg 2"; color:black; background-color: rgb(255, 255, 255);')

                    if len(sintactico.lista) > 0:
                        try:
                            self.textoSalida.appendHtml(
                                f'<span style="color: orange;">ESTO ES EL ERROR: {sintactico.lista[0]} O EL CARACTER QUE ESTA ANTES DE ESTO O FALTA ALGUN CARACTER </span>')
                            self.textoEntrada.setStyleSheet(
                                'border: 3px solid red; font: 15pt "MS Shell Dlg 2"; background-color: rgb(255, 255, 255);')
                            self.textoSalida.setStyleSheet(
                                'border: 3px solid red; font: 15pt "MS Shell Dlg 2"; background-color: rgb(255, 255, 255);')
                        except:
                            QMessageBox.critical(
                                None, "Error de sintaxis", 'Error de sintaxis, verificar datos!')
                    self.textoEntrada.setStyleSheet(
                        'border: 3px solid red; font: 15pt "MS Shell Dlg 2"; background-color: rgb(255, 255, 255);')
                    self.textoSalida.setStyleSheet(
                        'border: 3px solid red; font: 15pt "MS Shell Dlg 2"; background-color: rgb(255, 255, 255);')
                    # self.textoSalida.clear()
                    try:
                        QMessageBox.critical(
                            None, "ERROR DE SINTAXIS", f"ERROR DE SINTAXIS: ESTO ES EL ERROR: {sintactico.lista[0]} O EL CARACTER QUE ESTA ANTES DE ESTO O FALTA ALGUN CARACTER")
                    except:
                        QMessageBox.critical(
                            None, "Error de sintaxis", 'Error de sintaxis, verificar datos!')
                else:
                    # LLAMAR SEMANTICO
                    self.textoEntrada.setStyleSheet(
                        'border: 3px solid green; font: 15pt "MS Shell Dlg 2"; background-color: rgb(255, 255, 255);')
                    self.textoSalida.setStyleSheet(
                        'border: 3px solid green; font: 15pt "MS Shell Dlg 2"; background-color: rgb(255, 255, 255);')
                    QMessageBox.information(
                        None, "Sintaxis Correcta", "Sintaxis Correcto")

                    self.datosSemantico(cadena)

                sintactico.errorSintactico = False
            lexico.error = False

        else:
            self.textoSalida.clear()
            self.textoEntrada.setStyleSheet(
                'border: 3px solid red; font: 15pt "MS Shell Dlg 2"; background-color: rgb(255, 255, 255);')
            self.textoSalida.setStyleSheet(
                'border: 3px solid gray; font: 15pt "MS Shell Dlg 2"; background-color: rgb(255, 255, 255);')
            QMessageBox.warning(None, 'Campo Vacio','Sin datos de entrada, porfavor ingrese datos')

    def reemplazarCarateres(self, cadena):
        cadena = list(cadena)
        cadena1 = ''
        for pos, char in enumerate(cadena):
            if(char == "S" and cadena[pos+1] == "t" and cadena[pos+2] == "r" and cadena[pos+3] == "i" and cadena[pos+4] == "n" and cadena[pos+5] == "g"):
                cadena[pos] = cadena[pos].replace("S", "s")
            cadena1 += cadena[pos]

        # cadena1 = ''
        # for i in range(len(cadena)):
        #     if cadena[i] == chr(34):
        #         contador += 1
        #         if contador%2 == 0:
        #             cadena[i] = cadena[i].replace(chr(34), '”')
        #         else:
        #             cadena[i] = cadena[i].replace(chr(34), '“')
        #     cadena1 += cadena[i]
        return cadena1

    def datosSemantico(self, cadena):
        NClase = semantico.nombreClase
        atributo = semantico.atributo
        metodos = semantico.metodo

        # asd = cadena.strip('\t')
        nuevacadena = cadena.splitlines()
        # reemplazar = nuevacadena.strip()
        print(nuevacadena)
        try:
            for i in range(len(nuevacadena)):
                if nuevacadena[i] == nuevacadena[0]:
                    print(f"ESTO ES LO QUE HAY EN NUEVACADENA[i] --> {nuevacadena[i]}")
                    ncadena = nuevacadena[0].split()
                    for x in range(len(ncadena)):
                        print(f"ESTO ES LO QUE HAY EN NCADENA[x] {ncadena[x]}")
                        if ncadena[x] == ncadena[2]:
                            # print(ncadena[x])
                            NClase.clear()
                            NClase.append(ncadena[x][0:-1])
                            print(NClase[0])

                elif nuevacadena[i] == nuevacadena[1]:
                    ncadena = nuevacadena[1].split()
                    variable = ''
                    metodo = ''
                    acceso = ''
                    metodoEncontrado = ''
                    if len(ncadena) > 2:

                        for x in range(len(ncadena)):
                            print(f'TAMAÑOS DE LA CADENA ===========> {len(ncadena)}')
                            print(ncadena[x])
                            if ncadena[x] == ncadena[0]:
                                if ncadena[x] == 'public':
                                    acceso += '+'

                                elif ncadena[x] == 'private':
                                    acceso += '-'

                                elif ncadena[x] == 'protected':
                                    acceso += '#'

                                else:
                                    acceso += ''

                            else:
                                metodo += ' '
                                for m in range(len(ncadena[x])):
                                    print(ncadena[x][m])
                                    if ncadena[x][m] == ')':
                                        metodo += ncadena[x][m]
                                        break
                                    else:
                                        metodo += ncadena[x][m]

                                metodoEncontrado = acceso + metodo

                                metodos.clear()
                                atributo.clear()
                                atributo.append('')
                                metodos.append(metodoEncontrado)

                    else:
                        for x in range(len(ncadena)):
                            print(f'TAMAÑOS DE LA CADENA ===========> {len(ncadena)}')
                            print(ncadena[x])
                            # variable += ' ' + ncadena[x]
                            if x == 1:
                                variable = ncadena[x][:-1] + ': '+ncadena[x-1]
                                print(f'Esta es la variable --> {variable}')
                                atributo.clear()
                                atributo.append(variable)
                                print(atributo[0])
                                metodos.clear()
                                metodos.append('')
        except:
            QMessageBox.warning(None, "Error", "Hay un error")
        semantico.digramaUML()

    # Metodo cerrar ventana
    def salir(self):
        salir = QMessageBox.question(self, 'Salir', '¿Esta seguro/a de salir?', QMessageBox.Yes, QMessageBox.No)
        if salir == QMessageBox.Yes:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainView()
    window.show()
    sys.exit(app.exec_())
