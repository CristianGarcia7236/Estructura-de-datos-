Lista_articulos = []
switch = True

while switch == True:

      print("NEGOCIO DE FERRRETERIA")
      print("\n MENU \n")

      print("\n1.-REGISTRAR UNA VENTA\n")
      print("\n2.-CONSULTAR VENTA\n")
      print("\n3.-SALIR \n")
      eleccion = int(input("\nIngresa la opccion que deses realizar: "))

      if eleccion == 3:
         switch = False
         print("\nHas salido del Menu\n")
      
      
      
      if eleccion == 1:
         while eleccion == 1:
               print("REGISTRO DE VENTA")
               registro = []
               numero_venta=int(input(" Ingresa el Número de Venta: "))
               registro.append(numero_venta)
               pago_total = 0
    
               while eleccion == 1:
                     descripcion=input(" Ingresa la Descripción del articulo: ")
                     cantidad = int(input (" Ingresa la Cantidad de piezas vendidas: "))
                     precio= float(input(" Ingresa el Precio de Venta: "))
                     registro.append(descripcion)
                     registro.append(cantidad)
                     registro.append(precio)
                     monto = cantidad * precio
                     pago_total = pago_total + monto
                     eleccion = int(input(" Quieres Ingresar otro articulo: 1.- SI / 0.- NO: "))
                    
                     if eleccion == 0:
                         print(f" El Monto total a pagar es : {pago_total}")
                         Lista_articulos.append(registro)
                         eleccion = int(input(" Desea capturar otro registro de venta 1.- SI / 0.- NO: "))
                         if eleccion == 0:
                            switch == True
      
      if eleccion == 2:
         
               print("CONSULTA DE VENTA")
         
               codigo_venta = int(input("\nIngrese la clave de venta que desea buscar: "))
               for registro in Lista_articulos:
                   if registro[0] == codigo_venta:
                      print(registro) 
               
                      eleccion = int(input("\nIngrese la tecla 0 para regresar al Menu Principal: "))
                      if eleccion == 0:
                         switch == True
             
           
              
     
               