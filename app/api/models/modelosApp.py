from sqlalchemy import Column,Integer,String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tabla
Base=declarative_base()

#Listado de modelos de la aplicación
#Modelo Usuario

class Usuario(Base):
    __tablename__="usuarios"
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(50))
    age=Column(Integer)
    phone=Column(String(12))
    email=Column(String(20))
    password=Column(String(10))
    singUpDate=Column(Date)
    city=Column(String(50))

#Gasto

class Gasto(Base):
    __tablename__="gastos"
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(50))
    nombreGasto=Column(String(50))
#Categoria

class Categoria(Base):
    __tablename__="categoria"
    id=Column(Integer, primary_key=True, autoincrement=True)
    categoria=Column(String(50)) 
    descripcion=Column(String(50))
    fotoIcono=Column(String(50))



#Metodos de pago
class MetodosDePago(Base):
    __tablename__="base"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcion=Column(String(50))


#Ingresos
class Ingreso(Base):
    _tablename_ = 'ingresos' 
    id = Column(Integer, primary_key=True, autoincrement=True)  
    concepto = Column(String(50))  
    monto = Column(float(10, 2))  
    fecha = Column(String(10))

# Transacciones
class Transaccion(Base):
    _tablename_ = 'transacciones'  
    id = Column(Integer, primary_key=True, autoincrement=True)  
    cantidad = Column(Integer(12, 2))  
    fecha = Column(Date)  
    descripcion = Column(String(50))      