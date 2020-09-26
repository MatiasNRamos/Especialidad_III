def Perturbador(X, Y, YERR, b=10):
    """ Devuelve una muestra perturbada a partir de una original
    
    Parameters
    ----------
    X : list
        Valores X
    Y : list
        Valores Y 
    YERR : list
        Incertezas asociadas a Y
    b : int
        N° de puntos máximos omitidos en los bordes
    
    Returns
    -------
    XS : list
        Nuevos valores X
    YS : list
        Nuevos valores Y
    YERRS : list
        Nuevas incertezas para Y
    
    """
    import numpy as np
    # Creo el loop generador de la muestra
    ij = 0
    Door = np.empty(len(X)) # Deja o no que se agregue el punto ij a la nueva muestra
    Pert = [] # Valor de las perturbaciones, por ahora sólo serán en tao y no en times
    XS = []
    YS = []
    YERRS = []
    while ij<len(X):
        # Primero calculo las perturbaciones para cada punto, FIJAR SEMILLA de Numpy!!!!
        Pert.append( 2*YERR[ij]*np.random.random() - YERR[ij] ) # N° entre [-ERR[ij], ERR[ij]]
        # Ahora parto en tres en intervalo para ij. (0,b), (b, len(Time)-b) y 
        # (len(Time)-b, len(Time)). Esto me sirve para quitar o no puntos en el borde.
        if ij>0 and ij<b: # Borde inferior
            Door[ij] = np.random.choice([0,1])
            if Door[ij]==1: # Si Door[ij]=1 --> agrego el punto, sino no
                XS.append(X[ij])
                YS.append(Y[ij] + Pert[ij]) # Acá ingreso la perturbación
                YERRS.append(YERR[ij])
        elif ij>b and ij<(len(X)-b): # El medio (todos los puntos se agregan acá)
            XS.append(X[ij])
            YS.append(Y[ij] + Pert[ij])
            YERRS.append(YERR[ij])
        else: # Borde superior
            Door[ij] = np.random.choice([0,1])
            if Door[ij]==1:
                XS.append(X[ij])
                YS.append(Y[ij] + Pert[ij])
                YERRS.append(YERR[ij])
        ij = ij + 1
    return XS, YS, YERRS
