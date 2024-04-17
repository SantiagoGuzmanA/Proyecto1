#Calculo de la desviación estandar
import math

def desviacion_estandar(database):
    I1 = []
    I2 = []
    I3 = []
    for row in database[1:]:
        I1.append(row[4])
        I2.append(row[5])
        I3.append(row[6])
    
    I1avg = sum(I1) / len(I1)
    I2avg = sum(I2) / len(I2)
    I3avg = sum(I3) / len(I3)
    
    distMediaI1 =[]
    distMediaI2 =[]
    distMediaI3 =[]
    
    for row in database[1:]:
        distMediaI1.append(abs(row[4]-I1avg)**2)
        distMediaI2.append(abs(row[5]-I2avg)**2)
        distMediaI3.append(abs(row[6]-I3avg)**2)
    
    DEI1 = math.sqrt(sum(distMediaI1) / len(distMediaI1))
    DEI2 = math.sqrt(sum(distMediaI2) / len(distMediaI2))
    DEI3 = math.sqrt(sum(distMediaI3) / len(distMediaI3))
    return(DEI1,DEI2,DEI3)
        
        
    
    